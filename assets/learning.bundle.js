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
  function enhanceCodeBlock(pre){
    if(pre.parentElement&&pre.parentElement.classList.contains('code-block'))return;
    var wrapper=document.createElement('div');wrapper.className='code-block';pre.before(wrapper);wrapper.appendChild(pre);
    var button=document.createElement('button');button.type='button';button.className='copy-code';button.textContent='复制代码';wrapper.appendChild(button);
    button.addEventListener('click',function(){
      copy((pre.querySelector('code')||pre).textContent).then(function(){
        button.textContent='已复制 ✓';button.classList.add('is-copied');
        clearTimeout(button._copyTimer);
        button._copyTimer=setTimeout(function(){button.textContent='复制代码';button.classList.remove('is-copied');},1600);
        app.notify('代码已复制。');
      }).catch(function(error){app.notify(error.message);});
    });
  }
  var pres=Array.from(content.querySelectorAll('pre'));
  if(pres.length<=40||!window.IntersectionObserver){
    pres.forEach(enhanceCodeBlock);
  }else{
    var preObserver=new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(!entry.isIntersecting)return;
        preObserver.unobserve(entry.target);
        enhanceCodeBlock(entry.target);
      });
    },{rootMargin:'400px 0px'});
    pres.forEach(function(pre){preObserver.observe(pre);});
  }

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
  function openImageModal(img,link,event){
    if(event.ctrlKey||event.metaKey||event.shiftKey||event.altKey||typeof dialog.showModal!=='function')return;
    var source=img.dataset.fullSrc||img.getAttribute('src'),url;
    try{url=new URL(source,location.href);}catch(_){return;}
    if(!['http:','https:','file:','blob:'].includes(url.protocol))return;
    if(link&&new URL(link.href,location.href).href!==url.href&&new URL(link.href,location.href).href!==img.src)return;
    event.preventDefault();image.src=url.href;image.alt=img.alt||'课程图片';caption.textContent=img.alt||'原始课程图片';dialog.showModal();
  }
  var imgs=Array.from(content.querySelectorAll('img'));
  if(imgs.length<=40){
    imgs.forEach(function(img){
      var link=img.closest('a'),trigger=link;
      if(!trigger){trigger=document.createElement('button');trigger.type='button';trigger.className='image-zoom';trigger.setAttribute('aria-label','查看大图：'+(img.alt||'课程图片'));img.before(trigger);trigger.appendChild(img);}
      trigger.addEventListener('click',function(event){openImageModal(img,link,event);});
    });
  }else{
    // On massive pages (all.html with 460+ images), use single delegated click listener to avoid 460 DOM mutations.
    content.classList.add('delegated-zoom');
    content.addEventListener('click',function(event){
      var img=event.target.closest('img');
      if(!img||!content.contains(img))return;
      openImageModal(img,img.closest('a'),event);
    });
  }

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
    var detailsFallback=false;
    if(!questions.length){
      var dets=Array.from(section.querySelectorAll(':scope > details'));
      if(dets.length){questions=dets;detailsFallback=true;}
      else questions=[section];
    }
    questions.forEach(function(question,index){
      var prompt='';
      if(detailsFallback){
        var prev=question.previousElementSibling;
        prompt=(prev&&prev.tagName==='P'?prev.textContent:question.querySelector('summary')?question.querySelector('summary').textContent:'').trim().slice(0,1200);
      }else{
        var copy=question.cloneNode(true);copy.querySelectorAll('details,.ans').forEach(function(answer){answer.remove();});
        prompt=copy.textContent.trim().slice(0,1200);
      }
      var id=lecture+'/practice-'+(index+1);
      var anchorTarget=detailsFallback&&question.previousElementSibling&&question.previousElementSibling.tagName==='P'?question.previousElementSibling:question;
      if(!anchorTarget.id)anchorTarget.id='practice-'+(index+1);
      else{var anchor=document.createElement('span');anchor.id='practice-'+(index+1);anchor.className='practice-anchor';anchor.tabIndex=-1;anchorTarget.prepend(anchor);}
      var controls=document.createElement('div');controls.className='practice-controls';
      var label=document.createElement('label');label.textContent=questions.length>1?'第 '+(index+1)+' 题自评':'本讲练习自评';
      var select=document.createElement('select');select.name='practice-status-'+(index+1);select.dataset.practiceId=id;
      Object.keys(statuses).forEach(function(value){var option=document.createElement('option');option.value=value;option.textContent=statuses[value];select.appendChild(option);});
      label.appendChild(select);controls.appendChild(label);
      var bookmark=document.createElement('button');bookmark.type='button';bookmark.className='study-button';bookmark.textContent='收藏题目';controls.appendChild(bookmark);
      function refresh(){var row=app.store.read().practice[id]||{status:'todo',bookmarked:false};select.value=row.status;bookmark.setAttribute('aria-pressed',String(row.bookmarked));bookmark.textContent=row.bookmarked?'已收藏':'收藏题目';}
      select.addEventListener('change',function(){app.commit(app.store.setPractice(id,{status:select.value,prompt:prompt}),'练习状态已更新。');});
      bookmark.addEventListener('click',function(){var row=app.store.read().practice[id]||{};app.commit(app.store.setPractice(id,{bookmarked:!row.bookmarked,prompt:prompt}));});
      if(detailsFallback)question.after(controls);
      else question.appendChild(controls);
      refresh();addEventListener('lut:learning-changed',refresh);
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

;
/* courseware.js */
/* Source courseware lookup & Google Cloud Storage (GCS) direct link integration. */
(function () {
  'use strict';
  var KEY = 'lut-courseware-base-v1';
  var main = document.querySelector('[data-site-prefix]');
  var prefix = main ? (main.dataset.sitePrefix || '') : '';
  var catalogue = window.LUT_LEARNING_CATALOG || { courses: [], lectures: [] };
  var courseTitles = new Map(catalogue.courses.map(function (c) { return [String(c.id), c.title]; }));

  var CAT_LABELS = {
    all: '全部类型',
    pdf: 'PDF 讲义',
    slides: 'PPT 幻灯片',
    doc: 'Word / 文档',
    code: '代码 / 数据 / 压缩包',
    media: '音频 / 视频',
    image: '图片',
    other: '其他'
  };

  function validateBaseUrl(raw) {
    var trimmed = String(raw || '').trim().replace(/\/+$/, '');
    if (!trimmed) return '';
    var u = new URL(trimmed);
    if (u.protocol !== 'https:' || !u.hostname || u.username || u.password || u.search || u.hash) {
      throw new Error('云端课件地址必须是以 https:// 开头的公开根路径（不含账号或查询参数）。');
    }
    return u.origin + u.pathname.replace(/\/+$/, '');
  }

  function getOverride() {
    try {
      var saved = localStorage.getItem(KEY) || '';
      return saved ? validateBaseUrl(saved) : '';
    } catch (_) { return ''; }
  }

  function getBaseUrl() {
    var override = getOverride();
    if (override) return override;
    var cfg = window.STUDY_SITE_CONFIG || {};
    try { return validateBaseUrl(cfg.coursewareBaseUrl || ''); } catch (_) { return ''; }
  }

  function setOverride(raw) {
    var clean = validateBaseUrl(raw);
    if (!clean) throw new Error('请输入有效的 https:// 云端课件路径，例如 https://pub-xxxx.r2.dev/courseware');
    localStorage.setItem(KEY, clean);
    return clean;
  }

  function clearOverride() {
    try { localStorage.removeItem(KEY); } catch (_) {}
  }

  function encodePath(rel) {
    return String(rel || '').split('/').map(function (seg) { return encodeURIComponent(seg); }).join('/');
  }

  function fileUrl(file) {
    var base = getBaseUrl();
    if (!base || !file) return '';
    return base + '/' + encodeURIComponent(String(file.cid)) + '/' + encodePath(file.rel);
  }

  function formatSize(bytes) {
    var n = Number(bytes) || 0;
    if (n < 1024) return n + ' B';
    if (n < 1024 * 1024) return (n / 1024).toFixed(1) + ' KB';
    return (n / (1024 * 1024)).toFixed(2) + ' MB';
  }

  var loadPromise = null;
  function load() {
    if (window.LUT_COURSEWARE_INDEX) return Promise.resolve(window.LUT_COURSEWARE_INDEX);
    if (!loadPromise) {
      loadPromise = new Promise(function (resolve, reject) {
        var s = document.createElement('script');
        s.src = prefix + 'data/courseware-index.js';
        s.onload = function () {
          if (window.LUT_COURSEWARE_INDEX) resolve(window.LUT_COURSEWARE_INDEX);
          else reject(new Error('课件索引数据格式异常。'));
        };
        s.onerror = function () {
          loadPromise = null;
          reject(new Error('未能加载原始课件索引（data/courseware-index.js）。'));
        };
        document.head.appendChild(s);
      });
    }
    return loadPromise;
  }

  function isPreviewable(ext) {
    return ['.pdf', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg', '.mp3', '.wav', '.m4a', '.ogg', '.mp4', '.webm', '.txt', '.md'].includes(String(ext || '').toLowerCase());
  }

  function createFileRow(file, opts) {
    opts = opts || {};
    var li = document.createElement('li');
    li.className = 'cw-item';

    var info = document.createElement('div');
    info.className = 'cw-main';

    var head = document.createElement('div');
    head.className = 'cw-head';

    var extBadge = document.createElement('span');
    extBadge.className = 'cw-ext cw-cat-' + (file.cat || 'other');
    extBadge.textContent = (file.ext || 'file').replace(/^\./, '').toUpperCase() || 'FILE';
    head.appendChild(extBadge);

    var url = fileUrl(file);
    if (url) {
      var titleLink = document.createElement('a');
      titleLink.className = 'cw-name';
      titleLink.href = url;
      titleLink.target = '_blank';
      titleLink.rel = 'noopener';
      titleLink.textContent = file.name;
      head.appendChild(titleLink);
    } else {
      var titleSpan = document.createElement('span');
      titleSpan.className = 'cw-name';
      titleSpan.textContent = file.name;
      head.appendChild(titleSpan);
    }

    var sizeSpan = document.createElement('span');
    sizeSpan.className = 'cw-size';
    sizeSpan.textContent = formatSize(file.size);
    head.appendChild(sizeSpan);
    info.appendChild(head);

    var pathLine = document.createElement('div');
    pathLine.className = 'cw-meta';
    var coursePrefix = opts.showCourse ? ((courseTitles.get(String(file.cid)) || file.cid) + ' · ') : '';
    pathLine.textContent = coursePrefix + file.rel;
    info.appendChild(pathLine);

    if (opts.showLectures && Array.isArray(file.lectures) && file.lectures.length) {
      var lecRow = document.createElement('div');
      lecRow.className = 'cw-lectures';
      var lbl = document.createElement('span');
      lbl.textContent = '对应讲义：';
      lecRow.appendChild(lbl);
      file.lectures.forEach(function (lec) {
        var a = document.createElement('a');
        a.className = 'cw-lec-link';
        a.href = prefix + 'c/' + encodeURIComponent(file.cid) + '/' + encodeURIComponent(lec.slug) + '.html';
        a.textContent = lec.title;
        lecRow.appendChild(a);
      });
      info.appendChild(lecRow);
    }
    li.appendChild(info);

    var actions = document.createElement('div');
    actions.className = 'cw-actions';
    if (url) {
      var openBtn = document.createElement('a');
      openBtn.className = 'cw-btn primary';
      openBtn.href = url;
      openBtn.target = '_blank';
      openBtn.rel = 'noopener';
      openBtn.textContent = isPreviewable(file.ext) ? '在线打开 ↗' : '下载原件 ↗';
      actions.appendChild(openBtn);
      if (isPreviewable(file.ext)) {
        var dlBtn = document.createElement('a');
        dlBtn.className = 'cw-btn';
        dlBtn.href = url;
        dlBtn.setAttribute('download', file.name);
        dlBtn.textContent = '下载';
        actions.appendChild(dlBtn);
      }
    } else {
      var cfgLink = document.createElement('a');
      cfgLink.className = 'cw-btn muted';
      cfgLink.href = prefix + 'upload.html#courseware-cloud';
      cfgLink.textContent = '配置云端直链 →';
      cfgLink.title = '在 assets/config.js 或上传中心绑定 Cloudflare R2 / 对象存储地址后可直接打开原课件';
      actions.appendChild(cfgLink);
    }
    li.appendChild(actions);
    return li;
  }

  /* 1. Enhance lecture page .lecture-sources panel (preserves static text for tests) */
  function enhanceLectureSources() {
    var article = document.querySelector('article[data-lecture-id]');
    var details = document.querySelector('.lecture-sources');
    if (!article || !details) return;
    var lectureId = article.dataset.lectureId;
    var mounted = false;

    function mountPanel() {
      if (mounted) return;
      mounted = true;
      load().then(function (idx) {
        var ids = (idx.lectureFiles && idx.lectureFiles[lectureId]) || [];
        if (!ids.length) return;
        var byId = new Map(idx.files.map(function (f) { return [f.id, f]; }));
        var matched = ids.map(function (id) { return byId.get(id); }).filter(Boolean);
        if (!matched.length) return;

        var box = document.createElement('div');
        box.className = 'cw-lecture-box';
        var heading = document.createElement('div');
        heading.className = 'cw-lecture-head';
        var strong = document.createElement('strong');
        strong.textContent = '已匹配源头课件（' + matched.length + ' 份）';
        heading.appendChild(strong);
        var cloudTag = document.createElement('span');
        cloudTag.className = 'cw-cloud-pill' + (getBaseUrl() ? ' is-live' : '');
        cloudTag.textContent = getBaseUrl() ? '云端原件直链已启用' : '待绑定云端存储地址（R2 / GCS）';
        heading.appendChild(cloudTag);
        box.appendChild(heading);

        var ul = document.createElement('ul');
        ul.className = 'cw-list';
        matched.forEach(function (file) {
          ul.appendChild(createFileRow(file, { showCourse: false, showLectures: false }));
        });
        box.appendChild(ul);
        details.appendChild(box);
      }).catch(function () { /* keep static panel intact on load error */ });
    }

    if (details.open) mountPanel();
    else details.addEventListener('toggle', function () { if (details.open) mountPanel(); }, { once: true });
  }

  /* 2. Course page original courseware explorer (#course-source-files) */
  function mountCourseExplorer() {
    var panel = document.getElementById('course-source-files');
    if (!panel) return;
    var cid = panel.dataset.course;
    var details = panel.querySelector('details');
    var body = panel.querySelector('.cw-panel-body');
    var loaded = false;

    function init() {
      if (loaded) return;
      loaded = true;
      body.textContent = '正在加载本课原始课件目录…';
      load().then(function (idx) {
        var files = idx.files.filter(function (f) { return String(f.cid) === String(cid); });
        body.replaceChildren();
        if (!files.length) {
          var empty = document.createElement('p');
          empty.className = 'sub';
          empty.textContent = '暂未索引到本课原始课件文件。';
          body.appendChild(empty);
          return;
        }
        renderExplorer(body, files, { showCourse: false, showLectures: true, courseFilter: false });
      }).catch(function (err) {
        body.textContent = err.message;
      });
    }

    if (details) {
      if (details.open) init();
      else details.addEventListener('toggle', function () { if (details.open) init(); }, { once: true });
    } else {
      init();
    }
  }

  /* 3. Home page full courseware hub (#courseware-hub) */
  function mountHomeExplorer() {
    var hub = document.getElementById('courseware-hub');
    if (!hub) return;
    var body = hub.querySelector('.cw-panel-body');
    var loaded = false;

    function init() {
      if (loaded) return;
      loaded = true;
      body.textContent = '正在加载全站原始课件目录…';
      load().then(function (idx) {
        body.replaceChildren();
        renderExplorer(body, idx.files, { showCourse: true, showLectures: true, courseFilter: true });
      }).catch(function (err) {
        body.textContent = err.message;
      });
    }

    if (hub.open) init();
    else hub.addEventListener('toggle', function () { if (hub.open) init(); }, { once: true });
  }

  function renderExplorer(container, files, opts) {
    var bar = document.createElement('div');
    bar.className = 'cw-toolbar';

    var qInput = document.createElement('input');
    qInput.type = 'search';
    qInput.className = 'cw-search';
    qInput.placeholder = '按原课件文件名、章节路径或扩展名筛选（如 Lecture、Homework、pdf）…';
    qInput.setAttribute('aria-label', '筛选原始课件');
    bar.appendChild(qInput);

    var courseSel = null;
    if (opts.courseFilter) {
      courseSel = document.createElement('select');
      courseSel.className = 'cw-select';
      courseSel.setAttribute('aria-label', '按课程筛选原课件');
      var allOpt = document.createElement('option');
      allOpt.value = '';
      allOpt.textContent = '全部课程';
      courseSel.appendChild(allOpt);
      catalogue.courses.forEach(function (c) {
        var o = document.createElement('option');
        o.value = c.id;
        o.textContent = c.title;
        courseSel.appendChild(o);
      });
      bar.appendChild(courseSel);
    }

    var catSel = document.createElement('select');
    catSel.className = 'cw-select';
    catSel.setAttribute('aria-label', '按文件类型筛选原课件');
    Object.keys(CAT_LABELS).forEach(function (k) {
      var o = document.createElement('option');
      o.value = k;
      o.textContent = CAT_LABELS[k];
      catSel.appendChild(o);
    });
    bar.appendChild(catSel);
    container.appendChild(bar);

    var statusRow = document.createElement('div');
    statusRow.className = 'cw-status-row';
    var statusText = document.createElement('span');
    statusText.className = 'sub';
    var cloudPill = document.createElement('span');
    cloudPill.className = 'cw-cloud-pill' + (getBaseUrl() ? ' is-live' : '');
    cloudPill.textContent = getBaseUrl()
      ? ('已连接云端源：' + getBaseUrl())
      : '离线目录模式（绑定 Cloudflare R2 后支持免费在线直链预览/下载）';
    statusRow.appendChild(statusText);
    statusRow.appendChild(cloudPill);
    container.appendChild(statusRow);

    var ul = document.createElement('ul');
    ul.className = 'cw-list';
    container.appendChild(ul);

    var moreBtn = document.createElement('button');
    moreBtn.type = 'button';
    moreBtn.className = 'study-button compact';
    moreBtn.textContent = '显示更多原课件';
    moreBtn.hidden = true;
    container.appendChild(moreBtn);

    var limit = 30;
    var filtered = files;

    function draw() {
      ul.replaceChildren();
      var totalSize = filtered.reduce(function (s, f) { return s + (f.size || 0); }, 0);
      statusText.textContent = '匹配 ' + filtered.length + ' / ' + files.length + ' 份原课件（共 ' + formatSize(totalSize) + '）';
      if (!filtered.length) {
        var empty = document.createElement('li');
        empty.className = 'cw-empty';
        empty.textContent = '没有符合条件的原始课件，请放宽关键词或文件类型。';
        ul.appendChild(empty);
        moreBtn.hidden = true;
        return;
      }
      filtered.slice(0, limit).forEach(function (file) {
        ul.appendChild(createFileRow(file, opts));
      });
      moreBtn.hidden = filtered.length <= limit;
    }

    function apply() {
      var q = qInput.value.trim().toLowerCase();
      var tokens = q ? q.split(/\s+/).filter(Boolean) : [];
      var cid = courseSel ? courseSel.value : '';
      var cat = catSel.value;
      limit = 30;
      filtered = files.filter(function (f) {
        if (cid && String(f.cid) !== cid) return false;
        if (cat !== 'all' && f.cat !== cat) return false;
        if (!tokens.length) return true;
        var lecText = (f.lectures || []).map(function (l) { return l.title; }).join(' ');
        var hay = (f.name + ' ' + f.rel + ' ' + f.ext + ' ' + (courseTitles.get(String(f.cid)) || '') + ' ' + lecText).toLowerCase();
        return tokens.every(function (t) { return hay.indexOf(t) !== -1; });
      });
      draw();
    }

    qInput.addEventListener('input', apply);
    catSel.addEventListener('change', apply);
    if (courseSel) courseSel.addEventListener('change', apply);
    moreBtn.addEventListener('click', function () { limit += 40; draw(); });
    apply();
  }

  /* 4. Upload / Cloud Settings page: Google Cloud Storage courseware config (#courseware-cloud) */
  function mountCloudSetup() {
    var box = document.getElementById('courseware-cloud');
    if (!box) return;
    var input = document.getElementById('gcs-base-url');
    var testBtn = document.getElementById('gcs-test');
    var saveBtn = document.getElementById('gcs-save');
    var resetBtn = document.getElementById('gcs-reset');
    var status = document.getElementById('gcs-status');
    var snippet = document.getElementById('gcs-config-snippet');
    if (!input || !testBtn || !saveBtn || !resetBtn || !status) return;

    var current = getBaseUrl();
    input.value = current;
    function updateSnippet(val) {
      if (snippet) snippet.textContent = 'coursewareBaseUrl: "' + (val || 'https://pub-xxxxxxxxxxxxxxxx.r2.dev/courseware') + '",';
    }
    updateSnippet(current);
    status.textContent = current
      ? ('当前已启用云端课件地址：' + current + (getOverride() ? '（本机覆盖）' : '（来自 assets/config.js）'))
      : '尚未配置云端课件公开地址（推荐 Cloudflare R2，10 GB 免费 + 0 流量费）。配置后，全站原始课件均可直接在线预览与下载。';

    input.addEventListener('input', function () {
      updateSnippet(input.value.trim().replace(/\/+$/, ''));
    });

    testBtn.addEventListener('click', function () {
      var clean;
      try { clean = validateBaseUrl(input.value); } catch (err) {
        status.textContent = '地址格式无效：' + err.message;
        return;
      }
      if (!clean) { status.textContent = '请先输入 https://pub-xxxx.r2.dev/courseware（或其他 HTTPS 公开前缀）'; return; }
      status.textContent = '正在抽检云端课件可达性…';
      load().then(function (idx) {
        var sample = idx.files[0];
        var probeUrl = clean + '/' + encodeURIComponent(String(sample.cid)) + '/' + encodePath(sample.rel);
        return fetch(probeUrl, { method: 'HEAD', mode: 'cors', signal: AbortSignal.timeout(10000) }).then(function (res) {
          if (res.ok) {
            status.textContent = '连接成功（HTTP ' + res.status + '）：已验证 ' + sample.name + ' 可公开访问！可点击「保存本机生效」或写入 assets/config.js。';
          } else {
            status.textContent = '云端返回 HTTP ' + res.status + '（抽检文件：' + sample.cid + '/' + sample.rel + '）。请确认已运行 tools/sync_r2.py 并开启 r2.dev 公开访问与 CORS。';
          }
        });
      }).catch(function (err) {
        status.textContent = '连接检查未通过：' + err.message + '（请确认已在 R2 存储桶设置中开启公开访问并按 SETUP_R2.md 配置 CORS）。';
      });
    });

    saveBtn.addEventListener('click', function () {
      try {
        var clean = setOverride(input.value);
        status.textContent = '已在本机浏览器生效：' + clean + '，正在刷新页面…';
        location.reload();
      } catch (err) {
        status.textContent = err.message;
      }
    });

    resetBtn.addEventListener('click', function () {
      clearOverride();
      location.reload();
    });
  }

  window.LUTCourseware = {
    load: load,
    getBaseUrl: getBaseUrl,
    fileUrl: fileUrl,
    formatSize: formatSize,
    validateBaseUrl: validateBaseUrl,
    setOverride: setOverride,
    clearOverride: clearOverride
  };

  enhanceLectureSources();
  mountCourseExplorer();
  mountHomeExplorer();
  mountCloudSetup();
})();

;
/* quick-nav.js */
(function () {
  'use strict';
  var app = window.LUTLearning;
  var catalogue = window.LUT_LEARNING_CATALOG || { courses: [], lectures: [] };
  var main = document.querySelector('[data-site-prefix]');
  var prefix = main ? (main.dataset.sitePrefix || '') : '';
  var moduleName = document.body.dataset.module || '';

  function isEditable(el) {
    if (!el) return false;
    var tag = el.tagName;
    return tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || el.isContentEditable;
  }

  /* =====================================================================
   * 1. Global Command Palette (Ctrl+K / Cmd+K / '/' / header search button)
   * ===================================================================== */
  var MODULES = [
    { type: '模块', title: '课程总览', sub: '全部 15 门课程、全文搜索与学习看板', url: 'index.html' },
    { type: '模块', title: '期末考点清单', sub: '按必考 / 易错 / 进阶集中复习与进度勾选', url: 'review.html' },
    { type: '模块', title: '知识拓展', sub: '全站课内拓展提示框与原始文件补充对照', url: 'extend.html' },
    { type: '模块', title: '全站合订本', sub: '全站与分课程连排阅读版', url: 'all.html' },
    { type: '模块', title: '上传资料', sub: '按课程章节上传课件或撰写补充笔记', url: 'upload.html' }
  ];

  var palette = document.createElement('dialog');
  palette.className = 'cmd-palette';
  palette.setAttribute('aria-label', '全站快捷跳转与搜索');
  palette.setAttribute('closedby', 'any');

  var head = document.createElement('div');
  head.className = 'cmd-head';
  var input = document.createElement('input');
  input.type = 'search';
  input.className = 'cmd-input';
  input.placeholder = '输入课程名、讲义标题、关键词，或回车搜正文…';
  input.setAttribute('aria-label', '快捷跳转与全站搜索');
  input.autocomplete = 'off';
  input.spellcheck = false;
  var closeBtn = document.createElement('button');
  closeBtn.type = 'button';
  closeBtn.className = 'cmd-close';
  closeBtn.textContent = 'Esc';
  closeBtn.setAttribute('aria-label', '关闭快捷搜索');
  head.appendChild(input);
  head.appendChild(closeBtn);

  var modeBar = document.createElement('div');
  modeBar.className = 'cmd-mode-bar';
  var modeQuick = document.createElement('button');
  modeQuick.type = 'button';
  modeQuick.className = 'cmd-mode is-active';
  modeQuick.textContent = '快捷跳转（课程 / 讲义）';
  var modeFull = document.createElement('button');
  modeFull.type = 'button';
  modeFull.className = 'cmd-mode';
  modeFull.textContent = '全文正文搜索';
  var modeFiles = document.createElement('button');
  modeFiles.type = 'button';
  modeFiles.className = 'cmd-mode';
  modeFiles.textContent = '原版课件';
  var modeHint = document.createElement('span');
  modeHint.className = 'cmd-hint';
  modeHint.textContent = '↑↓ 选择 · Enter 打开';
  modeBar.appendChild(modeQuick);
  modeBar.appendChild(modeFull);
  modeBar.appendChild(modeFiles);
  modeBar.appendChild(modeHint);

  var statusLine = document.createElement('p');
  statusLine.className = 'cmd-status';
  statusLine.setAttribute('role', 'status');

  var list = document.createElement('ul');
  list.className = 'cmd-list';
  list.setAttribute('role', 'listbox');

  palette.appendChild(head);
  palette.appendChild(modeBar);
  palette.appendChild(statusLine);
  palette.appendChild(list);
  document.body.appendChild(palette);

  if (!('closedBy' in HTMLDialogElement.prototype)) {
    var outsideDown = false;
    function isOut(e) {
      var r = palette.getBoundingClientRect();
      return e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom;
    }
    palette.addEventListener('pointerdown', function (e) { outsideDown = isOut(e); });
    palette.addEventListener('pointerup', function (e) { if (outsideDown && isOut(e)) palette.close(); });
  }

  var paletteMode = 'quick';
  var activeIndex = -1;
  var fullIndexPromise = null;
  var searchTimer = null;

  function loadFullIndex() {
    if (window.LUT_SEARCH_DATA) return Promise.resolve(window.LUT_SEARCH_DATA.documents);
    if (!fullIndexPromise) {
      fullIndexPromise = new Promise(function (resolve, reject) {
        var s = document.createElement('script');
        s.src = prefix + 'data/search-index.js';
        s.onload = function () {
          if (window.LUT_SEARCH_DATA) resolve(window.LUT_SEARCH_DATA.documents);
          else reject(new Error('全文索引格式异常'));
        };
        s.onerror = function () {
          fullIndexPromise = null;
          reject(new Error('未能加载全文索引，请先确认站点文件完整。'));
        };
        document.head.appendChild(s);
      });
    }
    return fullIndexPromise;
  }

  function setMode(next) {
    paletteMode = next;
    modeQuick.classList.toggle('is-active', next === 'quick');
    modeFull.classList.toggle('is-active', next === 'full');
    modeFiles.classList.toggle('is-active', next === 'files');
    renderPalette();
  }

  function highlightActive(idx) {
    var items = Array.from(list.querySelectorAll('a.cmd-item'));
    if (!items.length) { activeIndex = -1; return; }
    activeIndex = Math.max(0, Math.min(idx, items.length - 1));
    items.forEach(function (a, i) {
      a.classList.toggle('is-selected', i === activeIndex);
      if (i === activeIndex) a.scrollIntoView({ block: 'nearest' });
    });
  }

  function buildQuickItems(rawQuery) {
    var q = (rawQuery || '').trim().toLowerCase();
    var tokens = q ? q.split(/\s+/).filter(Boolean) : [];
    var rows = [];

    if (!tokens.length) {
      if (app) {
        var data = app.store.read();
        var last = app.entries.get(data.lastLecture);
        if (last) {
          rows.push({
            type: '继续学习',
            title: last.title,
            sub: last.courseTitle + ' · ' + last.part,
            href: prefix + last.url + '?resume=1'
          });
        }
      }
      MODULES.forEach(function (m) {
        rows.push({ type: m.type, title: m.title, sub: m.sub, href: prefix + m.url });
      });
      catalogue.courses.forEach(function (c) {
        rows.push({ type: '课程', title: c.title, sub: '课程 ID: ' + c.id, href: prefix + 'c/' + c.id + '/index.html' });
      });
      return rows;
    }

    function matchAll(hay) {
      return tokens.every(function (t) { return hay.indexOf(t) !== -1; });
    }

    MODULES.forEach(function (m) {
      if (matchAll((m.title + ' ' + m.sub).toLowerCase())) {
        rows.push({ type: m.type, title: m.title, sub: m.sub, href: prefix + m.url, score: 30 });
      }
    });
    catalogue.courses.forEach(function (c) {
      var hay = (c.id + ' ' + c.title).toLowerCase();
      if (matchAll(hay)) {
        rows.push({ type: '课程', title: c.title, sub: '课程目录 · ID ' + c.id, href: prefix + 'c/' + c.id + '/index.html', score: 24 });
      }
    });
    catalogue.lectures.forEach(function (l) {
      var hay = (l.course + ' ' + l.courseTitle + ' ' + l.part + ' ' + l.title).toLowerCase();
      if (matchAll(hay)) {
        var score = l.title.toLowerCase().indexOf(q) !== -1 ? 20 : 10;
        rows.push({ type: '讲义', title: l.title, sub: l.courseTitle + ' / ' + l.part, href: prefix + l.url, score: score });
      }
    });
    rows.sort(function (a, b) { return (b.score || 0) - (a.score || 0); });
    return rows.slice(0, 40);
  }

  function renderItemList(rows) {
    list.replaceChildren();
    rows.forEach(function (row) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.className = 'cmd-item';
      a.href = row.href;
      if (row.external) { a.target = '_blank'; a.rel = 'noopener'; }
      var badge = document.createElement('span');
      badge.className = 'cmd-type';
      badge.textContent = row.type;
      var mainCol = document.createElement('span');
      mainCol.className = 'cmd-main';
      var title = document.createElement('strong');
      title.textContent = row.title;
      var sub = document.createElement('span');
      sub.className = 'cmd-sub';
      sub.textContent = row.sub;
      mainCol.appendChild(title);
      mainCol.appendChild(sub);
      a.appendChild(badge);
      a.appendChild(mainCol);
      a.addEventListener('click', function () { palette.close(); });
      li.appendChild(a);
      list.appendChild(li);
    });
    highlightActive(rows.length ? 0 : -1);
  }

  function renderPalette() {
    var q = input.value.trim();
    if (paletteMode === 'quick') {
      var rows = buildQuickItems(q);
      renderItemList(rows);
      if (!q) {
        statusLine.textContent = '显示快捷入口与全部 ' + catalogue.courses.length + ' 门课程；输入关键词可筛选 133 讲标题。';
      } else if (rows.length) {
        statusLine.textContent = '命中 ' + rows.length + ' 项标题；需要查正文/公式/例题请切换到「全文正文搜索」。';
      } else {
        statusLine.textContent = '标题未命中，可点击上方「全文正文搜索」在 3,300+ 正文小节中查找。';
      }
      return;
    }

    if (paletteMode === 'files') {
      if (!window.LUTCourseware) { statusLine.textContent = '课件索引模块未就绪。'; return; }
      statusLine.textContent = '正在加载原始课件索引…';
      window.LUTCourseware.load().then(function (idx) {
        if (paletteMode !== 'files' || input.value.trim() !== q) return;
        var tokens = q ? q.toLowerCase().split(/\s+/).filter(Boolean) : [];
        var cMap = new Map(catalogue.courses.map(function (c) { return [String(c.id), c.title]; }));
        var hits = idx.files.filter(function (f) {
          if (!tokens.length) return true;
          var lecText = (f.lectures || []).map(function (l) { return l.title; }).join(' ');
          var hay = (f.name + ' ' + f.rel + ' ' + f.ext + ' ' + (cMap.get(String(f.cid)) || '') + ' ' + lecText).toLowerCase();
          return tokens.every(function (t) { return hay.indexOf(t) !== -1; });
        });
        var rows = hits.slice(0, 35).map(function (f) {
          var cloudUrl = window.LUTCourseware.fileUrl(f);
          var firstLec = (f.lectures && f.lectures[0]) ? (prefix + 'c/' + f.cid + '/' + f.lectures[0].slug + '.html') : (prefix + 'c/' + f.cid + '/index.html#course-source-files');
          var lecHint = (f.lectures && f.lectures.length) ? (' · 对应讲义：' + f.lectures[0].title) : '';
          return {
            type: (f.ext || 'FILE').replace(/^\./, '').toUpperCase() || 'FILE',
            title: f.name,
            sub: (cMap.get(String(f.cid)) || f.cid) + ' / ' + f.rel + ' (' + window.LUTCourseware.formatSize(f.size) + ')' + lecHint,
            href: cloudUrl || firstLec,
            external: !!cloudUrl
          };
        });
        renderItemList(rows);
        statusLine.textContent = hits.length
          ? ('匹配 ' + hits.length + ' / ' + idx.totalFiles + ' 份原课件' + (window.LUTCourseware.getBaseUrl() ? '（点击直接打开云端原件）' : '（点击跳转对应讲义/课程源课件表；配置云端后直开原件）'))
          : '未找到匹配的原始课件文件名。';
      }).catch(function (err) {
        statusLine.textContent = err.message;
      });
      return;
    }

    if (!q) {
      list.replaceChildren();
      activeIndex = -1;
      statusLine.textContent = '输入关键词搜索全站正文、英文术语、公式、例题与练习答案。';
      return;
    }
    statusLine.textContent = '正在检索全站正文…';
    loadFullIndex().then(function (docs) {
      if (paletteMode !== 'full' || input.value.trim() !== q) return;
      var hits = window.LUTSearch ? window.LUTSearch.search(docs, q, {}) : [];
      var rows = hits.slice(0, 30).map(function (h) {
        var doc = h.doc;
        var pieces = doc.url.split('#');
        return {
          type: '正文',
          title: doc.lectureTitle + ' · ' + doc.title,
          sub: doc.courseTitle + ' — ' + (window.LUTSearch ? window.LUTSearch.snippet(doc.text, q, 95) : ''),
          href: prefix + pieces[0] + '?find=' + encodeURIComponent(q) + '#' + pieces[1]
        };
      });
      renderItemList(rows);
      statusLine.textContent = hits.length
        ? ('找到 ' + hits.length + ' 处正文匹配' + (hits.length > 30 ? '（显示前 30 条）' : '') + '，点击直达并高亮。')
        : '正文未找到匹配，建议缩短关键词或换用英文术语。';
    }).catch(function (err) {
      statusLine.textContent = err.message;
    });
  }

  function openPalette(initialMode) {
    if (typeof palette.showModal !== 'function') return false;
    if (palette.open) return true;
    palette.showModal();
    if (initialMode) setMode(initialMode);
    else renderPalette();
    input.focus();
    input.select();
    return true;
  }

  modeQuick.addEventListener('click', function () { setMode('quick'); input.focus(); });
  modeFull.addEventListener('click', function () { setMode('full'); input.focus(); });
  modeFiles.addEventListener('click', function () { setMode('files'); input.focus(); });
  closeBtn.addEventListener('click', function () { palette.close(); });
  input.addEventListener('input', function () {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(renderPalette, paletteMode === 'full' ? 180 : 60);
  });
  input.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
      event.preventDefault();
      palette.close();
      return;
    }
    if (event.key === 'ArrowDown') {
      event.preventDefault();
      highlightActive(activeIndex + 1);
    } else if (event.key === 'ArrowUp') {
      event.preventDefault();
      highlightActive(activeIndex - 1);
    } else if (event.key === 'Enter') {
      var selected = list.querySelector('a.cmd-item.is-selected');
      if (selected) {
        event.preventDefault();
        palette.close();
        location.href = selected.href;
      } else if (paletteMode === 'quick' && input.value.trim()) {
        event.preventDefault();
        setMode('full');
      }
    }
  });

  var headerSearch = document.querySelector('.search-shortcut');
  if (headerSearch) {
    headerSearch.addEventListener('click', function (event) {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      if (openPalette('quick')) event.preventDefault();
    });
  }

  var fabSearch = document.createElement('button');
  fabSearch.id = 'fab-search';
  fabSearch.className = 'fab-search';
  fabSearch.type = 'button';
  fabSearch.setAttribute('aria-label', '全站搜索与原版课件查询');
  fabSearch.title = '全站搜索 / 原版课件 (Ctrl+K)';
  var svgNS = 'http://www.w3.org/2000/svg';
  var fabSvg = document.createElementNS(svgNS, 'svg');
  fabSvg.setAttribute('viewBox', '0 0 24 24');
  fabSvg.setAttribute('width', '18');
  fabSvg.setAttribute('height', '18');
  fabSvg.setAttribute('fill', 'none');
  fabSvg.setAttribute('stroke', 'currentColor');
  fabSvg.setAttribute('stroke-width', '2.1');
  fabSvg.setAttribute('stroke-linecap', 'round');
  fabSvg.setAttribute('stroke-linejoin', 'round');
  fabSvg.setAttribute('aria-hidden', 'true');
  var circle = document.createElementNS(svgNS, 'circle');
  circle.setAttribute('cx', '11');
  circle.setAttribute('cy', '11');
  circle.setAttribute('r', '7');
  var line = document.createElementNS(svgNS, 'line');
  line.setAttribute('x1', '21');
  line.setAttribute('y1', '21');
  line.setAttribute('x2', '16.65');
  line.setAttribute('y2', '16.65');
  fabSvg.appendChild(circle);
  fabSvg.appendChild(line);
  fabSearch.appendChild(fabSvg);
  fabSearch.addEventListener('click', function () { openPalette('quick'); });
  document.body.appendChild(fabSearch);

  addEventListener('keydown', function (event) {
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
      event.preventDefault();
      if (palette.open) palette.close();
      else openPalette('quick');
      return;
    }
    if (document.querySelector('dialog[open]') || isEditable(document.activeElement)) return;
    if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey) {
      event.preventDefault();
      openPalette('quick');
      return;
    }
    if (event.key === '[' || (event.altKey && event.key === 'ArrowLeft')) {
      var prevLink = document.querySelector('.sequence-nav a[data-sequence="previous"]');
      if (prevLink) { event.preventDefault(); location.href = prevLink.href; }
    } else if (event.key === ']' || (event.altKey && event.key === 'ArrowRight')) {
      var nextLink = document.querySelector('.sequence-nav a[data-sequence="next"]');
      if (nextLink) { event.preventDefault(); location.href = nextLink.href; }
    } else if (event.key === 'f' && !event.ctrlKey && !event.metaKey && !event.altKey) {
      var focusBtn = document.getElementById('focus-reading');
      if (focusBtn) { event.preventDefault(); focusBtn.click(); }
    }
  });

  /* =====================================================================
   * 2. Sidebar Cross-Course Switcher + Sidebar Study-Status Dots
   * ===================================================================== */
  var dirEl = document.querySelector('.page-directory');
  var currentCourseId = '';
  var courseMatch = location.pathname.match(/\/c\/([^/]+)\//);
  if (courseMatch) currentCourseId = decodeURIComponent(courseMatch[1]);
  else {
    var art = document.querySelector('article[data-lecture-id]');
    if (art) currentCourseId = art.dataset.lectureId.split('/')[0];
    else {
      var prog = document.querySelector('[data-progress-course]');
      if (prog && prefix === '../../') currentCourseId = prog.dataset.progressCourse;
    }
  }

  if (dirEl && prefix === '../../' && catalogue.courses.length > 1) {
    var switcher = document.createElement('div');
    switcher.className = 'course-switcher';
    var swLabel = document.createElement('label');
    swLabel.textContent = '切换其他课程';
    var swSelect = document.createElement('select');
    swSelect.setAttribute('aria-label', '快速切换到其他课程');
    catalogue.courses.forEach(function (c) {
      var opt = document.createElement('option');
      opt.value = c.id;
      opt.textContent = c.title;
      if (c.id === currentCourseId) opt.selected = true;
      swSelect.appendChild(opt);
    });
    swSelect.addEventListener('change', function () {
      if (swSelect.value && swSelect.value !== currentCourseId) {
        location.href = '../' + encodeURIComponent(swSelect.value) + '/index.html';
      }
    });
    swLabel.appendChild(swSelect);
    switcher.appendChild(swLabel);
    dirEl.appendChild(switcher);
  }

  function syncDirectoryDots() {
    if (!app || !currentCourseId) return;
    var courseNav = document.querySelector('nav[aria-label="课程目录"]');
    if (!courseNav) return;
    var lectures = app.store.read().lectures;
    courseNav.querySelectorAll('a.directory-link').forEach(function (a) {
      var href = a.getAttribute('href') || '';
      if (!href.endsWith('.html') || href === 'index.html' || /^part-\d+\.html$/.test(href)) return;
      var slug = href.slice(0, -5);
      var status = (lectures[currentCourseId + '/' + slug] || {}).status || 'new';
      var dot = a.querySelector('.dir-status-dot');
      if (!dot) {
        dot = document.createElement('span');
        dot.className = 'dir-status-dot';
        dot.setAttribute('aria-hidden', 'true');
        a.prepend(dot);
      }
      dot.dataset.status = status;
      dot.title = app.labels[status] || '';
    });
  }
  syncDirectoryDots();
  addEventListener('lut:learning-changed', syncDirectoryDots);

  /* =====================================================================
   * 3. Home Course Category Filters & Expand/Collapse Chapters
   * ===================================================================== */
  var filterBar = document.getElementById('course-filter-bar');
  if (filterBar) {
    var catBtns = Array.from(filterBar.querySelectorAll('button[data-cat]'));
    var courseCards = Array.from(document.querySelectorAll('.courses .ccard'));
    var activeCat = 'all';

    function applyHomeFilter() {
      var data = app ? app.store.read() : { lectures: {} };
      courseCards.forEach(function (card) {
        var cat = card.dataset.category || '';
        var cid = card.id.slice(2);
        var visible = true;
        if (activeCat === 'pending') {
          var rows = catalogue.lectures.filter(function (e) { return e.course === cid; });
          var done = rows.filter(function (e) { return (data.lectures[e.id] || {}).status === 'mastered'; }).length;
          visible = done < rows.length;
        } else if (activeCat !== 'all') {
          visible = (cat === activeCat);
        }
        card.hidden = !visible;
        var navLink = document.querySelector('[data-scrollspy] a[href="#' + card.id + '"]');
        if (navLink) navLink.closest('li').hidden = !visible;
      });
    }

    catBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        activeCat = btn.dataset.cat;
        catBtns.forEach(function (b) {
          var on = b === btn;
          b.classList.toggle('is-active', on);
          b.setAttribute('aria-pressed', String(on));
        });
        applyHomeFilter();
      });
    });

    var toggleAllBtn = document.getElementById('toggle-all-chapters');
    if (toggleAllBtn) {
      toggleAllBtn.addEventListener('click', function () {
        var dets = Array.from(document.querySelectorAll('.ccard-chapters'));
        var anyClosed = dets.some(function (d) { return !d.open; });
        dets.forEach(function (d) { d.open = anyClosed; });
        toggleAllBtn.textContent = anyClosed ? '收起全部章节' : '展开全部章节';
        toggleAllBtn.setAttribute('aria-expanded', String(anyClosed));
      });
    }
  }

  /* =====================================================================
   * 4. Review Page Interactive Priority / Course / Unreviewed Filter
   * ===================================================================== */
  var revBar = document.getElementById('review-filter-bar');
  if (revBar && moduleName === 'review') {
    var revModeBtns = Array.from(revBar.querySelectorAll('button[data-rev-mode]'));
    var revCourseSel = document.getElementById('review-course-filter');
    var revUnrevChk = document.getElementById('review-only-unreviewed');
    var revStatus = document.getElementById('review-filter-status');
    var revMode = 'all';

    function updateCourseTickCounts() {
      document.querySelectorAll('.qcourse').forEach(function (card) {
        var boxes = Array.from(card.querySelectorAll('input.tick'));
        var done = boxes.filter(function (b) { return b.checked; }).length;
        var badge = card.querySelector('.qcourse-done');
        if (badge) badge.textContent = done + ' / ' + boxes.length + ' 已复习';
      });
    }

    function applyReviewFilter() {
      var data = app ? app.store.read() : { lectures: {} };
      var courseVal = revCourseSel ? revCourseSel.value : '';
      var onlyUnrev = revUnrevChk ? revUnrevChk.checked : false;
      var shownLecs = 0;
      var totalLecs = 0;

      document.querySelectorAll('.qcourse').forEach(function (qc) {
        qc.hidden = !!(courseVal && qc.dataset.course !== courseVal);
      });

      document.querySelectorAll('.revcourse').forEach(function (sec) {
        var cid = sec.id.slice(2);
        var courseMatch = !courseVal || cid === courseVal;
        if (!courseMatch) { sec.hidden = true; return; }
        var anyLecVisible = false;
        var lecs = Array.from(sec.querySelectorAll('.revlec'));
        lecs.forEach(function (lec) {
          totalLecs++;
          var studyId = lec.dataset.studyId || '';
          var mastered = studyId && (data.lectures[studyId] || {}).status === 'mastered';
          if (onlyUnrev && mastered) { lec.hidden = true; return; }

          var items = Array.from(lec.querySelectorAll('.revbody li, .revbody .callout, .revbody p'));
          var hasBadgeItems = items.some(function (el) { return el.querySelector('.badge'); });
          if (revMode === 'all' || !hasBadgeItems) {
            items.forEach(function (el) { el.hidden = false; });
            lec.hidden = false;
            anyLecVisible = true;
            shownLecs++;
          } else {
            var cls = revMode === 'must' ? '.badge.bad' : (revMode === 'warn' ? '.badge.warn' : '.badge.mute');
            var matched = 0;
            items.forEach(function (el) {
              if (!el.querySelector('.badge')) { el.hidden = false; return; }
              var hit = !!el.querySelector(cls);
              el.hidden = !hit;
              if (hit) matched++;
            });
            lec.hidden = matched === 0;
            if (matched > 0) { anyLecVisible = true; shownLecs++; }
          }
        });
        sec.hidden = !anyLecVisible;
      });

      if (revStatus) {
        var modeNames = { all: '全部考点', must: '仅看必考', warn: '仅看易错', adv: '仅看进阶' };
        revStatus.textContent = '当前筛选：' + modeNames[revMode]
          + (onlyUnrev ? ' · 仅未复习' : '')
          + ' — 显示 ' + shownLecs + ' / ' + totalLecs + ' 讲';
      }
      updateCourseTickCounts();
    }

    revModeBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        revMode = btn.dataset.revMode;
        revModeBtns.forEach(function (b) {
          var on = b === btn;
          b.classList.toggle('is-active', on);
          b.setAttribute('aria-pressed', String(on));
        });
        applyReviewFilter();
      });
    });
    if (revCourseSel) revCourseSel.addEventListener('change', applyReviewFilter);
    if (revUnrevChk) revUnrevChk.addEventListener('change', applyReviewFilter);
    addEventListener('lut:learning-changed', function () {
      updateCourseTickCounts();
      if (revUnrevChk && revUnrevChk.checked) applyReviewFilter();
    });
    applyReviewFilter();
  }

  /* =====================================================================
   * 5. Extension Page Interactive Course & Kind Filter
   * ===================================================================== */
  var extBar = document.getElementById('extend-filter-bar');
  if (extBar && moduleName === 'extension') {
    var extCourseSel = document.getElementById('extend-course-filter');
    var extKindBtns = Array.from(extBar.querySelectorAll('button[data-ext-kind]'));
    var extStatus = document.getElementById('extend-filter-status');
    var extKind = 'all';

    function applyExtendFilter() {
      var cid = extCourseSel ? extCourseSel.value : '';
      var shown = 0;
      document.querySelectorAll('.revcourse').forEach(function (sec) {
        var matchCourse = !cid || sec.id === ('e-' + cid);
        sec.hidden = !matchCourse;
        if (!matchCourse) return;
        shown++;
        var ideas = sec.querySelectorAll('.extidea, [id$="-ideas"]');
        var notes = sec.querySelectorAll('.table-scroll, [id$="-notes"]');
        ideas.forEach(function (el) { el.hidden = extKind === 'notes'; });
        notes.forEach(function (el) { el.hidden = extKind === 'ideas'; });
      });
      if (extStatus) extStatus.textContent = '当前显示 ' + shown + ' 门课程的知识拓展';
    }

    extKindBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        extKind = btn.dataset.extKind;
        extKindBtns.forEach(function (b) {
          var on = b === btn;
          b.classList.toggle('is-active', on);
          b.setAttribute('aria-pressed', String(on));
        });
        applyExtendFilter();
      });
    });
    if (extCourseSel) extCourseSel.addEventListener('change', applyExtendFilter);
    applyExtendFilter();
  }
})();
