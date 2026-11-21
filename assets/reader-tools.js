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
