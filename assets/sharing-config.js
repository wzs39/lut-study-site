(function(root,factory){
  var api=factory();
  if(typeof module==='object'&&module.exports)module.exports=api;
  else{root.LUTSharingConfig=api;api.mount();}
})(typeof globalThis!=='undefined'?globalThis:this,function(){
  'use strict';
  var KEY='lut-public-sharing-v1';
  function headers(key,extra){
    var result={apikey:key};
    if(!key.startsWith('sb_publishable_'))result.Authorization='Bearer '+key;
    return Object.assign(result,extra||{});
  }
  function validate(value){
    var url=new URL(String(value.supabaseUrl||'').trim()),key=String(value.supabaseAnonKey||'').trim();
    if(url.protocol!=='https:'||url.username||url.password||url.search||url.hash||!['','/'].includes(url.pathname))throw new Error('项目地址须为 HTTPS 根地址，不含账号、路径或参数。');
    var publicKey=/^sb_publishable_[A-Za-z0-9_-]+$/.test(key);
    if(!publicKey&&key.split('.').length===3){
      try{var payload=JSON.parse(atob(key.split('.')[1].replace(/-/g,'+').replace(/_/g,'/')));publicKey=payload.role==='anon';}catch(_){}
    }
    if(!publicKey)throw new Error('请使用公开 publishable / anon 密钥；服务端 secret / service_role 密钥不得填入网页。');
    return {supabaseUrl:url.origin,supabaseAnonKey:key};
  }
  function mount(){
    var base=window.STUDY_SITE_CONFIG||{},saved=null,problem='';
    try{var raw=localStorage.getItem(KEY);if(raw)saved=validate(JSON.parse(raw));}catch(error){problem='本机连接设置未采用：'+error.message;}
    var current=Object.assign({},base,saved||{});
    if(current.supabaseUrl||current.supabaseAnonKey){
      try{Object.assign(current,validate(current));}catch(error){problem='云端配置未采用：'+error.message;current.supabaseUrl='';current.supabaseAnonKey='';}
    }
    window.STUDY_SITE_CONFIG=current;
    var container=document.getElementById('sharing-setup');if(!container)return;
    var url=document.getElementById('sharing-url'),key=document.getElementById('sharing-key'),status=document.getElementById('sharing-status');
    url.value=current.supabaseUrl||'';key.value=current.supabaseAnonKey||'';
    status.textContent=problem||(current.supabaseUrl?'已有配置；可执行只读连接检查。':'尚未连接云端，当前发布仅保存在本机浏览器。');
    var checked='';
    function values(){return validate({supabaseUrl:url.value,supabaseAnonKey:key.value});}
    function signature(value){return JSON.stringify(value);}
    container.addEventListener('input',function(){checked='';document.getElementById('sharing-save').disabled=true;});
    document.getElementById('sharing-test').addEventListener('click',async function(){
      checked='';document.getElementById('sharing-save').disabled=true;
      try{
        var config=values();status.textContent='正在只读检查资料表…';
        var response=await fetch(config.supabaseUrl+'/rest/v1/'+encodeURIComponent(current.tableName||'chapter_materials')+'?select=id&limit=1',{
          headers:headers(config.supabaseAnonKey),signal:AbortSignal.timeout(10000),redirect:'error'});
        if(!response.ok)throw new Error('资料表返回 HTTP '+response.status+'，请检查建表和读取权限。');
        if(!Array.isArray(await response.json()))throw new Error('资料表响应格式不正确。');
        if(signature(values())!==signature(config))throw new Error('检查期间配置发生变化，请重新检查。');
        checked=signature(config);document.getElementById('sharing-save').disabled=false;
        status.textContent='读取连接通过。尚未验证写入权限；保存后仅实际发布成功才表示云端已收录。';
      }catch(error){status.textContent='连接未通过：'+error.message;}
    });
    document.getElementById('sharing-save').addEventListener('click',function(){
      try{var config=values();if(checked!==signature(config))throw new Error('请先通过只读连接检查。');localStorage.setItem(KEY,JSON.stringify(config));location.reload();}
      catch(error){status.textContent='设置未保存：'+error.message;}
    });
    document.getElementById('sharing-reset').addEventListener('click',function(){
      try{localStorage.removeItem(KEY);location.reload();}catch(error){status.textContent='设置未清除：'+error.message;}
    });
  }
  return {validate:validate,headers:headers,mount:mount};
});
