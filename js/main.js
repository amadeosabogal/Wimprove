/* Wimprove — interacciones y animaciones de la Home.
   Orden: funciones que no dependen de GSAP (menú, acordeón, formulario)
   y después el movimiento (Lenis, hero por scroll, revelados). */
(() => {
  'use strict';

  const root = document.documentElement;
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const ramp = (v, a, b) => clamp((v - a) / (b - a), 0, 1);

  const reduced = root.classList.contains('reduced');
  const header = $('#header');
  let lenis = null;

  // Formulario: portal y formulario de HubSpot que ya usa wimprove.com
  const HUBSPOT = { portalId: '50110305', formId: '5ce9d76e-c74c-4438-a541-1254953925d1' };

  /* ---------- Año del footer ---------- */
  const year = $('#year');
  if (year) year.textContent = new Date().getFullYear();

  /* ---------- Navegación ---------- */
  const toggle = $('.nav-toggle');

  function setMenu(open) {
    header.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    root.classList.toggle('menu-lock', open);
    if (lenis) open ? lenis.stop() : lenis.start();
  }

  toggle.addEventListener('click', () => setMenu(!header.classList.contains('nav-open')));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && header.classList.contains('nav-open')) { setMenu(false); toggle.focus(); }
  });
  matchMedia('(min-width: 981px)').addEventListener('change', (e) => { if (e.matches) setMenu(false); });

  function scrollToTarget(hash) {
    const el = hash === '#inicio' ? null : $(hash);
    if (hash !== '#inicio' && !el) return;
    if (lenis) {
      lenis.scrollTo(el || 0, { offset: el ? -(header.offsetHeight - 1) : 0, duration: 1.4 });
    } else {
      const top = el ? el.getBoundingClientRect().top + scrollY - header.offsetHeight + 1 : 0;
      scrollTo({ top, behavior: reduced ? 'auto' : 'smooth' });
    }
  }

  $$('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const hash = a.getAttribute('href');
      if (hash.length < 2) return;
      e.preventDefault();
      setMenu(false);
      // Espera un frame para que el scroll se libere si el menú móvil estaba abierto.
      requestAnimationFrame(() => scrollToTarget(hash));
      history.replaceState(null, '', hash);
    });
  });

  /* ---------- Acordeón de soluciones ---------- */
  const accItems = $$('.acc__item');

  function setAcc(item, open) {
    item.classList.toggle('is-open', open);
    $('.acc__btn', item).setAttribute('aria-expanded', String(open));
    $('.acc__panel', item).toggleAttribute('inert', !open);
  }

  accItems.forEach((item) => {
    const group = $$('.acc__item', item.closest('.acc'));
    $('.acc__btn', item).addEventListener('click', () => {
      const wasOpen = item.classList.contains('is-open');
      group.forEach((i) => setAcc(i, false));
      if (!wasOpen) setAcc(item, true);
    });
    // El alto de la página cambia al abrir/cerrar: recalcula posiciones de scroll.
    $('.acc__panel', item).addEventListener('transitionend', (e) => {
      if (e.propertyName === 'grid-template-rows' && window.ScrollTrigger) ScrollTrigger.refresh();
    });
  });

  /* ---------- Formularios de contacto ---------- */
  function setFieldError(input, message) {
    const field = input.closest('.field') || input.closest('.check');
    field.classList.toggle('is-invalid', Boolean(message));
    let err = $('.field__error', field);
    if (message) {
      if (!err) { err = document.createElement('span'); err.className = 'field__error'; field.appendChild(err); }
      err.textContent = message;
      input.setAttribute('aria-invalid', 'true');
    } else {
      if (err) err.remove();
      input.removeAttribute('aria-invalid');
    }
  }

  function validate(form) {
    let firstInvalid = null;
    $$('input[required], textarea[required]', form).forEach((input) => {
      let msg = '';
      if (input.type === 'checkbox') { if (!input.checked) msg = 'Debes aceptar la política de privacidad.'; }
      else if (!input.value.trim()) msg = 'Este campo es obligatorio.';
      else if (input.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim())) msg = 'Escribe un correo válido.';
      setFieldError(input, msg);
      if (msg && !firstInvalid) firstInvalid = input;
    });
    return firstInvalid;
  }

  function initForm(form) {
    const statusEl = $('.form__status', form);
    form.addEventListener('input', (e) => { if (e.target.closest('.is-invalid')) setFieldError(e.target, ''); });

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      statusEl.className = 'form__status field--full';
      statusEl.textContent = '';

      const firstInvalid = validate(form);
      if (firstInvalid) { firstInvalid.focus(); return; }
      if ($('[name="website"]', form).value) return; // trampa para bots

      const button = $('button[type="submit"]', form);
      const label = $('.btn__label', button);
      const original = label.textContent;
      button.disabled = true;
      label.textContent = 'Enviando…';

      // El producto o la solución de interés se antepone al mensaje para que ventas sepa de dónde viene.
      const context = form.dataset.context;
      const fields = ['firstname', 'lastname', 'company', 'email', 'message', 'mobilephone']
        .map((name) => {
          let value = form.elements[name].value.trim();
          if (name === 'message' && context) value = `${context}\n\n${value}`;
          return { name, value };
        })
        .filter((f) => f.value);

      try {
        const res = await fetch(
          `https://api.hsforms.com/submissions/v3/integration/submit/${HUBSPOT.portalId}/${HUBSPOT.formId}`,
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ fields, context: { pageUri: location.href, pageName: document.title } }),
          }
        );
        if (!res.ok) throw new Error(`HubSpot ${res.status}`);
        form.reset();
        statusEl.classList.add('is-ok');
        statusEl.textContent = '¡Gracias! Recibimos tu mensaje y te responderemos pronto.';
      } catch (err) {
        statusEl.classList.add('is-error');
        statusEl.textContent = 'No pudimos enviar tu mensaje. Inténtalo de nuevo o escríbenos a juan.gonzalez@mdybpo.com.';
      } finally {
        button.disabled = false;
        label.textContent = original;
      }
    });
  }

  $$('.js-contact-form').forEach(initForm);

  // Enlaces que fijan el contexto del formulario (p. ej. "Solicitar presupuesto" en una solución)
  $$('[data-set-context]').forEach((a) => {
    a.addEventListener('click', () => {
      const form = $('.js-contact-form');
      if (form) form.dataset.context = a.dataset.setContext;
    });
  });

  /* ---------- Movimiento ---------- */
  if (!window.gsap || !window.ScrollTrigger) {
    root.classList.add('show-all');
    return;
  }
  window.__wimproveReady = true;
  gsap.registerPlugin(ScrollTrigger);
  ScrollTrigger.config({ ignoreMobileResize: true });

  // Scroll suave
  if (window.Lenis && !reduced) {
    lenis = new Lenis({ duration: 1.1, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
    window.lenis = lenis;
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add((time) => lenis.raf(time * 1000));
    gsap.ticker.lagSmoothing(0);
  }

  /* Titulares: se parten en palabras para entrar con máscara */
  function splitWords(el) {
    const walk = (node) => {
      [...node.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach((tok) => {
            if (!tok) return;
            if (/^\s+$/.test(tok)) { frag.appendChild(document.createTextNode(' ')); return; }
            const w = document.createElement('span');
            w.className = 'w';
            const wi = document.createElement('span');
            wi.className = 'wi';
            wi.textContent = tok;
            w.appendChild(wi);
            frag.appendChild(w);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1) {
          walk(n);
        }
      });
    };
    walk(el);
  }

  function initReveals() {
    $$('[data-split]').forEach((h) => {
      splitWords(h);
      gsap.from($$('.wi', h), {
        yPercent: 115, duration: 1, ease: 'power4.out', stagger: 0.035,
        scrollTrigger: { trigger: h, start: 'top 88%', once: true },
      });
    });

    ScrollTrigger.batch('[data-reveal]', {
      start: 'top 90%',
      once: true,
      onEnter: (batch) => gsap.to(batch, { opacity: 1, y: 0, duration: 0.9, ease: 'power3.out', stagger: 0.09, overwrite: true }),
    });

    // Contadores
    $$('[data-count]').forEach((el) => {
      const end = Number(el.dataset.count);
      const obj = { v: 0 };
      el.textContent = '0';
      ScrollTrigger.create({
        trigger: el, start: 'top 92%', once: true,
        onEnter: () => gsap.to(obj, { v: end, duration: 1.8, ease: 'power2.out', onUpdate: () => { el.textContent = Math.round(obj.v).toLocaleString('es-MX'); } }),
      });
    });

    // Parallax sutil en imágenes
    $$('[data-parallax]').forEach((el) => {
      const s = parseFloat(el.dataset.parallax) || 0.06;
      gsap.fromTo(el, { yPercent: -s * 100 }, {
        yPercent: s * 100, ease: 'none',
        scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: true },
      });
    });
  }

  function initInteractions() {
    // Brillo que sigue al cursor en las tarjetas
    $$('.spot').forEach((card) => {
      card.addEventListener('pointermove', (e) => {
        const r = card.getBoundingClientRect();
        card.style.setProperty('--mx', `${e.clientX - r.left}px`);
        card.style.setProperty('--my', `${e.clientY - r.top}px`);
      });
    });

    // Botones magnéticos (solo con ratón)
    if (matchMedia('(hover: hover) and (pointer: fine)').matches) {
      $$('.btn--magnetic').forEach((btn) => {
        const x = gsap.quickTo(btn, 'x', { duration: 0.5, ease: 'power3' });
        const y = gsap.quickTo(btn, 'y', { duration: 0.5, ease: 'power3' });
        btn.addEventListener('pointermove', (e) => {
          const r = btn.getBoundingClientRect();
          x((e.clientX - (r.left + r.width / 2)) * 0.22);
          y((e.clientY - (r.top + r.height / 2)) * 0.3);
        });
        btn.addEventListener('pointerleave', () => { x(0); y(0); });
      });
    }

    // Las tarjetas del hero se mueven un poco con el cursor (solo con ratón)
    const hero = $('.home-hero');
    if (hero && !reduced && matchMedia('(hover: hover) and (pointer: fine)').matches) {
      const cards = $$('.hs', hero).map((el) => ({
        d: parseFloat(el.dataset.depth) || 1,
        x: gsap.quickTo(el, 'x', { duration: 0.9, ease: 'power3' }),
        y: gsap.quickTo(el, 'y', { duration: 0.9, ease: 'power3' }),
      }));
      hero.addEventListener('pointermove', (e) => {
        const r = hero.getBoundingClientRect();
        const nx = (e.clientX - r.left) / r.width - 0.5;
        const ny = (e.clientY - r.top) / r.height - 0.5;
        cards.forEach((c) => { c.x(nx * -26 * c.d); c.y(ny * -18 * c.d); });
      });
      hero.addEventListener('pointerleave', () => cards.forEach((c) => { c.x(0); c.y(0); }));
    }

    // Barra de progreso de lectura
    gsap.to('.progress span', {
      scaleX: 1, ease: 'none',
      scrollTrigger: { start: 0, end: 'max', scrub: 0.2 },
    });

    // Botón volver arriba
    const toTop = $('.to-top');
    ScrollTrigger.create({
      start: () => innerHeight * 1.5,
      end: 'max',
      onToggle: (self) => toTop.classList.toggle('is-visible', self.isActive),
    });
  }

  if (!reduced) initReveals();
  initInteractions();

  window.addEventListener('load', () => {
    ScrollTrigger.refresh();
    const target = location.hash.length > 1 ? $(location.hash) : null;
    if (target) {
      const offset = -(header.offsetHeight - 1);
      if (lenis) lenis.scrollTo(target, { offset, immediate: true });
      else target.scrollIntoView();
    }
  });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => ScrollTrigger.refresh());
})();
