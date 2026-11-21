(function () {
  'use strict';
  var form = document.getElementById('search-form');
  if (!form) return;
  var query = document.getElementById('q'), course = document.getElementById('search-course');
  var kind = document.getElementById('search-kind'), status = document.getElementById('search-status');
  var results = document.getElementById('search-results'), list = document.getElementById('search-result-list');
  var more = document.getElementById('search-more'), cards = Array.from(document.querySelectorAll('.ccard'));
  var request = 0, timer, loading, matches = [], limit = 30;
  function load() {
    if (window.LUT_SEARCH_DATA) return Promise.resolve(window.LUT_SEARCH_DATA.documents);
    if (!loading) loading = new Promise(function (resolve, reject) {
      var script = document.createElement('script'); script.src = 'data/search-index.js';
      script.onload = function () { resolve(window.LUT_SEARCH_DATA.documents); };
      script.onerror = function () { loading = null; reject(new Error('搜索索引尚未加载，请确认站点文件完整后重试。')); };
      document.head.appendChild(script);
    });
    return loading;
  }
  function appendText(parent, text, words) {
    LUTSearch.segments(text, words).forEach(function (part) {
      if (part.match) { var mark = document.createElement('mark'); mark.textContent = part.text; parent.appendChild(mark); }
      else parent.appendChild(document.createTextNode(part.text));
    });
  }
  function filterCards(ids) {
    cards.forEach(function (card) {
      var id = card.id.slice(2), visible = (!course.value || id === course.value) && (!ids || ids.has(id));
      card.hidden = !visible;
      var link = document.querySelector('[data-scrollspy] a[href="#' + card.id + '"]');
      if (link) link.closest('li').hidden = !visible;
    });
  }
  function render() {
    list.replaceChildren();
    matches.slice(0,limit).forEach(function (item) {
      var doc = item.doc, row = document.createElement('li'), a = document.createElement('a');
      var pieces = doc.url.split('#'); a.href = pieces[0] + '?find=' + encodeURIComponent(query.value.trim()) + '#' + pieces[1];
      appendText(a, doc.lectureTitle + ' · ' + doc.title, query.value); row.appendChild(a);
      var context = document.createElement('p'); context.className = 'search-context';
      context.textContent = doc.courseTitle + ' / ' + doc.part; row.appendChild(context);
      var excerpt = document.createElement('p'); appendText(excerpt, LUTSearch.snippet(doc.text,query.value,160),query.value); row.appendChild(excerpt);
      list.appendChild(row);
    });
    more.hidden = matches.length <= limit;
  }
  function updateURL() {
    try {
      var url = new URL(location.href);
      [['q',query.value.trim()],['course',course.value],['kind',kind.value]].forEach(function (entry) {
        if (entry[1]) url.searchParams.set(entry[0],entry[1]); else url.searchParams.delete(entry[0]);
      });
      history.replaceState(null,'',url);
    } catch (_) { /* Search remains functional when file:// history writes are restricted. */ }
  }
  function run() {
    var sequence = ++request, value = query.value.trim(); updateURL(); limit = 30;
    if (!value) { results.hidden = true; list.replaceChildren(); filterCards(null); status.textContent = '搜索覆盖正文、术语、例题与练习答案，输入关键词开始。'; return; }
    status.textContent = '正在搜索讲义全文…';
    load().then(function (documents) {
      if (sequence !== request) return;
      matches = LUTSearch.search(documents,value,{course:course.value,kind:kind.value});
      results.hidden = false; render();
      var ids = new Set(matches.map(function (item) { return item.doc.course; })); filterCards(ids);
      status.textContent = matches.length ? ('找到 ' + matches.length + ' 个小节，涉及 ' + ids.size + ' 门课程。') : '没有匹配结果，请换用较短关键词或放宽课程与板块筛选。';
    }).catch(function (error) { if(sequence === request) status.textContent = error.message; });
  }
  query.addEventListener('input',function (event) { if(event.isComposing)return; clearTimeout(timer); timer=setTimeout(run,180); });
  query.addEventListener('compositionend',function(){clearTimeout(timer);timer=setTimeout(run,180);});
  form.addEventListener('submit',function(event){event.preventDefault();clearTimeout(timer);run();});
  [course,kind].forEach(function (select) { select.addEventListener('change',run); });
  document.getElementById('search-clear').addEventListener('click',function(){query.value='';course.value='';kind.value='';run();query.focus();});
  more.addEventListener('click',function(){limit+=30;render();});
  var parameters = new URLSearchParams(location.search);
  query.value = (parameters.get('q') || '').slice(0,160); course.value=parameters.get('course') || ''; kind.value=parameters.get('kind') || '';
  if(query.value || course.value)run();
})();
