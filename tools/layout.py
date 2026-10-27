"""Layout compartido (head, header, footer) y componentes HTML reutilizables."""
from html import escape as esc

from data import CONTACT, PRIVACY_URL, PRODUCTS, SITE, SOLUTIONS


def ic(name):
    return f'<i class="ph-bold ph-{name}" aria-hidden="true"></i>'


def root_for(path):
    """Prefijo relativo hacia la raíz del sitio desde una ruta como 'catalogo/productos/wi-iaudit/'."""
    clean = path.strip("/")
    return "../" * (clean.count("/") + 1) if clean else ""


# ---------------------------------------------------------------- header / footer

def _menu_links(items, base, root):
    return "".join(
        f'<a class="menu__link" href="{root}{base}{i["slug"]}/"><span class="menu__icon">{ic(i["icon"])}</span>'
        f'<span><span class="menu__title">{esc(i["name"])}</span><span class="menu__desc">{esc(i["menu"])}</span></span></a>'
        for i in items
    )


def header(root, section="", home=False):
    def link(key, label, href, menu=""):
        current = ' aria-current="page"' if section == key else ""
        caret = f' {ic("caret-down")}' if menu else ""
        return (f'<li class="nav__item{" has-menu" if menu else ""}"><a class="nav__link" href="{href}"{current}>{label}{caret}</a>{menu}</li>')

    brand = "#inicio" if home else (root or "./")
    cls = "site-header is-visible"
    products_menu = f'<div class="menu menu--wide">{_menu_links(PRODUCTS, "catalogo/productos/", root)}</div>'
    solutions_menu = f'<div class="menu">{_menu_links(SOLUTIONS, "catalogo/soluciones/", root)}</div>'
    return f"""<header class="{cls}" id="header">
    <div class="container header__inner">
      <a class="brand" href="{brand}" aria-label="Wimprove, ir al inicio">
        <img src="{root}assets/brand/logo-wimprove.svg" alt="Wimprove" width="92" height="44" />
      </a>

      <nav class="nav" id="nav" aria-label="Principal">
        <ul class="nav__list">
          {link("productos", "Productos", root + "productos/", products_menu)}
          {link("soluciones", "Soluciones", root + "soluciones/", solutions_menu)}
          {link("nosotros", "Nosotros", root + "nosotros/")}
          {link("servicios", "Servicios", root + "servicios/")}
          <li class="nav__item nav__item--cta"><a class="btn btn--sm" href="{root}contactanos/">Contáctanos</a></li>
        </ul>
      </nav>

      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="Abrir menú">
        <span></span><span></span>
      </button>
    </div>
  </header>"""


def footer(root):
    prods = "".join(f'<li><a href="{root}catalogo/productos/{p["slug"]}/">{esc(p["name"])}</a></li>' for p in PRODUCTS)
    sols = "".join(f'<li><a href="{root}catalogo/soluciones/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SOLUTIONS)
    return f"""<footer class="site-footer on-dark">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <img src="{root}assets/brand/logo-footer.svg" alt="Wimprove" width="150" height="60" loading="lazy" />
          <p>Soluciones BPO y Contact Center con tecnología omnicanal e inteligencia artificial.</p>
          <div class="social">
            <a href="{CONTACT['facebook']}" target="_blank" rel="noopener" aria-label="Wimprove en Facebook"><i class="ph-bold ph-facebook-logo"></i></a>
            <a href="{CONTACT['linkedin']}" target="_blank" rel="noopener" aria-label="Wimprove en LinkedIn"><i class="ph-bold ph-linkedin-logo"></i></a>
          </div>
        </div>
        <nav class="footer__col" aria-label="Productos">
          <h3>Productos</h3>
          <ul>{prods}</ul>
        </nav>
        <nav class="footer__col" aria-label="Soluciones">
          <h3>Soluciones</h3>
          <ul>{sols}</ul>
        </nav>
        <nav class="footer__col" aria-label="Compañía">
          <h3>Compañía</h3>
          <ul>
            <li><a href="{root}nosotros/">Nosotros</a></li>
            <li><a href="{root}servicios/">Servicios</a></li>
            <li><a href="{root}contactanos/">Contacto</a></li>
            <li><a href="{root}{PRIVACY_URL}">Política de privacidad</a></li>
          </ul>
        </nav>
      </div>
      <div class="footer__bottom">
        <p>© <span id="year">2026</span> Wimprove. Todos los derechos reservados.</p>
        <p>Para fines de calidad y por su seguridad la llamada puede ser grabada (voz).</p>
      </div>
    </div>
  </footer>"""


# ---------------------------------------------------------------- página completa

HEAD_JS = """<script>
    // Marca JS activo antes del primer pintado (evita parpadeos en las animaciones de entrada).
    (function (d) {
      var c = d.documentElement.classList;
      c.add('js');
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) c.add('reduced');
      // Si los scripts externos no cargan, se muestra todo el contenido.
      setTimeout(function () { if (!window.__wimproveReady) c.add('show-all'); }, 4000);
    })(document);
  </script>"""


def render(path, title, desc, body, section="", noindex=False, root=None):
    root = root if root is not None else root_for(path)
    full_title = title if title.startswith("Wimprove") else f"{title} | Wimprove"
    robots = '\n  <meta name="robots" content="noindex" />' if noindex else ""
    canonical = f"{SITE}/{path.strip('/')}/" if path.strip("/") else f"{SITE}/"
    return f"""<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(full_title)}</title>
  <meta name="description" content="{esc(desc, quote=True)}" />
  <meta name="theme-color" content="#012832" />{robots}
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Wimprove" />
  <meta property="og:locale" content="es_MX" />
  <meta property="og:title" content="{esc(full_title, quote=True)}" />
  <meta property="og:description" content="{esc(desc, quote=True)}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{SITE}/assets/img/welcome-bg.webp" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="icon" href="data:," />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@500;600;700&display=swap" rel="stylesheet" />

  {HEAD_JS}
  <link rel="stylesheet" href="{root}css/styles.css" />
  <link rel="stylesheet" href="{root}css/pages.css" />
  <noscript>
    <style>
      [data-reveal] {{ opacity: 1 !important; transform: none !important; }}
    </style>
  </noscript>
  <script src="https://unpkg.com/@phosphor-icons/web@2.1.1" defer></script>
</head>

<body>
  <a class="skip-link" href="#main">Saltar al contenido</a>
  <div class="progress" aria-hidden="true"><span></span></div>

  {header(root, section)}

  <main id="main">
{body}
  </main>

  {footer(root)}

  <a class="to-top" href="#main" aria-label="Volver arriba"><i class="ph-bold ph-arrow-up" aria-hidden="true"></i></a>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js"></script>
  <script src="{root}js/main.js"></script>
  <script src="{root}js/pages.js"></script>
</body>

</html>
"""


# ---------------------------------------------------------------- componentes

def crumbs(root, trail):
    items = [("Inicio", root or "./")] + trail
    lis = []
    for i, (label, href) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li aria-current="page">{esc(label)}</li>')
        else:
            lis.append(f'<li><a href="{href}">{esc(label)}</a></li>')
    return f'<nav class="crumbs" aria-label="Ruta de navegación"><ol>{"".join(lis)}</ol></nav>'


def page_hero(root, trail, eyebrow, title, lead="", ctas="", media=""):
    has_media = " has-media" if media else ""
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    ctas_html = f'<div class="page-hero__ctas">{ctas}</div>' if ctas else ""
    media_html = f'<div class="page-hero__media">{media}</div>' if media else ""
    return f"""    <section class="page-hero on-dark">
      <span class="deco deco--a" aria-hidden="true"></span>
      <span class="deco deco--b" aria-hidden="true"></span>
      <div class="container page-hero__grid{has_media}">
        <div class="page-hero__copy">
          {crumbs(root, trail)}
          <span class="eyebrow">{esc(eyebrow)}</span>
          <h1 class="display">{title}</h1>
          {lead_html}
          {ctas_html}
        </div>
        {media_html}
      </div>
    </section>"""


def section(inner, *, eyebrow="", title="", lead="", soft=False, sid="", center=False, cls=""):
    head = ""
    if eyebrow or title:
        parts = []
        if eyebrow:
            parts.append(f'<span class="eyebrow" data-reveal>{esc(eyebrow)}</span>')
        if title:
            parts.append(f'<h2 class="h2" data-split>{title}</h2>')
        if lead:
            parts.append(f'<p class="lead section__lead" data-reveal>{lead}</p>')
        head = f'<div class="section__head section__head--stack{" section__head--center" if center else ""}"><div>{"".join(parts)}</div></div>'
    id_attr = f' id="{sid}"' if sid else ""
    return f"""    <section class="section{" section--soft" if soft else ""}{(" " + cls) if cls else ""}"{id_attr}>
      <div class="container">
        {head}
        {inner}
      </div>
    </section>"""


def feat_grid(items, cols=3):
    cards = "".join(
        f'<article class="feat" data-reveal><span class="feat__icon">{ic(icon)}</span><h3>{esc(t)}</h3><p>{esc(text)}</p></article>'
        for icon, t, text in items
    )
    return f'<div class="feat-grid feat-grid--{cols}">{cards}</div>'


def steps(items, cols=3):
    lis = "".join(
        f'<li class="step" data-reveal><span class="step__n">{i}</span><p>{esc(text)}</p></li>'
        for i, text in enumerate(items, 1)
    )
    return f'<ol class="steps steps--{cols}">{lis}</ol>'


def kpis(items):
    """items: (prefijo, numero | None, sufijo, etiqueta). Si numero es int se anima."""
    out = []
    for prefix, num, suffix, label in items:
        if isinstance(num, int):
            value = f'{esc(prefix)}<span data-count="{num}">{num:,}</span>{esc(suffix)}'
        else:
            value = esc(prefix + (num or "") + suffix)
        out.append(f'<div class="kpi" data-reveal><span class="kpi__num">{value}</span><span class="kpi__label">{esc(label)}</span></div>')
    return f'<div class="kpis kpis--{len(out)}">{"".join(out)}</div>'


def split(media, copy, reverse=False):
    return f'<div class="split{" split--reverse" if reverse else ""}"><div class="split__media" data-reveal>{media}</div><div class="split__copy">{copy}</div></div>'


def img(root, src, alt, w=None, h=None, cls=""):
    size = f' width="{w}" height="{h}"' if w and h else ""
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{root}assets/{src}" alt="{esc(alt, quote=True)}"{size} loading="lazy" />'


def bullet_list(items):
    return '<ul class="ticks">' + "".join(f"<li>{ic('check-circle')}<span>{i}</span></li>" for i in items) + "</ul>"


def tabs(tid, items):
    """items: (etiqueta, [(titulo, texto), ...])"""
    btns, panels = [], []
    for i, (label, entries) in enumerate(items):
        sel = "true" if i == 0 else "false"
        btns.append(f'<button class="tabs__btn" role="tab" id="{tid}-t{i}" aria-selected="{sel}" aria-controls="{tid}-p{i}" tabindex="{0 if i == 0 else -1}">{esc(label)}</button>')
        body = "".join(f"<div class=\"tabs__item\"><h3>{esc(t)}</h3><p>{esc(x)}</p></div>" for t, x in entries)
        hidden = "" if i == 0 else " hidden"
        panels.append(f'<div class="tabs__panel" role="tabpanel" id="{tid}-p{i}" aria-labelledby="{tid}-t{i}"{hidden}>{body}</div>')
    return f'<div class="tabs" data-tabs><div class="tabs__list" role="tablist" aria-orientation="vertical">{"".join(btns)}</div><div class="tabs__panels">{"".join(panels)}</div></div>'


def faq(prefix, items):
    out = []
    for i, (q, a) in enumerate(items):
        opened = i == 0
        out.append(f"""<div class="acc__item{" is-open" if opened else ""}">
          <button class="acc__btn" type="button" aria-expanded="{str(opened).lower()}" aria-controls="{prefix}-{i}"><span class="acc__title acc__title--sm">{esc(q)}</span><span class="acc__icon" aria-hidden="true"></span></button>
          <div class="acc__panel" id="{prefix}-{i}"{"" if opened else " inert"}><div><p>{esc(a)}</p></div></div>
        </div>""")
    return f'<div class="acc acc--faq">{"".join(out)}</div>'


def yt(video_id, title):
    return (f'<div class="yt" data-yt="{video_id}" data-title="{esc(title, quote=True)}">'
            f'<button class="yt__btn" type="button" aria-label="Reproducir video: {esc(title, quote=True)}">'
            f'<img src="https://i.ytimg.com/vi/{video_id}/hqdefault.jpg" alt="" loading="lazy" />'
            f'<span class="yt__play"><i class="ph-fill ph-play" aria-hidden="true"></i></span></button></div>')


def video(root, src, poster, label):
    return (f'<video class="media-video" src="{root}assets/video/{src}" poster="{root}assets/{poster}" muted loop playsinline preload="none" '
            f'data-autoplay aria-label="{esc(label, quote=True)}"></video>')


def contact_form(context=""):
    return f"""<div class="form-card">
          <form class="form js-contact-form" novalidate data-context="{esc(context, quote=True)}">
            <div class="field"><label for="f-nombre">Nombre</label><input id="f-nombre" name="firstname" type="text" autocomplete="given-name" required /></div>
            <div class="field"><label for="f-apellido">Apellido</label><input id="f-apellido" name="lastname" type="text" autocomplete="family-name" required /></div>
            <div class="field"><label for="f-empresa">Empresa</label><input id="f-empresa" name="company" type="text" autocomplete="organization" required /></div>
            <div class="field"><label for="f-email">Email de empresa</label><input id="f-email" name="email" type="email" autocomplete="email" required /></div>
            <div class="field field--full"><label for="f-movil">Número de móvil <span class="opt">(opcional)</span></label><input id="f-movil" name="mobilephone" type="tel" autocomplete="tel" /></div>
            <div class="field field--full"><label for="f-mensaje">Mensaje</label><textarea id="f-mensaje" name="message" rows="4" required></textarea></div>
            <div class="field field--full field--trap" aria-hidden="true"><label for="f-web">No llenar este campo</label><input id="f-web" name="website" type="text" tabindex="-1" autocomplete="off" /></div>
            <label class="check field--full"><input type="checkbox" name="consent" required /><span>Acepto la <a href="__ROOT__{PRIVACY_URL}" target="_blank" rel="noopener">política de privacidad</a>.</span></label>
            <button class="btn btn--magnetic field--full" type="submit"><span class="btn__label">Enviar mensaje</span> <i class="ph-bold ph-paper-plane-tilt" aria-hidden="true"></i></button>
            <p class="form__status field--full" role="status" aria-live="polite"></p>
          </form>
        </div>"""


def cta_band(root, title, text, context, extra=""):
    """Bloque oscuro de cierre con el formulario de contacto."""
    form = contact_form(context).replace("__ROOT__", root)
    return f"""    <section class="section contact on-dark" id="contacto">
      <span class="deco deco--c" aria-hidden="true"></span>
      <div class="container contact__grid">
        <div class="contact__info">
          <span class="eyebrow" data-reveal>Contáctanos</span>
          <h2 class="h2" data-split>{title}</h2>
          <p class="lead" data-reveal>{text}</p>
          {extra}
        </div>
        <div data-reveal>{form}</div>
      </div>
    </section>"""


def info_list(items):
    """items: (icono, rotulo, html_valor)"""
    lis = "".join(f'<li>{ic(i)}<div><strong>{esc(label)}</strong>{value}</div></li>' for i, label, value in items)
    return f'<ul class="info-list" data-reveal>{lis}</ul>'


def product_card(root, p):
    return (f'<a class="card card--thumb spot" data-reveal href="{root}catalogo/productos/{p["slug"]}/">'
            f'<div class="card__thumb"><img src="{root}assets/{p["img"]}" alt="" loading="lazy" width="400" height="278" /></div>'
            f'<div class="card__body"><span class="tag tag--soft">{esc(p["tag"])}</span><h3 class="card__title">{esc(p["name"])}</h3>'
            f'<p class="card__desc">{esc(p["short"])}</p></div>'
            f'<span class="card__go" aria-hidden="true"><i class="ph-bold ph-arrow-up-right"></i></span></a>')


def solution_card(root, s):
    return (f'<a class="card card--thumb spot" data-reveal href="{root}catalogo/soluciones/{s["slug"]}/">'
            f'<div class="card__thumb"><img src="{root}assets/{s["img"]}" alt="" loading="lazy" width="1195" height="800" /></div>'
            f'<div class="card__body"><h3 class="card__title">{esc(s["name"])}</h3>'
            f'<p class="card__desc">{esc(s["short"])}</p></div>'
            f'<span class="card__go" aria-hidden="true"><i class="ph-bold ph-arrow-up-right"></i></span></a>')


def related(root, kind, current_slug, slugs):
    items = PRODUCTS if kind == "productos" else SOLUTIONS
    chosen = [i for i in items if i["slug"] in slugs and i["slug"] != current_slug]
    card = product_card if kind == "productos" else solution_card
    return f'<div class="card-grid card-grid--{len(chosen)}">{"".join(card(root, i) for i in chosen)}</div>'
