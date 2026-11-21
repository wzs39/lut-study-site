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
    if (active) reveal(active);
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
  var initialLink = links.find(function (link) { return link.hash === location.hash; });
  if (initialLink) { anchorTarget = targets[links.indexOf(initialLink)]; settleAnchor(); }
  updateCurrent();
})();
