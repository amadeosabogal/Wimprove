"""Contenido de las páginas internas. Los textos vienen de wimprove.com (con erratas corregidas)."""
from pathlib import Path

from data import CONTACT, PRIVACY_URL, PRODUCTS, SOLUTIONS, product, solution
from layout import (
    bullet_list, contact_form, cta_band, faq, feat_grid, ic, img, info_list, kpis, page_hero,
    product_card, related, render, root_for, section, solution_card, split, steps, tabs, video, yt,
)

CONTENT = Path(__file__).parent / "content"
LINK_CTA = '<a class="btn btn--magnetic" href="#contacto">{label} ' + ic("arrow-right") + "</a>"


def hero_img(r, src, alt, small=False):
    cls = "hero-img hero-img--sm" if small else "hero-img"
    return f'<div class="{cls}"><img src="{r}assets/{src}" alt="{alt}" /></div>'


def p_ctas(label="Solicitar información", ghost=None):
    out = LINK_CTA.format(label=label)
    if ghost:
        out += f'<a class="btn btn--ghost" href="{ghost[1]}">{ghost[0]}</a>'
    return out


def hl(text):
    return f'<span class="hl">{text}</span>'


def trail_p(r, name):
    return [("Productos", r + "productos/"), (name, None)]


def trail_s(r, name):
    return [("Soluciones", r + "soluciones/"), (name, None)]


def product_page(slug, desc, body, trail_name=None):
    path = f"catalogo/productos/{slug}/"
    p = product(slug)
    return {"path": path, "title": p["name"], "desc": desc, "body": body, "section": "productos"}


def solution_page(slug, desc, body):
    path = f"catalogo/soluciones/{slug}/"
    s = solution(slug)
    return {"path": path, "title": s["name"], "desc": desc, "body": body, "section": "soluciones"}


# ================================================================ listados

def page_productos():
    path = "productos/"
    r = root_for(path)
    body = page_hero(r, [("Productos", None)], "Productos", "Herramientas tecnológicas para tu " + hl("operación"),
                     "Software, inteligencia artificial y omnicanalidad para BPO y Contact Centers.")
    body += "\n" + section(
        f'<div class="card-grid card-grid--4">{"".join(product_card(r, p) for p in PRODUCTS)}</div>', soft=True)
    body += "\n" + cta_band(r, "¿No sabes cuál elegir?", "Cuéntanos tu operación y diseñamos la solución a tu medida.", "Consulta general de productos")
    return {"path": path, "title": "Productos", "section": "productos", "body": body,
            "desc": "Wi IAudit, Wi Contact, WIXperiences, Wi Mail, Wi Inteligence, Wi Desk, Chatbots y Voicebots: herramientas tecnológicas de Wimprove para BPO y Contact Centers."}


def page_soluciones():
    path = "soluciones/"
    r = root_for(path)
    body = page_hero(r, [("Soluciones", None)], "Soluciones", "Impulsamos tu negocio de manera " + hl("eficaz"),
                     "Atención al cliente, cobranza, telemarketing, helpdesk y telemedicina.")
    body += "\n" + section(
        f'<div class="card-grid card-grid--3">{"".join(solution_card(r, s) for s in SOLUTIONS)}</div>', soft=True)
    body += "\n" + cta_band(r, "Diseña tu solución", "Cuéntanos qué necesita tu operación y te acompañamos desde la demostración hasta la implementación.", "Consulta general de soluciones")
    return {"path": path, "title": "Soluciones", "section": "soluciones", "body": body,
            "desc": "Soluciones de Wimprove: atención al cliente, cobranza, telemarketing, helpdesk y telemedicina para empresas en Latinoamérica."}


# ================================================================ productos

def page_iaudit():
    path = "catalogo/productos/wi-iaudit/"
    r = root_for(path)
    ctx = "Producto de interés: Wi IAudit"
    body = page_hero(
        r, trail_p(r, "Wi IAudit"), "Inteligencia artificial", "Wi " + hl("IAudit"),
        "Procesamos tus llamadas, chats y emails con inteligencia artificial para automatizar la calidad de los agentes de ventas o atención al cliente y la investigación de mercado.",
        p_ctas("Solicitar información", ("Ver resultados", "#resultados")),
        video(r, "wi-iaudit.mp4", "img/products/iaudit-hero.webp", "Demostración de Wi IAudit"))

    why = feat_grid([
        ("smiley", "Experiencia de cliente mejorada", "Con el entrenamiento continuo de los agentes a través de cientos de feedbacks, los agentes aceleran conocimientos del producto o servicio."),
        ("piggy-bank", "Ahorros de operación", "Multiplica 20 veces las evaluaciones de tu equipo de calidad para mayor acompañamiento a tus agentes y disminuye en 60% los gastos de tus equipos de calidad."),
        ("gear-six", "Optimización de procesos", "Tus plantillas de evaluaciones de calidad a tus ejecutivos, 100% realizadas por Wi IAudit."),
        ("user-focus", "Optimización del desempeño del agente", "Identifica oportunidades de capacitación y reconoce a los agentes destacados."),
        ("path", "Journey del cliente", "Analiza la historia completa de la relación con cada cliente, mejorando su experiencia en todo el recorrido con análisis de IA detallados."),
        ("trend-up", "Eficiencia en ventas y cobranza", "Acelera las herramientas de venta y cobranza, haciéndolas diez veces más eficientes mediante algoritmos de IA avanzados."),
        ("file-text", "Revisión de contratos", "Mejora los tiempos de revisión de contratos en un 98%, pasando de una semana a solo una hora, con la asistencia de IA que garantiza precisión y eficiencia."),
    ], cols=4)
    body += "\n" + section(why, eyebrow="Beneficios", title="¿Por qué elegir Wi " + hl("IAudit") + "?", soft=True)

    proc = steps([
        "Repositorio de audios, chats y emails. Integración con APIs.",
        "Metadata e integración con Wi IAudit.",
        "Procesamiento de miles de audios, chats y mails.",
        "Monitoreos de calidad listos para ser revisados por el ejecutivo.",
        "Conformidad de los monitores por parte de los ejecutivos.",
        "Promedios, análisis, detección de áreas de oportunidad y fortalezas.",
    ], cols=3)
    body += "\n" + section(proc, eyebrow="Cómo funciona", title="Proceso Wi " + hl("IAudit"))

    res = kpis([
        ("", 25, "%", "De aumento en la productividad"),
        ("", 50, "%", "Menos rotación de empleados"),
        ("", 140, "%", "De ROI"),
        ("$", 1, " M", "De ahorro de costos"),
        ("", 1, "M", "Evaluaciones"),
        ("< ", 2, " años", "Período de recupero"),
    ])
    body += "\n" + section(res, eyebrow="Resultados", title="Resultados que " + hl("hablan por sí solos"), sid="resultados", cls="section--kpi")

    diff = feat_grid([
        ("robot", "Automatización total", "Evalúa automáticamente todas las interacciones, ya sean llamadas telefónicas, correos electrónicos o chats de WhatsApp."),
        ("smiley", "Análisis de sentimiento", "Identifica y entiende las emociones o sentimientos del cliente para una mejor atención."),
        ("lightning", "Feedback en tiempo real", "Proporciona retroalimentación inmediata a los ejecutivos durante la atención, con causas de insatisfacción o recomendaciones."),
        ("clipboard-text", "Evaluación integral", "Analiza fortalezas, áreas de oportunidad, FCR y empatía del ejecutivo. Detecta áreas de mejora y éxitos de tus ejecutivos."),
        ("chart-line-up", "Pronóstico de NPS", "Anticipa el Net Promoter Score basado en interacciones reales para mejorar la satisfacción del cliente."),
        ("seal-check", "FCR", "Capacidad de resolver la consulta o problema de un cliente satisfactoriamente durante el primer contacto con el servicio de atención."),
        ("heart", "Indicadores de empatía del ejecutivo", "Métricas que evalúan cómo los ejecutivos manejan situaciones emocionales, expresan empatía genuina y adaptan su tono y respuesta según el contexto del cliente."),
        ("plugs-connected", "Integración con APIs", "Se integra fácilmente con llamadas telefónicas, correos electrónicos y WhatsApp. Sus robustas APIs permiten una implementación rápida y fluida."),
    ], cols=4)
    body += "\n" + section(diff, eyebrow="Diferenciadores", title=hl("Diferenciadores") + " clave", soft=True)

    biz = split(
        img(r, "img/iaudit/figura-contacto.webp", "Ejecutivo con laptop", 578, 578, "split__fig"),
        '<span class="eyebrow">Beneficios para el negocio</span>'
        '<h2 class="h2" data-split>Reducción de ' + hl("costos") + '</h2>'
        '<p class="lead">Un analista de calidad en promedio puede hacer 200 monitoreos al mes. Con Wi IAudit puedes hacer, por el mismo presupuesto, 1000 monitoreos, y con un feedback de valor al ejecutivo.</p>'
        + bullet_list([
            "<strong>Procesamiento rápido.</strong> Evalúa miles de interacciones en cuestión de minutos y optimiza los tiempos de respuesta ante las consultas de los clientes finales.",
            "<strong>Monitoreo continuo.</strong> Supervisa todas las interacciones en tiempo real, garantizando altos estándares de servicio. Con alertas proactivas y análisis detallados, permite resolver problemas antes de que afecten la satisfacción del cliente.",
            "<strong>Reduce el tiempo de aprendizaje.</strong> Mejora la experiencia de atención al cliente con un mejor aprendizaje del ejecutivo.",
        ]))
    body += "\n" + section(biz)

    cmp_ = f"""<div class="compare">
          <article class="compare__card" data-reveal>
            {img(r, "img/iaudit/tradicional.webp", "Analista de calidad con la evaluación tradicional", 653, 652, "compare__img")}
            <h3>Evaluación tradicional</h3>
            <ul class="crosses">
              <li>{ic("x-circle")}<span>Puede que se hagan hasta 8 monitoreos al mes por parte del supervisor.</span></li>
              <li>{ic("x-circle")}<span>Un analista de calidad cubre 200 monitoreos al mes.</span></li>
              <li>{ic("x-circle")}<span>Las plantillas de evaluación caen en error por falta de concentración del analista de calidad.</span></li>
              <li>{ic("x-circle")}<span>Los agentes no saben si están haciendo bien su trabajo y no están acompañados en sus procesos iniciales.</span></li>
            </ul>
          </article>
          <article class="compare__card compare__card--win" data-reveal>
            {img(r, "img/iaudit/evaluacion-ia.webp", "Panel de evaluación de Wi IAudit", 654, 653, "compare__img")}
            <h3>Evaluación Wi IAudit</h3>
            {bullet_list([
                "Puede monitorear el 100% de las llamadas, emails y chats de la gestión del asesor en el mes.",
                "Acelera la curva de aprendizaje con el incremento de feedback.",
                "Reduce costos de calidad.",
                "Reportes de monitoreos en línea.",
                "El asesor se siente acompañado en su proceso y sabe si está haciendo bien su trabajo.",
            ])}
          </article>
        </div>"""
    body += "\n" + section(cmp_, eyebrow="Comparativo", title="Evaluaciones " + hl("precisas") + " y accionables", soft=True)

    logos = '<ul class="logos" data-reveal>' + "".join(
        f'<li>{img(r, f"img/clients/marca-{i}.webp", n, 254, 254)}</li>'
        for i, n in enumerate(["MDY Customer Experience", "UTP", "Claro", "Telcel", "Maquinarias"], 1)) + "</ul>"
    body += "\n" + section(logos, eyebrow="Casos de éxito", title="Empresas que ya " + hl("lo usan"), center=True)

    contact = info_list([
        ("phone", "Abel Gutierrez", '<a href="tel:+5218125979368">+52 (1) 81 2597 9368</a>'),
        ("envelope-simple", "Email", '<a href="mailto:agutierrez@wimprove.com">agutierrez@wimprove.com</a>'),
    ])
    body += "\n" + cta_band(r, "Eleva la calidad de tus ventas y atención al cliente", "¿Tienes dudas? Déjanos un mensaje.", ctx, contact)
    return product_page("wi-iaudit", "Wi IAudit procesa tus llamadas, chats y emails con inteligencia artificial para automatizar la calidad de tus agentes. Más evaluaciones, menos costos.", body)


def page_wixperiences():
    path = "catalogo/productos/wixperiences/"
    r = root_for(path)
    ctx = "Producto de interés: WIXperiences"
    body = page_hero(
        r, trail_p(r, "WIXperiences"), "Videollamadas", "WI" + hl("Xperiences"),
        "Sistema de videollamadas para gestión con tus clientes. Atiende a tus clientes por videollamada desde tu web, kioscos virtuales o landing pages.",
        p_ctas("Contáctanos"),
        video(r, "wixperiences.mp4", "img/products/wixperiences.webp", "Demostración de WIXperiences"))

    feats = feat_grid([
        ("chats-circle", "Atención multicanal", "Tus ejecutivos podrán atender las videollamadas de la tienda virtual y hacer el seguimiento adecuado por WhatsApp."),
        ("plugs-connected", "Rápida integración", "La integración se realiza a través de sencillos pasos. Además, cuenta con un dashboard para el monitoreo online."),
        ("sliders-horizontal", "Funciones avanzadas", "Recuperación de videollamada, transferencia a un segundo nivel de atención y posibilidad de compartir pantalla."),
        ("qr-code", "Inicio múltiple", "Tus clientes podrán iniciar llamadas desde cualquier lugar, ya sea por web, QR, tótem o kioscos."),
    ], cols=4)
    body += "\n" + section(feats, soft=True)

    how = steps([
        "Inserción de script en tu página web.",
        "Aparece un icono de atención de videollamada.",
        "El usuario ingresa sus datos.",
        "Inicio de la videollamada.",
        "El sistema asigna la videollamada al agente de venta o atención al cliente disponible, que pueden ser remotos.",
        "Durante la videollamada los ejecutivos pueden compartir pantalla, transferir la videollamada a un especialista, compartir archivos, etc.",
        "Finalizada la videollamada, enviamos la encuesta al cliente para que califique la atención.",
        "Posibilidad de hacer seguimientos post atención por WhatsApp.",
    ], cols=4)
    intro = ('<p class="lead lead--wide" data-reveal>¿Te gustaría ofrecer a tus clientes la posibilidad de realizar una videollamada desde tu web y resolver todas sus dudas? '
             '¡Con nuestro sistema de “Video Consulta en Vivo” puedes eso y mucho más!</p>')
    body += "\n" + section(intro + how, eyebrow="¿Cómo funciona?", title="Videollamadas desde tu " + hl("propia web"))

    vids = f'<div class="video-grid"><div data-reveal>{yt("zWEc2dlb7Dg", "WIXperiences: videoconferencia")}</div><div data-reveal>{yt("RzZoi9rZBl4", "WIXperiences: una herramienta, múltiples posibilidades")}</div></div>'
    body += "\n" + section(
        vids, eyebrow="Videoconferencia", title="Una herramienta, " + hl("múltiples posibilidades"),
        lead="Podrás incrementar no solo las ventas en tu e-commerce, sino también la confianza en tu negocio y la calidad de la atención postventa.", soft=True)

    adv = feat_grid([
        ("storefront", "Eficiencia en la atención", "A través de las videollamadas, tu cliente podrá experimentar la modalidad de live video shopping, lo que permitirá generar una experiencia de compra personalizada."),
        ("trend-up", "Potenciar las ventas", "Gracias a la atención personalizada de tus ejecutivos, tus clientes se sentirán seguros de realizar la compra, lo que se traduce en una mejora en la tasa de conversión."),
        ("clock-counter-clockwise", "Trazabilidad de la atención", "Nuestro sistema te permite identificar al cliente y tener un histórico de sus últimas gestiones para mejorar y personalizar su experiencia con la marca."),
        ("headset", "Calidad de atención postventa", "Tus clientes se sentirán tranquilos de recibir la atención que requieren de una manera directa y eficaz, sin hacer largas colas ni desplazarse de su domicilio."),
        ("database", "Incremento de base de datos", "Todas las llamadas son registradas y derivadas a un CRM, lo que permite a los ejecutivos comerciales realizar el proceso de venta de una manera sencilla y eficaz."),
        ("arrows-out", "Escalabilidad en el negocio", "Mediante esta herramienta podrás mantener tu empresa actualizada a las tendencias del mercado y fortalecer tu ecosistema digital."),
    ], cols=3)
    body += "\n" + section(adv, eyebrow="Ventajas", title="Ventajas de Wi " + hl("Xperiences"))

    where = feat_grid([
        ("bank", "Banca y servicios financieros", "Compañías que se encargan de todo tipo de transacciones económicas."),
        ("first-aid-kit", "Ciencias de la salud", "Hospitales, clínicas y centros de salud, tanto privados como públicos."),
        ("factory", "Industria", "Compañías fabricantes de bienes con venta directa B2B o B2C."),
        ("shopping-bag", "Retail", "Empresas especializadas en la venta de productos al gran público."),
        ("buildings", "Sector público", "Organismos administrativos tanto gubernamentales como de comunidades autónomas."),
        ("shield-check", "Seguros", "Compañías aseguradoras, tanto de personas como a empresas y sectores."),
        ("lightning", "Telco, utilities y energía", "Empresas de telecomunicaciones, gas, agua, carreteras, electricidad…"),
        ("airplane-tilt", "Turismo y transporte", "Agencias de viajes, aerolíneas, tren, autobús y hospitality en general."),
    ], cols=4)
    body += "\n" + section(where, eyebrow="Sectores", title="¿Dónde " + hl("aplicarlo") + "?", soft=True)

    why = kpis([("", 200000, "+", "Videollamadas atendidas desde 2018"), ("", 10, "+", "Años en desarrollo de software para omnicanalidad")])
    body += "\n" + section(
        why + '<p class="lead lead--wide" data-reveal>Nuestra experiencia y éxito proveyendo el servicio de videollamadas ha sido imprescindible para el crecimiento de nuestros clientes en campos como la telemedicina, telecomunicaciones y retail. Somos parte de Wimprove, una empresa con proyectos de banca, telecomunicaciones, retail y seguros.</p>',
        eyebrow="Experiencia", title="Por qué Wi " + hl("Xperiences"))

    body += "\n" + cta_band(r, "¿Quieres empezar a mejorar tus ventas?", "Escríbenos para mayor información.", ctx)
    return product_page("wixperiences", "WIXperiences: sistema de videollamadas para atender a tus clientes desde tu web, QR, tótem o kioscos. Más de 200,000 videollamadas atendidas desde 2018.", body)


def page_wicontact():
    path = "catalogo/productos/wicontact/"
    r = root_for(path)
    ctx = "Producto de interés: Wi Contact"
    body = page_hero(
        r, trail_p(r, "Wi Contact"), "Con Wi Contact transforma tu Contact Center", "Experiencia " + hl("omnicanal") + " con IA",
        "Conecta con tus clientes a través de todos los canales en tiempo real: teléfono, chat, redes sociales, email y más, desde una única plataforma.",
        p_ctas("Contáctanos"), hero_img(r, "img/products/wicontact.webp", "Ejecutiva de contact center con diadema en una oficina", small=True))

    what = split(
        img(r, "img/wicontact/hombre-rombo.webp", "Ejecutivo con tablet", 410, 468, "split__fig"),
        '<span class="eyebrow">Plataforma</span><h2 class="h2" data-split>¿Qué es Wi ' + hl("Contact") + '?</h2>'
        '<p class="lead">Wi Contact es un software de contact center omnicanal diseñado para centralizar y gestionar de manera eficiente las interacciones con los clientes a través de diversos canales: voz, chat, correo electrónico, redes sociales, mensajería instantánea y videollamadas. Su integración con inteligencia artificial permite automatizar procesos clave, como la clasificación y priorización de interacciones, la generación de respuestas inteligentes y el análisis avanzado de datos para mejorar la toma de decisiones.</p>'
        '<p class="lead">Destaca por ofrecer una experiencia unificada, adaptándose a las necesidades específicas de cada cliente, al tiempo que optimiza el tiempo y los recursos de los agentes para maximizar la productividad y la satisfacción del cliente.</p>')
    body += "\n" + section(what)

    flujo = f'<div class="flow" data-reveal>{img(r, "img/wicontact/flujo.webp", "Diagrama del flujo general de Wi Contact", 1296, 813)}</div>'
    body += "\n" + section(flujo, eyebrow="Arquitectura", title="Flujo " + hl("general"), soft=True)

    feats = tabs("wc", [
        ("Omnicanalidad", [
            ("Integración de múltiples canales", "Un sistema omnicanal permite interactuar con los clientes a través de teléfono, correo electrónico, mensajería instantánea (WhatsApp, Telegram), redes sociales (Facebook, Twitter), chat en vivo y videollamadas, todo gestionado desde una única plataforma. Esto permite ofrecer una experiencia consistente al cliente, independientemente del canal que elija."),
            ("Transición fluida entre canales", "Los agentes tienen acceso completo al historial de la conversación del cliente, lo que facilita la continuidad sin que el cliente deba repetir su información o contexto al cambiar de canal."),
        ]),
        ("Chatbots y asistentes virtuales", [
            ("Automatización y respuestas rápidas", "Los chatbots basados en IA automatizan respuestas, resolviendo consultas frecuentes o simples y mejorando la eficiencia operativa al reducir la carga de trabajo de los agentes humanos. Pueden responder 24/7 y escalar a agentes humanos cuando sea necesario."),
            ("Procesamiento de lenguaje natural (PLN)", "A través de IA y PLN, los chatbots comprenden mejor las preguntas de los clientes, pueden identificar sentimientos y ofrecer respuestas más humanizadas."),
            ("Desempeño predictivo", "Utilizando machine learning, los chatbots mejoran con el tiempo, anticipando mejor las necesidades del cliente y ofreciendo soluciones más precisas."),
        ]),
        ("Inteligencia artificial en el contact", [
            ("Análisis de sentimientos y emociones", "La IA puede analizar las interacciones con los clientes (por texto o voz) para detectar el sentimiento o el tono emocional (satisfacción, frustración, etc.), lo que ayuda a los agentes a intervenir de manera más efectiva cuando se detecta un sentimiento negativo o urgente."),
            ("Asistencia en tiempo real para agentes", "Los sistemas de IA pueden proporcionar sugerencias o información adicional en tiempo real a los agentes durante una llamada o chat, mejorando la calidad y rapidez de las respuestas."),
            ("Enrutamiento inteligente de llamadas", "La IA puede dirigir automáticamente a los clientes al agente más adecuado basándose en su historial, necesidades y sentimientos detectados, optimizando la gestión de recursos."),
        ]),
        ("Videollamadas", [
            ("Interacción cara a cara a través de video", "Las videollamadas permiten una comunicación visual directa entre el cliente y el agente, útil para consultas complejas, demostraciones de productos o soluciones visuales."),
            ("Integración con otras funciones", "Durante una videollamada, los agentes pueden compartir pantallas, documentos o realizar demostraciones, lo que agrega un valor significativo a la experiencia del cliente."),
            ("Mejora de la relación con el cliente", "La videollamada puede ayudar a construir relaciones más cercanas y generar mayor confianza con los clientes, especialmente cuando se resuelven problemas complejos o se realizan ventas de productos que requieren una explicación detallada."),
        ]),
        ("Análisis y reportes en tiempo real", [
            ("Monitoreo y evaluación", "El sistema ofrece dashboards con información en tiempo real sobre el rendimiento de los agentes, la duración de las interacciones, los niveles de satisfacción del cliente y el desempeño del chatbot."),
            ("Análisis de tendencias", "La IA también puede generar informes sobre tendencias de comportamiento de clientes, patrones de consultas comunes y el rendimiento de la atención a través de distintos canales."),
        ]),
        ("Escalabilidad y adaptabilidad", [
            ("Escalabilidad de recursos", "Este tipo de sistema es altamente escalable: puede crecer junto con las necesidades de la empresa, agregando más agentes, canales y funcionalidades según sea necesario."),
            ("Adaptabilidad multicanal", "Los sistemas omnicanal permiten integrar nuevos canales conforme surgen, asegurando que el sistema esté siempre actualizado y alineado con las preferencias del cliente. Al ser una plataforma desarrollada por nosotros, se puede ajustar a las necesidades del cliente, desarrollándola e implementándola según lo que requiera."),
        ]),
    ])
    body += "\n" + section(feats, eyebrow="Funcionalidades", title="Características " + hl("principales"))

    benefits = [
        ("Mejora de la experiencia del cliente", "beneficios-01", [
            ("Disponibilidad 24/7", "Gracias a los chatbots y la automatización, los clientes pueden recibir asistencia en cualquier momento, incluso fuera del horario laboral. Esto asegura una experiencia continua, sin tiempos de espera."),
            ("Canales diversificados", "La omnicanalidad permite a los clientes elegir el canal más conveniente para ellos, como mensajería instantánea, redes sociales, correo electrónico o videollamadas, lo que mejora la accesibilidad y la satisfacción."),
            ("Interacciones más humanas", "Las videollamadas añaden un componente humano que fortalece la relación con el cliente, especialmente en situaciones complejas o cuando se necesita un toque más personalizado."),
            ("Respuestas rápidas y precisas", "Los chatbots, habilitados por IA, pueden manejar consultas frecuentes, reduciendo el tiempo de espera y proporcionando respuestas precisas de inmediato."),
        ]),
        ("Eficiencia operativa y reducción de costos", "beneficios-02", [
            ("Automatización de tareas repetitivas", "Los chatbots automatizan respuestas a preguntas comunes, liberando a los agentes humanos de tareas repetitivas para que se enfoquen en problemas más complejos."),
            ("Reducción de errores humanos", "Al automatizar la gestión de consultas básicas, se reduce el riesgo de errores humanos y mejora la precisión de la información proporcionada a los clientes."),
            ("Enrutamiento inteligente de llamadas", "Con IA, el sistema identifica automáticamente el motivo de la llamada o el chat y dirige a los clientes al agente adecuado, mejorando el tiempo de resolución y la eficiencia operativa."),
            ("Escalabilidad", "El sistema escala fácilmente a medida que aumentan los volúmenes de interacciones, sin necesidad de contratar más personal, lo que reduce los costos operativos."),
        ]),
        ("Optimización del tiempo de respuesta y resolución", "beneficios-03", [
            ("Atención inmediata", "Los chatbots proporcionan respuestas instantáneas a las consultas. Cuando se necesita atención humana, el sistema omnicanal asegura que el cliente sea transferido al agente adecuado de forma rápida."),
            ("Soporte multicanal sin interrupciones", "Los clientes pueden cambiar de un canal a otro (de chat a llamada o videollamada) sin perder el contexto de la conversación, lo que mejora la continuidad del servicio."),
        ]),
        ("Análisis y mejoras continuas", "beneficios-04", [
            ("Análisis de sentimientos y tiempos de respuesta", "Gracias a la IA, es posible analizar el sentimiento de las interacciones de los clientes (por ejemplo, frustración o satisfacción) y adaptar la estrategia de atención en tiempo real."),
            ("Informes y reportes detallados", "El sistema proporciona informes detallados sobre el desempeño, los tiempos de respuesta y las interacciones con los clientes, lo que facilita la evaluación de la calidad del servicio y la toma de decisiones informadas."),
        ]),
        ("Mejor gestión de recursos", "beneficios-05", [
            ("Reducción de la carga sobre los agentes humanos", "Al manejar los problemas más simples y rutinarios con chatbots, los agentes humanos tienen más tiempo para ocuparse de problemas más complejos, mejorando su productividad y reduciendo el riesgo de agotamiento."),
            ("Gestión de llamadas y chats eficiente", "Los sistemas omnicanal permiten gestionar una mayor cantidad de interacciones con un número limitado de agentes, optimizando la distribución de tareas y mejorando el rendimiento."),
        ]),
        ("Mejor rentabilidad", "beneficios-06", [
            ("Bajos costos de implementación", "A pesar de integrar múltiples tecnologías avanzadas, el sistema de contact center omnicanal con IA y chatbots tiene un bajo costo operativo, ya que muchas interacciones se manejan automáticamente sin intervención humana."),
            ("Menor necesidad de personal adicional", "Al automatizar una gran parte del servicio al cliente, las empresas pueden reducir la necesidad de contratar más personal y lograr una mayor rentabilidad."),
        ]),
        ("Competitividad y diferenciación", "beneficios-07", [
            ("Innovación y modernización del servicio", "La integración de videollamadas y IA no solo mejora la experiencia del cliente, sino que posiciona a la empresa como líder en innovación en su sector."),
            ("Atención personalizada", "La capacidad de usar videollamadas permite una interacción más cercana y personalizada, muy apreciada por los clientes, especialmente en industrias como la banca, la salud o la tecnología."),
        ]),
    ]
    rows = []
    for i, (title, image, items) in enumerate(benefits):
        copy = f'<h3 class="h3">{title}</h3><dl class="deflist">' + "".join(f"<div><dt>{t}</dt><dd>{x}</dd></div>" for t, x in items) + "</dl>"
        rows.append(f'<div class="benefit">{split(img(r, f"img/wicontact/{image}.webp", "", 397, 560, "split__photo"), copy, reverse=bool(i % 2))}</div>')
    body += "\n" + section("".join(rows), eyebrow="Beneficios", title=hl("Beneficios") + " de Wi Contact", soft=True, cls="section--benefits")

    cases = feat_grid([
        ("headset", "Atención al cliente", "Resolución de consultas rápida y personalizada, escalamiento inteligente a agentes humanos, gestión de reclamos y seguimiento, y análisis de sentimientos y retroalimentación."),
        ("clock-clockwise", "Soporte 24/7 y reducción de carga operativa", "Resolución rápida de problemas técnicos, escalamiento eficiente a soporte humano, proactividad en soporte técnico, seguimiento automatizado y gestión de casos, y análisis predictivo con mejoras continuas."),
        ("target", "Ventas y generación de leads", "Automatización del contacto inicial, calificación de prospectos, seguimiento multicanal personalizado, recomendaciones inteligentes, análisis de conversaciones y uso de IA."),
        ("users-three", "Gestión de recursos humanos", "Automatización de consultas comunes de empleados e integración con sistemas de gestión de personal."),
        ("graduation-cap", "Onboarding y capacitación automatizada", "Automatización del proceso de incorporación y capacitación continuada."),
        ("calendar-check", "Gestión de solicitudes y permisos", "Automatización de solicitudes de permiso y vacaciones, con aprobación rápida."),
        ("chart-bar", "Evaluaciones de desempeño y feedback", "Encuestas de retroalimentación automáticas y análisis de sentimientos y tendencias."),
    ], cols=3)
    body += "\n" + section(cases, eyebrow="Casos de uso", title="Casos de " + hl("uso"))

    faqs = faq("wcfaq", [
        ("¿Qué canales soporta?", "Wi Contact soporta una amplia gama de canales, incluyendo llamadas telefónicas, WhatsApp, redes sociales como Facebook Messenger e Instagram, correos electrónicos, chat en vivo y más. Además, ofrecemos soporte para chatbots impulsados por IA para automatizar interacciones."),
        ("¿Es fácil de integrar con mi sistema actual?", "Sí, Wi Contact está diseñado para integrarse sin complicaciones con la mayoría de los sistemas actuales, incluyendo CRMs, ERPs y plataformas de comunicación. Contamos con APIs robustas y documentación detallada para garantizar una implementación ágil."),
        ("¿Ofrecen soporte técnico?", "Claro que sí. Brindamos soporte técnico 24/7 con un equipo especializado listo para ayudarte en cualquier momento. Además, ofrecemos recursos como guías, tutoriales y capacitaciones para maximizar el uso de la plataforma."),
        ("¿Qué pasa si mi empresa crece y necesito más licencias o funcionalidades?", "Puedes ampliar tus licencias o agregar módulos adicionales según sea necesario. Nuestro equipo comercial y tecnológico te ayudará con el proceso."),
        ("¿Es posible monitorear las interacciones en tiempo real?", "Sí, los supervisores pueden escuchar llamadas en tiempo real, supervisar chats y realizar intervenciones si es necesario."),
        ("¿Cómo administrar a mis agentes?", "Puedes gestionar agentes desde un panel de administración, asignarles canales específicos, supervisar su desempeño y configurar roles y permisos."),
    ])
    faq_split = split('<div class="stack-sm">' + yt("vy82iU7lWqA", "Ejemplo práctico de atención omnicanal en Wi Contact") + img(r, "img/wicontact/dashboard.webp", "Dashboard de reportes de Wi Contact", 770, 489, "round") + '</div>',
                      '<span class="eyebrow">Preguntas frecuentes</span><h2 class="h2" data-split>Resolvemos tus ' + hl("dudas") + '</h2>' + faqs)
    body += "\n" + section(faq_split, soft=True)

    extra = bullet_list([
        "Te asesoraremos sobre qué modalidad se adapta mejor a tus necesidades.",
        "Wi Contact está disponible en modalidad cloud.",
        "Una vez dado de alta, nuestro equipo de consultores se encarga de la implementación, entregando un servicio integrado y garantizando el funcionamiento.",
    ])
    body += "\n" + cta_band(r, "Solicita un presupuesto personalizado", "Cuéntanos tu operación.", ctx, extra)
    return product_page("wicontact", "Wi Contact: software de contact center omnicanal con inteligencia artificial. Voz, chat, WhatsApp, redes sociales, email y videollamadas desde una sola plataforma.", body)


def page_wimail():
    path = "catalogo/productos/wi-mail/"
    r = root_for(path)
    body = page_hero(
        r, trail_p(r, "Wi Mail"), "Wi Mail", "Medición de atención de " + hl("cuentas de correo") + " corporativas",
        "Permite responder en forma rápida y eficiente los correos que van llegando a un buzón corporativo.",
        p_ctas("Contáctanos"), hero_img(r, "img/products/wimail.webp", "Laptop con correo electrónico", small=True))
    feats = feat_grid([
        ("envelope-simple", "Correos", "Prioriza la asignación de correos a los agentes, permitiendo medir sus tiempos de atención a través de herramientas de medición de SLA."),
        ("archive", "Almacena", "El sistema almacena toda la evidencia de los correos para que posteriormente sea un sustento para fines contractuales del servicio."),
    ], cols=2)
    body += "\n" + section(feats, eyebrow="Wi Mail", title="Características de " + hl("Wi Mail"), soft=True)
    body += "\n" + _iaudit_promo(r)
    body += "\n" + section(related(r, "productos", "wi-mail", ["wi-iaudit", "wicontact", "wi-desk"]), eyebrow="Otros productos", title="Te pueden " + hl("interesar"), soft=True)
    body += "\n" + cta_band(r, "Mejora la gestión de tu buzón corporativo", "Déjanos un mensaje y te contamos cómo funciona Wi Mail.", "Producto de interés: Wi Mail")
    return product_page("wi-mail", "Wi Mail es un sistema de medición de atención de cuentas de correo corporativas: prioriza correos, mide SLA y almacena la evidencia.", body)


def page_wiinteligence():
    path = "catalogo/productos/wi-inteligence/"
    r = root_for(path)
    body = page_hero(
        r, trail_p(r, "Wi Inteligence"), "Wi Inteligence", "Integración de información a través de un " + hl("almacén de datos") + " especializado",
        "Permite recabar la información histórica de las operaciones con la dimensionalidad y estructura necesarias para el desarrollo de las métricas.",
        p_ctas("Contáctanos"), hero_img(r, "img/products/iaudit-hero.webp", "Diagrama de un almacén de datos que integra llamadas, audios y correos"))
    feats = feat_grid([
        ("trend-up", "Productividad", "Aumentar el nivel de productividad implementando los controles en línea."),
        ("coins", "Reducción", "Reducir los costos en los puestos relacionados (back office y analistas)."),
        ("clock", "Tiempos", "Mejorar el tiempo de disposición de la información."),
    ], cols=3)
    body += "\n" + section(feats, eyebrow="Beneficios", title="Beneficios de Wi " + hl("Inteligence"), soft=True)
    body += "\n" + _iaudit_promo(r)
    body += "\n" + section(related(r, "productos", "wi-inteligence", ["wi-iaudit", "wicontact", "wi-desk"]), eyebrow="Otros productos", title="Te pueden " + hl("interesar"), soft=True)
    body += "\n" + cta_band(r, "Convierte tus datos en decisiones", "Déjanos un mensaje y te contamos cómo funciona Wi Inteligence.", "Producto de interés: Wi Inteligence")
    return product_page("wi-inteligence", "Wi Inteligence integra la información histórica de tu operación en un almacén de datos especializado para desarrollar métricas.", body)


def page_widesk():
    path = "catalogo/productos/wi-desk/"
    r = root_for(path)
    body = page_hero(
        r, trail_p(r, "Wi Desk"), "CRM", "Los agentes pueden administrar " + hl("interacciones omnicanal"),
        "Consultar KPI, realizar transferencias de llamadas y más. Gracias al clic para marcar, pueden hacer clic en cualquier contacto del CRM para llamar de inmediato.",
        p_ctas("Contáctanos"), hero_img(r, "img/products/widesk.webp", "Ejecutivo gestionando clientes desde un CRM", small=True))
    feats = feat_grid([
        ("clock-counter-clockwise", "Historial del cliente", "El historial del cliente brinda a los agentes la posibilidad de tener conversaciones contextuales, ofreciendo un soporte al cliente personalizado y sin problemas."),
        ("microphone", "Grabaciones y detalles", "Las grabaciones y los detalles de la interacción se almacenan automáticamente en tu CRM, lo que proporciona datos estadísticos más amplios y útiles para la gestión y los informes de clientes potenciales."),
    ], cols=2)
    body += "\n" + section(feats, eyebrow="Wi Desk", title="Características del " + hl("CRM"), soft=True)
    body += "\n" + _iaudit_promo(r)
    body += "\n" + section(related(r, "productos", "wi-desk", ["wicontact", "wi-iaudit", "chatbots"]), eyebrow="Otros productos", title="Te pueden " + hl("interesar"), soft=True)
    body += "\n" + cta_band(r, "Administra tus interacciones en un solo lugar", "Déjanos un mensaje y te contamos cómo funciona Wi Desk.", "Producto de interés: Wi Desk")
    return product_page("wi-desk", "Wi Desk: CRM para que los agentes administren interacciones omnicanal, consulten KPI, transfieran llamadas y marquen con un clic.", body)


def page_chatbots():
    path = "catalogo/productos/chatbots/"
    r = root_for(path)
    ctx = "Producto de interés: Chatbots"
    body = page_hero(
        r, trail_p(r, "Chatbots"), "Wi Contact Chatbot", "Despliega toda tu experiencia con nuestro servicio de " + hl("chatbot"),
        "Es un servicio ininterrumpido de chats sobre tu página web, para atender a tus clientes o capturar leads a través de las múltiples campañas que realices. Además, puedes integrar los canales de chat con llamadas y videollamadas.",
        p_ctas("Solicitar más información"),
        video(r, "chatbots.mp4", "img/chatbots/chatbot-03.webp", "Demostración del chatbot de Wi Contact"))

    c1 = ('<h3 class="h3">Coloca tu propio logotipo y los colores de la caja de texto de acuerdo con el branding de tu marca</h3>'
          '<p class="lead">Todos los mensajes de bienvenida y alertas que puedan generar una mejor experiencia al cliente.</p>'
          '<h4 class="h4">Personalización de tiempos por cada integración</h4>'
          '<p class="lead">Configura el horario comercial de tu negocio para que el chatbot responda de manera personalizada cuando no estén disponibles tus asesores comerciales.</p>')
    c2 = ('<h3 class="h3">Eficiencia en ventas</h3>'
          '<p class="lead">El diseño de los flujos de atención de los bots permite respuestas que orientan al cliente sobre tus productos o servicios. Si el bot requiere más orientación, se deriva a un agente humano para que se complete la atención y el cliente quede satisfecho.</p>')
    c3 = ('<h3 class="h3">Carteriza la atención de tus clientes con personal especializado en WhatsApp</h3>'
          '<p class="lead">Nuestro sistema puede identificar los números de tus clientes y derivarlos rápidamente con agentes especializados por WhatsApp, sin hacerlos pasar por un menú de opciones. Y si el cliente desea contactar al mismo agente por WhatsApp mediante un ID, lo derivamos al mismo agente de la atención.</p>'
          '<p class="lead">Para toda esta gestión se apoya en un sistema de CRM.</p>')
    rows = "".join([
        '<div class="benefit">' + split(img(r, "img/chatbots/chatbot-01.webp", "Branding personalizado del chatbot", 644, 644, "split__photo"), c1) + "</div>",
        '<div class="benefit">' + split(img(r, "img/chatbots/chatbot-02.webp", "Gráfica de ventas", 644, 644, "split__photo"), c2, reverse=True) + "</div>",
        '<div class="benefit">' + split(img(r, "img/chatbots/chatbot-03.webp", "Ejecutiva de Contact Center", 644, 644, "split__photo"), c3) + "</div>",
    ])
    body += "\n" + section(rows, soft=True, cls="section--benefits")

    srv = feat_grid([
        ("whatsapp-logo", "Inbound WhatsApp", "Uso de distintos números a nivel mundial. Múltiples clientes con múltiples asesores. Formularios dinámicos para datos adicionales o tipificaciones. Inserción sencilla en páginas web."),
        ("paper-plane-tilt", "Outbound WhatsApp", "Mensajes y plantillas preconfigurados. Interacciones salientes simultáneas por un mismo asesor. Transferencia de archivos (imágenes, audio, video y más). Envío de emojis."),
        ("star", "NPS", "Encuesta de satisfacción con preguntas personalizadas y derivación automática o manual hacia encuestas de satisfacción."),
        ("tree-structure", "IVR de WhatsApp", "Personalización de árboles de decisión sin restricción de niveles, con opciones de derivación hacia campañas y hacia asesores."),
        ("chat-text", "Mensajes preconfigurados", "Personalización de mensajes: bienvenida, fuera de horario y más."),
        ("arrows-left-right", "Transferencias de interacciones", "Traslado de chats a otro nivel de atención."),
    ], cols=3)
    body += "\n" + section(srv, eyebrow="Servicios", title=hl("Servicios") + " incluidos")

    imp = feat_grid([
        ("target", "Captura los leads 24 horas", "Nuestro sistema puede capturar los registros de los leads 24×7 y así ubicar a nuestros potenciales clientes."),
        ("sparkle", "Mejoramos la experiencia", "Nuestros sistemas de mensajería pueden cambiar de canal para dar una mejor experiencia al cliente a través de videollamadas o llamadas con ejecutivos especializados."),
        ("robot", "Atención automatizada", "De manera fácil y sencilla siempre estaremos para atender a los clientes por los canales digitales, a través de la página web, WhatsApp, etc."),
    ], cols=3)
    body += "\n" + section(imp, eyebrow="Beneficios", title="El chatbot de Wi Contact " + hl("mejora la experiencia") + " de tu cliente", soft=True)

    easy = feat_grid([
        ("headset", "Wi Contact online", "Un ejecutivo de servicio tomará la gestión de la conversación en lugar del chatbot cuando el cliente lo solicite o cuando se identifiquen oportunidades de venta."),
        ("address-book", "CRM Wi Contact", "De manera fácil podrás diseñar los formularios con los campos que necesitas, definiendo tipos de datos y validaciones que te permitan tener una base de datos impecable y reportes para las ventas."),
        ("browsers", "Widget de canales digitales", "Mediante nuestros widgets podemos generar en tiempo real videollamadas y chats por WhatsApp, Messenger, chat web, etc., insertados desde las páginas web o tiendas en línea para apoyar una venta con un bot o ejecutivo comercial."),
        ("whatsapp-logo", "Chatbot para WhatsApp", "Integra tu sistema con nuestra API para procesos de self-service para tus clientes a través de WhatsApp: ver fechas de pago, saldos de algún servicio, cambio de planes, etc. Tenemos integración con WhatsApp Business API y apoyamos al cliente en las altas."),
        ("facebook-logo", "Chatbot para Facebook", "De manera fácil podemos implementar FAQs para tus redes sociales y dar respuestas inmediatas, e incluir imágenes para seleccionar respuestas u orientar a los clientes."),
    ], cols=3)
    body += "\n" + section(
        '<p class="lead lead--wide" data-reveal>Nuestra omnicanalidad permite que tus clientes se comuniquen de manera sencilla y que la atención por bots o por agentes humanos sea más sencilla.</p>' + easy,
        eyebrow="Omnicanalidad", title="Wi Contact facilita que tus clientes " + hl("se comuniquen") + " de manera sencilla")

    ent = ('<p class="lead lead--wide" data-reveal>Podemos integrarnos con CRMs como Salesforce, Microsoft Dynamics, etc. Nuestra integración con WhatsApp mediante una API permite la consulta, el registro de eventos, la automatización y el control de flujo con cualquier sistema que soporte REST. '
           'Contamos con seguridad para el acceso a nuestra API y somos compatibles con todos los estándares de seguridad.</p>')
    body += "\n" + section(ent, eyebrow="Integraciones", title="Wi Contact " + hl("empresarial"), soft=True)
    body += "\n" + cta_band(r, "¿Quieres empezar a mejorar tus ventas?", "Escríbenos para mayor información.", ctx)
    return product_page("chatbots", "Chatbot de Wi Contact: atención ininterrumpida en tu web y WhatsApp, captura de leads 24/7, IVR, NPS e integración con tu CRM.", body)


def page_voicebots():
    path = "catalogo/productos/voicebots/"
    r = root_for(path)
    body = page_hero(
        r, trail_p(r, "Voicebots"), "Voicebots", "Una conversación " + hl("por voz") + " natural y guiada con tus usuarios",
        "Programa informático evolucionado, gracias al Procesamiento de Lenguaje Natural (NLP) y a la inteligencia artificial (IA).",
        p_ctas("Contáctanos"), hero_img(r, "img/products/voicebots.webp", "Ejecutivo hablando por teléfono mientras trabaja", small=True))
    feats = feat_grid([
        ("brain", "Intenciones y emociones", "Gracias a tecnologías como machine learning, sentiment analysis y natural language understanding, se pueden recoger, en una misma conversación, las intenciones y emociones de las personas, proporcionando una respuesta ágil y eficaz y re-entrenando al bot para predecir mejor estas consultas en el futuro."),
        ("chats-circle", "Omnicanalidad automatizada", "Las interacciones entre los sistemas automatizados y los clientes pueden realizarse por distintos canales. Los voicebots con IA y procesamiento de voz atienden telefónicamente las consultas y también en los mismos canales que un chatbot."),
        ("headset", "Atención más eficiente", "Los voicebots se adaptan al usuario y a la tarea, no tienen problemas con picos de peticiones, ayudan a los agentes a responder rápido si son híbridos, permiten respuestas multi-idioma y ofrecen un servicio 24/7 integrado con cualquier CRM de la compañía, con traza de todas las peticiones."),
        ("coins", "Menores costos, retorno rápido", "La gestión automatizada de las interacciones permite reducir los tiempos de llamada y solucionar dudas sin intervención de un agente humano, reduciendo los costos de capacitación, contratación, espacio en oficinas y equipos, y logrando un rápido retorno de la inversión (ROI)."),
    ], cols=2)
    body += "\n" + section(feats, eyebrow="Voicebots", title="Características de los " + hl("Voicebots"), soft=True)
    body += "\n" + _iaudit_promo(r)
    body += "\n" + section(related(r, "productos", "voicebots", ["chatbots", "wicontact", "wi-iaudit"]), eyebrow="Otros productos", title="Te pueden " + hl("interesar"), soft=True)
    body += "\n" + cta_band(r, "Automatiza tu atención por voz", "Déjanos un mensaje y te contamos cómo funcionan los Voicebots.", "Producto de interés: Voicebots")
    return product_page("voicebots", "Voicebots de Wimprove: conversación por voz natural y guiada con procesamiento de lenguaje natural e inteligencia artificial, 24/7.", body)


def _iaudit_promo(r):
    """Bloque de video compartido por varias fichas de producto (en la web actual aparece en todas)."""
    inner = f'<div class="video-solo" data-reveal>{yt("0QrAzBkCe1Q", "Cómo analizar la calidad de las llamadas del call center")}</div>'
    return section(
        inner, eyebrow="Wi IAudit", center=True,
        title="¿Quieres mejorar cómo analizas la calidad de las llamadas en el " + hl("call center") + "?",
        lead="Convertirás la información de tus llamadas en una fuente de eficiencia y productividad.")


# ================================================================ soluciones

ACTIONS = [
    ("presentation-chart", "Solicitar una demostración"),
    ("gift", "Prueba gratis"),
    ("puzzle-piece", "Diseña tu solución"),
    ("receipt", "Solicitar presupuesto"),
]


def _actions(name):
    cards = "".join(
        f'<a class="action" data-reveal href="#contacto" data-set-context="Solución de interés: {name} — {label}"><span class="action__icon">{ic(icon)}</span><span>{label}</span>{ic("arrow-right")}</a>'
        for icon, label in ACTIONS)
    return f'<div class="actions">{cards}</div>'


def _solution_body(slug, eyebrow, headline, lead, content_html, second_img, second_alt):
    path = f"catalogo/soluciones/{slug}/"
    r = root_for(path)
    s = solution(slug)
    ctx = f"Solución de interés: {s['name']}"
    body = page_hero(r, trail_s(r, s["name"]), eyebrow, headline, lead, p_ctas("Contáctanos"),
                     hero_img(r, s["img"], s["name"]))
    body += "\n" + section(_actions(s["name"]), soft=True, cls="section--tight")
    media = img(r, second_img, second_alt, 750, 580, "split__photo")
    body += "\n" + section(split(media, content_html, reverse=True))
    others = [x["slug"] for x in SOLUTIONS if x["slug"] != slug]
    body += "\n" + section(related(r, "soluciones", slug, others), eyebrow="Soluciones", title="Impulsamos tu negocio de manera " + hl("eficaz"), soft=True)
    body += "\n" + cta_band(r, "Hablemos de " + s["name"].lower(), "Cuéntanos qué necesitas y te acompañamos.", ctx)
    return r, body


def page_atencion():
    content = ('<span class="eyebrow">Desde el punto de vista estratégico</span><h2 class="h2" data-split>El servicio al cliente es ' + hl("lo más importante") + '</h2>'
               '<p class="lead">Entregamos al cliente una experiencia única de atención con el objetivo primordial de resolver las necesidades del cliente en la primera llamada, con los mejores índices de calidad del mercado.</p>'
               '<p class="lead">El servicio al cliente es lo más importante desde el punto de vista estratégico: hoy los clientes son más exigentes que en el pasado. Wi Contact puede cerrar la brecha entre tus objetivos de servicio al cliente y el servicio que realmente puedes brindar. Podemos implementar un voicebot con funciones de enrutamiento y un self-service para un primer contacto con los clientes con bots y, en una segunda línea, un agente de servicio al cliente, todo acompañado de un CRM de gestión interna o externa como Salesforce y Dynamics.</p>')
    r, body = _solution_body("atencion-al-cliente", "Atención al cliente", "Genera una experiencia " + hl("única") + " de servicio",
                             "Entregamos al cliente una experiencia única de atención con el objetivo primordial de resolver sus necesidades.",
                             content, "img/solutions/atencion-al-cliente-2.webp", "Cliente atendido por teléfono")
    return solution_page("atencion-al-cliente", "Atención al cliente con Wimprove: resolución en la primera llamada, voicebots, self-service y CRM integrado.", body)


def page_cobranza():
    content = ('<span class="eyebrow">Cobranza</span><h2 class="h2" data-split>Recupera ingresos y mantén a tus clientes ' + hl("satisfechos") + '</h2>'
               '<p class="lead">Recuperación de clientes en cartera vencida: rescatar ese ingreso y mantener a tus clientes satisfechos.</p>')
    r, body = _solution_body("cobranza", "Cobranza", "Recuperación de clientes en " + hl("cartera vencida"),
                             "Rescata ese ingreso y mantén a tus clientes satisfechos.",
                             content, "img/solutions/cobranza-2.webp", "Pagos desde un teléfono móvil")
    return solution_page("cobranza", "Cobranza con Wimprove: recuperación de clientes en cartera vencida manteniendo a tus clientes satisfechos.", body)


def page_telemarketing():
    content = ('<span class="eyebrow">Servicios de crecimiento</span><h2 class="h2" data-split>Más contactos y más ventas por ' + hl("hora") + '</h2>'
               '<p class="lead">Atendemos de manera directa con medios de comunicación efectivos, contactando a tus clientes potenciales y ayudando a la comercialización de tus servicios o productos.</p>'
               '<p class="lead">El centro de contacto de salida Wi Contact ofrece una mayor productividad al mismo tiempo que ayuda a cumplir con regulaciones como la Ley de Protección al Consumidor de cada país. El marcador predictivo de Wi Contact reduce el costo por cliente potencial y mejora la eficiencia del agente, con hasta tres veces más contactos por hora.</p>'
               + bullet_list([
                   "<strong>Ventas: tasas de cierre más altas.</strong> Ya sea un centro de recepción, una operación de ventas de salida o una combinación de ventas de entrada y salida, con Wi Contact experimentarás más contactos y ventas por hora y tiempos de aceleración más rápidos para los nuevos agentes.",
                   "<strong>Marketing: reduce tu costo por cliente potencial.</strong> Para operaciones de marketing que necesitan nutrir prospectos y convertirlos en oportunidades de ventas, Wi Contact permite llegar a más clientes potenciales por hora con la información que tus representantes necesitan para convertirlos más rápido.",
               ]))
    r, body = _solution_body("telemarketing", "Telemarketing", "Aumenta la productividad del " + hl("centro de llamadas"),
                             "Atendemos de manera directa con medios de comunicación efectivos, contactando a tus clientes potenciales.",
                             content, "img/solutions/telemarketing-2.webp", "Ejecutiva de telemarketing")
    return solution_page("telemarketing", "Telemarketing con Wimprove: marcador predictivo, más contactos por hora y mayores tasas de cierre.", body)


def page_helpdesk():
    # Contenido breve a propósito: la web actual casi no tiene texto para esta solución.
    content = ('<span class="eyebrow">Helpdesk</span><h2 class="h2" data-split>Gestiona y ' + hl("soluciona") + ' las necesidades de tus clientes</h2>'
               '<p class="lead">Es un conjunto de recursos tecnológicos y humanos para prestar servicios con la posibilidad de gestionar y solucionar las necesidades de tus clientes.</p>')
    r, body = _solution_body("helpdesk", "Helpdesk", hl("Helpdesk"),
                             "Recursos tecnológicos y humanos para prestar servicios con la posibilidad de gestionar y solucionar.",
                             content, "img/solutions/helpdesk-2.webp", "Ejecutiva de helpdesk")
    return solution_page("helpdesk", "Helpdesk con Wimprove: recursos tecnológicos y humanos para gestionar y solucionar las necesidades de tus clientes.", body)


def page_telemedicina():
    content = ('<span class="eyebrow">Telemedicina</span><h2 class="h2" data-split>La mejor opción para solucionar muchos vacíos en el ' + hl("sistema sanitario") + '</h2>'
               '<p class="lead">Desde la escasez de médicos de atención primaria para poblaciones vulnerables. Nuestra solución se ha implementado hace 6 años en MiConsultorioya: el 80% de las visitas al doctor son enfermedades de primer contacto (gripe, dolor de estómago, dolor muscular, etc.).</p>'
               '<p class="lead">Todo esto se resuelve en minutos, sin salir de la oficina o de casa, sin gastos de traslado ni tiempo de espera, con un costo que no llega al 5% del de una consulta normal y con la más alta calidad de diagnóstico y tratamiento.</p>'
               + bullet_list([
                   "Ayuda a salvar los obstáculos sociales en la sanidad, ya que elimina las barreras físicas para el acceso a la medicina.",
                   "Garantiza una atención más rápida, lo que permite una mayor satisfacción del paciente a la vez que se reducen los costos operacionales.",
                   "Permite distribuir mejor los recursos.",
               ]))
    r, body = _solution_body("telemedicina", "Telemedicina", "Para la " + hl("satisfacción") + " del paciente",
                             "Consulta médica a distancia, sin traslados ni tiempos de espera.",
                             content, "img/solutions/telemedicina-2.webp", "Médico atendiendo a través de una tablet")
    return solution_page("telemedicina", "Telemedicina con Wimprove, implementada hace 6 años en MiConsultorioya: consulta médica a distancia sin traslados ni esperas.", body)


# ================================================================ institucionales

def page_nosotros():
    path = "nosotros/"
    r = root_for(path)
    body = page_hero(r, [("Nosotros", None)], "Nosotros", "De la experiencia al " + hl("software"),
                     "Wimprove nace para desarrollar aplicaciones de software con el fin de asegurar la demanda de los usuarios.")

    ba = (f'<div class="ba" data-ba><img class="ba__after" src="{r}assets/img/about/despues.webp" alt="Ejecutiva trabajando con calma frente a su computadora" width="750" height="580" loading="lazy" />'
          f'<div class="ba__before"><img src="{r}assets/img/about/antes.webp" alt="Ejecutivo de call center frustrado" width="750" height="580" loading="lazy" /></div>'
          '<span class="ba__label ba__label--l">Antes</span><span class="ba__label ba__label--r">Después</span><span class="ba__handle" aria-hidden="true">' + ic("arrows-left-right") + '</span>'
          '<input class="ba__range" type="range" min="0" max="100" value="50" aria-label="Deslizar para comparar antes y después" /></div>')
    story = split(
        ba,
        '<span class="eyebrow">Nuestra historia</span><h2 class="h2" data-split>Software a la medida de lo que ' + hl("requiere tu negocio") + '</h2>'
        '<p class="lead">Hoy en día, las aplicaciones de software deben estar a la altura de las necesidades de las empresas. Nuestro principal beneficio es hacer que los desarrollos estén a la medida de lo que requiere el negocio, con resultados visibles, que respondan a picos de demanda, asequibles y de bajo costo.</p>'
        '<p class="lead">La actividad de las empresas necesita que sus herramientas tecnológicas se mantengan a pleno rendimiento, estén protegidas y supervisadas por un equipo preparado para solucionar cualquier eventualidad en el mínimo espacio de tiempo.</p>')
    body += "\n" + section(story)

    nums = kpis([("", "2014", "", "Año en que iniciamos Wimprove"), ("", 10, "+", "Años en desarrollo de software"),
                 ("", 3, "", "Países con operaciones"), ("", 8, "", "Productos")])
    body += "\n" + section(nums, soft=True, cls="section--kpi")

    vals = feat_grid([
        ("gauge", "Eficiencia", "De la forma más eficiente y económica."),
        ("lightning", "Rapidez", "Superamos la curva de aprendizaje rápido."),
        ("lightbulb", "Innovación", "Desarrollo interno más la suma de soluciones accesibles de clase mundial."),
        ("path", "Sencillez", "En el camino de uso y aprendizaje más sencillo y simple."),
        ("handshake", "Compromiso", "Superar las expectativas del cliente."),
        ("seal-check", "Calidad", "Que sea percibido un servicio de alta calidad y clase mundial."),
    ], cols=3)
    body += "\n" + section(vals, eyebrow="Valores", title="Lo que " + hl("nos mueve"))

    flags = '<ul class="flags" data-reveal>' + "".join(
        f'<li><img src="{r}assets/img/flags/{f}.svg" alt="" width="56" height="56" loading="lazy" /><span>{n}</span></li>'
        for f, n in [("mexico", "México"), ("colombia", "Colombia"), ("peru", "Perú")]) + "</ul>"
    body += "\n" + section(
        flags, eyebrow="Presencia", title="Calidad reconocida en " + hl("Latinoamérica"), soft=True, center=True,
        lead="Wimprove es tu mejor alternativa para soluciones BPO y Contact Center. Nuestras soluciones operan en Latinoamérica, probadas con la rigurosidad de clientes de telecomunicaciones, banca, retail, etc.")

    why = ('<div class="prose prose--center"><p class="lead" data-reveal>Wimprove es una organización con una visión global, dedicada a generar servicios y soluciones tecnológicas estratégicas, generadoras de valor, mayores ingresos y una excelente experiencia para nuestros aliados.</p>'
           '<blockquote class="quote" data-reveal>“Hacer más rentables a nuestros clientes.”</blockquote>'
           '<p class="lead" data-reveal>En 2014 iniciamos Wimprove con esa firme convicción, que nos ha permitido crecer y ganar confianza en México y el mundo. Contamos con la experiencia de tener operaciones en Perú, Colombia y México.</p></div>')
    body += "\n" + section(why, eyebrow="¿Por qué Wimprove?", title="Una organización con " + hl("visión global"), center=True)
    body += "\n" + cta_band(r, "Hablemos de tu operación", "Cuéntanos qué necesitas y te acompañamos.", "Consulta desde Nosotros")
    return {"path": path, "title": "Nosotros", "section": "nosotros", "body": body,
            "desc": "Wimprove desarrolla software a la medida para BPO y Contact Centers desde 2014, con operaciones en México, Colombia y Perú."}


def page_servicios():
    path = "servicios/"
    r = root_for(path)
    body = page_hero(r, [("Servicios", None)], "Servicios", "Te acompañamos en " + hl("cada etapa"),
                     "Entrenamiento, desarrollo y soporte técnico para tu operación.")
    items = [
        ("entrenamiento", "Entrenamiento", "chalkboard-teacher", "img/about/despues.webp", "Ejecutiva en capacitación",
         "<p class=\"lead\">Tenemos una herramienta llamada Wi Learning, en la que podemos configurar una serie de materiales para el entrenamiento sobre la plataforma y la operación de nuestros agentes, supervisores y ejecutivos.</p>"),
        ("desarrollo", "Servicios de desarrollo", "code", "img/solutions/helpdesk.webp", "Equipo desarrollando una solución",
         "<p class=\"lead\">Podemos personalizar nuestra plataforma de acuerdo con tus necesidades e integrarla con CRMs. Contamos con profesionales con mucha experiencia en el negocio, que facilitan al usuario generar valor a su solicitud.</p>"
         "<p class=\"lead\">Para ello usamos metodologías ágiles, con una entrega y un control de cambios supervisados por el cliente.</p>"),
        ("tecnico", "Soporte técnico", "lifebuoy", "img/solutions/telemarketing.webp", "Ejecutivo de soporte con diadema",
         "<p class=\"lead\">Por el canal que más se adecue a tu operación, te acompañamos en el soporte para tener continuidad en el servicio, con ingenieros empáticos con tu negocio.</p>"
         "<p class=\"lead\">Nuestro equipo cuenta con personal las 24 horas del día, los 7 días de la semana y está dedicado a tu éxito continuo.</p>"),
    ]
    for i, (sid, title, icon, image, alt, text) in enumerate(items):
        copy = f'<span class="feat__icon">{ic(icon)}</span><h2 class="h2" data-split>{title}</h2>{text}'
        body += "\n" + section(split(img(r, image, alt, 750, 580, "split__photo"), copy, reverse=bool(i % 2)), sid=sid, soft=bool(i % 2))
    body += "\n" + cta_band(r, "Contamos con todas las herramientas para hacer crecer tu empresa", "Contacta con nosotros.", "Consulta desde Servicios")
    return {"path": path, "title": "Servicios", "section": "servicios", "body": body,
            "desc": "Servicios de Wimprove: entrenamiento con Wi Learning, servicios de desarrollo a la medida y soporte técnico 24/7."}


def page_contacto():
    path = "contactanos/"
    r = root_for(path)
    from layout import crumbs
    form = contact_form("Consulta desde Contacto").replace("__ROOT__", r)
    info = info_list([
        ("phone", CONTACT["name"], f'<a href="tel:{CONTACT["phone_href"]}">{CONTACT["phone"]}</a>'),
        ("envelope-simple", "Email", f'<a href="mailto:{CONTACT["email"]}">{CONTACT["email"]}</a>'),
        ("map-pin", "Ubicación", f'<a href="https://maps.google.com/?q={CONTACT["map_q"]}" target="_blank" rel="noopener">Av. Ruiz Cortines 390, Mitras Centro,<br />64460 Monterrey, N.L., México</a>'),
    ])
    body = f"""    <section class="section contact contact--page on-dark" id="contacto">
      <span class="deco deco--c" aria-hidden="true"></span>
      <div class="container contact__grid">
        <div class="contact__info">
          {crumbs(r, [("Contáctanos", None)])}
          <span class="eyebrow">Contáctanos</span>
          <h1 class="display">¿Tienes dudas? <span class="hl">Déjanos un mensaje</span></h1>
          {info}
          <div class="map" data-reveal>
            <iframe title="Ubicación de Wimprove en Monterrey" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
              src="https://maps.google.com/maps?q={CONTACT["map_q"]}&z=15&output=embed"></iframe>
          </div>
        </div>
        <div data-reveal>{form}</div>
      </div>
    </section>"""
    return {"path": path, "title": "Contáctanos", "section": "contactanos", "body": body,
            "desc": "Contacta a Wimprove en Monterrey, N.L., México. Escríbenos y te responderemos pronto."}


def page_privacidad():
    path = PRIVACY_URL
    r = root_for(path)
    text = (CONTENT / "privacy.html").read_text(encoding="utf-8")
    body = page_hero(r, [("Política de privacidad", None)], "Legal", "Política de Privacidad y Protección de Datos Personales")
    body += "\n" + section(f'<div class="prose prose--legal">{text}</div>')
    return {"path": path, "title": "Política de Privacidad y Protección de Datos Personales", "section": "", "body": body,
            "desc": "Política de Privacidad y Protección de Datos Personales de WIMPROVE SAC."}


def page_404():
    # Se sirve desde cualquier profundidad de URL, así que usa rutas absolutas desde la raíz.
    r = "/"
    body = page_hero(r, [("Página no encontrada", None)], "Error 404", "Esta página " + hl("no existe"),
                     "Puede que el enlace haya cambiado. Vuelve al inicio o explora nuestros productos.",
                     f'<a class="btn" href="{r}">Ir al inicio</a><a class="btn btn--ghost" href="{r}productos/">Ver productos</a>')
    return {"path": "404.html", "title": "Página no encontrada", "section": "", "body": body,
            "desc": "Página no encontrada.", "noindex": True, "root": r}


ALL_PAGES = [
    page_productos, page_soluciones,
    page_iaudit, page_wixperiences, page_wicontact, page_wimail, page_wiinteligence, page_widesk, page_chatbots, page_voicebots,
    page_atencion, page_cobranza, page_telemarketing, page_helpdesk, page_telemedicina,
    page_nosotros, page_servicios, page_contacto, page_privacidad, page_404,
]
