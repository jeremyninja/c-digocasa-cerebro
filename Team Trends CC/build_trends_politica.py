#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Trends Politica — Forecast Deck (18 slides)
Capitulo: OPINIONES POLITICAS
Layout: 3 dividers macro + 15 micros (5 por macro)
Canvas 13.333 x 7.5 in (1440x810 px @ 108dpi base)
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

BASE = "/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC"
SHOTS = os.path.join(BASE, "screenshots/trends-politica")
OUT = os.path.join(BASE, "outputs/trends-politica-forecast.pptx")

# Colors
BG = RGBColor(0x0D, 0x0D, 0x0D)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY_LABEL = RGBColor(0xA0, 0xA0, 0xA0)
GREY_MUTED = RGBColor(0x66, 0x66, 0x66)
ACCENT = RGBColor(0xFF, 0x2D, 0x2D)
TAB_BG = RGBColor(0xE8, 0xE8, 0xE8)
BLACK = RGBColor(0x00, 0x00, 0x00)
PLACEHOLDER_BG = RGBColor(0x22, 0x22, 0x22)

FONT_SERIF = "Instrument Serif"
FONT_SANS = "Poppins"

# ============================================================
# MACRO + MICRO DATA
# ============================================================

MACROS = [
    {
        "num": 1,
        "name": "INVENTOLOGÍA DE LA ADULTEZ",
        "short": "INVENTOLOGÍA",
        "tagline": "Un mundo en crisis está reescribiendo qué significa ser adulto y formar familia.",
    },
    {
        "num": 2,
        "name": "LOS HERNÁNDEZ ARE PROMPTED",
        "short": "HERNÁNDEZ PROMPTED",
        "tagline": "El dominicano ya entró al mundo prompteado. Solo no lo nombra así.",
    },
    {
        "num": 3,
        "name": "ALGORITMO DEL HOGAR",
        "short": "ALGORITMO DEL HOGAR",
        "tagline": "El feed se sentó en la mesa y nadie le ofreció silla.",
    },
]

MICROS = [
    # ----- MACRO 1 -----
    {
        "macro": 1,
        "headline": "VOTA PORQUE TOCA, NO PORQUE CREA: EL SUFRAGIO SOBREVIVE COMO RITUAL MIENTRAS LA FE EN QUE CAMBIE ALGO SE EROSIONA EN TODA LATAM.",
        "body": "Antes votar y creer venían juntos. Hoy se separan. En LATAM convive una tasa de voto declarado alta con desconfianza profunda en que el sistema sea justo: solo 45% de los jóvenes está satisfecho con la democracia y casi 40% desconfía de su gobierno (Latinobarómetro 2024). El acto se mantiene como hábito cívico — la esperanza no. Aparece un lenguaje de \"el menos malo\" que convierte el voto en cálculo de daño, no en proyecto.",
        "hashtags": "#elmenosmalo · #votoútil · #desencanto",
        "needs": "VACÍO · MIEDO · RESENTIMIENTO",
        "triggers": [
            {
                "big": "45%",
                "desc": "Jóvenes LATAM satisfechos con la democracia; casi 40% desconfía del gobierno.",
                "src": "LATINOBARÓMETRO · 2024",
            },
            {
                "big": "\"el menos malo\"",
                "desc": "Lenguaje del voto estratégico — cálculo de daño, no proyecto de futuro.",
                "src": "TIKTOK · 2026",
            },
            {
                "big": "77%",
                "desc": "De dominicanos votó en la última elección mientras 46.6% ve el sistema como nada justo.",
                "src": "CÓDIGO CASA · 2024",
            },
        ],
        "signals": [
            {
                "img": "macro-1-1-tiktok-votoutil-hashtag.png",
                "cap": "Página hashtag #votoútil en TikTok — grid de videos sobre voto estratégico sin entusiasmo.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/votoútil",
            },
            {
                "img": "macro-1-1-unav-desencanto-latam.png",
                "cap": "Artículo U. Navarra: LATAM del desencanto político a la redefinición de la democracia.",
                "src": "GLOBAL AFFAIRS U. NAVARRA · 2024",
                "url": "https://en.unav.edu/web/global-affairs/latinoam%C3%A9rica-del-desencanto-de-la-pol%C3%ADtica-a-la-redefinici%C3%B3n-de-la-democracia",
            },
            {
                "img": "macro-1-0-baker-latinobarometro-2024.png",
                "cap": "Baker Institute: análisis Latinobarómetro 2024 — satisfacción con democracia en mínimos.",
                "src": "BAKER INSTITUTE · 2024",
                "url": "https://www.bakerinstitute.org/research/latinobarometro-most-dissatisfied-govt",
            },
        ],
    },
    {
        "macro": 1,
        "headline": "LA SALIDA EN VEZ DE LA VOZ: ANTE UN SISTEMA QUE SE SIENTE INJUSTO, LA RESPUESTA DE MUCHOS JÓVENES NO ES PROTESTA, ES PASAPORTE.",
        "body": "La teoría cívica clásica decía: si algo te molesta, alza la voz. Una generación está cambiando la voz por la salida. Emigrar funciona como voto con los pies — una respuesta personal a un problema que se percibe colectivo. Los vlogs de \"me voy del país\" ordenan el futuro como proyecto migratorio antes que como proyecto cívico. La energía que antes iba a la plaza ahora va al trámite de la visa.",
        "hashtags": "#salirdelpaís · #diáspora · #dominicanosporelmundo",
        "needs": "SOLEDAD · MIEDO · INVISIBILIDAD",
        "triggers": [
            {
                "big": "66.1%",
                "desc": "Jóvenes dominicanos 18-21 que ha considerado vivir fuera del país.",
                "src": "DIARIO LIBRE · 2024",
            },
            {
                "big": "2.87M",
                "desc": "Dominicanos en la diáspora al cierre de 2024 — 37.2% menor de 25 años.",
                "src": "PRENSA LATINA · 2025",
            },
            {
                "big": "#salirdelpaís",
                "desc": "Migration vlogs como narrativa de futuro joven — la salida como género propio en TikTok.",
                "src": "TIKTOK · 2026",
            },
        ],
        "signals": [
            {
                "img": "macro-1-2-tiktok-salirdelpais-hashtag.png",
                "cap": "Página hashtag #salirdelpaís en TikTok — vlogs de emigración como futura narrativa.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/salirdelpais",
            },
            {
                "img": "macro-1-2-diariolibre-migracion-dominicana.png",
                "cap": "Diario Libre: 66.1% de jóvenes 18-21 ha considerado emigrar — dato local duro.",
                "src": "DIARIO LIBRE · 2024",
                "url": "https://www.diariolibre.com/opinion/mas-firmas/2024/09/16/migracion-los-dominicanos-tambien-emigran/2851533",
            },
            {
                "img": "macro-1-2-prensalatina-emigracion-rd.png",
                "cap": "Prensa Latina: 2.87M dominicanos en la diáspora, +27,408 vs 2023.",
                "src": "PRENSA LATINA · 2025",
                "url": "https://www.prensa-latina.cu/2025/07/17/mas-de-27-mil-dominicanos-emigraron-en-2024-revela-investigacion/",
            },
        ],
    },
    {
        "macro": 1,
        "headline": "EL SUEÑO DEJÓ DE SER UN LÍDER Y PASÓ A SER UNA REGLA QUE SE CUMPLA: LA LEALTAD DE BANDERA CEDE ANTE EL DESEO DE INSTITUCIONES QUE FUNCIONEN.",
        "body": "El ideal cívico migra de la persona a la regla. Antes la aspiración tenía cara y bandera. Ahora la aspiración es más seca: que las leyes y los servicios operen igual para todos, sin importar quién esté arriba. En LATAM la confianza en instituciones formales cae mientras sube la confianza en pares y líderes comunitarios (Security Journal Americas 2026). El lenguaje cambia de \"es de los míos\" a \"que cumpla lo que prometió\". Se premia y castiga gestión por resultado, no por color.",
        "hashtags": "#queseaolacumplan · #instituciones · #resultados",
        "needs": "RESENTIMIENTO · VACÍO · INVISIBILIDAD",
        "triggers": [
            {
                "big": "46.6%",
                "desc": "Dominicanos que considera el sistema nada justo — aspiran a regla, no a caudillo.",
                "src": "CÓDIGO CASA · 2024",
            },
            {
                "big": "↓ confianza",
                "desc": "En instituciones formales LATAM/Caribe; sube en pares, comunitarios e influencers.",
                "src": "SECURITY JOURNAL AMERICAS · 2026",
            },
            {
                "big": "\"gestión\"",
                "desc": "Contenido \"vota por la política, no por el partido\" crece entre jóvenes en TikTok.",
                "src": "TIKTOK · 2026",
            },
        ],
        "signals": [
            {
                "img": "macro-1-3-securityjournal-trust-gap.png",
                "cap": "Security Journal Americas 2026: brecha de confianza institucional LATAM/Caribe.",
                "src": "SECURITY JOURNAL AMERICAS · 2026",
                "url": "https://securityjournalamericas.com/caribbean-latin-american-security-2026/",
            },
            {
                "img": "macro-1-1-unav-desencanto-latam.png",
                "cap": "U. Navarra: de la identidad partidista al resultado — ciudadano exige gestión.",
                "src": "GLOBAL AFFAIRS U. NAVARRA · 2024",
                "url": "https://en.unav.edu/web/global-affairs/latinoam%C3%A9rica-del-desencanto-de-la-pol%C3%ADtica-a-la-redefinici%C3%B3n-de-la-democracia",
            },
            {
                "img": "macro-1-3-securityjournal-trust-gap.png",
                "cap": "Brecha de confianza institucional en el Caribe — contexto del report 2026.",
                "src": "SECURITY JOURNAL AMERICAS · 2026",
                "url": "https://securityjournalamericas.com/caribbean-latin-american-security-2026/",
            },
        ],
    },
    {
        "macro": 1,
        "headline": "CIUDADANÍA DE CAUSA, NO DE CARNET: EL 70% DE LA GEN Z GLOBAL APOYA ALGO, PERO LO HACE POR TEMA PUNTUAL Y ONLINE, NO POR MILITANCIA NI MEMBRESÍA.",
        "body": "La adultez cívica nueva no se afilia: se activa. Antes pertenecer era firmar una membresía estable. Ahora el compromiso es por tema — clima, género, justicia — y por temporada. El 70% de la Gen Z global dice estar involucrado en alguna causa social o política, pero la mayoría lo hace online y de forma intermitente (ShoutOut UK 2025). El mismo estudio detecta activismo, fatiga y división conviviendo en la misma persona. Se apoya sin atarse.",
        "hashtags": "#causa · #cambiosocial · #sinpartido",
        "needs": "SOLEDAD · VACÍO · MIEDO",
        "triggers": [
            {
                "big": "70%",
                "desc": "Gen Z global involucrado en una causa social/política; un tercio son activistas regulares.",
                "src": "SHOUTOUT UK · 2025",
            },
            {
                "big": "58%",
                "desc": "Dominicanos nada interesados en política — pero \"política\" significa aparato, no causa.",
                "src": "CÓDIGO CASA · 2024",
            },
            {
                "big": "activismo\n+ fatiga",
                "desc": "Activismo, fatiga y división simultáneos en torno a la participación Gen Z.",
                "src": "MONTCLAIR STATE · 2024",
            },
        ],
        "signals": [
            {
                "img": "macro-1-4-shoutoutuk-genz-activism.png",
                "cap": "ShoutOut UK: 70% de Gen Z apoya causas, mayormente online — auge del activismo selectivo.",
                "src": "SHOUTOUT UK · 2025",
                "url": "https://www.shoutoutuk.org/2025/09/19/gen-z-and-the-rise-of-performative-activism/",
            },
            {
                "img": "macro-1-5-montclair-genz-fatigue.png",
                "cap": "Montclair 2024: activismo + fatiga + división conviviendo en la misma persona Gen Z.",
                "src": "MONTCLAIR STATE UNIVERSITY · 2024",
                "url": "https://www.montclair.edu/college-of-communication-and-media/2024/12/05/negativity-activism-division-and-fatigue-gen-z-social-media-and-the-2024-election/",
            },
            {
                "img": "macro-1-4-shoutoutuk-genz-activism.png",
                "cap": "El carnet murió. La causa, no — activismo sin afiliación como nueva forma de pertenecer.",
                "src": "SHOUTOUT UK · 2025",
                "url": "https://www.shoutoutuk.org/2025/09/19/gen-z-and-the-rise-of-performative-activism/",
            },
        ],
    },
    {
        "macro": 1,
        "headline": "DECIR \"NO ME INTERESA LA POLÍTICA\" DEJÓ DE SER IGNORANCIA: PARA EL JOVEN LATAM ES BLINDAJE EMOCIONAL, AUTOCUIDADO CONTRA UN SISTEMA QUE SOLO LE DA FRUSTRACIÓN.",
        "body": "Lo que parecía apatía es, cada vez más, una postura activa. Antes desconectarse de la política se leía como falta de información. Hoy buena parte del joven LATAM ve el sistema como distante, burocrático e inefectivo para resolver lo cotidiano (Latinobarómetro 2024) — y se aparta a propósito. La \"fatiga\" aparece como uno de los cuatro ejes de la relación Gen Z con la política (Montclair 2024). Mutear noticias se vuelve contenido de bienestar. El detox no es vacío: es defensa.",
        "hashtags": "#newsdetox · #apolítico · #desconectar",
        "needs": "SOLEDAD · MIEDO · VACÍO",
        "triggers": [
            {
                "big": "58%",
                "desc": "Dominicanos que se declara nada interesado en política — leído como protección, no descuido.",
                "src": "CÓDIGO CASA · 2024",
            },
            {
                "big": "fatiga",
                "desc": "Uno de los cuatro ejes de la relación Gen Z con la política — Montclair 2024.",
                "src": "MONTCLAIR STATE UNIVERSITY · 2024",
            },
            {
                "big": "#newsdetox",
                "desc": "Mutear noticias como contenido de bienestar y protección emocional en TikTok.",
                "src": "TIKTOK · 2026",
            },
        ],
        "signals": [
            {
                "img": "macro-1-5-tiktok-newsdetox-hashtag.png",
                "cap": "Hashtag #newsdetox en TikTok — detox de noticias como bienestar y autocuidado.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/newsdetox",
            },
            {
                "img": "macro-1-5-montclair-genz-fatigue.png",
                "cap": "Montclair 2024: negatividad, activismo, división y fatiga — los 4 ejes Gen Z y política.",
                "src": "MONTCLAIR STATE UNIVERSITY · 2024",
                "url": "https://www.montclair.edu/college-of-communication-and-media/2024/12/05/negativity-activism-division-and-fatigue-gen-z-social-media-and-the-2024-election/",
            },
            {
                "img": "macro-1-1-unav-desencanto-latam.png",
                "cap": "La política vista como distante e inefectiva para lo cotidiano — el LATAM se aparta.",
                "src": "LATINOBARÓMETRO · 2024",
                "url": "https://en.unav.edu/web/global-affairs/latinoam%C3%A9rica-del-desencanto-de-la-pol%C3%ADtica-a-la-redefinici%C3%B3n-de-la-democracia",
            },
        ],
    },
    # ----- MACRO 2 -----
    {
        "macro": 2,
        "headline": "EL DEEPFAKE QUE HABLA COMO TU PRESIDENTE: LA IA YA FALSIFICA VOZ Y CARA DE FIGURAS PÚBLICAS, Y EN RD 2024 UN AUDIO PRESIDENCIAL FALSO CIRCULÓ POR BOTS.",
        "body": "La voz y la cara de figuras públicas se volvieron material falsificable. Antes oír era creer. Ya no. En la campaña RD 2024 circuló un audio deepfake presidencial sobre un tema sensible, difundido por cientos de bots IA vía una interfaz falsa de WhatsApp (N Digital 2024). La consecuencia es un reflejo nuevo: el votante duda de lo que oye antes de reenviarlo. \"¿Esto es real o es IA?\" se vuelve pregunta de rutina.",
        "hashtags": "#deepfake · #esIA · #verifica",
        "needs": "MIEDO · RESENTIMIENTO · VACÍO",
        "triggers": [
            {
                "big": "+350-550%",
                "desc": "Proyección de campañas de desinformación con IA en Sudamérica y el Caribe para 2026.",
                "src": "GLOBENEWSWIRE · 2025",
            },
            {
                "big": "bots IA",
                "desc": "Cientos de bots IA difundieron el audio deepfake presidencial en RD 2024 vía WhatsApp falso.",
                "src": "N DIGITAL · 2024",
            },
            {
                "big": "#deepfake",
                "desc": "Auge de videos \"esto es un deepfake\" desmontando contenido político falso en TikTok.",
                "src": "TIKTOK · 2026",
            },
        ],
        "signals": [
            {
                "img": "macro-2-1-tiktok-deepfake-hashtag.png",
                "cap": "Hashtag #deepfake en TikTok — desmontaje ciudadano de contenido político falso.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/deepfake",
            },
            {
                "img": "macro-2-1-ndigital-deepfake-rd.png",
                "cap": "N Digital: hero image del artículo sobre deepfake presidencial RD 2024 — el caso local.",
                "src": "N DIGITAL · 2024",
                "url": "https://n.com.do/2024/05/14/el-deep-fake-irrumpe-en-las-elecciones-de-rd/",
            },
            {
                "img": "macro-2-1-globenewswire-disinfo-550pct.png",
                "cap": "GlobeNewswire: proyección +350-550% de desinformación IA en Sudamérica/Caribe a 2026.",
                "src": "GLOBENEWSWIRE · 2025",
                "url": "https://www.globenewswire.com/news-release/2025/10/10/3164963/0/en/AI-Disinformation-amp-Security-Threats-South-America-amp-Caribbean-2026-Assessment-Reveals-a-350-550-Projected-Increase-in-AI-Disinformation-Campaigns.html",
            },
        ],
    },
    {
        "macro": 2,
        "headline": "LE PREGUNTÓ AL CHATBOT SI ERA VERDAD Y LE MINTIÓ: EL CIUDADANO USA GROK O CHATGPT PARA VERIFICAR NOTICIAS, PERO LOS ESTUDIOS MUESTRAN QUE REPITEN EL BULO.",
        "body": "El árbitro de la verdad cambió de cara. Antes se verificaba en el buscador o el medio. Ahora se le pregunta al chatbot. El problema: AFP documentó que Grok, ChatGPT y Gemini repiten desinformación cuando se usan como fact-checkers, sobre todo en breaking news (TechXplore 2025). El comportamiento observable es citar la respuesta del bot como prueba ante otros — \"lo dijo Grok\". La herramienta de verificación se convierte en fuente de error con cara de autoridad.",
        "hashtags": "#preguntéalachat · #grok · #verifica",
        "needs": "MIEDO · SOLEDAD · VACÍO",
        "triggers": [
            {
                "big": "Grok",
                "desc": "Usuarios citan a Grok como evidencia de clips reales cuando eran generados por IA.",
                "src": "AFP / TECHXPLORE · 2025",
            },
            {
                "big": "WhatsApp",
                "desc": "Mercado clave de chatbots IA en LATAM — terreno de verificación y desinformación.",
                "src": "AURORA INBOX · 2025",
            },
            {
                "big": "\"lo dijo Grok\"",
                "desc": "Formato viral: \"le pregunté a ChatGPT si esto era verdad\" como verificación amateur.",
                "src": "TIKTOK · 2026",
            },
        ],
        "signals": [
            {
                "img": "macro-2-2-tiktok-fakenews-hashtag.png",
                "cap": "Hashtag #fakenews en TikTok — videos de verificación y denuncia de contenido falso.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/fakenews",
            },
            {
                "img": "macro-2-2-techxplore-chatbot-factcheck.png",
                "cap": "TechXplore/AFP: Grok, ChatGPT y Gemini repiten desinformación como fact-checkers.",
                "src": "TECHXPLORE / AFP · 2025",
                "url": "https://techxplore.com/news/2025-06-hey-chatbot-true-ai-factchecks.html",
            },
            {
                "img": "macro-2-3-aurora-whatsapp-chatbot-latam.png",
                "cap": "Aurora Inbox: chatbots IA en WhatsApp LATAM — el árbitro de la verdad en la app familiar.",
                "src": "AURORA INBOX · 2025",
                "url": "https://www.aurorainbox.com/en/2025/05/15/future-chatbots-whatsapp-trends-ai-automation/",
            },
        ],
    },
    {
        "macro": 2,
        "headline": "LA VERIFICACIÓN ENTRA AL WHATSAPP DE LA FAMILIA: FRENTE A LA CADENA DEL TÍO SURGE LA CIVIC TECH QUE CHEQUEA EL BULO EN LA MISMA APP DONDE CIRCULA.",
        "body": "Contra la cadena de WhatsApp aparece una respuesta del mismo formato. Antes el bulo familiar no tenía contrapeso conversacional — circulaba y se quedaba. Ahora la civic tech entra al chat: chatbots y servicios de fact-checking (AFP, Maldita) que verifican por la misma app donde llega el audio sospechoso. AFP opera fact-checking en 26 idiomas dentro del programa de Meta, LATAM incluida (TechXplore 2025). El gesto nuevo: reenviar el audio al bot antes de creerlo.",
        "hashtags": "#factchecking · #verificado · #cadenadewhatsapp",
        "needs": "MIEDO · INVISIBILIDAD · SOLEDAD",
        "triggers": [
            {
                "big": "26 idiomas",
                "desc": "AFP opera fact-checking en 26 idiomas dentro del programa de Meta, LATAM incluida.",
                "src": "AFP / TECHXPLORE · 2025",
            },
            {
                "big": "UNESCO RD",
                "desc": "UNESCO impulsa alfabetización mediática en RD — taller Santo Domingo, oct 2024.",
                "src": "UNESCO · 2024",
            },
            {
                "big": "#factchecking",
                "desc": "Cómo verificar una cadena de WhatsApp — civic tech como contenido en TikTok.",
                "src": "TIKTOK · 2026",
            },
        ],
        "signals": [
            {
                "img": "macro-2-3-tiktok-factchecking-hashtag.png",
                "cap": "Hashtag #factchecking en TikTok — tutoriales de verificación y civic tech doméstica.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/factchecking",
            },
            {
                "img": "macro-2-3-unesco-alfabetizacion-rd.png",
                "cap": "UNESCO: taller de alfabetización mediática en Santo Domingo para combatir desinformación.",
                "src": "UNESCO · 2024",
                "url": "https://www.unesco.org/en/articles/unesco-promotes-media-and-information-literacy-means-counteract-disinformation-dominican-republic",
            },
            {
                "img": "macro-2-3-aurora-whatsapp-chatbot-latam.png",
                "cap": "Chatbots de verificación en WhatsApp LATAM — la civic tech en la misma app del bulo.",
                "src": "AURORA INBOX · 2025",
                "url": "https://www.aurorainbox.com/en/2025/05/15/future-chatbots-whatsapp-trends-ai-automation/",
            },
        ],
    },
    {
        "macro": 2,
        "headline": "BOTS, NO MILITANTES: LA \"BASE\" QUE VES APOYANDO ONLINE PUEDE SER SINTÉTICA; CIENTOS DE CUENTAS IA AMPLIFICAN A UNA ESCALA QUE NINGÚN HUMANO ALCANZA.",
        "body": "La movilización política se automatiza. Antes la base de apoyo eran personas que tú podías contar. Ahora cientos de bots IA amplifican narrativas y contenido falso a una escala que ningún militante humano alcanza — el deepfake presidencial RD 2024 se difundió justo así (N Digital 2024). La consecuencia es un reflejo de sospecha: cuando algo se vuelve tendencia muy rápido, la pregunta es si los comentarios coordinados son gente o cuentas. La \"base\" del feed puede no existir.",
        "hashtags": "#bots · #cuentasfalsas · #manipulación",
        "needs": "MIEDO · RESENTIMIENTO · INVISIBILIDAD",
        "triggers": [
            {
                "big": "cientos",
                "desc": "De bots IA detrás de la difusión del audio deepfake presidencial RD 2024.",
                "src": "N DIGITAL · 2024",
            },
            {
                "big": "+350-550%",
                "desc": "Operaciones de desinformación IA apuntan a procesos electorales en la región.",
                "src": "GLOBENEWSWIRE · 2025",
            },
            {
                "big": "\"¿es bot?\"",
                "desc": "\"Cómo detectar un bot o cuenta falsa\" — contenido de educación digital en TikTok.",
                "src": "TIKTOK · 2026",
            },
        ],
        "signals": [
            {
                "img": "macro-2-1-tiktok-deepfake-hashtag.png",
                "cap": "Hashtag #deepfake en TikTok — \"cómo detectar una cuenta falsa\" como educación digital.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/deepfake",
            },
            {
                "img": "macro-2-1-ndigital-deepfake-article.png",
                "cap": "N Digital: cientos de bots IA en la difusión del deepfake presidencial RD 2024.",
                "src": "N DIGITAL · 2024",
                "url": "https://n.com.do/2024/05/14/el-deep-fake-irrumpe-en-las-elecciones-de-rd/",
            },
            {
                "img": "macro-2-4-globenewswire-ai-disinfo.png",
                "cap": "GlobeNewswire: operaciones de desinformación IA dirigidas a procesos electorales.",
                "src": "GLOBENEWSWIRE · 2025",
                "url": "https://www.globenewswire.com/news-release/2025/10/10/3164963/0/en/AI-Disinformation-amp-Security-Threats-South-America-amp-Caribbean-2026-Assessment-Reveals-a-350-550-Projected-Increase-in-AI-Disinformation-Campaigns.html",
            },
        ],
    },
    {
        "macro": 2,
        "headline": "EL ALGORITMO COMO ASESOR DE CAMPAÑA: KAMALA HQ HIZO 1.5B DE VISTAS EN TIKTOK. LA POLÍTICA YA OPERA COMO CUENTA DE CREADOR — REMIX, CLIP Y ENGAGEMENT.",
        "body": "La campaña dejó de hablar como institución y empezó a hablar como creador. Antes el mensaje político venía en discurso y debate. Ahora viene en clip de 15 segundos, remix y meme. En 2024 la cuenta KamalaHQ acumuló 1.5B de vistas con 5M de seguidores; la de Trump, 1B de vistas con 12M (eMarketer 2024). El 48% de los usuarios de TikTok 18-29 usa la plataforma para seguir política (Pew 2024). Y el feed tiene sesgo: el contenido tóxico atrae más engagement (HKS 2024).",
        "hashtags": "#campañatiktok · #clips · #remix",
        "needs": "VACÍO · RESENTIMIENTO · SOLEDAD",
        "triggers": [
            {
                "big": "1.5B",
                "desc": "Vistas de KamalaHQ en TikTok 2024 (5M seguidores) — la campaña como cuenta de creador.",
                "src": "EMARKETER · 2024",
            },
            {
                "big": "48%",
                "desc": "Usuarios TikTok 18-29 que usa la plataforma para seguir política.",
                "src": "PEW RESEARCH · 2024",
            },
            {
                "big": "51,680",
                "desc": "Videos políticos analizados — el contenido tóxico atrae más engagement en todos.",
                "src": "HKS MISINFORMATION REVIEW · 2024",
            },
        ],
        "signals": [
            {
                "img": "macro-2-5-emarketer-tiktok-election.png",
                "cap": "eMarketer: KamalaHQ 1.5B vistas — TikTok como campo de batalla político en 2024.",
                "src": "EMARKETER · 2024",
                "url": "https://www.emarketer.com/content/tiktok-becomes-key-battleground-gen-z-voters-2024-election",
            },
            {
                "img": "macro-2-5-pew-tiktok-news.png",
                "cap": "Pew Research: 48% de usuarios TikTok 18-29 usa la plataforma para seguir política.",
                "src": "PEW RESEARCH · 2025",
                "url": "https://www.pewresearch.org/short-reads/2025/01/17/a-closer-look-at-americans-experiences-with-news-on-tiktok/",
            },
            {
                "img": "macro-2-5-hks-toxic-tiktok-article.png",
                "cap": "HKS Misinformation Review: análisis de 51,680 videos políticos 2024 — lo tóxico engancha.",
                "src": "HKS MISINFORMATION REVIEW · 2024",
                "url": "https://misinforeview.hks.harvard.edu/article/toxic-politics-and-tiktok-engagement-in-the-2024-u-s-election/",
            },
        ],
    },
    # ----- MACRO 3 -----
    {
        "macro": 3,
        "headline": "EL NOTICIERO ERES TÚ, NO EL CANAL: 38% DE LOS MENORES DE 30 RECIBE NOTICIAS DE CREADORES, Y 77% DE ELLOS NUNCA TRABAJÓ EN PERIODISMO.",
        "body": "El medio dejó de ser una institución y pasó a ser una persona. Antes la noticia venía de un canal con nombre y redacción. Ahora viene de un creador con cara y voz. El 38% de los menores de 30 obtiene noticias de news influencers y el 77% de esos creadores nunca trabajó en periodismo — 84% de ellos opera en TikTok (Pew 2024). La credibilidad se vuelve parasocial: confío en él, no en su fuente. El comportamiento observable es seguir a un creador como \"mi\" fuente y citarlo como autoridad.",
        "hashtags": "#newsinfluencer · #creadordenoticias · #fuente",
        "needs": "SOLEDAD · VACÍO · INVISIBILIDAD",
        "triggers": [
            {
                "big": "38%",
                "desc": "Menores de 30 que recibe noticias de news influencers — 77% sin experiencia periodística.",
                "src": "PEW RESEARCH · 2024",
            },
            {
                "big": "84%",
                "desc": "De los news influencers opera en TikTok — sin editorial ni editor detrás.",
                "src": "PEW RESEARCH · 2024",
            },
            {
                "big": "40%",
                "desc": "De jóvenes EE.UU. recibe noticias de influencers — la cercanía gana a la credencial.",
                "src": "CNN BUSINESS · 2024",
            },
        ],
        "signals": [
            {
                "img": "macro-3-0-tiktok-newsinfluencer-hashtag.png",
                "cap": "Hashtag #newsinfluencer en TikTok — grid de creadores de noticias como medio principal.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/newsinfluencer",
            },
            {
                "img": "macro-3-1-pew-news-influencers.png",
                "cap": "Pew Research: 77% de news influencers sin experiencia periodística, 84% en TikTok.",
                "src": "PEW RESEARCH · 2025",
                "url": "https://www.pewresearch.org/journalism/2025/12/03/young-adults-and-the-future-of-news/",
            },
            {
                "img": "macro-3-1-cnn-news-influencers.png",
                "cap": "CNN Business: casi 40% de jóvenes EE.UU. recibe noticias de influencers.",
                "src": "CNN BUSINESS · 2024",
                "url": "https://www.cnn.com/2024/11/18/media/news-influencers-social-media-conservative-study",
            },
        ],
    },
    {
        "macro": 3,
        "headline": "EL FEED PREMIA LA RABIA: EN 51,680 VIDEOS POLÍTICOS, EL CONTENIDO TÓXICO GANÓ MÁS ENGAGEMENT. LA INDIGNACIÓN VIRALIZA MEJOR QUE EL MATIZ.",
        "body": "El algoritmo no es un espejo neutral. Un análisis de 51,680 videos políticos de 2024 encontró que el contenido tóxico y partidista atrae consistentemente más engagement; inmigración y fraude electoral están entre los temas más tóxicos (HKS 2024). Hay evidencia causal: rerankear la animosidad partidista en el feed altera la polarización afectiva de la gente (PNAS 2025). La consecuencia observable es que se interactúa más con lo que indigna que con lo que informa.",
        "hashtags": "#outragebait · #polarización · #indignación",
        "needs": "RESENTIMIENTO · MIEDO · SOLEDAD",
        "triggers": [
            {
                "big": "51,680",
                "desc": "Videos políticos 2024 analizados — el contenido tóxico y partidista atrae más engagement.",
                "src": "HKS MISINFORMATION REVIEW · 2024",
            },
            {
                "big": "evidencia\ncausal",
                "desc": "Rerankear la animosidad partidista en feeds altera la polarización afectiva.",
                "src": "PNAS / PUBMED · 2025",
            },
            {
                "big": "#outragebait",
                "desc": "Outrage bait político como formato de alto alcance — la rabia cobra en métricas.",
                "src": "TIKTOK · 2026",
            },
        ],
        "signals": [
            {
                "img": "macro-3-2-hks-toxic-politics-chart.png",
                "cap": "HKS: chart de toxicidad — contenido tóxico y partidista atrae más engagement.",
                "src": "HKS MISINFORMATION REVIEW · 2024",
                "url": "https://misinforeview.hks.harvard.edu/article/toxic-politics-and-tiktok-engagement-in-the-2024-u-s-election/",
            },
            {
                "img": "macro-3-2-pubmed-reranking-polarization.png",
                "cap": "PNAS / PubMed: rerankear animosidad partidista en el feed altera la polarización afectiva.",
                "src": "PNAS / PUBMED · 2025",
                "url": "https://pubmed.ncbi.nlm.nih.gov/41308156/",
            },
            {
                "img": "macro-3-2-tiktok-outragebait-hashtag.png",
                "cap": "Hashtag #outragebait en TikTok — la indignación como formato de alto alcance.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/outragebait",
            },
        ],
    },
    {
        "macro": 3,
        "headline": "LA NOTICIA EN 60 SEGUNDOS O NO EXISTE: 55% DE USUARIOS DE TIKTOK SE INFORMA AHÍ (22% EN 2020), Y EL EVENTO QUE NO ENTRA EN UN CLIP NO ENTRA A LA CONVERSACIÓN.",
        "body": "El consumo político se comprimió al formato del feed. Antes informarse pedía tiempo de lectura. Ahora pide 60 segundos verticales. El 55% de los usuarios de TikTok obtiene noticias en la app, frente a 22% en 2020 (Pew 2024), y los mismos usuarios prefieren entretenimiento sobre noticia (Marketing Brew 2024). La consecuencia es dura para el evento complejo: lo que no se explica en un clip corto se cae de la conversación. El artículo largo y el debate completo quedan fuera del scroll.",
        "hashtags": "#en60segundos · #explainer · #tldr",
        "needs": "VACÍO · INVISIBILIDAD · SOLEDAD",
        "triggers": [
            {
                "big": "55%",
                "desc": "Usuarios TikTok que obtiene noticias en la app — vs 22% en 2020.",
                "src": "PEW RESEARCH · 2024",
            },
            {
                "big": "80%",
                "desc": "Dominicanos 18-24 que se informa por redes — el clip corto es su política.",
                "src": "CÓDIGO CASA · 2024",
            },
            {
                "big": "entretenimiento\n> noticias",
                "desc": "Usuarios de TikTok prefieren entretenimiento sobre noticias — Pew findings.",
                "src": "MARKETING BREW · 2024",
            },
        ],
        "signals": [
            {
                "img": "macro-3-3-pew-social-media-news.png",
                "cap": "Pew Research fact sheet: 55% usuarios TikTok obtiene noticias ahí vs 22% en 2020.",
                "src": "PEW RESEARCH · 2024",
                "url": "https://www.pewresearch.org/journalism/fact-sheet/social-media-and-news-fact-sheet/",
            },
            {
                "img": "macro-3-3-marketingbrew-tiktok-entertainment.png",
                "cap": "Marketing Brew: usuarios TikTok prefieren entretenimiento sobre noticias según Pew.",
                "src": "MARKETING BREW · 2024",
                "url": "https://www.marketingbrew.com/stories/2024/10/08/tiktok-users-prefer-entertainment-over-news-pew-finds",
            },
            {
                "img": "macro-3-3-pew-social-media-news.png",
                "cap": "El evento que no cabe en 60 segundos no entra a la conversación — la compresión del feed.",
                "src": "PEW RESEARCH · 2024",
                "url": "https://www.pewresearch.org/journalism/fact-sheet/social-media-and-news-fact-sheet/",
            },
        ],
    },
    {
        "macro": 3,
        "headline": "POSTEAR ES PARTICIPAR: EL 70% DE LA GEN Z DICE APOYAR UNA CAUSA, CASI TODO ONLINE. COMPARTIR LA STORY SE SIENTE COMO ACCIÓN AUNQUE RARA VEZ SALGA DEL FEED.",
        "body": "Para mucha gente, el gesto digital reemplazó la acción offline. Antes participar tenía un costo físico: ir, marchar, organizarse. Ahora el 70% de la Gen Z global dice apoyar una causa, mayormente online (ShoutOut UK 2025), y el estudio Montclair 2024 describe ese activismo como más performativo que sustantivo. El comportamiento observable es compartir la story, cambiar la foto de perfil o comentar como forma principal de involucrarse. Se siente como acción. Casi nunca cruza la pantalla.",
        "hashtags": "#performativeactivism · #slacktivism · #posteo",
        "needs": "VACÍO · SOLEDAD · CULPA",
        "triggers": [
            {
                "big": "70%",
                "desc": "Gen Z global apoya una causa, mayormente online — auge del activismo performativo.",
                "src": "SHOUTOUT UK · 2025",
            },
            {
                "big": "performativo",
                "desc": "El activismo Gen Z online suele ser más performativo que sustantivo — Montclair 2024.",
                "src": "MONTCLAIR STATE UNIVERSITY · 2024",
            },
            {
                "big": "#slacktivism",
                "desc": "Debate autorreflexivo sobre el post como acción — la crítica al activismo de pantalla.",
                "src": "TIKTOK · 2026",
            },
        ],
        "signals": [
            {
                "img": "macro-3-4-tiktok-performative-activism.png",
                "cap": "Hashtag #performativeactivism en TikTok — crítica autorreflexiva del activismo de pantalla.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/performativeactivism",
            },
            {
                "img": "macro-3-4-montclair-performative-activism.png",
                "cap": "Montclair 2024: activismo Gen Z online más performativo que sustantivo — la story como gesto.",
                "src": "MONTCLAIR STATE UNIVERSITY · 2024",
                "url": "https://www.montclair.edu/college-of-communication-and-media/2024/12/05/negativity-activism-division-and-fatigue-gen-z-social-media-and-the-2024-election/",
            },
            {
                "img": "macro-3-4-tiktok-slacktivism-hashtag.png",
                "cap": "Hashtag #slacktivism en TikTok — debate sobre participación digital vs acción real.",
                "src": "TIKTOK · 2026",
                "url": "https://www.tiktok.com/tag/slacktivism",
            },
        ],
    },
    {
        "macro": 3,
        "headline": "EL FEED MIDE LA GESTIÓN: LA EVALUACIÓN DEL GOBIERNO SE ARMA EN TIEMPO REAL CON CLIPS VIRALES, DONDE LA NARRATIVA SIMPLE LE GANA A LA DATA Y EL DESMENTIDO NUNCA ALCANZA AL BULO.",
        "body": "La evaluación de un gobierno ya no espera al noticiero ni al informe. Se construye en el feed, en vivo. Las narrativas simples superan al mensaje institucional complejo y la desinformación corre más rápido que las aclaraciones oficiales en LATAM y el Caribe (Security Journal Americas 2026). Los motores de recomendación moldean política con efectos medibles (Pew 2024-2025). El comportamiento observable: formarse un juicio sobre la gestión a partir de clips y narrativas del feed, no de cifras ni reportes.",
        "hashtags": "#loqueprometió · #gestión · #narrativa",
        "needs": "RESENTIMIENTO · VACÍO · INVISIBILIDAD",
        "triggers": [
            {
                "big": "narrativa\nvs dato",
                "desc": "Narrativas simplistas superan al mensaje complejo; desinformación corre más rápido que aclaraciones.",
                "src": "SECURITY JOURNAL AMERICAS · 2026",
            },
            {
                "big": "46.6%",
                "desc": "Dominicanos que ve el sistema como nada justo — el clip confirmador viaja sin fricción.",
                "src": "CÓDIGO CASA · 2024",
            },
            {
                "big": "recomendación",
                "desc": "Motores de recomendación moldean política, crianza y fe con efectos medibles.",
                "src": "PEW RESEARCH · 2024-2025",
            },
        ],
        "signals": [
            {
                "img": "macro-3-5-securityjournal-latam-2026.png",
                "cap": "Security Journal Americas 2026: la narrativa simple le gana al mensaje institucional complejo.",
                "src": "SECURITY JOURNAL AMERICAS · 2026",
                "url": "https://securityjournalamericas.com/caribbean-latin-american-security-2026/",
            },
            {
                "img": "macro-3-5-securityjournal-latam-2026.png",
                "cap": "La desinformación corre más rápido que las aclaraciones oficiales en LATAM/Caribe.",
                "src": "SECURITY JOURNAL AMERICAS · 2026",
                "url": "https://securityjournalamericas.com/caribbean-latin-american-security-2026/",
            },
            {
                "img": "macro-3-5-securityjournal-latam-2026.png",
                "cap": "Pew Research: motores de recomendación moldean política y percepciones con efectos medibles.",
                "src": "PEW RESEARCH · 2024-2025",
                "url": "https://www.pewresearch.org/topic/internet-technology/platforms-services/social-media/",
            },
        ],
    },
]

assert len(MICROS) == 15, f"Expected 15 micros, got {len(MICROS)}"

# ============================================================
# HELPERS
# ============================================================

def add_bg(slide, prs):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.line.fill.background()
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG
    return bg

def set_run(run, text, font=FONT_SANS, size=10, bold=False, italic=False, color=WHITE):
    run.text = text
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color

def add_textbox(slide, x, y, w, h, text, font=FONT_SANS, size=10, bold=False, italic=False,
                color=WHITE, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=1.0,
                word_wrap=True):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = word_wrap
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    r = p.add_run()
    set_run(r, text, font, size, bold, italic, color)
    return tb

def add_line(slide, x1, y1, x2, y2, color_hex="FFFFFF", alpha_pct=6, weight_emu=9525):
    line = slide.shapes.add_connector(1, x1, y1, x2, y2)
    line.line.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    line.line.width = Emu(weight_emu)
    ln = line.line._get_or_add_ln()
    solidFill = ln.find(qn('a:solidFill'))
    if solidFill is None:
        solidFill = etree.SubElement(ln, qn('a:solidFill'))
    for child in list(solidFill):
        solidFill.remove(child)
    srgb = etree.SubElement(solidFill, qn('a:srgbClr'))
    srgb.set('val', color_hex)
    alpha = etree.SubElement(srgb, qn('a:alpha'))
    alpha.set('val', str(int(alpha_pct * 1000)))
    return line

def add_hyperlink_rect(slide, x, y, w, h, url):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    sh.fill.background()
    sh.line.fill.background()
    sh.click_action.hyperlink.address = url
    return sh

def add_badge_click_me(slide, x, y):
    bw = Pt(46)
    bh = Pt(14)
    b = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, bw, bh)
    b.fill.solid()
    b.fill.fore_color.rgb = ACCENT
    b.line.fill.background()
    tf = b.text_frame
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    set_run(r, "CLICK ME", font=FONT_SANS, size=7, bold=True, color=WHITE)
    return b

# ============================================================
# DIVIDER SLIDE
# ============================================================

def build_divider(prs, macro):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, prs)

    sw, sh = prs.slide_width, prs.slide_height
    cx = sw // 2

    # Etiqueta MACRO N — Poppins Bold 14pt #A0A0A0 UPPERCASE
    lbl_w = Inches(4)
    lbl_h = Inches(0.4)
    lbl_y = sh // 2 - Inches(1.8)
    add_textbox(slide, cx - lbl_w // 2, lbl_y, lbl_w, lbl_h,
                f"MACRO {macro['num']}",
                font=FONT_SANS, size=14, bold=True, color=GREY_LABEL,
                align=PP_ALIGN.CENTER)

    # Nombre macro — Instrument Serif Regular 100pt UPPERCASE white centered
    name_y = lbl_y + lbl_h + Pt(24)
    name_h = Inches(2.5)
    name_w = Inches(12.5)
    tb = slide.shapes.add_textbox(cx - name_w // 2, name_y, name_w, name_h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.line_spacing = 0.95
    r = p.add_run()
    set_run(r, macro['name'].upper(), font=FONT_SERIF, size=100, color=WHITE)

    # Tagline — Instrument Serif Italic 24pt #A0A0A0 centrada con comillas
    tag_y = name_y + name_h + Pt(16)
    tag_w = Inches(11)
    add_textbox(slide, cx - tag_w // 2, tag_y, tag_w, Inches(0.6),
                f"“{macro['tagline']}”",
                font=FONT_SERIF, size=24, italic=True, color=GREY_LABEL,
                align=PP_ALIGN.CENTER)

# ============================================================
# MICRO SLIDE
# ============================================================

def build_micro(prs, micro):
    macro = MACROS[micro['macro'] - 1]
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, prs)

    sw, sh = prs.slide_width, prs.slide_height
    # Grid
    margin_x = Inches(0.4)
    top_y = Inches(0.35)
    gutter = Inches(0.2)
    col_w = (sw - 2 * margin_x - 2 * gutter) // 3
    col_left_x = margin_x
    col_center_x = col_left_x + col_w + gutter
    col_right_x = col_center_x + col_w + gutter

    # ---- TABS arriba col-left ----
    tab_y = top_y
    tab_h = Inches(0.22)
    tab1_w = Inches(0.85)
    tab2_w = Inches(2.2)
    # tab1 MACRO N
    t1 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, col_left_x, tab_y, tab1_w, tab_h)
    t1.fill.solid(); t1.fill.fore_color.rgb = TAB_BG
    t1.line.color.rgb = TAB_BG
    t1.line.width = Emu(3175)
    tf = t1.text_frame
    tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05); tf.margin_top = 0; tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); set_run(r, f"MACRO {macro['num']}", font=FONT_SANS, size=8, bold=True, color=BLACK)
    # tab2 short name
    t2 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, col_left_x + tab1_w, tab_y, tab2_w, tab_h)
    t2.fill.background()
    t2.line.color.rgb = RGBColor(0x60, 0x60, 0x60)
    t2.line.width = Emu(3175)
    tf = t2.text_frame
    tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05); tf.margin_top = 0; tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); set_run(r, macro['short'], font=FONT_SANS, size=8, color=GREY_LABEL)

    # ---- Column labels ----
    labels_y = tab_y + tab_h + Inches(0.25)
    labels_h = Inches(0.25)
    add_textbox(slide, col_left_x, labels_y, col_w, labels_h,
                "DEFINICIÓN", font=FONT_SANS, size=8, bold=True, color=GREY_LABEL)
    add_textbox(slide, col_center_x, labels_y, col_w, labels_h,
                "TRIGGERS", font=FONT_SANS, size=8, bold=True, color=GREY_LABEL)
    add_textbox(slide, col_right_x, labels_y, col_w, labels_h,
                "SEÑALES", font=FONT_SANS, size=8, bold=True, color=GREY_LABEL)

    # Horizontal line under labels
    line_y = labels_y + labels_h + Inches(0.04)
    add_line(slide, margin_x, line_y, sw - margin_x, line_y, alpha_pct=6, weight_emu=9525)

    # Vertical lines between columns
    content_top = line_y + Inches(0.15)
    content_bottom = sh - Inches(0.3)
    add_line(slide, col_center_x - gutter // 2, content_top, col_center_x - gutter // 2, content_bottom, alpha_pct=6, weight_emu=9525)
    add_line(slide, col_right_x - gutter // 2, content_top, col_right_x - gutter // 2, content_bottom, alpha_pct=6, weight_emu=9525)

    # ===== COL LEFT — Headline + Body + Hashtags + Needs =====
    cur_y = content_top
    headline = micro['headline']
    hl = len(headline)
    if hl <= 80:
        hl_size = 50
    elif hl <= 120:
        hl_size = 42
    elif hl <= 160:
        hl_size = 30
    elif hl <= 200:
        hl_size = 22
    else:
        hl_size = 18
    hl_h = Inches(2.2)
    tb = slide.shapes.add_textbox(col_left_x, cur_y, col_w - Inches(0.1), hl_h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.line_spacing = 0.95
    r = p.add_run()
    set_run(r, headline.upper(), font=FONT_SERIF, size=hl_size, color=WHITE)
    cur_y += hl_h + Inches(0.1)

    # EL FENÓMENO label
    add_textbox(slide, col_left_x, cur_y, col_w, Inches(0.18),
                "EL FENÓMENO", font=FONT_SANS, size=7, bold=True, color=GREY_LABEL)
    cur_y += Inches(0.2)
    # Body — Poppins Regular 10pt white line-spacing 1.0
    body_h = Inches(1.5)
    tb = slide.shapes.add_textbox(col_left_x, cur_y, col_w - Inches(0.1), body_h)
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.line_spacing = 1.0
    r = p.add_run()
    set_run(r, micro['body'], font=FONT_SANS, size=10, color=WHITE)
    cur_y += body_h + Inches(0.05)

    # HASHTAGS label + content — Instrument Serif Regular 23pt
    add_textbox(slide, col_left_x, cur_y, col_w, Inches(0.18),
                "HASHTAGS", font=FONT_SANS, size=7, bold=True, color=GREY_LABEL)
    cur_y += Inches(0.2)
    tb = slide.shapes.add_textbox(col_left_x, cur_y, col_w - Inches(0.1), Inches(0.7))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.line_spacing = 1.1
    r = p.add_run()
    set_run(r, micro['hashtags'], font=FONT_SERIF, size=23, color=WHITE)
    cur_y += Inches(0.75)

    # 3 NEEDS label + content — Instrument Serif Regular 14pt
    add_textbox(slide, col_left_x, cur_y, col_w, Inches(0.18),
                "3 NEEDS", font=FONT_SANS, size=7, bold=True, color=GREY_LABEL)
    cur_y += Inches(0.2)
    tb = slide.shapes.add_textbox(col_left_x, cur_y, col_w - Inches(0.1), Inches(0.5))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.line_spacing = 1.05
    r = p.add_run()
    set_run(r, micro['needs'], font=FONT_SERIF, size=14, color=WHITE)

    # ===== COL CENTER — TRIGGERS (3 vertical stats + desc box 170x35pt) =====
    trig_top = content_top
    block_h = (content_bottom - trig_top) / 3
    big_w = Inches(1.5)
    desc_box_w = Pt(170)
    desc_box_h = Pt(35)
    src_h = Inches(0.18)

    for i, trig in enumerate(micro['triggers']):
        bx = col_center_x
        by = int(trig_top + i * block_h)
        # Big stat
        big = trig['big']
        big_len = len(big)
        if big_len <= 3:
            big_size = 72
        elif big_len <= 5:
            big_size = 54
        elif big_len <= 7:
            big_size = 42
        elif big_len <= 10:
            big_size = 32
        else:
            big_size = 24
        tb = slide.shapes.add_textbox(bx, by, big_w, Inches(1.2))
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.line_spacing = 1.0
        r = p.add_run()
        set_run(r, big, font=FONT_SERIF, size=big_size, color=WHITE)
        # Source under big
        add_textbox(slide, bx, by + Inches(1.25), big_w, src_h,
                    trig['src'], font=FONT_SANS, size=7, color=GREY_MUTED)
        # Desc box to the right — W170pt x H35pt Poppins 10pt white
        dbx = bx + big_w + Inches(0.05)
        dby = by + Inches(0.15)
        tb = slide.shapes.add_textbox(dbx, dby, desc_box_w, desc_box_h)
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.line_spacing = 1.0
        r = p.add_run()
        set_run(r, trig['desc'], font=FONT_SANS, size=10, color=WHITE)

    # ===== COL RIGHT — SEÑALES (3 fotos 149x220pt + caja caption 170x35pt) =====
    sig_top = content_top
    photo_w = Pt(149)
    photo_h = Pt(220)
    cap_box_w = Pt(170)
    cap_box_h = Pt(35)
    block_h_r = (content_bottom - sig_top) / 3

    for i, sig in enumerate(micro['signals']):
        bx = col_right_x
        by = int(sig_top + i * block_h_r)
        img_path = os.path.join(SHOTS, sig['img'])
        if os.path.exists(img_path):
            try:
                slide.shapes.add_picture(img_path, bx, by, width=photo_w, height=photo_h)
            except Exception as e:
                print(f"  WARNING: could not add image {sig['img']}: {e}")
                ph = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, bx, by, photo_w, photo_h)
                ph.fill.solid(); ph.fill.fore_color.rgb = PLACEHOLDER_BG
                ph.line.color.rgb = WHITE; ph.line.width = Emu(3175)
                tf = ph.text_frame; tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
                tf.vertical_anchor = MSO_ANCHOR.MIDDLE
                p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
                r = p.add_run()
                set_run(r, "CAPTURA MANUAL\nJEREMY", font=FONT_SANS, size=8, bold=True, color=GREY_MUTED)
        else:
            print(f"  WARNING: image not found: {img_path}")
            ph = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, bx, by, photo_w, photo_h)
            ph.fill.solid(); ph.fill.fore_color.rgb = PLACEHOLDER_BG
            ph.line.color.rgb = WHITE; ph.line.width = Emu(3175)
            tf = ph.text_frame; tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
            r = p.add_run()
            set_run(r, "CAPTURA MANUAL\nJEREMY", font=FONT_SANS, size=8, bold=True, color=GREY_MUTED)

        # Badge "Click me" upper right of photo
        bd_x = bx + photo_w - Pt(38)
        bd_y = by - Pt(6)
        add_badge_click_me(slide, bd_x, bd_y)

        # Hyperlink invisible overlay over photo
        add_hyperlink_rect(slide, bx, by, photo_w, photo_h, sig['url'])

        # Caption box to the right — W170pt x H35pt Poppins 10pt white
        cap_x = bx + photo_w + Inches(0.08)
        cap_y = by + Inches(0.15)
        tb = slide.shapes.add_textbox(cap_x, cap_y, cap_box_w, cap_box_h)
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.line_spacing = 1.0
        r = p.add_run()
        set_run(r, sig['cap'], font=FONT_SANS, size=10, color=WHITE)
        # Source under caption
        add_textbox(slide, cap_x, cap_y + cap_box_h + Inches(0.02), cap_box_w, src_h,
                    sig['src'], font=FONT_SANS, size=7, color=GREY_MUTED)

# ============================================================
# MAIN
# ============================================================

def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    micros_by_macro = {1: [], 2: [], 3: []}
    for m in MICROS:
        micros_by_macro[m['macro']].append(m)

    for macro in MACROS:
        build_divider(prs, macro)
        for micro in micros_by_macro[macro['num']]:
            build_micro(prs, micro)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    prs.save(OUT)
    print(f"Saved: {OUT}")
    print(f"Total slides: {len(prs.slides)}")

if __name__ == "__main__":
    main()
