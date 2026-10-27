"""Datos compartidos del sitio: productos, soluciones y contacto."""

SITE = "https://www.wimprove.com"

CONTACT = {
    "name": "Juan Gonzalez",
    "phone": "(+52) 812321838",
    "phone_href": "+52812321838",
    "email": "juan.gonzalez@mdybpo.com",
    "address": "Av. Ruiz Cortines 390, Mitras Centro, 64460 Monterrey, N.L., México",
    "map_q": "Av.%20Ruiz%20Cortines%20390,%20Mitras%20Centro,%2064460%20Monterrey,%20N.L.,%20M%C3%A9xico",
    "facebook": "https://www.facebook.com/wimprove.oficial",
    "linkedin": "https://www.linkedin.com/company/wimprove-contact-center/",
}

PRIVACY_URL = "politica-de-privacidad-y-proteccion-de-datos-personales/"

PRODUCTS = [
    {"slug": "wi-iaudit", "name": "Wi IAudit", "icon": "sparkle", "tag": "Inteligencia artificial",
     "short": "Procesamos tus llamadas, chats y emails con inteligencia artificial.",
     "menu": "Llamadas, chats y emails con IA", "img": "img/products/iaudit.webp"},
    {"slug": "wicontact", "name": "Wi Contact", "icon": "chart-line-up", "tag": "Omnicanal",
     "short": "Suite para Contact Centers de calidad omnicanal.",
     "menu": "Suite omnicanal para Contact Centers", "img": "img/products/wicontact.webp"},
    {"slug": "wixperiences", "name": "WIXperiences", "icon": "video-camera", "tag": "Videollamadas",
     "short": "Sistema de videollamadas para gestión con tus clientes.",
     "menu": "Videollamadas con tus clientes", "img": "img/products/wixperiences.webp"},
    {"slug": "wi-mail", "name": "Wi Mail", "icon": "envelope-simple", "tag": "Correo",
     "short": "Sistema de medición de atención de cuentas de correo corporativas.",
     "menu": "Medición de cuentas de correo", "img": "img/products/wimail.webp"},
    {"slug": "wi-inteligence", "name": "Wi Inteligence", "icon": "database", "tag": "Datos",
     "short": "Integración de información a través de un almacén de datos.",
     "menu": "Almacén de datos integrado", "img": "img/products/wiinteligence.webp"},
    {"slug": "wi-desk", "name": "Wi Desk", "icon": "headset", "tag": "CRM",
     "short": "Administración de interacciones omnicanal.",
     "menu": "Interacciones omnicanal", "img": "img/products/widesk.webp"},
    {"slug": "chatbots", "name": "Chatbots", "icon": "chats-circle", "tag": "Mensajería",
     "short": "Respuesta con mensajes estructurados.",
     "menu": "Mensajes estructurados", "img": "img/products/chatbots.webp"},
    {"slug": "voicebots", "name": "Voicebots", "icon": "microphone", "tag": "Voz",
     "short": "Programa informático para mantener una conversación.",
     "menu": "Conversación automatizada", "img": "img/products/voicebots.webp"},
]

SOLUTIONS = [
    {"slug": "atencion-al-cliente", "name": "Atención al cliente", "icon": "smiley",
     "short": "Entregamos al cliente una experiencia única de atención con el objetivo primordial de resolver las necesidades del cliente.",
     "menu": "Experiencia única de atención", "img": "img/solutions/atencion-al-cliente.webp"},
    {"slug": "cobranza", "name": "Cobranza", "icon": "coins",
     "short": "Recuperación de clientes en cartera vencida, rescatar ese ingreso y mantener a tus clientes satisfechos.",
     "menu": "Recuperación de cartera vencida", "img": "img/solutions/cobranza.webp"},
    {"slug": "telemarketing", "name": "Telemarketing", "icon": "phone-call",
     "short": "Atendemos de manera directa con medios de comunicación efectivos, contactando a tus clientes potenciales.",
     "menu": "Contacto directo con prospectos", "img": "img/solutions/telemarketing.webp"},
    {"slug": "helpdesk", "name": "Helpdesk", "icon": "lifebuoy",
     # Texto provisional: la web actual tiene "Lorem ipsum" y una frase cortada. Pendiente de aprobación.
     "short": "Recursos tecnológicos y humanos para prestar servicios con la posibilidad de gestionar y solucionar las necesidades de tus clientes.",
     "menu": "Gestión y solución de casos", "img": "img/solutions/helpdesk.webp"},
    {"slug": "telemedicina", "name": "Telemedicina", "icon": "heartbeat",
     "short": "Se ha implementado hace 6 años en MiConsultorioya: el 80% de las visitas al doctor son enfermedades de primer contacto.",
     "menu": "Consulta médica a distancia", "img": "img/solutions/telemedicina.webp"},
]


def product(slug):
    return next(p for p in PRODUCTS if p["slug"] == slug)


def solution(slug):
    return next(s for s in SOLUTIONS if s["slug"] == slug)
