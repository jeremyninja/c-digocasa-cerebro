#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Trends Tecnologia — Forecast Deck (18 slides)
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
SHOTS = os.path.join(BASE, "screenshots/trends-tecnologia")
OUT = os.path.join(BASE, "outputs/trends-tecnologia-forecast.pptx")

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
        "headline": "EL ADULTO LATAM TRABAJA, FACTURA Y ESTUDIA DESDE UN SOLO TELÉFONO, Y NUNCA TOCA UNA LAPTOP: LA ÚNICA COMPUTADORA QUE TENDRÁ YA ESTÁ EN SU MANO.",
        "body": "El hogar multi-dispositivo del siglo XX asumía que ibas acumulando: PC, después tablet, después consola. Esa escalera se saltó. La penetración de internet en RD llegó a 88.6% (10.2M usuarios) mientras la computadora sigue siendo minoritaria en el hogar. Plataformas como Rappi, Uber y Workana hacen del móvil la oficina del trabajador joven LATAM. El adulto no aspira a poseer varios aparatos; concentra todo en uno y lo muestra como normal.",
        "hashtags": "#trabajodesdeelcelular · #soloconmicelular · #emprenderdominicana",
        "needs": "PERTENENCIA · CONTROL · MIEDO",
        "triggers": [
            {"big": "88.6%", "desc": "Penetración de internet en RD (10.2M usuarios); la computadora sigue minoritaria en el hogar.", "src": "DATAREPORTAL · 2025"},
            {"big": "Móvil\nPrimero", "desc": "El mobile gaming domina el mercado de videojuegos LATAM por adopción de smartphone sobre PC/consola.", "src": "MORDOR INTELLIGENCE · 2025"},
            {"big": "Gig\nLATAM", "desc": "Rappi, Uber y Workana hacen del móvil la oficina del trabajador joven LATAM.", "src": "UNDP LATAM · 2025"},
        ],
        "signals": [
            {"img": "macro-1-1-datareportal-digital-2025-rd.png", "cap": "Portada del informe Digital 2025 RD con métricas de penetración internet 88.6% y dispositivos.", "src": "DATAREPORTAL · 2025", "url": "https://datareportal.com/reports/digital-2025-dominican-republic"},
            {"img": "macro-1-1-konvoy-latam-gig-economy.png", "cap": "Newsletter con logos de apps gig (Rappi, Uber, iFood) y gráfico de market share ride-hailing LATAM.", "src": "KONVOY VC · 2025", "url": "https://www.konvoy.vc/newsletters/latams-local-gig-economy"},
            {"img": "macro-1-1-tiktok-tag-emprenderdominicana.png", "cap": "Hashtag #emprenderdominicana en TikTok — negocios dominicanos gestionados desde el teléfono.", "src": "TIKTOK · 2026", "url": "https://www.tiktok.com/tag/emprenderdominicana"},
        ],
    },
    {
        "macro": 1,
        "headline": "GANAR EN DÓLARES DESDE EL CUARTO: EL JOVEN LATAM SE INVENTA UNA CARRERA SIN OFICINA, SIN EMPLEADOR FIJO Y SIN PAÍS QUE LO AMARRE.",
        "body": "La carrera tradicional asumía una empresa, una ciudad y un horario. El gig remoto cross-border rompió las tres. Las altas en plataformas freelance subieron 24% desde ciudades tier-2 y tier-3 en LATAM y el Sudeste Asiático. Costa Rica, México y Colombia ya lanzaron visas de nómada digital de hasta un año. El resultado observable: gente facturando a clientes de USA y Europa desde casa, en moneda dura, y mostrándolo como estilo de vida.",
        "hashtags": "#nomadadigital · #cobroendolares · #trabajoremotord",
        "needs": "LIBERTAD · LOGRO · SOLEDAD",
        "triggers": [
            {"big": "+24%", "desc": "Altas en plataformas gig desde ciudades tier-2/tier-3 en LATAM y SE Asia.", "src": "HRSTACKS / KONVOY · 2025"},
            {"big": "Workana\n#1", "desc": "Workana se consolida como la plataforma freelance #1 para nómadas en Sudamérica.", "src": "GIGEXCHANGE / HOLAFLY · 2025"},
            {"big": "3 Visas", "desc": "Costa Rica, México y Colombia lanzan visas de nómada digital de hasta 1 año.", "src": "HOLAFLY · 2025"},
        ],
        "signals": [
            {"img": "macro-1-2-tiktok-tag-nomadadigital.png", "cap": "Hashtag #nomadadigital en TikTok — grid con lifestyle remoto de freelancers latinoamericanos.", "src": "TIKTOK · 2026", "url": "https://www.tiktok.com/tag/nomadadigital"},
            {"img": "macro-1-2-hrstacks-gig-statistics.png", "cap": "Estadísticas gig economy con datos clave de crecimiento freelance incluyendo +24% desde ciudades tier-2/3.", "src": "HRSTACKS · 2025", "url": "https://www.hrstacks.com/gig-economy-freelance-work-statistics/"},
            {"img": "macro-1-2-holafly-nomada-digital-latam.png", "cap": "Plataformas de trabajo remoto para nómadas digitales con sección 'Best websites to find remote jobs'.", "src": "HOLAFLY · 2025", "url": "https://esim.holafly.com/digital-nomad/digital-nomad-jobs/"},
        ],
    },
    {
        "macro": 1,
        "headline": "EL TELÉFONO FIJO SE MURIÓ SIN QUE NADIE LO LLORARA: HOY SE FORMA UN HOGAR Y NADIE PREGUNTA DÓNDE SE PONE LA LÍNEA.",
        "body": "Inaugurar la adultez 'poniendo la línea fija' era un rito del siglo XX. Ese rito desapareció sin reemplazo simbólico. El landline se extingue globalmente y los hogares jóvenes nacen mobile-only. INDOTEL reporta un +24% en uso de internet móvil en RD: la conectividad se volvió móvil-céntrica de punta a punta. WhatsApp pasó a ser la infraestructura de comunicación del hogar y la llamada al fijo dejó de existir como gesto.",
        "hashtags": "#sintelefonofijo · #soloWhatsApp · #conectividadrd",
        "needs": "PERTENENCIA · CONTROL · VACÍO",
        "triggers": [
            {"big": "Mobile\nOnly", "desc": "El landline se extingue globalmente; los hogares jóvenes nacen sin teléfono fijo.", "src": "MICROSOFT AI ECONOMY INSTITUTE · 2026"},
            {"big": "+24%", "desc": "INDOTEL reporta +24% en uso de internet móvil en RD; conectividad 100% móvil-céntrica.", "src": "INDOTEL · 2025"},
            {"big": "6.2%", "desc": "Hogares RD conserva teléfono fijo — nadie está reponiéndolo. El rito de la línea ya se apagó.", "src": "DATAREPORTAL · 2025"},
        ],
        "signals": [
            {"img": "macro-1-3-indotel-conectividad-movil-24.png", "cap": "Nota oficial INDOTEL sobre +24% uso internet móvil en RD — fuente primaria local con logo institucional.", "src": "INDOTEL · 2025", "url": "https://indotel.gob.do/indotel-revela-incremento-en-los-niveles-de-conectividad-fija-y-movil-en-la-republica-dominicana-un-aumento-de-un-24-en-uso-de-internet-movil-en-rd/"},
            {"img": "macro-1-3-microsoft-ai-economy-mobile.png", "cap": "Blog Microsoft con análisis de adopción global de IA en 2025 y referencia a brecha digital por conectividad móvil.", "src": "MICROSOFT ON THE ISSUES · ENE 2026", "url": "https://blogs.microsoft.com/on-the-issues/2026/01/08/global-ai-adoption-in-2025/"},
            {"img": "macro-1-3-indotel-conectividad-movil-24.png", "cap": "Conectividad móvil como nueva base de la vida adulta — la línea fija como marcador que se apagó.", "src": "INDOTEL · 2025", "url": "https://www.tiktok.com/tag/conectividadrd"},
        ],
    },
    {
        "macro": 1,
        "headline": "SABER PROMPTEAR ES LA NUEVA ALFABETIZACIÓN: LA BRECHA YA NO ES TENER INTERNET, ES MANEJAR LA IA. EL QUE NO LA USA QUEDA MARCADO COMO ATRASADO.",
        "body": "Antes la competencia adulta se medía en leer, después en usar Excel. Ahora la frontera se corre a la IA. Microsoft describe una brecha digital 'que se ensancha' entre quien domina la IA y quien no. Ya hay +122M de personas usando herramientas gen-AI cada día — 1 de cada 6 globalmente. La consecuencia observable: adultos pagando cursos de IA y mostrando 'cómo uso ChatGPT en mi trabajo' como credencial.",
        "hashtags": "#aprenderIA · #habilidadesdigitales · #upskilling",
        "needs": "LOGRO · RECONOCIMIENTO · MIEDO",
        "triggers": [
            {"big": "+122M", "desc": "Personas usan herramientas gen-AI cada día; 1 de cada 6 globalmente.", "src": "DEMANDSAGE · 2026"},
            {"big": "Brecha\nIA", "desc": "La adopción de IA en 2025 abre una brecha digital 'que se ensancha' entre quien la domina y quien no.", "src": "MICROSOFT ON THE ISSUES · ENE 2026"},
            {"big": "100K", "desc": "INDOTEL adjudica capacitación en habilidades digitales a 100,000 beneficiarios en RD.", "src": "INDOTEL PLAN BIANUAL 2025-2026"},
        ],
        "signals": [
            {"img": "macro-1-4-tiktok-tag-aprendia.png", "cap": "Hashtag #aprendia en TikTok — grid de videos sobre aprendizaje de IA en español con thumbnails cargados.", "src": "TIKTOK · 2026", "url": "https://www.tiktok.com/tag/aprendia"},
            {"img": "macro-1-4-demandsage-genai-statistics.png", "cap": "Estadísticas gen-AI: +122M usuarios diarios, 1 de cada 6 personas globalmente usa herramientas de IA.", "src": "DEMANDSAGE · 2026", "url": "https://www.demandsage.com/generative-ai-statistics/"},
            {"img": "macro-1-4-indotel-capacitacion-digital.png", "cap": "Sección INDOTEL con referencia al Plan Bianual 2025-2026 de capacitación digital — fuente local.", "src": "INDOTEL · 2025", "url": "https://indotel.gob.do/acceso-e-infraestructura/"},
        ],
    },
    {
        "macro": 1,
        "headline": "LA CONSOLA MURIÓ DE PIE EN LA SALA: EL OCIO ADULTO SE MUDÓ DEL LIVING AL TELÉFONO EN LA CAMA, Y EL CUARTO DE JUEGOS FAMILIAR DEJÓ DE SER ALGO QUE SE ASPIRA.",
        "body": "La consola más la TV grande marcaban el hogar acomodado. Ese centro de ocio se desarmó. Menos del 10% de hogares LATAM tiene consola next-gen; el gaming se volvió íntimo, móvil y constante. El mercado gaming LATAM cerró 2025 en US$25.7B con el mobile dominando por pura adopción de smartphone. La consecuencia visible: adultos gastando en skins y gachas del móvil más que en consola, jugando en la cama en vez de la sala.",
        "hashtags": "#mobilegaming · #gamerrd · #jugardesdeelcelular",
        "needs": "PLACER · ESCAPE · SOLEDAD",
        "triggers": [
            {"big": "US$25.7B", "desc": "Mercado gaming LATAM en 2025; el mobile dominó por adopción de smartphone sobre consola.", "src": "MARKETDATAFORECAST · 2025"},
            {"big": "89.9%", "desc": "Jugadores brasileños que topan con juegos monetizados pagan al menos una vez.", "src": "PESQUISA GAME BRASIL · 2025"},
            {"big": "<10%", "desc": "Hogares LATAM posee consola next-gen; 300M+ gamers, casi todos móviles.", "src": "LAVGA / TERRA · 2025"},
        ],
        "signals": [
            {"img": "macro-1-5-tiktok-tag-mobilegaming.png", "cap": "Hashtag #mobilegaming en TikTok — gameplay móvil como el ocio dominante, sin consola.", "src": "TIKTOK · 2026", "url": "https://www.tiktok.com/tag/mobilegaming"},
            {"img": "macro-1-5-marketdataforecast-latam-videogames.png", "cap": "Reporte con market overview, gráfico de crecimiento y breakdown por segmento (mobile dominante) LATAM.", "src": "MARKETDATAFORECAST · 2025", "url": "https://www.marketdataforecast.com/market-reports/latin-america-video-game-market"},
            {"img": "macro-1-5-terra-latam-gaming-market.png", "cap": "Análisis del mercado gaming LATAM US$25.7B con breakdown de plataformas — mobile vs consola <10%.", "src": "TERRA LOCALIZATIONS · JUL 2025", "url": "https://terralocalizations.com/2025/07/03/latin-american-gaming-market-power/"},
        ],
    },
    # ----- MACRO 2 -----
    {
        "macro": 2,
        "headline": "EL BANCO REAL YA NO TIENE EDIFICIO: CIENTOS DE MILES DE DOMINICANOS MUEVEN TODA SU PLATA DESDE UNA APP Y A ESO NO LE LLAMAN FINTECH, LE LLAMAN NORMAL.",
        "body": "La banca era un edificio al que ibas. Dejó de serlo. Neobancos como Qik y wallets como tPago volvieron la app el banco principal de cientos de miles de dominicanos: Qik superó 600,000 clientes, tPago 556,000 registrados, y la banca digital RD creció 20% interanual. Los pagos digitales se proyectan a US$7.91B en 2028. El comportamiento observable: pagar la luz, enviarle a un familiar y ahorrar sin pisar una sucursal.",
        "hashtags": "#qikrd · #pagocontelefono · #neobanco",
        "needs": "CONTROL · SEGURIDAD · MIEDO",
        "triggers": [
            {"big": "600K", "desc": "Qik superó 600,000 clientes; tPago 556,000 registrados; banca digital RD +20% interanual.", "src": "GLOBAL FINANCE / FINTECH TIMES · 2026"},
            {"big": "US$7.91B", "desc": "Pagos digitales RD proyectados a US$7.91B en 2028, creciendo 9.07% anual.", "src": "STATISTA · 2024-2028"},
            {"big": "50+", "desc": "Fintechs operando en RD (vs 20 en 2018), con respaldo regulatorio del BCRD.", "src": "GLOBAL FINANCE · 2025"},
        ],
        "signals": [
            {"img": "macro-2-1-fintechtimes-rd-2026.png", "cap": "Artículo 'Fintech Landscape of the Dominican Republic in 2026' con hero foto aérea de Santo Domingo.", "src": "THE FINTECH TIMES · 2026", "url": "https://thefintechtimes.com/fintech-landscape-of-the-dominican-republic-in-2026/"},
            {"img": "macro-2-1-statista-digital-payments-rd.png", "cap": "Dashboard Statista con proyección de pagos digitales RD y chart de Transaction Value 2018-2030.", "src": "STATISTA · 2025", "url": "https://www.statista.com/outlook/dmo/fintech/digital-payments/dominican-republic"},
            {"img": "macro-2-1-tiktok-tag-qikrd.png", "cap": "Hashtag #qikrd en TikTok — onboarding y demos cotidianas de pago móvil dominicano.", "src": "TIKTOK · 2026", "url": "https://www.tiktok.com/tag/qikrd"},
        ],
    },
    {
        "macro": 2,
        "headline": "EL CUERPO DE LA FAMILIA SE VOLVIÓ UN PANEL DE DATOS: EL RELOJ CUENTA EL SUEÑO Y LOS PASOS, Y LA CONSULTA MÉDICA PASÓ A SER UNA VIDEOLLAMADA.",
        "body": "La salud entraba al hogar como cita: ibas al doctor. El wearable la convirtió en métrica que vive en la muñeca. El mercado de dispositivos médicos wearables va hacia US$499.2B en 2035 (CAGR 21.6%). En LATAM hay demanda alta de smartwatches y fitness trackers por urbanización y conciencia de salud, mientras Philips despliega biosensores para monitoreo cardíaco post-alta y la teleconsulta escala en Colombia y Brasil.",
        "hashtags": "#smartwatch · #telemedicina · #saluddigital",
        "needs": "SEGURIDAD · CONTROL · MIEDO",
        "triggers": [
            {"big": "US$499B", "desc": "Mercado de dispositivos médicos wearables hacia US$499.2B en 2035 (CAGR 21.6%).", "src": "MARKETSANDMARKETS / PRNEWSWIRE · 2025"},
            {"big": "LATAM\nSalud", "desc": "Philips despliega biosensores wearables para monitoreo cardíaco post-alta en Argentina; teleconsulta masiva en Colombia y Brasil.", "src": "MARKETDATAFORECAST LATAM · 2025"},
            {"big": "Alta\nDemanda", "desc": "Demanda alta de smartwatches y fitness trackers en LATAM por urbanización y conciencia de salud.", "src": "MAXIMIZE MARKET RESEARCH · 2025"},
        ],
        "signals": [
            {"img": "macro-2-2-prnewswire-wearables-499b.png", "cap": "Press release con infografía mercado wearables médicos: US$499.2B para 2035, CAGR 21.6%, pie chart.", "src": "MARKETSANDMARKETS VIA PRNEWSWIRE · 2025", "url": "https://www.prnewswire.com/news-releases/wearable-medical-devices-market-poised-for-usd-499-2-billion-by-2035--growing-at-a-cagr-21-6--strategic-insights-for-cxos-and-healthcare-leaders-302579862.html"},
            {"img": "macro-2-2-marketdataforecast-latam-digital-health.png", "cap": "Reporte salud digital LATAM con overview incluyendo telesalud y wearables — crecimiento y actores clave.", "src": "MARKETDATAFORECAST · 2025", "url": "https://www.marketdataforecast.com/market-reports/latin-america-digital-health-market"},
            {"img": "macro-2-2-maximize-latam-wearables.png", "cap": "Reporte wearables LATAM con múltiples charts de segmentación y datos de CAGR por producto y geografía.", "src": "MAXIMIZE MARKET RESEARCH · 2025", "url": "https://www.maximizemarketresearch.com/market-report/wearable-medical-devices-market-latin-america/2245/"},
        ],
    },
    {
        "macro": 2,
        "headline": "LA CASA EMPEZÓ A TENER OÍDOS: CÁMARAS, BOMBILLOS Y BOCINAS CON VOZ ENTRAN AL HOGAR URBANO LATAM, Y EL DUEÑO LA MANEJA DESDE EL SOFÁ HABLÁNDOLE EN VOZ ALTA.",
        "body": "El smart home era lujo gringo de película. Dejó de serlo. Cámaras, bombillos, cerraduras y bocinas con voz entran a hogares urbanos LATAM por seguridad y por status: el mercado va de US$3.4B (2025) a US$8.2B+, y 45% de hogares urbanos de clase media ya compró un producto smart. México lidera con +38% interanual en dispositivos conectados, y Sudamérica proyecta 90.8% de penetración para 2029.",
        "hashtags": "#smarthome · #alexarutina · #domotica",
        "needs": "SEGURIDAD · CONTROL · RECONOCIMIENTO",
        "triggers": [
            {"big": "US$3.4B", "desc": "Smart home LATAM (2025) → US$8.2B+; 45% de hogares urbanos de clase media ya compró un producto smart.", "src": "IMARC / NEXTMSC · 2025"},
            {"big": "+38%", "desc": "México lidera la región con +38% interanual en ventas de dispositivos conectados.", "src": "NEXTMSC · 2025"},
            {"big": "90.8%", "desc": "Penetración de smart home en hogares sudamericanos llegará a 90.8% en 2029.", "src": "STATISTA · 2026"},
        ],
        "signals": [
            {"img": "macro-2-3-statista-smarthome-southamerica.png", "cap": "Dashboard Statista Smart Home Sudamérica con chart de Revenue 2018-2029 por segmento — proyección 90.8%.", "src": "STATISTA MARKET INSIGHTS · ABR 2026", "url": "https://www.statista.com/outlook/cmo/smart-home/south-america"},
            {"img": "macro-2-3-imarc-smart-home-latam.png", "cap": "Portada del reporte smart home LATAM con market overview — US$3.4B 2025, 45% hogares urbanos clase media.", "src": "IMARC GROUP · 2025", "url": "https://www.imarcgroup.com/latin-america-smart-home-market"},
            {"img": "macro-2-3-nextmsc-mexico-smarthome.png", "cap": "Reporte smart home México con hero image y headline de +38% interanual en ventas de dispositivos conectados.", "src": "NEXTMSC · 2025", "url": "https://www.nextmsc.com/report/mexico-smart-home-market"},
        ],
    },
    {
        "macro": 2,
        "headline": "LLEGA EL MOMENTO INCÓMODO: YA NO LE PIDES A LA IA QUE RECOMIENDE, LE PIDES QUE COMPRE. RUFUS EJECUTA SOLO AL PRECIO OBJETIVO Y EL HUMANO SOLO PONE LAS REGLAS.",
        "body": "La IA recomendaba; tú decidías y comprabas. Esa frontera se está cruzando. Rufus llegó a 250M de usuarios al mes (+140% interanual) y ahora compra autónomamente al precio objetivo; OpenAI lanzó Operator para hacer clic, scroll y ordenar con eBay, Instacart y Etsy; Amazon pivota a un agente de compra en Alexa. El reto medible es la confianza: 48% confiaría en IA para recomendar, pero solo 20% para que compre.",
        "hashtags": "#agenticAI · #compraautomatica · #shoppingbot",
        "needs": "CONTROL · PLACER · MIEDO",
        "triggers": [
            {"big": "250M", "desc": "Usuarios/mes de Rufus, +140% interanual; ahora compra autónomamente al precio objetivo.", "src": "AWS / NOVADATA · 2026"},
            {"big": "48%\nvs 20%", "desc": "48% confiaría en IA para recomendar productos, solo 20% para que compre — la brecha de confianza agentic.", "src": "AI TRENDS STUDY 2026 (N=1,037)"},
            {"big": "Operator", "desc": "OpenAI lanza Operator (clic/scroll/orden) con eBay, Instacart, Etsy; Amazon pivota a Alexa shopping agéntico.", "src": "CNBC · MAY 2026"},
        ],
        "signals": [
            {"img": "macro-2-4-novadata-rufus-250m.png", "cap": "Noticia sobre Rufus con 250M usuarios/mes y capacidad de auto-compra al precio objetivo.", "src": "NOVADATA · 2025", "url": "https://novadata.io/resources/news/amazon-rufus-agentic-auto-buy-250-million-users"},
            {"img": "macro-2-4-forrester-agentic-commerce.png", "cap": "Blog Forrester 'Power Couple OpenAI + Amazon May Have Just Won Consumer Agentic Commerce' — dato 48%/20%.", "src": "FORRESTER · MAR 2026", "url": "https://www.forrester.com/blogs/power-couple-openai-amazon-may-have-just-won-consumer-agentic-commerce/"},
            {"img": "macro-2-4-cnbc-amazon-alexa-shopping-agent.png", "cap": "CNBC: 'Amazon Ditches Rufus AI Chatbot in Favor of Alexa Shopping Agent' — el pivote al comercio agéntico.", "src": "CNBC · MAY 2026", "url": "https://www.cnbc.com/2026/05/13/amazon-ditches-rufus-ai-chatbot-in-favor-of-alexa-shopping-agent.html"},
        ],
    },
    {
        "macro": 2,
        "headline": "LOS PADRES SON LOS POWER USERS QUE NADIE VIO VENIR: USAN CHATGPT MÁS QUE QUIEN NO TIENE HIJOS, Y NO PARA LA TAREA, SINO PARA EL MENÚ, LOS BERRINCHES Y SUS PROPIAS EMOCIONES.",
        "body": "ChatGPT empezó haciendo la tarea escolar. Terminó copilotando el hogar. Un estudio de OpenAI con Harvard reporta que 79% de padres usa IA frente a 54% de no-padres, y el uso no laboral pasó de 53% (jun-2024) a más de 70% en 2025. Lo que hacen es concreto: planear comidas, redactar la lista del súper, manejar un berrinche, gestionar sus propias emociones. LATAM ya es usuario diario activo — Brasil 5.8% del uso global.",
        "hashtags": "#chatgptmama · #IAenlacasa · #parentingAI",
        "needs": "APOYO · PERTENENCIA · CULPA",
        "triggers": [
            {"big": "79%", "desc": "De padres usa IA vs 54% de no-padres; uso no laboral pasó de 53% (jun-2024) a +70% (2025).", "src": "OPENAI + HARVARD (DEMING) · SEPT 2025"},
            {"big": "Menú\nCrianza", "desc": "Padres usan ChatGPT para planear comidas, listas de súper, berrinches y sus propias emociones.", "src": "BOSTON GLOBE / CNBC · 2026"},
            {"big": "Brasil\n5.8%", "desc": "Brasil 5.8% del uso global de ChatGPT, México 4.1%, Colombia 1.6% — LATAM ya es usuario diario activo.", "src": "DEMANDSAGE · 2026"},
        ],
        "signals": [
            {"img": "macro-2-5-bostonglobe-ai-parenthood-79.png", "cap": "Boston Globe Magazine sobre IA en crianza moderna — fotografía editorial y dato 79% de padres usa IA.", "src": "THE BOSTON GLOBE MAGAZINE · ENE 2026", "url": "https://www.bostonglobe.com/2026/01/14/magazine/ai-tools-modern-parenthood/"},
            {"img": "macro-2-5-cnbc-ai-parenting-chatbots.png", "cap": "CNBC sobre uso de chatbots para consejos de crianza — padres usan ChatGPT para planear comidas y berrinches.", "src": "CNBC · ENE 2026", "url": "https://www.cnbc.com/2026/01/22/when-how-to-use-ai-chatbots-for-parenting-advice-researcher.html"},
            {"img": "macro-2-5-demandsage-chatgpt-latam.png", "cap": "Dashboard estadísticas ChatGPT 2026 con datos LATAM: Brasil 5.8%, México 4.1%, Colombia 1.6% del uso global.", "src": "DEMANDSAGE · 2026", "url": "https://www.demandsage.com/chatgpt-statistics/"},
        ],
    },
    # ----- MACRO 3 -----
    {
        "macro": 3,
        "headline": "EL FEED SE VOLVIÓ GÓNDOLA: EN LATAM EL LO VI Y LO COMPRÉ AHÍ MISMO CORRE A US$20B Y REEMPLAZA LA LISTA DE COMPRAS POR EL HAUL DE IMPULSO.",
        "body": "La compra arrancaba con una lista. Ahora arranca con un scroll. TikTok Shop convierte el feed en góndola sin fricción —belleza, hogar, accesorios— y ya es ~20% del social commerce. En LATAM los usuarios pasan +70 min/día en la app y el social commerce se proyecta a US$172.4B en 2025. El comportamiento observable: comprar dentro de TikTok lo que mostró un creador y grabar hauls de 'TikTok me hizo comprar'.",
        "hashtags": "#tiktokmehizocomprar · #tiktokshop · #haul",
        "needs": "PLACER · PERTENENCIA · VACÍO",
        "triggers": [
            {"big": "~20%", "desc": "TikTok Shop = ~20% del social commerce en 2025.", "src": "EMARKETER · 2025"},
            {"big": "+70 min", "desc": "Usuarios LATAM pasan +70 min/día en la app; categorías top: belleza, skincare, accesorios, hogar.", "src": "AWISEE · 2025"},
            {"big": "US$172B", "desc": "Social commerce LATAM US$172.4B (2025); +60% sigue influencers que venden.", "src": "GLOBENEWSWIRE / GALILEO · 2026"},
        ],
        "signals": [
            {"img": "macro-3-1-emarketer-tiktokshop-20pct.png", "cap": "Press release EMARKETER con gráfico 'TikTok Shop Retail Ecommerce Sales US 2023-2027' — share ~20%.", "src": "EMARKETER · 2025", "url": "https://www.emarketer.com/press-releases/tiktok-shop-makes-up-nearly-20-of-social-commerce-in-2025/"},
            {"img": "macro-3-1-awisee-tiktokshop-latam.png", "cap": "Artículo sobre TikTok Shop en LATAM — hero con imagen y datos de categorías top (belleza, hogar, accesorios).", "src": "AWISEE · 2025", "url": "https://awisee.com/blog/tiktok-shop-in-latin-america/"},
            {"img": "macro-3-1-awisee-tiktokshop-latam.png", "cap": "Social commerce LATAM US$172.4B en 2025 — el carrito se llena con lo que el algoritmo decidió mostrar.", "src": "AWISEE · 2025", "url": "https://awisee.com/blog/tiktok-shop-in-latin-america/"},
        ],
    },
    {
        "macro": 3,
        "headline": "TU HIJO YA TIENE UN MEJOR AMIGO QUE NUNCA LO CONTRADICE: 72% DE ADOLESCENTES USÓ UN COMPAÑERO DE IA Y 1 DE CADA 4 LE CONFÍA SECRETOS REALES.",
        "body": "El confidente del adolescente era un amigo, un hermano, a veces un padre. Llegó un competidor diseñado para nunca contradecirlo. 72% de adolescentes ya usó compañeros de IA; 23% les confía 'bastante o completamente'; 25% comparte nombre, ubicación y secretos reales. Ya hay demandas contra Character.AI por daño emocional a menores y la APA alerta de un reformateo del vínculo afectivo.",
        "hashtags": "#characterai · #aicompanion · #aifriend",
        "needs": "PERTENENCIA · APOYO · SOLEDAD",
        "triggers": [
            {"big": "72%", "desc": "De adolescentes usó compañeros de IA; 23% les confía 'bastante/completamente'; 25% comparte datos reales.", "src": "COMMON SENSE MEDIA · 2025"},
            {"big": "33%", "desc": "De adolescentes prefiere hablar con IA que con personas para temas serios.", "src": "COMMON SENSE MEDIA · JUL 2025 (N=1,060)"},
            {"big": "Demandas\nChar.AI", "desc": "Demandas contra Character.AI por daño emocional a menores; la APA alerta del reformateo del vínculo afectivo.", "src": "AXIOS / APA · 2026"},
        ],
        "signals": [
            {"img": "macro-3-2-commonsense-ai-companions-72pct.png", "cap": "Press release Common Sense Media: 72% teens usó AI companions, 23% confía bastante, 25% comparte datos.", "src": "COMMON SENSE MEDIA · JUL 2025", "url": "https://www.commonsensemedia.org/press-releases/nearly-3-in-4-teens-have-used-ai-companions-new-national-survey-finds"},
            {"img": "macro-3-2-commonsense-ai-companions-72pct.png", "cap": "Estudio n=1,060 con hallazgos clave — 33% prefiere la IA para temas serios. La familia compite con un chatbot.", "src": "COMMON SENSE MEDIA · JUL 2025", "url": "https://www.commonsensemedia.org/press-releases/nearly-3-in-4-teens-have-used-ai-companions-new-national-survey-finds"},
            {"img": "macro-3-2-commonsense-ai-companions-report.png", "cap": "Reporte completo de AI companions en adolescentes — reformateo del vínculo afectivo y riesgo de sobre-dependencia.", "src": "COMMON SENSE MEDIA · JUL 2025", "url": "https://www.commonsensemedia.org/press-releases/nearly-3-in-4-teens-have-used-ai-companions-new-national-survey-finds"},
        ],
    },
    {
        "macro": 3,
        "headline": "EL FEED REEMPLAZÓ A LA ABUELA COMO AUTORIDAD: LO QUE SE COCINA Y CÓMO SE CRÍA LO DICTA LA PANTALLA, Y DESPUÉS SE CRUZA CON CHATGPT PARA CONFIRMARLO.",
        "body": "La autoridad de cómo cocinar y criar venía de la abuela, de la madre, de la tradición. Se mudó al feed. Las recetas virales, los 'what I feed my kid' y los consejos de crianza del scroll reemplazan a la transmisión familiar. Padres son los power users inesperados de IA (79%), usándola para planear comidas y crianza, así que el consejo del feed se cruza con ChatGPT como segunda opinión. 15% de consumidores globales compra un producto solo porque es tendencia en TikTok.",
        "hashtags": "#recetatiktok · #whatmykideats · #cocinaviral",
        "needs": "APOYO · RECONOCIMIENTO · CULPA",
        "triggers": [
            {"big": "79%", "desc": "Padres son los power users inesperados de IA, usándola para planear comidas y crianza.", "src": "OPENAI + HARVARD · 2025"},
            {"big": "15%", "desc": "De consumidores globales compra productos solo porque son tendencia en TikTok.", "src": "SAP EMARSYS · 2025"},
            {"big": "Hogar\nTop", "desc": "Categorías hogar y comida entre las top en TikTok Shop LATAM; recetas y rutinas de crianza dominan el feed.", "src": "AWISEE · 2025"},
        ],
        "signals": [
            {"img": "macro-3-3-bostonglobe-feed-crianza.png", "cap": "Fotografía editorial Boston Globe: padres que usan IA para planear comidas y crianza — el feed como co-autoridad.", "src": "THE BOSTON GLOBE MAGAZINE · ENE 2026", "url": "https://www.bostonglobe.com/2026/01/14/magazine/ai-tools-modern-parenthood/"},
            {"img": "macro-3-3-awisee-feed-recetas-hogar.png", "cap": "Artículo Awisee mostrando categorías top de TikTok Shop LATAM incluyendo hogar y comida.", "src": "AWISEE · 2025", "url": "https://awisee.com/blog/tiktok-shop-in-latin-america/"},
            {"img": "macro-3-3-awisee-feed-recetas-hogar.png", "cap": "El consejo del feed se valida en TikTok primero — la abuela sigue ahí, pero opina después del algoritmo.", "src": "AWISEE · 2025", "url": "https://awisee.com/blog/tiktok-shop-in-latin-america/"},
        ],
    },
    {
        "macro": 3,
        "headline": "EL MISMO FEED QUE VENDE TAMBIÉN ESTAFA: EL PHISHING POR WHATSAPP Y LOS ESQUEMAS CRIPTO ENTRAN POR EL GRUPO FAMILIAR Y VAN DIRECTO A LOS MAYORES.",
        "body": "La infraestructura digital del hogar es también su superficie de ataque más vulnerable. LATAM subió 108% interanual en amenazas cibernéticas en el Q1 2025, con la ingeniería social vía phishing como driver principal. Meta desactivó ~8M de cuentas ligadas a centros de estafa que apuntan a personas mayores. En grupos públicos de WhatsApp latinos circularon 3,000+ mensajes fraudulentos entre enero y septiembre 2025, alcanzando 192,000+ usuarios.",
        "hashtags": "#estafawhatsapp · #fraudedigital · #ciberseguridadrd",
        "needs": "SEGURIDAD · APOYO · MIEDO",
        "triggers": [
            {"big": "+108%", "desc": "LATAM en amenazas cibernéticas (Q1 2025); ingeniería social vía phishing como driver principal.", "src": "INDUSTRIAL CYBER · 2025"},
            {"big": "8M", "desc": "Cuentas desactivadas por Meta ligadas a centros de estafa que apuntan a personas mayores vía mensajería.", "src": "THE HACKER NEWS / MALWAREBYTES · 2025"},
            {"big": "3,000+", "desc": "Mensajes fraudulentos en grupos públicos de WhatsApp latinos (ene-sept 2025), alcanzando 192,000+ usuarios.", "src": "DDIA · 2025"},
        ],
        "signals": [
            {"img": "macro-3-4-ddia-whatsapp-scam-latinos.png", "cap": "Investigación DDIA: 3,000+ mensajes fraudulentos en grupos WhatsApp latinos, 192,000+ usuarios alcanzados.", "src": "DDIA · 2025", "url": "https://ddia.org/en/whatsapp-weaponized-how-scammers-target-us-latinos-part3"},
            {"img": "macro-3-4-industrialcyber-latam-phishing.png", "cap": "Artículo con hero gráfico 'Las 1 in 3' y headline sobre incremento de ransomware y phishing LATAM +108%.", "src": "INDUSTRIAL CYBER · 2025", "url": "https://industrialcyber.co/reports/latin-america-sees-sharp-rise-in-ransomware-hacktivist-attacks-in-2025-amid-expanding-fraud-and-phishing-threats/"},
            {"img": "macro-3-4-hackernews-meta-scam-tools.png", "cap": "Meta desactiva 8M cuentas de estafa y lanza herramientas de protección para personas mayores.", "src": "THE HACKER NEWS · OCT 2025", "url": "https://thehackernews.com/2025/10/meta-rolls-out-new-tools-to-protect.html"},
        ],
    },
    {
        "macro": 3,
        "headline": "EL NIÑO VIVE EN EL FEED Y LA BARRERA LLEGA TARDE: SOLO LA MITAD DE LOS PADRES USA CONTROLES PARENTALES, Y LA FAMILIA DESCUBRE DESPUÉS QUÉ CONSUMIÓ EL HIJO.",
        "body": "La preocupación por las pantallas es alta; el uso de controles, bajo. Solo 51% de padres usa controles parentales en tablets, 47% en smartphones y 35% en consolas. La APA vincula el screen time con problemas emocionales infantiles en un círculo vicioso. En RD, 89% de usuarios de internet accede a redes diariamente en un país con 88.6% de penetración: el menor accede al algoritmo temprano y poco mediado.",
        "hashtags": "#controlparental · #crianzadigital · #screentime",
        "needs": "SEGURIDAD · CONTROL · CULPA",
        "triggers": [
            {"big": "51%", "desc": "De padres usa controles parentales en tablets, 47% en smartphones, 35% en consolas.", "src": "FOSI · 2025"},
            {"big": "APA\n2025", "desc": "Estudio APA vincula screen time y problemas emocionales infantiles en círculo vicioso.", "src": "APA · JUN 2025"},
            {"big": "89%", "desc": "De usuarios de internet en RD accede a redes diariamente; exposición infantil temprana con 88.6% de penetración.", "src": "DATAREPORTAL · 2025"},
        ],
        "signals": [
            {"img": "macro-3-5-fosi-parental-controls-51pct.png", "cap": "Estudio FOSI 2025 sobre subutilización de controles parentales — 51% tablets, 47% smartphones, 35% consolas.", "src": "FOSI · 2025", "url": "https://fosi.org/parental-controls-for-online-safety-are-underutilized-new-study-finds/"},
            {"img": "macro-3-5-apa-screentime-children.png", "cap": "Press release APA vinculando screen time con problemas emocionales infantiles en un círculo vicioso.", "src": "APA · JUN 2025", "url": "https://www.apa.org/news/press/releases/2025/06/screen-time-problems-children"},
            {"img": "macro-3-5-datareportal-rd-redes-diario.png", "cap": "Informe Digital 2025 RD: 89% de usuarios accede a redes diariamente — contexto de exposición infantil.", "src": "DATAREPORTAL · 2025", "url": "https://datareportal.com/reports/digital-2025-dominican-republic"},
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
