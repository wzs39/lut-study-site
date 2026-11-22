/* One disclosure/navigation contract for every static page. Inlined by build.py. */
(function () {
  'use strict';
  var root = document.documentElement;
  var header = document.querySelector('.topbar');
  var directory = document.querySelector('.page-directory');
  var toggle = document.getElementById('directory-toggle');
  var content = document.getElementById('directory-content');
  var localNav = directory.querySelector('[data-scrollspy]');
  var compact = matchMedia('(max-width:980px)');
  var branches = Array.from(directory.querySelectorAll('.directory-expand'));
  var links = Array.from(localNav.querySelectorAll('a[href^="#"]'));
  var targets = links.map(function (a) {
    var target = document.getElementById(decodeURIComponent(a.hash.slice(1)));
    if (target) target.setAttribute('tabindex', '-1');
    return target;
  });
  var nativeSpy = window.CSS && CSS.supports('scroll-target-group: auto');
  var previous = null;
  var queued = false;
  var anchorTarget = null;

  function expand(button, open) {
    button.setAttribute('aria-expanded', String(open));
    document.getElementById(button.getAttribute('aria-controls')).hidden = !open;
  }
  function setDirectory(open) {
    expand(toggle, open);
    toggle.querySelector('.directory-toggle-state').textContent = open ? '收起' : '展开';
  }
  function measure() {
    root.style.setProperty('--topbar-height', Math.ceil(header.getBoundingClientRect().height) + 'px');
    root.style.setProperty('--page-directory-height', compact.matches && !root.classList.contains('focus-reading') ? (toggle.offsetHeight + 18) + 'px' : '0px');
  }
  function reveal(link) {
    var parent = link.parentElement;
    while (parent && parent !== content) {
      if (parent.id && parent.id.indexOf('directory-branch-') === 0) {
        var button = directory.querySelector('[aria-controls="' + parent.id + '"]');
        if (button) expand(button, true);
      }
      parent = parent.parentElement;
    }
  }
  function revealHash() {
    var link = links.find(function (item) { return item.hash === location.hash; });
    if (link) reveal(link);
  }
  function settleAnchor() {
    if (!anchorTarget) return;
    // Lazy media above a destination can otherwise move it after the jump.
    anchorTarget.scrollIntoView({ block: 'start', behavior: 'instant' });
    var waiting = Array.from(document.images).some(function (image) {
      return !image.complete && !!(image.compareDocumentPosition(anchorTarget) & Node.DOCUMENT_POSITION_FOLLOWING);
    });
    if (!waiting) anchorTarget = null;
  }
  function scrollDirectoryItemIntoView(link) {
    if (!link || content.hidden || compact.matches) return;
    var cRect = content.getBoundingClientRect();
    var lRect = link.getBoundingClientRect();
    if (lRect.height === 0) return;
    if (lRect.top < cRect.top + 36) {
      content.scrollTop -= (cRect.top + 36 - lRect.top);
    } else if (lRect.bottom > cRect.bottom - 24) {
      content.scrollTop += (lRect.bottom - (cRect.bottom - 24));
    }
  }
  function updateCurrent() {
    var active = nativeSpy ? localNav.querySelector('a:target-current') : null;
    if (!active) {
      var edge = parseFloat(getComputedStyle(root).scrollPaddingTop) + 8;
      for (var i = 0; i < targets.length; i++) {
        if (targets[i] && targets[i].getClientRects().length && targets[i].getBoundingClientRect().top <= edge) active = links[i];
      }
    }
    if (active === previous) return;
    links.forEach(function (a) {
      a.classList.toggle('is-current', a === active);
      if (a === active) a.setAttribute('aria-current', 'location');
      else a.removeAttribute('aria-current');
    });
    if (active) {
      reveal(active);
      scrollDirectoryItemIntoView(active);
    }
    previous = active;
  }
  function schedule() {
    if (queued) return;
    queued = true;
    requestAnimationFrame(function () { queued = false; updateCurrent(); });
  }

  root.classList.add('navigation-ready');
  toggle.hidden = false;
  branches.forEach(function (button) {
    button.hidden = false;
    expand(button, button.getAttribute('data-start-open') === 'true');
    button.addEventListener('click', function () {
      expand(button, button.getAttribute('aria-expanded') !== 'true');
    });
  });
  setDirectory(!compact.matches);
  revealHash();
  measure();
  toggle.addEventListener('click', function () {
    setDirectory(toggle.getAttribute('aria-expanded') !== 'true');
  });
  compact.addEventListener('change', function () { setDirectory(!compact.matches); measure(); schedule(); });
  directory.addEventListener('click', function (event) {
    var link = event.target.closest('a');
    if (!link || !link.getAttribute('href').startsWith('#') || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    reveal(link);
    if (compact.matches) setDirectory(false);
    measure();
    var target = document.getElementById(decodeURIComponent(link.hash.slice(1)));
    if (target) {
      event.preventDefault();
      if (location.hash !== link.hash) history.pushState(null, '', link.hash);
      target.focus({ preventScroll: true });
      anchorTarget = target; settleAnchor(); schedule();
    }
  });
  directory.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && compact.matches && !content.hidden) {
      setDirectory(false); toggle.focus(); event.preventDefault();
    }
  });
  addEventListener('scroll', schedule, { passive: true });
  addEventListener('scrollend', schedule);
  addEventListener('hashchange', function () { anchorTarget = null; revealHash(); schedule(); });
  addEventListener('popstate', function () { anchorTarget = null; revealHash(); schedule(); });
  addEventListener('resize', function () { measure(); schedule(); });
  addEventListener('load', function () { measure(); schedule(); });
  if (window.ResizeObserver) {
    var observer = new ResizeObserver(function () { measure(); settleAnchor(); schedule(); });
    observer.observe(header);
    observer.observe(document.getElementById('page-content'));
  }
  // Stop following the selected anchor as soon as the reader takes control.
  ['wheel', 'touchstart', 'pointerdown'].forEach(function (name) {
    addEventListener(name, function () { anchorTarget = null; }, { passive: true });
  });
  addEventListener('keydown', function (event) {
    if (/^(Arrow|Page|Home|End| )/.test(event.key)) anchorTarget = null;
  });
  var allDirLinks = Array.from(content.querySelectorAll('.directory-link'));
  if (allDirLinks.length >= 8) {
    var filterWrap = document.createElement('div');
    filterWrap.className = 'directory-filter';
    var filterInput = document.createElement('input');
    filterInput.type = 'search';
    filterInput.className = 'directory-filter-input';
    filterInput.placeholder = '筛选本页目录…';
    filterInput.setAttribute('aria-label', '筛选本页目录');
    filterInput.autocomplete = 'off';
    filterWrap.appendChild(filterInput);
    var contextEl = content.querySelector('.directory-context');
    if (contextEl) contextEl.after(filterWrap);
    else content.prepend(filterWrap);

    var savedExpanded = null;
    function applyDirFilter() {
      var q = filterInput.value.trim().toLowerCase();
      var items = Array.from(content.querySelectorAll('.directory-list li'));
      if (!q) {
        items.forEach(function (li) { li.hidden = false; });
        if (savedExpanded) {
          branches.forEach(function (btn) {
            var id = btn.getAttribute('aria-controls');
            if (Object.prototype.hasOwnProperty.call(savedExpanded, id)) expand(btn, savedExpanded[id]);
          });
          savedExpanded = null;
        }
        return;
      }
      if (!savedExpanded) {
        savedExpanded = {};
        branches.forEach(function (btn) {
          savedExpanded[btn.getAttribute('aria-controls')] = btn.getAttribute('aria-expanded') === 'true';
        });
      }
      items.forEach(function (li) { li.hidden = true; });
      allDirLinks.forEach(function (a) {
        var label = a.textContent.toLowerCase();
        if (label.indexOf(q) !== -1) {
          var li = a.closest('li');
          while (li && content.contains(li)) {
            li.hidden = false;
            var branch = li.parentElement && li.parentElement.parentElement;
            if (branch && branch.id && branch.id.indexOf('directory-branch-') === 0) {
              var btn = directory.querySelector('[aria-controls="' + branch.id + '"]');
              if (btn) expand(btn, true);
            }
            li = li.parentElement ? li.parentElement.closest('li') : null;
          }
        }
      });
    }
    filterInput.addEventListener('input', applyDirFilter);
    filterInput.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && filterInput.value) {
        filterInput.value = '';
        applyDirFilter();
        event.stopPropagation();
      }
    });
  }

  var initialLink = links.find(function (link) { return link.hash === location.hash; });
  if (initialLink) { anchorTarget = targets[links.indexOf(initialLink)]; settleAnchor(); }
  updateCurrent();
})();
