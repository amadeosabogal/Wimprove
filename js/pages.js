/* Wimprove — componentes de las páginas internas: tabs, videos, comparador antes/después. */
(() => {
  'use strict';

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduced = document.documentElement.classList.contains('reduced');

  /* ---------- Tabs (Wi Contact) ---------- */
  $$('[data-tabs]').forEach((root) => {
    const tabs = $$('[role="tab"]', root);
    const panels = $$('[role="tabpanel"]', root);

    function select(tab, focus) {
      tabs.forEach((t, i) => {
        const on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        panels[i].hidden = !on;
      });
      if (focus) tab.focus();
      if (window.ScrollTrigger) ScrollTrigger.refresh();
    }

    tabs.forEach((tab, i) => {
      tab.addEventListener('click', () => select(tab));
      tab.addEventListener('keydown', (e) => {
        const next = { ArrowDown: i + 1, ArrowRight: i + 1, ArrowUp: i - 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
        if (next === undefined) return;
        e.preventDefault();
        select(tabs[(next + tabs.length) % tabs.length], true);
      });
    });
  });

  /* ---------- YouTube sin cargar el reproductor hasta que se pulsa ---------- */
  $$('[data-yt]').forEach((box) => {
    $('.yt__btn', box).addEventListener('click', () => {
      const iframe = document.createElement('iframe');
      iframe.src = `https://www.youtube-nocookie.com/embed/${box.dataset.yt}?autoplay=1&rel=0`;
      iframe.title = box.dataset.title || 'Video';
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      iframe.allowFullscreen = true;
      box.replaceChildren(iframe);
    });
  });

  /* ---------- Videos de fondo: solo se reproducen cuando se ven ---------- */
  const videos = $$('video[data-autoplay]');
  if (videos.length) {
    if (reduced || !('IntersectionObserver' in window)) {
      videos.forEach((v) => { v.controls = true; });
    } else {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          const v = entry.target;
          if (entry.isIntersecting) {
            v.preload = 'auto';
            v.play().catch(() => { v.controls = true; });
          } else {
            v.pause();
          }
        });
      }, { threshold: 0.35 });
      videos.forEach((v) => io.observe(v));
    }
  }

  /* ---------- Comparador antes / después ---------- */
  $$('[data-ba]').forEach((ba) => {
    const range = $('.ba__range', ba);
    const set = () => ba.style.setProperty('--pos', `${range.value}%`);
    range.addEventListener('input', set);
    set();
  });
})();
