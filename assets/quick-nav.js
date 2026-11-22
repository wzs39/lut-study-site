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
