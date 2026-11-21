/* search-core.js */
(function (root, factory) {
  var api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.LUTSearch = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  function normalize(value) { return String(value || '').normalize('NFKC').toLowerCase().replace(/\s+/g, ' ').trim(); }
  function terms(query) { return Array.from(new Set(normalize(query).slice(0, 160).split(' ').filter(Boolean))).slice(0, 16); }
  function search(documents, query, filters) {
    var tokens = terms(query); filters = filters || {};
    if (!tokens.length) return [];
    return documents.reduce(function (results, doc) {
      if ((filters.course && doc.course !== filters.course) || (filters.kind && doc.kind !== filters.kind)) return results;
      var title = normalize(doc.title + ' ' + (doc.lectureTitle || ''));
      var metadata = normalize([doc.course, doc.courseTitle, doc.part].concat(doc.keywords || []).join(' '));
      var body = normalize(doc.text), all = title + ' ' + metadata + ' ' + body;
      if (tokens.every(function (word) { return all.includes(word); })) {
        var score = tokens.reduce(function (n, word) {
          return n + (title.includes(word) ? 12 : 0) + (metadata.includes(word) ? 4 : 0) + (body.includes(word) ? 2 : 0);
        }, 0);
        results.push({ doc: doc, score: score });
      }
      return results;
    }, []).sort(function (a, b) { return b.score - a.score || a.doc.id.localeCompare(b.doc.id); });
  }
  function snippet(text, query, length) {
    text = String(text || ''); length = Math.max(30, length || 160);
    var folded = text.toLowerCase(), offsets = terms(query).map(function (word) { return folded.indexOf(word); }).filter(function (i) { return i >= 0; });
    var start = offsets.length ? Math.max(0, Math.min.apply(null, offsets) - Math.floor(length / 3)) : 0;
    return (start ? '…' : '') + text.slice(start, start + length) + (start + length < text.length ? '…' : '');
  }
  function segments(text, query) {
    text = String(text || '');
    var words = terms(query).sort(function (a, b) { return b.length - a.length; });
    if (!words.length) return [{ text: text, match: false }];
    var pattern = new RegExp(words.map(function (s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('|'), 'gi');
    var result = [], index = 0, match;
    while ((match = pattern.exec(text))) {
      if (match.index > index) result.push({ text: text.slice(index, match.index), match: false });
      result.push({ text: match[0], match: true }); index = pattern.lastIndex;
    }
    if (index < text.length) result.push({ text: text.slice(index), match: false });
    return result;
  }
  return { normalize: normalize, terms: terms, search: search, snippet: snippet, segments: segments };
});

;
/* study-store.js */
(function (root, factory) {
  var api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.LUTStudyStore = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  var KEY = 'lut-learning-v1', LEGACY = 'lut-review-v1';
  var STATUSES = ['new', 'learning', 'review', 'mastered'];
  var PRACTICE = ['todo', 'done', 'wrong', 'retry'];
  var ID = /^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+$/;
  var QUESTION = /^[A-Za-z0-9_-]+\/[A-Za-z0-9_-]+\/practice-[1-9]\d*$/;
  function object(value) { return value && typeof value === 'object' && !Array.isArray(value); }
  function text(value, max) { return typeof value === 'string' ? value.slice(0, max) : ''; }
  function time(value) { return Number.isFinite(value) ? Math.max(0, Math.min(4102444800000, value)) : 0; }
  function defaults() { return { schema:'lut-learning', version:1, lectures:{}, practice:{}, preferences:{fontSize:17,lineHeight:1.85,focus:false}, lastLecture:'' }; }
  function lecture(value) {
    value = object(value) ? value : {};
    return {status:STATUSES.includes(value.status) ? value.status : 'new',
      anchor:/^[A-Za-z0-9_-]{1,160}$/.test(value.anchor || '') ? value.anchor : '',
      ratio:Number.isFinite(value.ratio) ? Math.max(0, Math.min(1, value.ratio)) : 0,
      revision:/^[a-f0-9]{12}$/.test(value.revision || '') ? value.revision : '',
      updatedAt:time(value.updatedAt), visitedAt:time(value.visitedAt)};
  }
  function preferences(value) {
    value = object(value) ? value : {};
    return {fontSize:[17,19,22].includes(value.fontSize) ? value.fontSize : 17,
      lineHeight:[1.65,1.85,2.1].includes(value.lineHeight) ? value.lineHeight : 1.85, focus:value.focus === true};
  }
  function clean(value) {
    var result = defaults();
    if (!object(value) || value.version !== 1) return result;
    Object.keys(object(value.lectures) ? value.lectures : {}).forEach(function (id) {
      if (ID.test(id)) result.lectures[id] = lecture(value.lectures[id]);
    });
    Object.keys(object(value.practice) ? value.practice : {}).forEach(function (id) {
      var row = value.practice[id];
      if (!QUESTION.test(id) || !object(row)) return;
      result.practice[id] = {status:PRACTICE.includes(row.status) ? row.status : 'todo', bookmarked:row.bookmarked === true,
        prompt:text(row.prompt,1200), updatedAt:time(row.updatedAt)};
    });
    result.preferences = preferences(value.preferences);
    result.lastLecture = ID.test(value.lastLecture || '') ? value.lastLecture : '';
    return result;
  }
  function create(storage, options) {
    options = options || {};
    var clock = options.now || Date.now, memory = defaults(), dirty = false;
    function read() {
      var state = memory;
      if (!dirty) {
        try { state = clean(JSON.parse(storage.getItem(KEY) || 'null')); } catch (_) { state = clean(memory); }
        try {
          var old = JSON.parse(storage.getItem(LEGACY) || '{}');
          (options.ids || []).forEach(function (id) {
            if (ID.test(id) && !state.lectures[id] && old[id.replace('/', '-')] === true) state.lectures[id] = lecture({status:'mastered'});
          });
        } catch (_) { /* Corrupt legacy data must not prevent reading current progress. */ }
      }
      memory = clean(state); return clean(memory);
    }
    function save(state, legacyId) {
      memory = clean(state);
      try {
        storage.setItem(KEY, JSON.stringify(memory));
        if (legacyId) {
          var old;
          try { old = JSON.parse(storage.getItem(LEGACY) || '{}'); } catch (_) { old = {}; }
          if (!object(old)) old = {};
          (Array.isArray(legacyId) ? legacyId : [legacyId]).forEach(function(id){old[id.replace('/', '-')] = memory.lectures[id].status === 'mastered';});
          storage.setItem(LEGACY, JSON.stringify(old));
        }
        dirty = false; return {state:clean(memory), persisted:true};
      } catch (_) { dirty = true; return {state:clean(memory), persisted:false}; }
    }
    function setLecture(id, patch) {
      if (!ID.test(id)) throw new Error('讲义标识无效');
      var state = read(), current = state.lectures[id] || lecture({});
      patch = patch || {};
      state.lectures[id] = lecture(Object.assign({}, current, patch, {updatedAt:clock()}));
      if (patch.visited) { state.lastLecture = id; state.lectures[id].visitedAt = clock(); }
      return save(state, Object.hasOwn(patch, 'status') ? id : null);
    }
    function setPractice(id, patch) {
      if (!QUESTION.test(id)) throw new Error('练习标识无效');
      var state = read();
      state.practice[id] = Object.assign({status:'todo',bookmarked:false,prompt:''}, state.practice[id] || {}, patch || {}, {updatedAt:clock()});
      return save(state);
    }
    function setPreferences(patch) {
      var state = read(); state.preferences = preferences(Object.assign({},state.preferences,patch)); return save(state);
    }
    function importData(serialized) {
      if (typeof serialized !== 'string' || serialized.length > 2000000) throw new Error('备份文件过大或格式无效');
      var incoming = JSON.parse(serialized);
      if (!object(incoming) || incoming.schema !== 'lut-learning' || incoming.version !== 1 || !object(incoming.lectures) || !object(incoming.practice)) throw new Error('请选择本站导出的学习记录备份');
      Object.entries(incoming.lectures).forEach(function (entry) {
        if (!ID.test(entry[0]) || !object(entry[1]) || !STATUSES.includes(entry[1].status)) throw new Error('备份含无效讲义记录');
      });
      Object.entries(incoming.practice).forEach(function (entry) {
        if (!QUESTION.test(entry[0]) || !object(entry[1]) || !PRACTICE.includes(entry[1].status)) throw new Error('备份含无效练习记录');
      });
      var state = read(), next = clean(incoming);
      ['lectures','practice'].forEach(function (key) {
        Object.keys(next[key]).forEach(function (id) {
          if (!state[key][id] || next[key][id].updatedAt >= state[key][id].updatedAt) state[key][id] = next[key][id];
        });
      });
      state.preferences = next.preferences;
      if (next.lastLecture) state.lastLecture = next.lastLecture;
      return save(state,Object.keys(state.lectures));
    }
    return {read:read,getLecture:function(id){return read().lectures[id] || lecture({});},
      setLecture:setLecture,setPractice:setPractice,setPreferences:setPreferences,
      exportData:function(){return JSON.stringify(read(),null,2);},importData:importData};
  }
  return {create:create,statuses:STATUSES,practiceStatuses:PRACTICE,key:KEY,legacyKey:LEGACY};
});

;
/* study.js */
(function () {
  'use strict';
  var catalogue = window.LUT_LEARNING_CATALOG || {lectures:[],courses:[]};
  var entries = new Map(catalogue.lectures.map(function (row) { return [row.id,row]; }));
  var prefix = document.querySelector('[data-site-prefix]').dataset.sitePrefix || '';
  var labels = {new:'未开始',learning:'学习中',review:'待复习',mastered:'已掌握'};
  var storage;
  try { storage = localStorage; } catch (_) { storage = {getItem:function(){return null;},setItem:function(){throw new Error('storage unavailable');}}; }
  var store = LUTStudyStore.create(storage,{ids:catalogue.lectures.map(function(row){return row.id;})});
  var notice = document.createElement('p'); notice.id='study-notice';notice.className='study-notice';notice.hidden=true;
  notice.setAttribute('role','status');document.body.appendChild(notice);
  var noticeTimer, warned=false;
  function notify(message, persistent) {
    clearTimeout(noticeTimer);notice.textContent=message;notice.hidden=false;
    if(!persistent)noticeTimer=setTimeout(function(){notice.hidden=true;},4000);
  }
  function commit(result, message) {
    if(!result.persisted){if(!warned){warned=true;notify('浏览器未能保存记录，当前变更仅在本页有效。请导出备份并检查浏览器存储设置。',true);}}
    else if(message)notify(message);
    refresh();window.dispatchEvent(new CustomEvent('lut:learning-changed'));
    return result;
  }
  function resumeURL(entry, state) {
    var anchor=state.revision && state.revision!==entry.revision?'sec-overview':state.anchor;
    return prefix+entry.url+'?resume=1'+(anchor?'#'+encodeURIComponent(anchor):'');
  }
  function refresh() {
    var data=store.read();
    document.querySelectorAll('[data-study-id]').forEach(function(el){
      var status=(data.lectures[el.dataset.studyId]||{}).status||'new';
      if(el.matches('input.tick'))el.checked=status==='mastered';
      else{el.textContent=labels[status];el.dataset.status=status;}
    });
    document.querySelectorAll('[data-progress-course]').forEach(function(el){
      var rows=catalogue.lectures.filter(function(entry){return entry.course===el.dataset.progressCourse;});
      var done=rows.filter(function(entry){return(data.lectures[entry.id]||{}).status==='mastered';}).length;
      el.querySelector('progress').value=done;
      el.querySelector('span').textContent=done+' / '+rows.length+' 讲已掌握';
    });
    var home=document.getElementById('continue-learning');
    if(home){
      var entry=entries.get(data.lastLecture);home.replaceChildren();
      if(entry){
        var a=document.createElement('a');a.className='continue-link';a.href=resumeURL(entry,data.lectures[entry.id]||{});
        a.textContent='继续学习：'+entry.title;home.appendChild(a);
        var context=document.createElement('p');context.className='sub';context.textContent=entry.courseTitle+' · '+entry.part;home.appendChild(context);
      }else{var empty=document.createElement('p');empty.className='sub';empty.textContent='还没有阅读记录，从下方选择课程开始。';home.appendChild(empty);}
      var done=Object.values(data.lectures).filter(function(row){return row.status==='mastered';}).length;
      var review=Object.values(data.lectures).filter(function(row){return row.status==='review';}).length;
      document.getElementById('study-totals').textContent='已掌握 '+done+' / '+catalogue.lectures.length+' 讲 · 待复习 '+review+' 讲';
    }
    if(article){
      var status=store.getLecture(article.dataset.lectureId).status;
      document.querySelectorAll('input[name="lecture-status"]').forEach(function(input){input.checked=input.value===status;});
    }
  }
  var article=document.querySelector('article[data-lecture-id]');
  if(article){
    var id=article.dataset.lectureId, saved=store.getLecture(id), entry=entries.get(id);
    var resume=document.getElementById('resume-lecture');
    if(saved.anchor && entry && resume){resume.href=resumeURL(entry,saved);resume.hidden=false;}
    var changed=saved.revision && entry && saved.revision!==entry.revision;
    commit(store.setLecture(id,{status:saved.status==='new'?'learning':saved.status,anchor:changed?'sec-overview':saved.anchor,revision:entry?entry.revision:'',visited:true}));
    if(changed){
      notify('本讲内容已有更新，学习状态保留；继续阅读从本讲概览开始。');
      if(new URLSearchParams(location.search).has('resume'))location.replace('#sec-overview');
    }
    document.querySelectorAll('input[name="lecture-status"]').forEach(function(input){
      input.addEventListener('change',function(){if(input.checked)commit(store.setLecture(id,{status:input.value}),'已标记为'+labels[input.value]);});
    });
    var saveTimer;
    function savePosition(){
      var active=document.querySelector('[data-scrollspy] [aria-current="location"]');
      var max=Math.max(1,document.documentElement.scrollHeight-innerHeight);
      commit(store.setLecture(id,{anchor:active?active.hash.slice(1):'lecture-title',ratio:Math.max(0,scrollY/max)}));
    }
    addEventListener('scroll',function(){clearTimeout(saveTimer);saveTimer=setTimeout(savePosition,700);},{passive:true});
    addEventListener('pagehide',savePosition);
  }
  var exportButton=document.getElementById('export-study');
  if(exportButton)exportButton.addEventListener('click',function(){
    var blob=new Blob([store.exportData()],{type:'application/json'}),url=URL.createObjectURL(blob),a=document.createElement('a');
    a.href=url;a.download='lut-learning-backup.json';a.click();setTimeout(function(){URL.revokeObjectURL(url);},1000);
    notify('已导出学习记录备份。');
  });
  var importInput=document.getElementById('import-study');
  if(importInput)importInput.addEventListener('change',function(){
    var file=importInput.files[0];if(!file)return;
    if(file.size>2000000){notify('请选择小于 2 MB 的本站学习记录备份。');importInput.value='';return;}
    file.text().then(function(text){commit(store.importData(text),'学习记录已合并。');}).catch(function(error){notify('导入未完成：'+error.message);}).finally(function(){importInput.value='';});
  });
  window.LUTLearning={store:store,commit:commit,notify:notify,refresh:refresh,entries:entries,prefix:prefix,labels:labels};
  addEventListener('storage',function(event){if(event.key==='lut-learning-v1'||event.key==='lut-review-v1'){refresh();dispatchEvent(new CustomEvent('lut:learning-changed'));}});
  refresh();
})();

;
/* reader-tools.js */
(function () {
  'use strict';
  var app=window.LUTLearning,root=document.documentElement,content=document.getElementById('page-content');
  if(!app||!content)return;
  var font=document.getElementById('reader-font'),line=document.getElementById('reader-line'),focus=document.getElementById('focus-reading');
  var lastPreferences='';
  var exit=document.createElement('button');exit.id='focus-exit';exit.type='button';exit.className='study-button focus-exit';exit.textContent='退出专注阅读';exit.hidden=true;
  if(focus){document.body.appendChild(exit);exit.addEventListener('click',function(){app.commit(app.store.setPreferences({focus:false}));});}
  function applyPreferences(){
    var prefs=app.store.read().preferences;
    var signature=JSON.stringify(prefs);if(signature===lastPreferences)return;lastPreferences=signature;
    root.style.setProperty('--reader-font-size',(prefs.fontSize/16)+'rem');root.style.setProperty('--reader-line-height',String(prefs.lineHeight));
    if(font)font.value=String(prefs.fontSize);if(line)line.value=String(prefs.lineHeight);
    root.classList.toggle('focus-reading',!!focus&&prefs.focus);
    exit.hidden=!focus||!prefs.focus;
    if(focus){focus.setAttribute('aria-pressed',String(prefs.focus));focus.textContent=prefs.focus?'退出专注阅读':'专注阅读';}
    window.dispatchEvent(new Event('resize'));
  }
  if(font)font.addEventListener('change',function(){app.commit(app.store.setPreferences({fontSize:Number(font.value)}));});
  if(line)line.addEventListener('change',function(){app.commit(app.store.setPreferences({lineHeight:Number(line.value)}));});
  if(focus)focus.addEventListener('click',function(){app.commit(app.store.setPreferences({focus:!app.store.read().preferences.focus}));});
  addEventListener('keydown',function(event){if(event.key==='Escape'&&root.classList.contains('focus-reading')&&!document.querySelector('dialog[open]'))app.commit(app.store.setPreferences({focus:false}));});
  addEventListener('lut:learning-changed',applyPreferences);applyPreferences();

  function copy(text){
    if(navigator.clipboard&&window.isSecureContext)return navigator.clipboard.writeText(text);
    return new Promise(function(resolve,reject){
      var field=document.createElement('textarea');field.value=text;field.className='clipboard-fallback';document.body.appendChild(field);field.select();
      var ok=false;try{ok=document.execCommand('copy');}catch(_){}field.remove();
      if(ok)resolve();else reject(new Error('请选中代码后手动复制。'));
    });
  }
  content.querySelectorAll('pre').forEach(function(pre){
    var wrapper=document.createElement('div');wrapper.className='code-block';pre.before(wrapper);wrapper.appendChild(pre);
    var button=document.createElement('button');button.type='button';button.className='copy-code';button.textContent='复制代码';wrapper.appendChild(button);
    button.addEventListener('click',function(){copy((pre.querySelector('code')||pre).textContent).then(function(){app.notify('代码已复制。');}).catch(function(error){app.notify(error.message);});});
  });

  var dialog=document.createElement('dialog');dialog.className='image-viewer';dialog.setAttribute('aria-label','图片大图预览');
  dialog.setAttribute('closedby','any');
  var close=document.createElement('button');close.type='button';close.className='study-button image-close';close.textContent='关闭大图';close.autofocus=true;dialog.appendChild(close);
  var image=document.createElement('img');image.alt='';dialog.appendChild(image);
  var caption=document.createElement('p');caption.className='sub';dialog.appendChild(caption);document.body.appendChild(dialog);
  close.addEventListener('click',function(){dialog.close();});
  if(!('closedBy' in HTMLDialogElement.prototype)){
    var pressedOutside=false;
    function outside(event){var rect=dialog.getBoundingClientRect();return event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom;}
    dialog.addEventListener('pointerdown',function(event){pressedOutside=outside(event);});
    dialog.addEventListener('pointerup',function(event){if(pressedOutside&&outside(event))dialog.close();});
  }
  content.querySelectorAll('img').forEach(function(img){
    var link=img.closest('a'),trigger=link;
    if(!trigger){trigger=document.createElement('button');trigger.type='button';trigger.className='image-zoom';trigger.setAttribute('aria-label','查看大图：'+(img.alt||'课程图片'));img.before(trigger);trigger.appendChild(img);}
    trigger.addEventListener('click',function(event){
      if(event.ctrlKey||event.metaKey||event.shiftKey||event.altKey||typeof dialog.showModal!=='function')return;
      var source=img.dataset.fullSrc||img.getAttribute('src'),url;
      try{url=new URL(source,location.href);}catch(_){return;}
      if(!['http:','https:','file:','blob:'].includes(url.protocol))return;
      if(link&&new URL(link.href,location.href).href!==url.href&&new URL(link.href,location.href).href!==img.src)return;
      event.preventDefault();image.src=url.href;image.alt=img.alt||'课程图片';caption.textContent=img.alt||'原始课程图片';dialog.showModal();
    });
  });

  var query=(new URLSearchParams(location.search).get('find')||'').slice(0,160);
  var article=document.querySelector('article[data-lecture-id]');if(!query||!article)return;
  var walker=document.createTreeWalker(article,NodeFilter.SHOW_TEXT,{acceptNode:function(node){return node.parentElement.closest('script,style,button,input,select,textarea,.study-toolbar,.lecture-head')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT;}});
  var nodes=[],node;while((node=walker.nextNode()))nodes.push(node);
  var ranges=[],count=0,native=!!(window.CSS&&CSS.highlights&&window.Highlight);
  nodes.forEach(function(textNode){
    if(count>=2000)return;
    var parts=LUTSearch.segments(textNode.textContent,query);if(!parts.some(function(part){return part.match;}))return;
    var parent=textNode.parentElement;while(parent&&parent!==article){if(parent.tagName==='DETAILS')parent.open=true;parent=parent.parentElement;}
    var offset=0,fragment=document.createDocumentFragment();
    parts.forEach(function(part){
      if(part.match&&count<2000){
        count++;
        if(native){var range=new Range();range.setStart(textNode,offset);range.setEnd(textNode,offset+part.text.length);ranges.push(range);}
        else{var mark=document.createElement('mark');mark.className='lut-search-mark';mark.textContent=part.text;fragment.appendChild(mark);}
      }else if(!native)fragment.appendChild(document.createTextNode(part.text));
      offset+=part.text.length;
    });
    if(!native)textNode.replaceWith(fragment);
  });
  if(native){CSS.highlights.delete('lut-search');CSS.highlights.set('lut-search',new Highlight(...ranges));}
  var context=document.createElement('div');context.className='search-jump';
  var message=document.createElement('span');message.textContent='查找“'+query+'”：'+(count>=2000?'已高亮前 2000 处':count+' 处匹配');context.appendChild(message);
  var clear=document.createElement('button');clear.type='button';clear.className='study-button';clear.textContent='清除高亮';context.appendChild(clear);
  var first=article.querySelector('section[data-type]');if(first)first.before(context);
  clear.addEventListener('click',function(){
    if(native)CSS.highlights.delete('lut-search');
    article.querySelectorAll('mark.lut-search-mark').forEach(function(mark){var p=mark.parentNode;mark.replaceWith(document.createTextNode(mark.textContent));p.normalize();});
    context.remove();try{var url=new URL(location.href);url.searchParams.delete('find');history.replaceState(null,'',url);}catch(_){}
  });
})();

;
/* practice.js */
(function () {
  'use strict';
  var app=window.LUTLearning;if(!app)return;
  var section=document.querySelector('article[data-lecture-id] #sec-practice');
  var statuses={todo:'未做',done:'已完成',wrong:'做错了',retry:'需要重做'};
  if(section){
    var lecture=section.closest('article').dataset.lectureId;
    var questions=Array.from(section.querySelectorAll(':scope > .qa, :scope > ol > li, :scope > ul > li'));
    if(!questions.length)questions=[section];
    questions.forEach(function(question,index){
      var copy=question.cloneNode(true);copy.querySelectorAll('details,.ans').forEach(function(answer){answer.remove();});
      var id=lecture+'/practice-'+(index+1),prompt=copy.textContent.trim().slice(0,1200);
      if(!question.id)question.id='practice-'+(index+1);
      else{var anchor=document.createElement('span');anchor.id='practice-'+(index+1);anchor.className='practice-anchor';anchor.tabIndex=-1;question.prepend(anchor);}
      var controls=document.createElement('div');controls.className='practice-controls';
      var label=document.createElement('label');label.textContent=questions.length>1?'第 '+(index+1)+' 题自评':'本讲练习自评';
      var select=document.createElement('select');select.name='practice-status-'+(index+1);select.dataset.practiceId=id;
      Object.keys(statuses).forEach(function(value){var option=document.createElement('option');option.value=value;option.textContent=statuses[value];select.appendChild(option);});
      label.appendChild(select);controls.appendChild(label);
      var bookmark=document.createElement('button');bookmark.type='button';bookmark.className='study-button';bookmark.textContent='收藏题目';controls.appendChild(bookmark);
      function refresh(){var row=app.store.read().practice[id]||{status:'todo',bookmarked:false};select.value=row.status;bookmark.setAttribute('aria-pressed',String(row.bookmarked));bookmark.textContent=row.bookmarked?'已收藏':'收藏题目';}
      select.addEventListener('change',function(){app.commit(app.store.setPractice(id,{status:select.value,prompt:prompt}),'练习状态已更新。');});
      bookmark.addEventListener('click',function(){var row=app.store.read().practice[id]||{};app.commit(app.store.setPractice(id,{bookmarked:!row.bookmarked,prompt:prompt}));});
      question.appendChild(controls);refresh();addEventListener('lut:learning-changed',refresh);
    });
    if(/^#practice-\d+$/.test(location.hash)){var target=document.getElementById(location.hash.slice(1));if(target){target.tabIndex=-1;target.focus({preventScroll:true});target.scrollIntoView({block:'start',behavior:'instant'});}}
  }
  var list=document.getElementById('practice-book-list');if(!list)return;
  var course=document.getElementById('practice-course'),filter=document.getElementById('practice-filter');
  function render(){
    var records=Object.entries(app.store.read().practice).filter(function(pair){return pair[1].bookmarked||['wrong','retry'].includes(pair[1].status);});
    document.getElementById('practice-book-count').textContent=String(records.length);
    records=records.filter(function(pair){
      return(!course.value||pair[0].split('/')[0]===course.value)&&(filter.value==='all'||(filter.value==='bookmarked'?pair[1].bookmarked:pair[1].status===filter.value));
    }).sort(function(a,b){return b[1].updatedAt-a[1].updatedAt;});
    list.replaceChildren();
    if(!records.length){var empty=document.createElement('p');empty.className='sub';empty.textContent='当前筛选下没有错题或收藏。在讲义的练习板块标记后会显示在这里。';list.appendChild(empty);return;}
    records.forEach(function(pair){
      var id=pair[0],row=pair[1],lectureId=id.split('/').slice(0,2).join('/'),entry=app.entries.get(lectureId);if(!entry)return;
      var item=document.createElement('div');item.className='practice-book-item';
      var a=document.createElement('a');a.href=app.prefix+entry.url+'#'+id.split('/')[2];a.textContent=entry.title+' · 第 '+id.split('-').pop()+' 题';item.appendChild(a);
      var state=document.createElement('span');state.className='study-state';state.textContent=statuses[row.status]+(row.bookmarked?' · 已收藏':'');item.appendChild(state);
      var prompt=document.createElement('p');prompt.textContent=row.prompt.slice(0,260);item.appendChild(prompt);
      var done=document.createElement('button');done.type='button';done.className='study-button';done.textContent='已完成重做';done.addEventListener('click',function(){app.commit(app.store.setPractice(id,{status:'done',bookmarked:row.bookmarked}));});item.appendChild(done);
      list.appendChild(item);
    });
  }
  [course,filter].forEach(function(control){control.addEventListener('change',render);});
  addEventListener('lut:learning-changed',render);render();
})();
