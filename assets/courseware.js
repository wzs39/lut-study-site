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
