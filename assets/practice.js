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
