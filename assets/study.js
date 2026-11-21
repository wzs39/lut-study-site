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
