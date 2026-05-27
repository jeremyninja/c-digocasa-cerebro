#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Trends Consumos — Forecast Deck (18 slides)
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
SHOTS = os.path.join(BASE, "screenshots/trends-consumos")
OUT = os.path.join(BASE, "outputs/trends-consumos-forecast.pptx")

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
        "headline": "EL \"NO COMPRÉ NADA ESTE MES\" REEMPLAZÓ AL ESTRENO COMO FLEX: EL UNDERCONSUMPTION CORE HIZO DEL ARMARIO MÍNIMO UNA SEÑAL DE ESTATUS.",
        "body": "Antes presumías lo que estrenabas. Ahora hay toda una estética de presumir lo contrario: el armario que repites, el \"what I didn't buy\", el reto de cero compras. La austeridad se volvió performance. No es que falte la plata — es que mostrar que no gastas se lee como criterio, como madurez financiera. El flex aspiracional se invirtió. Comprar menos pasó a ser el contenido.",
        "hashtags": "#underconsumptioncore · #nobuy2025 · #lowbuy · #deinfluencing",
        "needs": "CRITERIO · PERTENENCIA · VACÍO",
        "triggers": [
            {"big": "37%", "desc": "De Gen Z planea ahorrar más, 29% invertir — el pivote se lee como corrección, no restricción.", "src": "YOUGOV · 2025"},
            {"big": "#underconsumption\ncore", "desc": "Documentado como contra-tendencia viral al deinfluencing — el no-comprar como performance.", "src": "VISIBRAIN · 2025"},
            {"big": "\"No-Buy\"", "desc": "De Labubu al No-Buy: virales de consumo chocan con la realidad económica — el ciclo se acelera.", "src": "GIRLS UNITED / ESSENCE · 2025"},
        ],
        "signals": [
            {"img": "macro-1-1-tiktok-underconsumptioncore-1.png", "cap": "\"underconsumption core / all my furniture\" — armario mínimo como flex aspiracional en TikTok.", "src": "TIKTOK @CHELSYCHRISTINA · 2024", "url": "https://www.tiktok.com/@chelsychristina/video/7395747286262828319"},
            {"img": "macro-1-1-tiktok-underconsumptioncore-2.png", "cap": "\"Underconsumption is a CHOICE you make every day\" — el no-comprar como performance intencional.", "src": "TIKTOK @BREAKYOURBUDGET · 2025", "url": "https://www.tiktok.com/@breakyourbudget/video/7502132957872819502"},
            {"img": "macro-1-1-girlsunited-labubu-nobuy.png", "cap": "De Labubu al No-Buy: virales de consumo chocan con la realidad económica.", "src": "GIRLS UNITED / ESSENCE · 2025", "url": "https://girlsunited.essence.com/feedback/from-labubu-to-no-buy-how-viral-trends-are-colliding-with-economic-reality/"},
        ],
    },
    {
        "macro": 1,
        "headline": "EL DUPE SALIÓ DEL CLÓSET: COMPRAR LA VERSIÓN BARATA DEL LUJO DEJÓ DE DAR PENA Y PASÓ A PRESUMIRSE COMO INTELIGENCIA DE COMPRA.",
        "body": "El dupe vivía escondido. Era el truco que no decías. Ahora es el contenido: \"dupe vs original\", reseñas lado a lado, el ahorro presumido como logro. Mega-creadoras de belleza ponen el dupe en cámara sin filtro de culpa. La marca cara ya no compite solo con otras marcas — compite con su propia copia, legitimada por el feed. Acceder al código aspiracional sin pagar el precio del código se volvió la jugada lista, no la jugada vergonzosa.",
        "hashtags": "#dupe · #dupecheck · #lookforless · #amazonfinds · #dupes",
        "needs": "ASTUCIA · PERTENENCIA · RESENTIMIENTO",
        "triggers": [
            {"big": "6B+", "desc": "#dupe supera 6 mil millones de views en TikTok — la comparativa es el contenido.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "70%", "desc": "De Gen Z dice haber comprado dupes \"ocasional o muy regularmente\" el último año.", "src": "BUSINESS INSIDER / YOUGOV · 2025"},
            {"big": "\"Aspirational\nshift\"", "desc": "Dupe culture como reconfiguración del estatus de Gen Z — tener el original ya no es el flex.", "src": "LUXURY TRIBUNE · 2025"},
        ],
        "signals": [
            {"img": "macro-1-2-tiktok-dupe-7546363805240921399.png", "cap": "\"Viral perfumes — Dupe VS Original\" — reseña lado a lado de alternativas masivas vs. lujo.", "src": "TIKTOK @PERFUMESIREN · 2025", "url": "https://www.tiktok.com/@perfumesiren/video/7546363805240921399"},
            {"img": "macro-1-2-tiktok-dupe-mikayla-mco.png", "cap": "\"MCO Beauty vs. Original Products\" — el dupe legitimado por una mega-creadora de belleza.", "src": "TIKTOK @MIKAYLANOGUEIRA · 2025", "url": "https://www.tiktok.com/@mikaylanogueira/video/7496555296874188074"},
            {"img": "macro-1-2-tiktok-dupe-7526268718016400671.png", "cap": "Top 5 drugstore dupes de maquillaje high-end — la astucia del consumidor como contenido.", "src": "TIKTOK @MANNYMUA733 · 2025", "url": "https://www.tiktok.com/@mannymua733/video/7526268718016400671"},
        ],
    },
    {
        "macro": 1,
        "headline": "LO USADO DEJÓ DE SER COSA DE POBRE: EN LATAM LA REVENTA PASÓ DE NECESIDAD A ELECCIÓN DE CRITERIO, Y EL PREOWNED SE VOLVIÓ CANAL ASPIRACIONAL.",
        "body": "Comprar usado cargaba un estigma de clase. Eso se está cayendo en LATAM. El thrift haul es contenido, vender lo propio para financiar lo nuevo es práctica normal, y comprar lujo autenticado de segunda mano se lee como gusto, no como falta de plata. Plataformas como Mercado Libre y OLX vuelven el preowned un canal para jóvenes urbanos que quieren ahorrar y consumir alineado con sus valores sin perder estilo.",
        "hashtags": "#thrifthaul · #segundamano · #preloved · #reventa · #thriftflip",
        "needs": "SENTIDO · CRITERIO · INVISIBILIDAD",
        "triggers": [
            {"big": "US$17.9B", "desc": "Ropa segunda mano LATAM: US$5.2B (2025) → US$17.9B (2031), CAGR 22.8% — Brasil y México lideran.", "src": "MOBILITY FORESIGHTS / 6WRESEARCH · 2025"},
            {"big": "83%", "desc": "De Gen Z global compró o quiere comprar usado — 10.7 pts sobre el promedio total.", "src": "COGNITIVE MARKET RESEARCH · 2025"},
            {"big": "Corotos", "desc": "Corotos.com.do ya corre como marketplace dominicano de segunda mano — RD$10K a US$80,600.", "src": "COROTOS.COM.DO · 2026"},
        ],
        "signals": [
            {"img": "macro-1-3-tiktok-thrifthaul-7546587734941404471.png", "cap": "Thrift haul de la semana — botín visual de reventa aspiracional en TikTok.", "src": "TIKTOK @METALROMANTIC · 2025", "url": "https://www.tiktok.com/@metalromantic/video/7546587734941404471"},
            {"img": "macro-1-3-bankvogue-latam-secondhand.png", "cap": "Secondhand LATAM 2026: economía empuja al usado como opción mainstream para revendedores.", "src": "BANKVOGUE · 2025", "url": "https://www.bankvogue.com/blog/secondhand-latam-market-outlook-2026-what-resellers-should-expect/"},
            {"img": "macro-1-3-corotos-rd-plataforma-usados.png", "cap": "Corotos.com.do — plataforma dominicana de segunda mano con listings de RD$10,000 a US$80,600.", "src": "COROTOS.COM.DO · 2026", "url": "https://www.corotos.com.do"},
        ],
    },
    {
        "macro": 1,
        "headline": "\"NO PUEDO, ESTOY PRESUPUESTANDO\" SE VOLVIÓ PRESUMIBLE: EL LOUD BUDGETING CONVIRTIÓ EL AHORRO EN PERFORMANCE Y EL GASTO IMPULSIVO EN COSA DE INMADUROS.",
        "body": "Decir que no tenías plata daba pena. El loud budgeting le dio la vuelta: ahora anuncias en voz alta que no vas porque estás presupuestando, y eso te hace ver con control, no con carencia. Trackear gastos en público, retos de ahorro, \"swaps\" de presupuesto. El consumo se subordina a un plan financiero que se muestra. La adultez nueva no se prueba gastando — se prueba demostrando que tienes la mano en el timón en pleno contexto inflacionario.",
        "hashtags": "#loudbudgeting · #presupuesto · #ahorro2025 · #moneytok",
        "needs": "CONTROL · CRITERIO · MIEDO",
        "triggers": [
            {"big": "37%", "desc": "De Gen Z planea ahorrar más, 29% invertir — el consumo se subordina al plan financiero.", "src": "YOUGOV · 2025"},
            {"big": "\"Loud\nBudgeting\"", "desc": "Normaliza decir \"no\" al gasto social — presupuestar en público como nueva señal de adultez.", "src": "TIKTOK · 2025"},
            {"big": "BNPL\nLATAM", "desc": "Inestabilidad inflacionaria empuja a LATAM a estabilizar el poder de compra con instrumentos de planificación.", "src": "GLOBENEWSWIRE / LATAM BNPL REPORT · 2025"},
        ],
        "signals": [
            {"img": "macro-1-4-tiktok-loudbudgeting-7451260628603473198.png", "cap": "\"2025 we are LOUD BUDGETING\" — presupuestar en público como nueva señal de adultez.", "src": "TIKTOK @BREAKYOURBUDGET · 2025", "url": "https://www.tiktok.com/@breakyourbudget/video/7451260628603473198"},
            {"img": "macro-1-4-tiktok-loudbudgeting-7340699620734995754.png", "cap": "Loud budgeting swaps: marca financiera adopta el lenguaje viral para normalizar el \"no\" al gasto social.", "src": "TIKTOK @FIFTHTHIRDBANK · 2024", "url": "https://www.tiktok.com/@fifththirdbank/video/7337773119731584302"},
            {"img": "macro-2-0-globenewswire-latam-bnpl.png", "cap": "BNPL LATAM +27% en 2025 a US$16.2B — el crédito invisible democratiza el consumo digital.", "src": "GLOBENEWSWIRE · FEBRERO 2025", "url": "https://www.globenewswire.com/news-release/2025/02/27/3033728/28124/en/Latin-America-Buy-Now-Pay-Later-Business-Report-2025-2030.html"},
        ],
    },
    {
        "macro": 1,
        "headline": "EL GASTO ASPIRACIONAL SE MUDÓ DEL OBJETO A LA EXPERIENCIA: GIRL MATH Y SOFT LIFE HACEN QUE EL VIAJE PESE MÁS QUE EL CARRO NUEVO.",
        "body": "El nuevo capital social no se acumula en cosas, se acumula en momentos. El gasto aspiracional se corrió de electrodomésticos y lujo material a viajes, conciertos, autocuidado. La \"girl math\" es el marco viral que justifica el gasto experiencial — si lo usas mucho, sale gratis, esa lógica. El soft life vende vivir bien por encima de tener cosas. El recuerdo rinde más que la posesión.",
        "hashtags": "#girlmath · #softlife · #treatculture · #selfcarespending",
        "needs": "VIVENCIA · SENTIDO · VACÍO",
        "triggers": [
            {"big": "66%", "desc": "De la población global pagaría premium por productos alineados con sus valores — gasto guiado por sentido.", "src": "GREEN PREMIUM STUDIES · 2025"},
            {"big": "\"Girl Math\"", "desc": "Marco viral para justificar gasto experiencial vs. material — si lo usas mucho, sale gratis.", "src": "TIKTOK · 2023 [HISTÓRICO · CONTRASTE]"},
            {"big": "Soft Life", "desc": "Auge de wellness influencers que venden experiencia y servicio en live commerce LATAM.", "src": "GRAND VIEW RESEARCH · 2025"},
        ],
        "signals": [
            {"img": "macro-1-5-tiktok-girlmath-softlife-7454705982652943621.png", "cap": "\"Dear 2025\" con CEO SoftLife — vivir bien como aspiración post-acumulación.", "src": "TIKTOK @TASHAMICHIE124 · 2025", "url": "https://www.tiktok.com/@tashamichie124/video/7454705982652943621"},
            {"img": "macro-1-5-tiktok-girlmath-softlife-7264583361304333611.png", "cap": "\"somehow it makes sense #girlmath\" — la lógica aspiracional que convierte experiencias en inversión.", "src": "TIKTOK @MCKENNAELIANNA · 2023", "url": "https://www.tiktok.com/@mckennaelianna/video/7264583361304333611"},
            {"img": "macro-1-5-tiktok-girlmath-softlife-7276207307921313030.png", "cap": "\"Justifying purchases with GIRL MATH\" — el marco que valida el gasto experiencial sobre el material.", "src": "TIKTOK @CASANDRA.MAZZUCCO · 2023", "url": "https://www.tiktok.com/@casandra.mazzucco/video/7276207307921313030"},
        ],
    },
    # ----- MACRO 2 -----
    {
        "macro": 2,
        "headline": "EL AGENTE DE IA PASÓ DE RECOMENDARTE A COMPRAR POR TI: FIJAS EL PRECIO OBJETIVO Y RUFUS AUTO-BUY EJECUTA EL CHECKOUT SIN QUE TOQUES NADA.",
        "body": "La IA recomendaba. Ahora ejecuta. Rufus Auto-Buy compra cuando se cumplen los parámetros que tú fijaste — precio, condición, momento. El humano deja de hacer el checkout. Preguntarle a una IA \"¿qué compro?\" antes de buscar ya es comportamiento documentado. La compra se vuelve una orden delegada bajo reglas, no un acto consciente cada vez. Externalizas la fricción de comprar a un software que decide por ti dentro de los límites que pusiste.",
        "hashtags": "#aishopping · #rufus · #agenticcommerce · #shoppingassistant",
        "needs": "DELEGACIÓN · CONTROL · MIEDO",
        "triggers": [
            {"big": "250M", "desc": "Usuarios activos mensuales de Rufus (+149% YoY) — quien lo usa compra 60% más.", "src": "NOVA ANALYTICS · 2025"},
            {"big": "US$1T", "desc": "Commerce agéntico proyectado en retail USA para 2030 — McKinsey / Morgan Stanley.", "src": "MCKINSEY / MORGAN STANLEY · 2025"},
            {"big": "+US$115B", "desc": "En e-commerce adicional proyectado por agentes de IA — Amazon pivota de Rufus a Alexa Shopping Agent.", "src": "CNBC · 2026"},
        ],
        "signals": [
            {"img": "macro-2-1-tiktok-aishopping-7469936286556589344.png", "cap": "#aishopping — creadores documentan cómo la IA selecciona sus compras en TikTok.", "src": "TIKTOK @UNIQUE21OFFICIAL · 2025", "url": "https://www.tiktok.com/@unique21official/video/7469936286556589344"},
            {"img": "macro-2-1-retailtech-rufus-ai-shopping.png", "cap": "Rufus en acción: el agente de IA recomienda productos — la batalla por la intención de compra.", "src": "RETAILTECH INNOVATION HUB · ENERO 2026", "url": "https://retailtechinnovationhub.com/home/2026/1/5/rufus-and-the-ai-shopping-war-why-amazons-assistant-reveals-the-battle-for-customer-intent"},
            {"img": "macro-2-1-novadata-rufus-autobuy.png", "cap": "Rufus Auto-Buy: 250M usuarios activos mensuales (+149% YoY) — quien lo usa compra 60% más.", "src": "NOVA ANALYTICS · 2025", "url": "https://novadata.io/resources/news/amazon-rufus-agentic-auto-buy-250-million-users"},
        ],
    },
    {
        "macro": 2,
        "headline": "PÁGALO EN CUATRO Y NO LO SIENTAS: EL BNPL BORRA EL LÍMITE DEL PRESUPUESTO DE LA EXPERIENCIA DE COMPRA Y CRECE EN LATAM COMO CRÉDITO PARA LOS QUE EL BANCO NO BANCA.",
        "body": "Partir el pago en cuotas sin tarjeta cambia cómo se siente el precio. El límite del presupuesto desaparece de la pantalla: ves \"4 cuotas sin interés\" y la fricción de la deuda se diluye. En LATAM, donde +40% de la población carece de crédito formal, el BNPL crece como herramienta de inclusión y de estabilización del poder de compra. Compras ahora aunque el flujo de caja esté apretado.",
        "hashtags": "#bnpl · #cuotassininteres · #pagaen4 · #mercadopago · #fintechlatam",
        "needs": "ACCESO · CONTROL · MIEDO",
        "triggers": [
            {"big": "US$16.2B", "desc": "BNPL LATAM +27% en 2025 a US$16.2B — +40% de la población sin crédito formal.", "src": "LATAM BNPL REPORT · 2025"},
            {"big": "2026", "desc": "BNPL se expande de e-commerce a in-store y omnicanal — las super apps dominan el ecosistema.", "src": "GLOBENEWSWIRE · 2026"},
            {"big": "Inclusión", "desc": "Mercado Pago, Kueski y Creditas diseñan cuotas para no-bancarizados — BNPL como herramienta de acceso.", "src": "HOPE RESEARCH GROUP · 2025"},
        ],
        "signals": [
            {"img": "macro-2-2-addi-bnpl-checkout.png", "cap": "ADDI: \"Compra lo que quieres hoy, págalo después\" — el BNPL hace invisible el límite del presupuesto.", "src": "ADDI · 2025", "url": "https://addi.com"},
            {"img": "macro-2-2-globenewswire-bnpl-latam-2026.png", "cap": "BNPL LATAM 2026: expansión de e-commerce a in-store y omnicanal — super apps dominan.", "src": "GLOBENEWSWIRE · ENERO 2026", "url": "https://www.globenewswire.com/news-release/2026/01/20/3221587/28124/en/Latin-America-Buy-Now-Pay-Later-Business-Report-2026-2031.html"},
            {"img": "macro-2-3-tiktok-tiktokshop-7441997574112021806.png", "cap": "Creador LATAM explicando cómo monetizar el pago fraccionado — el BNPL como herramienta de sellers.", "src": "TIKTOK @CRECE.CON.LAMORE · 2025", "url": "https://www.tiktok.com/@crece.con.lamore/video/7441997574112021806"},
        ],
    },
    {
        "macro": 2,
        "headline": "EL CHECKOUT SE MUDÓ ADENTRO DEL VIDEO: TIKTOK SHOP COLAPSA ENTRETENIMIENTO Y COMPRA, Y EN BRASIL EL GMV PASÓ DE US$1M A US$25.7M EN TRES MESES.",
        "body": "Ver y comprar eran dos momentos separados. TikTok Shop los fundió: el \"yellow basket\" vive dentro del video, descubres-deseas-pagas en segundos sin salir del scroll. Ya está en cinco países de LATAM, y los números de adopción se mueven rápido — en México los registros de sellers subieron +300% desde 2023. La intención de compra ya no sale de la app. El feed dejó de ser vitrina para volverse caja registradora.",
        "hashtags": "#tiktokshop · #tiktokmademebuyit · #socialcommerce · #yellowbasket",
        "needs": "INMEDIATEZ · PERTENENCIA · VACÍO",
        "triggers": [
            {"big": "US$25.7M", "desc": "GMV mensual de TikTok Shop Brasil en 3 meses — desde US$1M; +300% sellers en México.", "src": "AWISEE / M2E CLOUD · 2025"},
            {"big": "~20%", "desc": "De share del social commerce USA capturado por TikTok Shop — proyectado a 24.1% en 2027.", "src": "EMARKETER · 2025"},
            {"big": "US$20B", "desc": "Social commerce LATAM proyectado en 2025 — +60% sigue influencers que recomiendan o venden.", "src": "LATAM INTERSECT PR · 2025"},
        ],
        "signals": [
            {"img": "macro-2-3-tiktok-tiktokshop-7441997574112021806.png", "cap": "Creador LATAM explicando TikTok Shop — el checkout integrado al video ya llega a vendedores locales.", "src": "TIKTOK @CRECE.CON.LAMORE · 2025", "url": "https://www.tiktok.com/@crece.con.lamore/video/7441997574112021806"},
            {"img": "macro-2-3-awisee-tiktokshop-latam.png", "cap": "TikTok Shop en MX, BR, CO, CL, PE — en Brasil GMV pasó de US$1M a US$25.7M en 3 meses.", "src": "AWISEE · 2025", "url": "https://awisee.com/blog/tiktok-shop-in-latin-america/"},
            {"img": "macro-2-3-emarketer-tiktokshop-20pct.png", "cap": "TikTok Shop captura ~20% del social commerce USA en 2025; proyectado a 24.1% en 2027.", "src": "EMARKETER · 2025", "url": "https://www.emarketer.com/press-releases/tiktok-shop-makes-up-nearly-20-of-social-commerce-in-2025/"},
        ],
    },
    {
        "macro": 2,
        "headline": "LA DESPENSA EMPEZÓ A LLENARSE SOLA: ESTANTERÍAS INTELIGENTES Y ELECTRODOMÉSTICOS CONECTADOS PESAN EL DETERGENTE Y LO REORDENAN ANTES DE QUE SE ACABE.",
        "body": "Ir a comprar lo básico era una tarea mental fija: revisar, anotar, salir. Esa tarea se está automatizando. El Dash Smart Shelf pesa el inventario y reordena solo vía Subscribe & Save. Lavadoras, cafeteras y electrodomésticos con Dash Replenishment integrado piden cápsulas y filtros sin que nadie lo decida en el momento. El hogar deja de \"ir a comprar\" papel y jabón — el dispositivo lo hace.",
        "hashtags": "#smarthome · #autoreplenish · #subscribeandsave · #casainteligente",
        "needs": "AUTOMATIZACIÓN · CONTROL · INVISIBILIDAD",
        "triggers": [
            {"big": "US$19.99", "desc": "Dash Smart Shelf pesa el inventario y reordena solo con Subscribe & Save — sin intervención humana.", "src": "AMAZON / RETAIL DIVE · 2020"},
            {"big": "DRS", "desc": "Fabricantes como Bosch, Toshiba, illy y Beko integran Dash Replenishment — el appliance reordena solo.", "src": "TRUSTED REVIEWS · 2018"},
            {"big": "2x dígito", "desc": "Mercado de smart home appliances LATAM crece a doble dígito anual — la adopción llega.", "src": "GRAND VIEW RESEARCH · 2025"},
        ],
        "signals": [
            {"img": "macro-2-4-retaildive-amazon-dash-shelf.png", "cap": "Amazon Dash Smart Shelf (US$19.99) — pesa el inventario y reordena solo vía Subscribe & Save.", "src": "RETAIL DIVE · 2020", "url": "https://www.retaildive.com/news/amazon-releases-dash-smart-shelf-for-consumers-small-businesses/588465/"},
            {"img": "macro-2-4-trustedreviews-amazon-drs-appliances.png", "cap": "Bosch HomeConnect con Amazon DRS: el electrodoméstico que reordena jabón y cápsulas solo.", "src": "TRUSTED REVIEWS · 2018", "url": "https://www.trustedreviews.com/news/amazon-dash-replenishment-service-3514666"},
            {"img": "macro-2-5-grandviewresearch-livecommerce-latam.png", "cap": "Smart home appliances LATAM creciendo a doble dígito anual — la automatización del hogar llega.", "src": "GRAND VIEW RESEARCH · 2025", "url": "https://www.grandviewresearch.com/industry-analysis/latin-america-live-commerce-market-report"},
        ],
    },
    {
        "macro": 2,
        "headline": "COMPRAR EN VIVO SE VOLVIÓ EVENTO: EL LIVE SHOPPING CONVIERTE HASTA EL 30% DE QUIEN MIRA (VS 2-3% DEL E-COMMERCE) Y 64% DE LATAM ASISTE A SESIONES CADA MES.",
        "body": "El live shopping vuelve el stream un piso de venta. La oferta-relámpago, el drop cronometrado, el chat en tiempo real — todo empuja a comprar ahí mismo, empujado por escasez y comunidad. Los números de conversión son otra liga: 9-30% contra el 2-3% del e-commerce normal, y 65% de los compradores deciden en menos de 10 minutos. En LATAM 64% asiste a sesiones mensualmente.",
        "hashtags": "#liveshopping · #livecommerce · #ventaenvivo · #droplive · #tiktoklive",
        "needs": "URGENCIA · PERTENENCIA · SOLEDAD",
        "triggers": [
            {"big": "US$32B", "desc": "Live commerce LATAM: US$3.87B (2024) → US$32.08B (2033), CAGR 27.2%; Brasil +90% anual.", "src": "GRAND VIEW RESEARCH · 2025"},
            {"big": "30%", "desc": "Conversión en live shopping vs 2-3% del e-commerce convencional — 65% decide en <10 minutos.", "src": "MCKINSEY / YAVENDIO · 2025"},
            {"big": "64%", "desc": "De consumidores LATAM asiste a sesiones de live shopping mensualmente.", "src": "EAE / GRAND VIEW · 2025"},
        ],
        "signals": [
            {"img": "macro-2-5-yavendio-livecommerce-latam-stats.png", "cap": "64% de LATAM asiste a live shopping mensual; conversión hasta 30% vs. 2-3% e-commerce.", "src": "YAVENDIO · 2025", "url": "https://www.yavendio.com/en/blog/live-commerce-latam-estadisticas"},
            {"img": "macro-2-5-grandviewresearch-livecommerce-latam.png", "cap": "Live commerce LATAM: US$3.87B (2024) → US$32.08B (2033), CAGR 27.2%; Brasil +90% anual.", "src": "GRAND VIEW RESEARCH · 2025", "url": "https://www.grandviewresearch.com/industry-analysis/latin-america-live-commerce-market-report"},
            {"img": "macro-2-3-tiktok-tiktokshop-7441997574112021806.png", "cap": "Creador LATAM montando venta en TikTok — el live como tienda: descubres, deseas y pagas sin salir del scroll.", "src": "TIKTOK @CRECE.CON.LAMORE · 2025", "url": "https://www.tiktok.com/@crece.con.lamore/video/7441997574112021806"},
        ],
    },
    # ----- MACRO 3 -----
    {
        "macro": 3,
        "headline": "TIKTOK NO TE SUGIERE, TE OBLIGA: UN VIDEO AGOTA GÓNDOLAS EN DÍAS, Y SOL DE JANEIRO PASÓ DE VIRAL A +US$1B MIENTRAS LABUBU LLEGABA A US$150K EN SUBASTA.",
        "body": "El algoritmo fabrica must-haves que vacían el stock en días. Sol de Janeiro acumuló +850M de views y triplicó ventas hasta superar los US$1B. Stanley y Labubu agotaron góndolas por puro hype. El deseo no lo programa la necesidad — lo programa el feed. Aparecen los \"restock alerts\", la reventa del objeto agotado, la carrera por tener el producto que valida tu membresía a la conversación cultural del momento.",
        "hashtags": "#tiktokmademebuyit · #viralproduct · #amazonmusthaves · #soldout",
        "needs": "PERTENENCIA · ACTUALIDAD · VACÍO",
        "triggers": [
            {"big": "15%", "desc": "De consumidores globales compra solo porque algo es tendencia en TikTok.", "src": "SAP EMARSYS · 2025"},
            {"big": "+US$1B", "desc": "Sol de Janeiro: +850M views, ventas triplicadas — Labubu llegó a US$150K en subasta récord.", "src": "FREE YOURSELF / UC SAN DIEGO · 2025"},
            {"big": "Viral\nranking", "desc": "Ranking de productos TikTok más vendidos 2025 — virales que se agotan en días.", "src": "ACCIO · 2025"},
        ],
        "signals": [
            {"img": "macro-3-1-tiktok-tiktokmademebuyit-7470330136718527777.png", "cap": "#tiktokmademebuyit — el hashtag que acumula 80B de views documenta cada must-have del feed.", "src": "TIKTOK @UNIQUE21OFFICIAL · 2025", "url": "https://www.tiktok.com/@unique21official/video/7470330136718527777"},
            {"img": "macro-3-4-freeyourself-soldejaneiro-viral.png", "cap": "Sol de Janeiro: +850M views TikTok, ventas triplicadas a +US$1B — el frasco diseñado para el feed.", "src": "FREEYOURSELF · 2025", "url": "https://freeyourself.com/blogs/news/tiktok-viral-perfume-sales-stats"},
            {"img": "macro-3-1-accio-top-tiktok-products-page.png", "cap": "Ranking de productos TikTok más vendidos 2025 — el feed como árbitro del must-have.", "src": "ACCIO · 2025", "url": "https://www.accio.com/business/top-selling-tiktok-products"},
        ],
    },
    {
        "macro": 3,
        "headline": "LA SUEGRA QUE DECÍA QUÉ COMPRAR PARA LA CASA AHORA ES UNA FAMILY INFLUENCER: +60% DE LATAM LE COPIA LA DESPENSA A QUIEN LA MOSTRÓ EN CÁMARA.",
        "body": "El consejo de qué sirve para la casa venía de la familia. Ahora viene del family/home influencer. La casa compra lo que la creadora-vecina enseñó: replica su despensa, su decoración, su \"Amazon storefront\" como lista de compras. +60% de LATAM sigue a alguien que recomienda o vende productos. La autoridad de consumo doméstico migró del consejo familiar al grid.",
        "hashtags": "#homeinfluencer · #amazonstorefront · #momtok · #hometok",
        "needs": "GUÍA · PERTENENCIA · INVISIBILIDAD",
        "triggers": [
            {"big": "+60%", "desc": "De LATAM sigue influencers que recomiendan o venden productos — el grid reemplaza al consejo familiar.", "src": "LATAM INTERSECT PR · 2025"},
            {"big": "10K-100K", "desc": "Micro-influencers en el sweet spot de purchase intent; CPMs caen >50% YoY — más creadores chiquitos.", "src": "JOINSTATUS / INFLUENCER MARKETING HUB · 2025"},
            {"big": "Top 1K\nRD", "desc": "HypeTrace rastrea top 1,000 TikTok RD — influencer marketing como estrategia mainstream local.", "src": "STARNGAGE / HYPETRACE · 2025"},
        ],
        "signals": [
            {"img": "macro-3-2-tiktok-momtok-amazon-storefront-7511087614015966495.png", "cap": "\"Linked in my Amazon storefront #momtok\" — el hogar como vitrina de compra curada.", "src": "TIKTOK @__JBARSTY · 2025", "url": "https://www.tiktok.com/@__jbarsty/video/7511087614015966495"},
            {"img": "macro-3-2-latamintersect-social-ecommerce.png", "cap": "+60% de LATAM sigue influencers que recomiendan o venden productos — el grid reemplaza al consejo familiar.", "src": "LATAM INTERSECT PR · 2025", "url": "https://latamintersectpr.com/2025-e-commerce-trends-social-medias-impact-on-latin-american-consumer-behavior/"},
            {"img": "macro-3-2-hypetrace-top-tiktok-rd.png", "cap": "Top 1,000 TikTok RD — la comunidad de influencers locales que dicta el consumo doméstico dominicano.", "src": "HYPETRACE · 2025", "url": "https://hypetrace.com/top/tiktok/dominican-republic/"},
        ],
    },
    {
        "macro": 3,
        "headline": "HOY ESTATUS, MAÑANA CRINGE: EL ALGORITMO COMPRIME LA VIDA ÚTIL DEL OBJETO, Y EL STANLEY QUE REINÓ EN 2023 QUEDÓ \"OUT\" CUANDO LLEGÓ EL OWALA.",
        "body": "El feed acelera la muerte cultural del producto. Lo que volvió deseable — el Stanley — muere en meses cuando aparece el siguiente — el Owala. Labubu pasó de récord de reventa a valor caído cuando se desinfló el trend. El consumidor compra-descarta al ritmo del trend, no del uso: salen las listas \"out vs in\", el \"this is so 2024\", la reventa del hype caído. Quedarte con el objeto que ya pasó de moda en el feed se vuelve el nuevo error social.",
        "hashtags": "#outvsin · #cringe · #trendcycle · #microtrend · #hypecycle",
        "needs": "ACTUALIDAD · PERTENENCIA · MIEDO",
        "triggers": [
            {"big": "Stanley\n→ Owala", "desc": "Stanley reinó en 2023 por hype y escasez; en 2024 quedó \"out\" desplazado por Owala.", "src": "ACCIO · 2025"},
            {"big": "Labubu", "desc": "Pasó de hype récord a caída de valor de reventa al desinflarse el trend — el algoritmo crea y destruye.", "src": "GIRLS UNITED / ESSENCE · 2025"},
            {"big": "15%", "desc": "Compra puramente por tendencia — base estructural de un consumo de vida cultural corta.", "src": "SAP EMARSYS · 2025"},
        ],
        "signals": [
            {"img": "macro-3-3-girlsunited-labubu-resale-drop.png", "cap": "Labubu: de récord de reventa a valor caído al desinflarse el trend — el algoritmo crea y destruye el deseo.", "src": "GIRLS UNITED / ESSENCE · 2025", "url": "https://girlsunited.essence.com/feedback/from-labubu-to-no-buy-how-viral-trends-are-colliding-with-economic-reality/"},
            {"img": "macro-3-3-accio-stanley-owala-trendcycle.png", "cap": "El ciclo de hype: Stanley reinó en 2023, Owala lo desplazó en 2024 — el feed comprime la vida útil del objeto.", "src": "ACCIO · 2025", "url": "https://www.accio.com/business/tik-tok-trending-products"},
            {"img": "macro-3-3-tiktok-whats-next-2025-report.png", "cap": "TikTok What's Next 2025 — el reporte de tendencias que anticipa qué productos fabricará el algoritmo.", "src": "TIKTOK NEWSROOM · 2025", "url": "https://newsroom.tiktok.com/en-us/tiktok-whats-next-2025-trend-report-us"},
        ],
    },
    {
        "macro": 3,
        "headline": "EL PRODUCTO AHORA SE DISEÑA PARA GRABARSE: EL EMPAQUE CON MOMENTO ASMR Y EL UNBOXING VIRAL LLEGAN ANTES QUE LA FUNCIÓN, Y LA GRABABILIDAD ES LA NUEVA FEATURE.",
        "body": "La marca diseña empaque y producto pensando en cómo se ve en cámara. El unboxing grabable, el ASMR de apertura, el frasco \"estético\" preceden a la función. Sol de Janeiro es el caso central — un perfume que rinde como contenido antes que como producto. Los blind boxes de Labubu existen para el momento de apertura: el valor no está en el juguete, está en grabar la sorpresa. Lo grabable se volvió una feature de venta tan real como cualquier otra.",
        "hashtags": "#unboxing · #asmrunboxing · #packaging · #aesthetic · #satisfying",
        "needs": "ESPECTÁCULO · VALIDACIÓN · VACÍO",
        "triggers": [
            {"big": "850M+", "desc": "Views de Sol de Janeiro en TikTok — perfume diseñado para el feed, ventas a +US$1B.", "src": "FREE YOURSELF · 2025"},
            {"big": "#unboxing", "desc": "Y #asmr como motores de descubrimiento de producto — el packaging es el contenido.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "Labubu\nBlind Box", "desc": "Juguetes coleccionables diseñados para el unboxing viral — el valor es el momento de apertura.", "src": "ACCIO · 2025"},
        ],
        "signals": [
            {"img": "macro-3-4-tiktok-thrift-unboxing-7569567092769443094.png", "cap": "#thrift2ship — reseller que graba el empaque y envío: el packaging ES el contenido.", "src": "TIKTOK @THRIFT2SHIP1 · 2025", "url": "https://www.tiktok.com/@thrift2ship1/video/7569567092769443094"},
            {"img": "macro-3-4-freeyourself-soldejaneiro-viral.png", "cap": "Sol de Janeiro: el frasco diseñado para el feed — +850M views, ventas triplicadas a +US$1B.", "src": "FREEYOURSELF · 2025", "url": "https://freeyourself.com/blogs/news/tiktok-viral-perfume-sales-stats"},
            {"img": "macro-3-4-accio-labubu-blindbox-toy.png", "cap": "Labubu blind box — el producto cuyo valor es el momento de apertura: diseñado para ser grabado.", "src": "ACCIO · 2025", "url": "https://www.accio.com/business/tiktokhotsellingtoy"},
        ],
    },
    {
        "macro": 3,
        "headline": "COMPRAR ES CONTENIDO: EL HAUL VOLVIÓ LA COMPRA UN RITUAL DE GRABACIÓN, DONDE SE COMPRA PARA MOSTRAR EL \"QUÉ ME COMPRÉ\" Y LA AUDIENCIA MIRA, DESEA Y REPLICA.",
        "body": "El haul convirtió el acto de comprar en formato de contenido. Se compra para grabar el \"qué me compré\", no solo para usar. El \"come shopping with me\", el shopping vlog, el inventario de compras — el gasto se performa en público y se vuelve capital social. La audiencia que mira no solo observa: desea y replica. El acto privado de adquirir pasó a ser espectáculo público con vista.",
        "hashtags": "#haul · #comeshoppingwithme · #whatibought · #shoppingvlog",
        "needs": "VALIDACIÓN · PERTENENCIA · SOLEDAD",
        "triggers": [
            {"big": "#haul", "desc": "Y \"come shopping with me\" como formatos masivos de contenido-compra en TikTok.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "Gen Z", "desc": "TikTok moldea las compras de Gen Z como práctica cultural: haul, GRWM-shopping.", "src": "YR MEDIA · 2025"},
            {"big": "64%", "desc": "De LATAM asiste a live commerce mensualmente — sesiones de 25 min: comprar es entretenimiento.", "src": "GRAND VIEW / YAVENDIO · 2025"},
        ],
        "signals": [
            {"img": "macro-3-5-tiktok-haul-7558965114267782422.png", "cap": "#vintedhaul #thrifthaul — comprar para grabar: la audiencia mira, desea y replica.", "src": "TIKTOK @EVAMEGANOSOVA · 2025", "url": "https://www.tiktok.com/@evameganosova/video/7558965114267782422"},
            {"img": "macro-3-5-tiktok-haul-7552292928236915989.png", "cap": "#thrifthaul — el ritual de comprar como contenido: se documenta el proceso, no solo el botín.", "src": "TIKTOK @MR.CHIEFGRIEF9131149 · 2025", "url": "https://www.tiktok.com/@mr.chiefgrief9131149/video/7552292928236915989"},
            {"img": "macro-3-5-tiktok-haul-7556270397939780919.png", "cap": "Baby thrift haul — el haul se extiende al consumo familiar: cada compra es potencial contenido.", "src": "TIKTOK @ASHLEYKATEBURKE · 2025", "url": "https://www.tiktok.com/@ashleykateburke/video/7556270397939780919"},
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
