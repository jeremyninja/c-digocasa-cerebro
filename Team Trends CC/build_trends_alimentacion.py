#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Trends Alimentacion - Forecast Deck (18 slides)
Layout: 3 dividers macro + 15 micros (5 por macro)
Canvas 13.333 x 7.5 in
DS: headline 42-50pt Instrument Serif UPPERCASE, hashtags 23pt Instrument Serif,
    triggers vertical (stat grande + caja 170x35pt al lado), senales 149x220pt + caja caption 170x35pt al lado
Placeholders: #222222 fill, texto "CAPTURA MANUAL — JEREMY" 8pt Poppins Bold #666666
"""
import os
import math
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

# -- Paths ---------------------------------------------------------------------
BASE  = "/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC"
SHOTS = os.path.join(BASE, "screenshots/trends-alimentacion")
OUT   = os.path.join(BASE, "outputs/trends-alimentacion-forecast.pptx")

# -- Colors --------------------------------------------------------------------
BG         = RGBColor(0x0D, 0x0D, 0x0D)
PLACEHOLDER_BG = RGBColor(0x22, 0x22, 0x22)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
GREY_LABEL = RGBColor(0xA0, 0xA0, 0xA0)
GREY_MUTED = RGBColor(0x66, 0x66, 0x66)
ACCENT     = RGBColor(0xFF, 0x2D, 0x2D)
TAB_BG     = RGBColor(0xE8, 0xE8, 0xE8)
BLACK_CLR  = RGBColor(0x00, 0x00, 0x00)

FONT_SERIF = "Instrument Serif"
FONT_SANS  = "Poppins"

# -- Slide dimensions ----------------------------------------------------------
W = Inches(13.333)
H = Inches(7.5)

# -- XML helpers ---------------------------------------------------------------

def _set_shape_alpha(shape, pct):
    """Set fill alpha on a solid-filled shape via XML (pct = 0-100)."""
    spPr = shape._element.spPr
    ns = 'http://schemas.openxmlformats.org/drawingml/2006/main'
    solidFill = spPr.find(f'{{{ns}}}solidFill')
    if solidFill is None:
        return
    srgbClr = solidFill.find(f'{{{ns}}}srgbClr')
    if srgbClr is not None:
        alpha_val = int(pct / 100 * 100000)
        alpha_el = etree.SubElement(srgbClr, f'{{{ns}}}alpha')
        alpha_el.set('val', str(alpha_val))


def _set_line_spacing(paragraph, spacing):
    """Set paragraph line spacing (1.0 = single, 0.95 = tight)."""
    pPr = paragraph._p.get_or_add_pPr()
    lnSpc = etree.SubElement(pPr, qn('a:lnSpc'))
    spcPct = etree.SubElement(lnSpc, qn('a:spcPct'))
    spcPct.set('val', str(int(spacing * 100000)))


# -- Low-level builders --------------------------------------------------------

def add_bg(slide):
    bg = slide.shapes.add_shape(1, 0, 0, W, H)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG
    bg.line.fill.background()
    return bg


def add_textbox(slide, x, y, w, h, text, font_name, font_size, color,
                bold=False, italic=False, align=PP_ALIGN.LEFT,
                line_spacing=None, word_wrap=True):
    txBox = slide.shapes.add_textbox(x, y, w, h)
    tf = txBox.text_frame
    tf.word_wrap = word_wrap
    tf.auto_size = None
    p = tf.paragraphs[0]
    p.alignment = align
    if line_spacing is not None:
        _set_line_spacing(p, line_spacing)
    run = p.add_run()
    run.text = text
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    return txBox


def add_separator_h(slide, x, y, w):
    """1px horizontal separator at 6% white opacity."""
    line = slide.shapes.add_shape(1, x, y, w, Emu(9525))
    line.fill.solid()
    line.fill.fore_color.rgb = WHITE
    line.line.fill.background()
    _set_shape_alpha(line, 6)
    return line


def add_separator_v(slide, x, y, h):
    """1px vertical separator at 6% white opacity."""
    line = slide.shapes.add_shape(1, x, y, Emu(9525), h)
    line.fill.solid()
    line.fill.fore_color.rgb = WHITE
    line.line.fill.background()
    _set_shape_alpha(line, 6)
    return line


def add_image_hyperlink(slide, img_path, x, y, w, h, url):
    """Insert image at exact w×h with hyperlink."""
    pic = slide.shapes.add_picture(img_path, x, y, w, h)
    if url:
        rId = slide.part.relate_to(
            url,
            'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',
            is_external=True)
        hlinkClick = etree.SubElement(pic._element.nvPicPr.cNvPr, qn('a:hlinkClick'))
        hlinkClick.set(qn('r:id'), rId)
    return pic


def add_placeholder(slide, x, y, w, h, url):
    """#222222 placeholder with text + hyperlink."""
    rect = slide.shapes.add_shape(1, x, y, w, h)
    rect.fill.solid()
    rect.fill.fore_color.rgb = PLACEHOLDER_BG
    rect.line.color.rgb = WHITE
    rect.line.width = Emu(9525)
    tf = rect.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = "CAPTURA MANUAL\n— JEREMY"
    run.font.name = FONT_SANS
    run.font.size = Pt(8)
    run.font.bold = True
    run.font.color.rgb = GREY_MUTED
    if url:
        rId = slide.part.relate_to(
            url,
            'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',
            is_external=True)
        cNvPr = rect._element.nvSpPr.cNvPr
        hlinkClick = etree.SubElement(cNvPr, qn('a:hlinkClick'))
        hlinkClick.set(qn('r:id'), rId)
    return rect


def add_click_me_badge(slide, img_x, img_y, img_w):
    """Red 'CLICK ME' badge at top-right of image."""
    bw = Inches(0.55)
    bh = Inches(0.18)
    bx = img_x + img_w - bw
    by = img_y
    badge = slide.shapes.add_shape(1, bx, by, bw, bh)
    badge.fill.solid()
    badge.fill.fore_color.rgb = ACCENT
    badge.line.fill.background()
    tf = badge.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = "CLICK ME"
    run.font.name = FONT_SANS
    run.font.size = Pt(7)
    run.font.bold = True
    run.font.color.rgb = WHITE
    return badge


# -- Content data --------------------------------------------------------------

MACROS = [
    {
        "num": "MACRO 1",
        "name": "INVENTOLOGÍA DE LA ADULTEZ",
        "tagline": '"Un mundo en crisis está reescribiendo qué significa ser adulto y formar familia."',
    },
    {
        "num": "MACRO 2",
        "name": "LOS HERNÁNDEZ ARE PROMPTED",
        "tagline": '"El dominicano ya entró al mundo prompteado. Solo no lo nombra así."',
    },
    {
        "num": "MACRO 3",
        "name": "ALGORITMO DEL HOGAR",
        "tagline": '"El feed se sentó en la mesa y nadie le ofreció silla."',
    },
]

# trigger: {stat, desc, fuente}
# senal:   {img, url, caption}   — img=None → placeholder

MICROS = [
    # -------------------------------------------------------------------------
    # MACRO 1
    # -------------------------------------------------------------------------
    {
        "macro_num":  "MACRO 1",
        "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "headline":   "La generación sin tiempo entre semana descubrió que dos horas el domingo le devuelven la semana entera.",
        "fenomeno":   "El joven dominicano prepara comidas el domingo para ahorrar tiempo, comer mejor y controlar lo que ingiere. No es dieta — es autonomía. El meal prep entra como ritual de adultez sin mamá-cocinera detrás. Domingo 5pm: tuppers, arroz integral, pechuga, etiqueta con día de la semana.",
        "hashtags":   "#MealPrepDominicano · #DomingoDePrep · #ControlDeLoQueComo · #AdultoJovenRD",
        "triggers": [
            {"stat": "US$36B",  "desc": "mercado global de meal prep en 2026, CAGR 9.84% hasta 2035.", "fuente": "MARKET REPORTS WORLD · 2026"},
            {"stat": "48%",     "desc": "de adultos ya practica meal prep; 62% de profesionales >8h/día cita falta de tiempo como driver.", "fuente": "HELLOFRESH STATE OF HOME COOKING · 2025"},
            {"stat": "62%",     "desc": "de profesionales que trabajan más de 8 h/día elige meal prep como solución al tiempo.", "fuente": "HELLOFRESH · 2025"},
        ],
        "senales": [
            {"img": "macro-1-1-tiktok-morechulaa-mealprep.png",    "url": "https://www.tiktok.com/@morechulaa/video/7636986702262717704",    "caption": "Creadora dominicana @morechulaa: meal prep de 4 días con tuppers etiquetados por día."},
            {"img": "macro-1-1-tiktok-viviankh-mealprep.png",      "url": "https://www.tiktok.com/@viviank.h/video/7620501104765177108",      "caption": "@viviank.h documenta 10 sándwiches + 9 porciones en el freezer — meal prep de 3 semanas."},
            {"img": "macro-1-0-mktreports-mealprep-market.png",    "url": "https://www.marketreportsworld.com/market-reports/meal-prep-market-14713709", "caption": "Chart: mercado global meal prep US$36,433M en 2026, CAGR 9.84%."},
        ],
    },
    {
        "macro_num":  "MACRO 1",
        "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "headline":   "Las empresas descubrieron que si el empleado come bien al mediodía rinde mejor en la tarde — y el menú de almuerzo se volvió beneficio.",
        "fenomeno":   "Fripick deja que la empresa pague la comida y la descuente en quincena; los restaurantes RD lanzan lunch menus de 12-3 a precio asequible. La comida del mediodía dejó de ser problema individual del empleado — ahora es categoría B2B.",
        "hashtags":   "#LunchMenuRD · #AlmuerzoDeTrabajo · #MenúDelDía · #PrecioAccesible · #NegocioOyó",
        "triggers": [
            {"stat": "+13%",    "desc": "YoY de tráfico en horario almuerzo con shoulder hour pricing en LATAM.", "fuente": "OPENTABLE / QSR MAGAZINE · 2025"},
            {"stat": "84%",     "desc": "de consumidores percibe los precios de alimentos como altos; dos tercios prefieren opciones más económicas para almuerzo.", "fuente": "PURDUE UNIVERSITY / FAMILY DINNER PROJECT · 2025"},
            {"stat": "8.03%",   "desc": "inflación alimentaria interanual RD enero 2026; precios subieron 50% vs julio 2019.", "fuente": "BCRD / DOMINICAN TODAY · 2026"},
        ],
        "senales": [
            {"img": "macro-1-2-tiktok-toyantoja-noccila-lunch.png", "url": "https://www.tiktok.com/@toyantoja/video/7610215257000234247", "caption": "@toyantoja muestra lunch completo en Nocciola por menos de RD$500 — dato que vale oro para el trabajador."},
            {"img": "macro-1-2-fripick-rd-brand.png",               "url": "https://fripick.com",                                          "caption": "Fripick RD — beneficio alimentario corporativo B2B con descuento de quincena."},
            {"img": None,                                            "url": "https://www.bcrd.gov.do",                                      "caption": "BCRD: inflación alimentaria 8.03% interanual ene 2026; precios +50% vs 2019."},
        ],
    },
    {
        "macro_num":  "MACRO 1",
        "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "headline":   "Te crió con miedo a lo «malo» y ahora comer se siente como culpa. TikTok escuchó el término y lo convirtió en trend con millones de views.",
        "fenomeno":   "La mamá que controlaba cada bocado crió hijas con relación rota con el plato. La almond mom no es solo un meme — es una cadena generacional. La adultez de esa hija inventa otra forma de comer sin que la voz de mamá comente cada mordida.",
        "hashtags":   "#AlmondMom · #TraumasDietéticos · #ComerConCulpa · #GeneraciónSinRefresco · #LaVozDeMamá",
        "triggers": [
            {"stat": "30M",     "desc": "americanos desarrollarán un trastorno alimentario en su vida — 2da enfermedad mental más mortal.", "fuente": "ANAD / ABC NEWS · 2025"},
            {"stat": "42%",     "desc": "de niñas de 1°-3° quiere ser más delgada; 81% de niños de 10 años teme engordar.", "fuente": "ANAD STATISTICS · 2025"},
            {"stat": "#AlmondMom", "desc": "circula como documento generacional del trauma dietético heredado — millones de views en TikTok/YouTube.", "fuente": "TIKTOK · 2025"},
        ],
        "senales": [
            {"img": "macro-1-3-tiktok-lielle-almondmom.png",   "url": "https://www.tiktok.com/@liellewaldman17/video/7617943870797630750", "caption": "@Lielle & Dee recrea rutina matutina bajo #almondmom — suplementos, restricción, herencia sin cuestionar."},
            {"img": "macro-1-3-tiktok-nourvilaa-almondmom.png", "url": "https://www.tiktok.com/@nourvilaa/video/7642383470026657046",    "caption": "@nour vilà — versión LATAM del trauma dietético bajo #almondmum."},
            {"img": None,                                        "url": "https://anad.org/eating-disorder-statistics/",                     "caption": "ANAD 2025: 73% de pacientes con trastorno usaba MyFitnessPal y cree que contribuyó."},
        ],
    },
    {
        "macro_num":  "MACRO 1",
        "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "headline":   "La diferencia entre un domingo con familia y uno solo se mide en una pregunta: ¿qué vamos a comer?",
        "fenomeno":   "Para familias grandes el domingo es sancocho, mesa llena, todos. Para el foráneo que vive solo, es el día más difícil — sin ritual, sin mesa, con delivery en la cama. La brecha no es nutricional — es emocional.",
        "hashtags":   "#DomingoSolo · #AlmuerzoDeFamilia · #SancochoDelDomingo · #ForáneoEnLaCapital · #SinMesaNoHayDomingo",
        "triggers": [
            {"stat": "45%",     "desc": "de hogares come junto menos que hace una década; 84% querría más comidas compartidas.", "fuente": "SIMIRITY / FMI FOUNDATION · 2025"},
            {"stat": "17%",     "desc": "de familias dominicanas no comparte las horas de comida — el foráneo en Bonao en su cuartito de Naco.", "fuente": "CÓDIGO CASA N=500 · NINJA · 2025"},
            {"stat": "WHR 2025", "desc": "World Happiness Report vincula compartir comidas con conectividad social y bienestar subjetivo.", "fuente": "WORLD HAPPINESS REPORT · 2025"},
        ],
        "senales": [
            {"img": "macro-1-4-tiktok-josheilyn-foranea-capital.png",  "url": "https://www.tiktok.com/@josheilyndls1/video/7549991019169811768",  "caption": "@Josheilyn — foránea RD en la capital: \"yo amo estar en mi hogar los domingos\"."},
            {"img": "macro-1-4-tiktok-mariannycorderoo-domingo.png",   "url": "https://www.tiktok.com/@mariannycorderoo/video/7643570804885572882", "caption": "@mariannycorderoo — domingo solo en Bogotá con #amorpropio, ritual sin mesa familiar."},
            {"img": "macro-1-4-tiktok-macaseason-domingo-familiar.png","url": "https://www.tiktok.com/@macaseason/video/7625031259835665685",      "caption": "@macaseason — el ritual completo del domingo familiar como contraste."},
        ],
    },
    {
        "macro_num":  "MACRO 1",
        "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "headline":   "PedidosYa es la app #1 de food en RD: el adulto joven ya no decide qué cocinar entre semana, decide qué pedir — y esa es su nueva forma de ser adulto.",
        "fenomeno":   "La adultez tradicional cocinaba todos los días. La adultez 2026 delega el jueves a una app. No es flojera — es renegociación del rol de buen adulto en una economía donde el tiempo cuesta más que la comida.",
        "hashtags":   "#PedidosYaRD · #DeliveryEsMiMamá · #AdultoQueNoCocina · #JuevesDeApp · #ComerSinCocinar",
        "triggers": [
            {"stat": "#1 RD",   "desc": "PedidosYa, app #1 food & drink iOS en RD; 13K-21.7K descargas semanales Q1 2025.", "fuente": "SENSOR TOWER · Q1 2025"},
            {"stat": "50%",     "desc": "subieron los precios de alimentos en RD entre julio 2019 y julio 2025 — el delivery se vuelve cálculo costo-tiempo.", "fuente": "BCRD / DOMINICAN TODAY · 2026"},
            {"stat": "1er",     "desc": "supermercado 100% online abre en Santo Domingo — la grocería migra a app.", "fuente": "ST KITTS NEVIS OBSERVER · 2025"},
        ],
        "senales": [
            {"img": "macro-1-5-pedidosya-country-selector.png",      "url": "https://www.pedidosya.com",                                                                               "caption": "Selector de país PedidosYa con República Dominicana listada + badges App Store y Google Play."},
            {"img": "macro-1-5-sensortower-pedidosya-rd-chart.png",  "url": "https://sensortower.com/blog/2025-q1-unified-top-5-food%20delivery%20services-units-do-63da96fbe1714cfff1c1e5a1", "caption": "Sensor Tower: PedidosYa #1 en descargas food delivery RD, Q1 2025."},
            {"img": "macro-1-5-stkitts-online-super-sd.png",         "url": "https://www.thestkittsnevisobserver.com/first-online-only-supermarket-opens-in-santo-domingo/",          "caption": "Primer supermercado 100% online en Santo Domingo — la grocería migra a app."},
        ],
    },
    # -------------------------------------------------------------------------
    # MACRO 2
    # -------------------------------------------------------------------------
    {
        "macro_num":  "MACRO 2",
        "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "headline":   "Una foto de tu plato no sabe lo que comes. Pero el algoritmo te convence de que sí — y le crees más a la app que a tu propio cuerpo.",
        "fenomeno":   "Las apps de conteo calórico pasaron de herramienta a obsesión. El algoritmo que te ayuda a comer mejor se convierte en la voz que condena cada nutriente. Foto del plato → IA reconoce → 487 kcal → silencio incómodo → no almorzar postre.",
        "hashtags":   "#AppQueEnfermó · #MyFitnessPalToxic · #AlgoritmoDeMiDieta · #ContarCalorías · #ComerConMiedo",
        "triggers": [
            {"stat": "180M",    "desc": "usuarios de MyFitnessPal; 75% de pacientes con trastorno alimentario la usaba.", "fuente": "GRIPROOM / PMC NLM · 2026"},
            {"stat": "73%",     "desc": "de pacientes con trastorno alimentario creyó que la app contribuyó al desarrollo del trastorno.", "fuente": "PMC NLM · 2026"},
            {"stat": "#MFPToxic", "desc": "creadoras documentan recuperación de relación rota con apps de conteo calórico.", "fuente": "TIKTOK · 2025"},
        ],
        "senales": [
            {"img": "macro-2-1-myfitnesspal-app-ui.png", "url": "https://www.myfitnesspal.com", "caption": "UI de MyFitnessPal: 976 cal + macro breakdown del día — \"Nutrition tracking for real life\"."},
            {"img": None,                                 "url": "https://griproom.com",          "caption": "GripRoom / PMC NLM 2026: 73% de pacientes cree que la app contribuyó al trastorno alimentario."},
            {"img": None,                                 "url": "https://pubmed.ncbi.nlm.nih.gov", "caption": "Ohio State / Sage Journals: apps con IA foto actúan como gateway a trastorno alimentario."},
        ],
    },
    {
        "macro_num":  "MACRO 2",
        "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "headline":   "Antes mamá decidía qué había de comer. Hoy lo decide el For You Page — y de paso te vende los ingredientes en el mismo scroll.",
        "fenomeno":   "El joven dominicano abre TikTok antes de abrir el refrigerador. Las recetas virales compiten con la tradición oral heredada — y en muchos hogares jóvenes el algoritmo está ganando.",
        "hashtags":   "#TikTokRecetas · #ForYouPageDeCocina · #RecetaViralVsAbuela · #QuéComiHoy · #AlgoritmoDeAlmuerzo",
        "triggers": [
            {"stat": "42",      "desc": "índice de contenido food en TikTok en pico enero 2026 — la plataforma como primer recetario.", "fuente": "ACCIO / TIKTOK FOOD TRENDS · 2026"},
            {"stat": "US$759M", "desc": "GMV food en TikTok Shop 2025 — integración receta → carrito en la misma plataforma.", "fuente": "CAPITAL ONE SHOPPING · 2025"},
            {"stat": "2x",      "desc": "casi duplicaron ventas las marcas grandes en TikTok Shop en 2025.", "fuente": "MODERN RETAIL · 2025"},
        ],
        "senales": [
            {"img": "macro-2-2-tiktokshop-food-gmv.png",          "url": "https://resourcera.com/data/social/tiktok-shop-statistics/",                                                      "caption": "TikTok es el nuevo libro de recetas Y el nuevo supermercado — food = 13.6% del GMV 2025."},
            {"img": "macro-2-2-modernretail-tiktokshop-brands.png","url": "https://www.modernretail.co/technology/sales-from-major-brands-on-tiktok-shop-nearly-doubled-in-2025-drawing-ulta-and-sally-beauty/", "caption": "Modern Retail: marcas grandes casi duplicaron ventas en TikTok Shop en 2025."},
            {"img": None,                                           "url": "https://finedininglovers.com",                                                                                   "caption": "Fine Dining Lovers ES: creadores latinos llevan recetas tradicionales a los códigos narrativos de 2025."},
        ],
    },
    {
        "macro_num":  "MACRO 2",
        "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "headline":   "El truco de poner un video para que el niño coma se convirtió en condición — el iPad es la única forma de que el plato baje.",
        "fenomeno":   "El niño no come sin el iPad. La pantalla dejó de ser acompañamiento y se volvió condición. La mesa familiar tiene un competidor que casi siempre gana: Cocomelon en iPad apoyado en jugo de naranja; niño come pollo en piloto automático.",
        "hashtags":   "#iPadKid · #PantallaMientrasCome · #NetflixYCena · #MesaSinPantalla · #ComerSinPantalla",
        "triggers": [
            {"stat": "40%",     "desc": "de niños tiene iPad a los 2 años; 2.6 hrs/día promedio; solo 1% cumple límites recomendados.", "fuente": "COMMON SENSE MEDIA · 2025"},
            {"stat": "2.6h",    "desc": "promedio de pantalla diaria en menores de 8 años; vínculo con desconexión de señales de hambre.", "fuente": "SCIENCEDIRECT / BUSINESS STANDARD · 2026"},
            {"stat": "17%",     "desc": "de familias RD no comparte las horas de comida — la mesa está compartida, con un tercero encendido.", "fuente": "CÓDIGO CASA N=500 · NINJA · 2025"},
        ],
        "senales": [
            {"img": "macro-2-3-newsmedical-screentime-proxy.png", "url": "https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx", "caption": "News Medical: la tech que interviene en cómo comemos (proxy visual de medicalización del comer)."},
            {"img": None,                                          "url": "https://www.unicef.org/innocenti/reports/children-and-digital-technologies",                               "caption": "UNICEF Kids Online: exposición infantil a pantallas más temprana y menos mediada en LATAM/RD."},
            {"img": None,                                          "url": "https://www.commonsensemedia.org/research/zero-to-eight-childrens-media-use-in-america",                  "caption": "Common Sense Media 2025: 40% de niños tiene iPad a los 2 años; 1% cumple límites."},
        ],
    },
    {
        "macro_num":  "MACRO 2",
        "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "headline":   "El consumidor sano se pega un sensor de glucosa por dos semanas y descubre que la uva le sube más el azúcar que el helado. La nutrición ya es dato en tiempo real.",
        "fenomeno":   "Los wearables de glucosa OTC salieron del nicho diabético y entraron al consumer health. El comer bien dejó de ser opinión — ahora es métrica continua que cambia qué desayunas mañana.",
        "hashtags":   "#LingoRD · #SensorDeGlucosa · #ComerConDato · #MetabolicAge · #ElPlatoYElGráfico",
        "triggers": [
            {"stat": "US$80B",  "desc": "generó el mercado de wearables y health tracking en 2024 — proyecta US$200B+ para 2030.", "fuente": "STATISTA · 2025"},
            {"stat": "OTC",     "desc": "Abbott Lingo (CGM sin prescripción) expande a Android dic 2025; en Walmart y Amazon.", "fuente": "ABBOTT NEWSROOM · 2025"},
            {"stat": "\"Glucose Goddess\"", "desc": "#glucosegoddess (Jessie Inchauspé) cruza cientos de millones de views — glucose hacks como género.", "fuente": "TIKTOK · 2025"},
        ],
        "senales": [
            {"img": "macro-2-4-hellolingo-cgm-hero.png",    "url": "https://www.hellolingo.com",                                                                                     "caption": "Abbott Lingo: mujer con sensor en el brazo + \"My glucose, my insights\" — CGM OTC sin prescripción."},
            {"img": "macro-2-4-scripps-cgm-sensor-arm.png", "url": "https://www.scrippsnews.com/health/continuous-glucose-monitors-are-in-vogue-but-do-you-really-need-to-track-your-blood-sugar", "caption": "Scripps News / AP: brazo con sensor de glucosa continuo — CGMs in vogue para consumidor no-diabético."},
            {"img": None,                                    "url": "https://www.statista.com/topics/1236/wearable-technology/",                                                       "caption": "Statista 2025: mercado wearables US$80B en 2024, rumbo a US$200B en 2030."},
        ],
    },
    {
        "macro_num":  "MACRO 2",
        "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "headline":   "Una creadora cocina en vivo, te muestra el producto, lo agregas al carrito sin salir del feed. El supermercado se volvió streaming.",
        "fenomeno":   "Live shopping pasó del nicho beauty al supermercado: snacks, salsas, kits de receta vendidos durante el video. Food es 13.6% del GMV de TikTok Shop. El próximo carrito de compras será un live stream — no un walk-in.",
        "hashtags":   "#TikTokShopFood · #CocinaEnVivo · #CarritoDelFeed · #LiveSnacks · #CompraLoQueCocinas",
        "triggers": [
            {"stat": "US$64B",  "desc": "GMV total TikTok Shop 2025; food US$759.84M (13.6%); ticket promedio food shopper US$43.20.", "fuente": "CAPITAL ONE SHOPPING / RESOURCERA · 2025"},
            {"stat": "+84%",    "desc": "creció el live shopping YoY en 2025; conversión live 6.1% vs feed 4.7%.", "fuente": "RESOURCERA · 2026"},
            {"stat": "1er",     "desc": "supermercado 100% online abre en Santo Domingo — grocery digital prepara terreno para social commerce en RD.", "fuente": "ST KITTS NEVIS OBSERVER · 2025"},
        ],
        "senales": [
            {"img": "macro-2-5-modernretail-tiktokshop-2025.png",   "url": "https://www.modernretail.co/technology/sales-from-major-brands-on-tiktok-shop-nearly-doubled-in-2025-drawing-ulta-and-sally-beauty/", "caption": "Modern Retail TikTok Shop: marcas grandes duplicaron ventas en 2025; food = categoría líder."},
            {"img": "macro-2-5-resourcera-tiktokshop-stats.png",    "url": "https://resourcera.com/data/social/tiktok-shop-statistics/",                                                     "caption": "Resourcera: GMV US$64.3B, ticket food US$43.20, live shopping +84% YoY."},
            {"img": "macro-1-5-stkitts-online-super-sd.png",        "url": "https://www.thestkittsnevisobserver.com/first-online-only-supermarket-opens-in-santo-domingo/",               "caption": "Primer super online SD — grocery 100% digital en RD (señal local de social commerce)."},
        ],
    },
    # -------------------------------------------------------------------------
    # MACRO 3
    # -------------------------------------------------------------------------
    {
        "macro_num":  "MACRO 3",
        "macro_name": "ALGORITMO DEL HOGAR",
        "headline":   "Ver lo que otros comen se convirtió en uno de los formatos más consumidos de internet. Ya no es comida — es identidad.",
        "fenomeno":   "What I Eat in a Day explota no por curiosidad culinaria — por validación. Ver lo que come otro para confirmar, comparar o inspirarse. En RD ya hay creadoras adoptándolo con identidad local. El plato ajeno es espejo. Y juez.",
        "hashtags":   "#QuéComoEnUnDía · #WhatIEatInADay · #ComidaParaVer · #AlimentaciónEnPantalla · #DíaDeComidaRD",
        "triggers": [
            {"stat": "74%",     "desc": "de personas usa redes para decidir qué/dónde comer; 50% dice que influyen directamente.", "fuente": "CROPINK · 2026"},
            {"stat": "Top 2026","desc": "\"What I Eat in a Day\" entre top food trends; genera engagement positivo y negativo que el algoritmo premia.", "fuente": "CHOWHOUND TIKTOK TRENDS · 2026"},
            {"stat": "Bowl",    "desc": "colorido aspiracional de Whole Foods 2026 que WIEIAD replica y el algoritmo distribuye como estándar.", "fuente": "VEGNEWS / WHOLE FOODS · 2026"},
        ],
        "senales": [
            {"img": "macro-3-1-vegnews-food-trend-hero.png", "url": "https://vegnews.com/fiber-whole-foods-2026-top-trend",  "caption": "VegNews 2026: bowl de proteína + grains + vegetales coloridos — el comer bien aspiracional que WIEIAD replica."},
            {"img": None,                                     "url": "https://www.tiktok.com/search?q=que+como+en+un+dia+dominicana", "caption": "Búsqueda TikTok: adaptación local de WIEIAD con mangú, sancocho y dieta de barrio."},
            {"img": None,                                     "url": "https://cropink.com/tiktok-statistics",                  "caption": "Cropink 2026: 74% usa redes para decidir qué comer; 50% afirma influencia directa."},
        ],
    },
    {
        "macro_num":  "MACRO 3",
        "macro_name": "ALGORITMO DEL HOGAR",
        "headline":   "El mukbang nació porque hay gente que come sola y prefiere ver a alguien comer antes que comer en silencio.",
        "fenomeno":   "Nació en Corea como compañía virtual. Hoy es negocio millonario. El dominicano lo consume porque la mesa vacía duele — y una pantalla llena el silencio del comedor. La cena ya viene con co-cenador incluido. En pantalla.",
        "hashtags":   "#MukbangLatino · #ComerSoloPeroNoTanto · #AcompañamientoPorPantalla · #SoledadEnLaMesa · #CenarConPantalla",
        "triggers": [
            {"stat": "5.3M",    "desc": "#mukbang supera 5.3M videos en 2025; top creadores ganan hasta US$10K/mes.", "fuente": "DISTRACTION MAGAZINE / PMC · 2025"},
            {"stat": "68.5%",   "desc": "de jóvenes universitarias ve videos de comida regularmente; hasta 40 min/día — efecto parasocial en soledad.", "fuente": "WESTERN GAZETTE / PMC · 2025"},
            {"stat": ">2B",     "desc": "vistas de Nickocado Avocado en YouTube — mukbang como formato mainstream de entretenimiento.", "fuente": "PMC / DISTRACTION MAGAZINE · 2025"},
        ],
        "senales": [
            {"img": "macro-3-2-youtube-mukbang-search-grid.png", "url": "https://www.youtube.com/results?search_query=mukbang", "caption": "YouTube mukbang: thumbnails de comida extrema + ASMR con millones de vistas — volumen del formato."},
            {"img": None,                                          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10010030/",  "caption": "PMC 2025: 68.5% de jóvenes ve videos de comida regularmente; vínculo con efecto parasocial y soledad."},
            {"img": None,                                          "url": "https://distractionmagazine.com",                         "caption": "Distraction Magazine: top mukbangers ganan hasta US$10K/mes — formato masivo de acompañamiento virtual."},
        ],
    },
    {
        "macro_num":  "MACRO 3",
        "macro_name": "ALGORITMO DEL HOGAR",
        "headline":   "Cuando todo lo demás está fuera de control, la cocina es el único sitio donde lo que hago sí sale como quiero.",
        "fenomeno":   "Bajo burnout y presión social, adultos jóvenes descubrieron que cocinar y hornear son terapia real. No es hobbyismo — es el único espacio donde lo que controlas eres tú. El horno escucha mejor que el psicólogo en lista de espera.",
        "hashtags":   "#CocinaComoTerapia · #HornearParaDesestresarse · #LoveLanguageCocina · #Repostería · #CocinaQueControlo",
        "triggers": [
            {"stat": "Dopamina", "desc": "Hornear activa rutas de dopamina y reduce cortisol — equivalente a mindfulness clínico.", "fuente": "KAISER PERMANENTE / NEUROLAUNCH / ICE · 2025"},
            {"stat": "2026",    "desc": "ola de cancelaciones de delivery + vuelta a la cocina como anti-ansiedad digital documentada.", "fuente": "EDITORIALGE / COOKING AS THERAPY · 2026"},
            {"stat": "85%",     "desc": "dominicanos come siempre en casa (P21, CC) — para el joven 2026 cocinar es la única hora sin notificaciones.", "fuente": "CÓDIGO CASA N=500 · NINJA · 2025"},
        ],
        "senales": [
            {"img": "macro-3-3-newsmedical-cooking-proxy.png", "url": "https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx", "caption": "News Medical: la cocina como contrapunto analógico a la farmacología del hambre (GLP-1)."},
            {"img": None,                                       "url": "https://www.tiktok.com/search?q=%23cookingastherapy",                                                      "caption": "#cookingastherapy en TikTok — creadoras LATAM documentan cocina y repostería como bienestar."},
            {"img": None,                                       "url": "https://www.neurolaunch.com/baking-and-mental-health/",                                                    "caption": "NeuroLaunch: hornear reduce cortisol, activa dopamina — equivalente a mindfulness según evidencia clínica."},
        ],
    },
    {
        "macro_num":  "MACRO 3",
        "macro_name": "ALGORITMO DEL HOGAR",
        "headline":   "El FOMO de bajar de peso llegó a su versión más extrema: eliminar todo lo que no sea animal. Los análisis de sangre cuentan otra historia.",
        "fenomeno":   "Joe Rogan lo popularizó, los influencers lo viralizaron, el que lleva años sin bajar de peso lo consideró. Solo carne, mantequilla y huevo. El algoritmo lo distribuye más rápido que la evidencia clínica que lo contradice.",
        "hashtags":   "#DietaCarnívora · #SoloCarneMantequillaYHuevo · #FOMODeBajarDePeso · #ExtremoNutricional · #CarnivoreVsColesterol",
        "triggers": [
            {"stat": "2.6M",    "desc": "#carnivore supera 2.6M publicaciones a noviembre 2025 — entre las dietas más comentadas.", "fuente": "RESEARCHGATE / FOX NEWS · 2025"},
            {"stat": "LDL +46", "desc": "LDL promedio sube de 126 a 172 mg/dL en seguidores de dieta carnívora — caso reportado: 163→365.", "fuente": "NUTRIENTS JOURNAL · ENE 2026"},
            {"stat": "Fibra 2026", "desc": "Whole Foods predice 2026 = Year of the Fiber — mainstream pivota al opuesto mientras carnivore escala.", "fuente": "VEGNEWS / WHOLE FOODS 2026 TREND REPORT · 2026"},
        ],
        "senales": [
            {"img": "macro-3-4-vegnews-protein-fiber-trend.png", "url": "https://vegnews.com/fiber-whole-foods-2026-top-trend",                           "caption": "VegNews: mainstream pivota a fibra mientras carnivore escala — bowl colorido vs tabla de bistec."},
            {"img": None,                                          "url": "https://www.mdpi.com/2072-6643/18/2/247",                                        "caption": "Nutrients Journal ene 2026: LDL promedio sube 126→172 mg/dL en seguidores de dieta carnívora."},
            {"img": None,                                          "url": "https://www.tiktok.com/search?q=ex+carnivore+my+labs",                          "caption": "TikTok: \"ex-carnivore my labs\" — backlash de creadores que salen de la dieta carnívora por análisis."},
        ],
    },
    {
        "macro_num":  "MACRO 3",
        "macro_name": "ALGORITMO DEL HOGAR",
        "headline":   "GLP-1 silencia el «food noise» del cerebro. La nueva conversación sobre comer no es qué cocinar — es si lo deseo o solo me acordé que existía.",
        "fenomeno":   "Ozempic y Mounjaro reescriben la relación con la comida: ya no se trata de fuerza de voluntad, se trata de farmacología que apaga el ruido mental. El feed normaliza la conversación; el endocrinólogo no está en el loop.",
        "hashtags":   "#FoodNoise · #OzempicDiary · #SinHambreSinAnsiedad · #GLP1RD · #LaCabezaSinComida",
        "triggers": [
            {"stat": "58%",     "desc": "siente menos hambre con GLP-1; 64% se llena antes; 21-23% reporta cambios de sabor — EASD 2025 n=411.", "fuente": "EASD 2025 / NEWS-MEDICAL · 2025"},
            {"stat": "#FoodNoise", "desc": "viralizado por usuarias de GLP-1 documentando cambio cognitivo — decenas de millones de views en 2025.", "fuente": "TIKTOK · 2025"},
            {"stat": "Fibra vs GLP-1", "desc": "Whole Foods 2026: longevity y fibra como aspiracional opuesto al cuerpo medicado — dos lados del mismo deseo.", "fuente": "WHOLE FOODS 2026 · 2026"},
        ],
        "senales": [
            {"img": "macro-3-5-sciam-ozempic-food-noise.png",     "url": "https://www.scientificamerican.com/article/ozempic-quiets-food-noise-in-the-brain-but-how/", "caption": "Scientific American: cabeza de estatua con comida flotando — Ozempic silencia el food noise en el cerebro."},
            {"img": "macro-3-5-newsmedical-glp1-appetite.png",    "url": "https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx", "caption": "News Medical: jeringa de semaglutide — 58% menos hambre, 64% saciedad precoz según EASD 2025."},
            {"img": None,                                           "url": "https://www.tiktok.com/search?q=%23foodnoise",                                              "caption": "#foodnoise TikTok — usuarias GLP-1 documentando cambio cognitivo, decenas de millones de views."},
        ],
    },
]


# -- Slide builders ------------------------------------------------------------

def build_macro_divider(prs, macro):
    """Macro divider slide — solo nombre 100pt + tagline 24pt italic. Sin info."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    add_bg(slide)

    cx = W / 2

    # Etiqueta MACRO N — Poppins Bold 14pt #A0A0A0 UPPERCASE
    lbl_w = Inches(4)
    lbl_h = Inches(0.35)
    lbl_x = cx - lbl_w / 2
    lbl_y = Inches(2.5)
    add_textbox(slide, lbl_x, lbl_y, lbl_w, lbl_h,
                macro["num"], FONT_SANS, 14, GREY_LABEL, bold=True,
                align=PP_ALIGN.CENTER, word_wrap=False)

    # Nombre macro — Instrument Serif Regular 100pt UPPERCASE white centered
    nm_w = Inches(12)
    nm_h = Inches(2.2)
    nm_x = cx - nm_w / 2
    nm_y = lbl_y + lbl_h + Inches(0.15)
    tb = slide.shapes.add_textbox(nm_x, nm_y, nm_w, nm_h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = macro["name"]
    run.font.name = FONT_SERIF
    run.font.size = Pt(100)
    run.font.color.rgb = WHITE
    run.font.bold = False

    # Tagline — Instrument Serif Italic 24pt #A0A0A0
    tg_w = Inches(10)
    tg_h = Inches(0.7)
    tg_x = cx - tg_w / 2
    tg_y = nm_y + nm_h + Inches(0.08)
    add_textbox(slide, tg_x, tg_y, tg_w, tg_h,
                macro["tagline"], FONT_SERIF, 24, GREY_LABEL,
                italic=True, align=PP_ALIGN.CENTER)

    return slide


def _headline_size(text):
    """Auto-size: ≤80 chars → 50pt, >120 chars → 42pt, else 46pt."""
    n = len(text)
    if n <= 80:
        return 50
    elif n >= 120:
        return 42
    else:
        return 46


def build_micro_slide(prs, micro):
    """3-column micro slide following DS spec."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide)

    # -- Layout constants ------------------------------------------------------
    MARGIN_TOP  = Inches(0.22)
    MARGIN_SIDE = Inches(0.28)
    MARGIN_BOT  = Inches(0.22)

    USABLE_W = W - 2 * MARGIN_SIDE
    COL_W = USABLE_W / 3

    COL1_X = MARGIN_SIDE
    COL2_X = MARGIN_SIDE + COL_W
    COL3_X = MARGIN_SIDE + 2 * COL_W

    col_pad  = Inches(0.14)

    # -- Column inner bounds
    content_x1 = COL1_X + col_pad
    content_w1 = COL_W - 2 * col_pad
    content_x2 = COL2_X + col_pad
    content_w2 = COL_W - 2 * col_pad
    content_x3 = COL3_X + col_pad
    content_w3 = COL_W - 2 * col_pad

    content_bot = H - MARGIN_BOT

    # -- Column labels row at MARGIN_TOP
    labels_y = MARGIN_TOP
    labels_h = Inches(0.22)
    for lbl, cx in [("DEFINICIÓN", COL1_X), ("TRIGGERS", COL2_X), ("SEÑALES", COL3_X)]:
        tb = slide.shapes.add_textbox(cx + col_pad, labels_y, COL_W - col_pad, labels_h)
        tf = tb.text_frame
        tf.word_wrap = False
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        run.text = lbl
        run.font.name = FONT_SANS
        run.font.size = Pt(8)
        run.font.bold = True
        run.font.color.rgb = GREY_LABEL

    # Horizontal line under labels
    line_y = labels_y + labels_h + Inches(0.04)
    add_separator_h(slide, COL1_X, line_y, USABLE_W)

    # Vertical lines between columns
    for vx in [COL2_X, COL3_X]:
        add_separator_v(slide, vx, MARGIN_TOP, H - 2 * MARGIN_TOP)

    # Base content top (same for all 3 cols)
    base_top = line_y + Inches(0.12)

    # -------------------------------------------------------------------------
    # COL-LEFT: DEFINICIÓN
    # -------------------------------------------------------------------------
    # Tab MACRO N + NOMBRE MACRO
    tab_h = Inches(0.26)
    tab_y = base_top

    tab1_w = Inches(0.72)
    tab1 = slide.shapes.add_shape(1, COL1_X, tab_y, tab1_w, tab_h)
    tab1.fill.solid()
    tab1.fill.fore_color.rgb = TAB_BG
    tab1.line.fill.background()
    tf1 = tab1.text_frame
    tf1.word_wrap = False
    p1 = tf1.paragraphs[0]
    p1.alignment = PP_ALIGN.CENTER
    r1 = p1.add_run()
    r1.text = micro["macro_num"]
    r1.font.name = FONT_SANS
    r1.font.size = Pt(7.5)
    r1.font.bold = True
    r1.font.color.rgb = BLACK_CLR

    tab2_x = COL1_X + tab1_w + Inches(0.04)
    tab2_w = Inches(2.2)
    tab2 = slide.shapes.add_shape(1, tab2_x, tab_y, tab2_w, tab_h)
    tab2.fill.background()
    tab2.line.color.rgb = GREY_LABEL
    tab2.line.width = Emu(9525)
    tf2 = tab2.text_frame
    tf2.word_wrap = False
    p2 = tf2.paragraphs[0]
    p2.alignment = PP_ALIGN.CENTER
    r2 = p2.add_run()
    r2.text = micro["macro_name"]
    r2.font.name = FONT_SANS
    r2.font.size = Pt(7.5)
    r2.font.color.rgb = GREY_LABEL

    # Content starts below tab
    col1_top = tab_y + tab_h + Inches(0.10)
    col1_h   = content_bot - col1_top

    # Fixed block sizes
    hl_size  = _headline_size(micro["headline"])
    # headline: allow up to ~40% of column height
    hl_h     = Inches(1.80)
    fen_lbl_h = Inches(0.20)
    fen_h    = Inches(1.55)
    hash_lbl_h = Inches(0.20)
    hash_h   = Inches(0.55)
    needs_lbl_h = Inches(0.20)
    needs_h  = Inches(0.50)

    fixed_total = hl_h + fen_lbl_h + fen_h + hash_lbl_h + hash_h + needs_lbl_h + needs_h
    surplus = max(0, col1_h - fixed_total)
    gap1 = surplus * 0.20
    gap2 = surplus * 0.25
    gap3 = surplus * 0.25

    # Headline — Instrument Serif UPPERCASE auto-size 42-50pt
    hl_y = col1_top
    tb_hl = slide.shapes.add_textbox(content_x1, hl_y, content_w1, hl_h)
    tf = tb_hl.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    _set_line_spacing(p, 0.95)
    run = p.add_run()
    run.text = micro["headline"].upper()
    run.font.name = FONT_SERIF
    run.font.size = Pt(hl_size)
    run.font.color.rgb = WHITE
    run.font.bold = False

    # EL FENÓMENO label
    fen_lbl_y = hl_y + hl_h + gap1
    add_textbox(slide, content_x1, fen_lbl_y, content_w1, fen_lbl_h,
                "EL FENÓMENO", FONT_SANS, 8, GREY_LABEL, bold=True, word_wrap=False)

    # Fenomeno body — Poppins 10pt white line-spacing 1.0
    fen_y = fen_lbl_y + fen_lbl_h + Inches(0.04)
    tb_fen = slide.shapes.add_textbox(content_x1, fen_y, content_w1, fen_h)
    tf = tb_fen.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    _set_line_spacing(p, 1.0)
    run = p.add_run()
    run.text = micro["fenomeno"]
    run.font.name = FONT_SANS
    run.font.size = Pt(10)
    run.font.color.rgb = WHITE

    # HASHTAGS label
    hash_lbl_y = fen_y + fen_h + gap2
    add_textbox(slide, content_x1, hash_lbl_y, content_w1, hash_lbl_h,
                "HASHTAGS", FONT_SANS, 8, GREY_LABEL, bold=True, word_wrap=False)

    # Hashtags — Instrument Serif Regular 23pt white
    hash_y = hash_lbl_y + hash_lbl_h + Inches(0.04)
    # Clamp hash_h
    max_hash_h = content_bot - Inches(0.18) - (needs_lbl_h + needs_h + gap3) - hash_y
    hash_h_actual = min(hash_h, max(Inches(0.30), max_hash_h))
    tb_hash = slide.shapes.add_textbox(content_x1, hash_y, content_w1, hash_h_actual)
    tf = tb_hash.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    run = p.add_run()
    run.text = micro["hashtags"]
    run.font.name = FONT_SERIF
    run.font.size = Pt(23)
    run.font.color.rgb = WHITE
    run.font.bold = False

    # 3 NEEDS label
    needs_lbl_y = hash_y + hash_h_actual + gap3
    add_textbox(slide, content_x1, needs_lbl_y, content_w1, needs_lbl_h,
                "3 NEEDS", FONT_SANS, 8, GREY_LABEL, bold=True, word_wrap=False)

    # Needs — Instrument Serif Regular 28pt UPPERCASE white
    needs_y = needs_lbl_y + needs_lbl_h + Inches(0.04)
    needs_h_actual = min(needs_h, content_bot - needs_y)
    # Extract needs from triggers section (not stored separately — pull from micro key if exists, else derive)
    needs_text = micro.get("needs", "")
    if not needs_text:
        # Build from hashtags structure — not available; leave empty as fallback
        needs_text = ""
    tb_needs = slide.shapes.add_textbox(content_x1, needs_y, content_w1, needs_h_actual)
    tf = tb_needs.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    _set_line_spacing(p, 1.0)
    run = p.add_run()
    run.text = needs_text.upper() if needs_text else ""
    run.font.name = FONT_SERIF
    run.font.size = Pt(28)
    run.font.color.rgb = WHITE
    run.font.bold = False

    # -------------------------------------------------------------------------
    # COL-CENTER: TRIGGERS — stat grande + caja desc 170×35pt al lado
    # -------------------------------------------------------------------------
    trigger_area_h = content_bot - base_top
    trigger_slot_h = trigger_area_h / 3

    # Widths for stat + desc side-by-side
    # Available width = content_w2 (~4.1")
    # Stat box: ~1.35" wide, desc box: 170pt = 2.361"
    stat_w   = content_w2 - Inches(2.50)   # ~1.6"
    desc_w   = Inches(2.361)               # 170pt exactly
    stat_gap = Inches(0.10)
    # If stat_w too small, share differently
    if stat_w < Inches(0.8):
        stat_w = Inches(0.8)
    desc_w = content_w2 - stat_w - stat_gap
    if desc_w < Inches(1.5):
        desc_w = Inches(1.5)

    desc_h_box = Inches(0.486)   # 35pt exactly
    src_h_box  = Inches(0.22)

    for i, trig in enumerate(micro["triggers"]):
        slot_top = base_top + i * trigger_slot_h
        # Center stat vertically in slot
        stat_size = 72
        # Reduce for long keyword stats
        if len(trig["stat"]) > 8:
            stat_size = 36
        elif len(trig["stat"]) > 4:
            stat_size = 52

        stat_h_box = Inches(1.10)
        ty = slot_top + Inches(0.08)

        # Stat left
        tb_stat = slide.shapes.add_textbox(content_x2, ty, stat_w, stat_h_box)
        tf = tb_stat.text_frame
        tf.word_wrap = False
        tf.auto_size = None
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        _set_line_spacing(p, 1.0)
        run = p.add_run()
        run.text = trig["stat"]
        run.font.name = FONT_SERIF
        run.font.size = Pt(stat_size)
        run.font.color.rgb = WHITE

        # Desc right — Poppins 10pt white 170×35pt caja
        desc_x = content_x2 + stat_w + stat_gap
        desc_y = ty + Inches(0.05)
        tb_desc = slide.shapes.add_textbox(desc_x, desc_y, desc_w, desc_h_box)
        tf = tb_desc.text_frame
        tf.word_wrap = True
        tf.auto_size = None
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        _set_line_spacing(p, 1.0)
        run = p.add_run()
        run.text = trig["desc"]
        run.font.name = FONT_SANS
        run.font.size = Pt(10)
        run.font.color.rgb = WHITE

        # Fuente inline — Poppins 7pt #666666
        src_y = desc_y + desc_h_box + Inches(0.03)
        tb_src = slide.shapes.add_textbox(desc_x, src_y, desc_w, src_h_box)
        tf = tb_src.text_frame
        tf.word_wrap = False
        tf.auto_size = None
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        run.text = trig["fuente"]
        run.font.name = FONT_SANS
        run.font.size = Pt(7)
        run.font.color.rgb = GREY_MUTED

    # -------------------------------------------------------------------------
    # COL-RIGHT: SEÑALES — foto 149×220pt + caja caption 170×35pt al lado
    # -------------------------------------------------------------------------
    IMG_W = Inches(2.069)   # 149pt
    IMG_H = Inches(3.056)   # 220pt

    cap_w_box  = Inches(2.361)   # 170pt
    cap_h_box  = Inches(0.486)   # 35pt
    img_cap_gap = Inches(0.10)

    # 3 slots stacked vertically
    senal_area_h = content_bot - base_top
    senal_slot_h = senal_area_h / 3

    for i, senal in enumerate(micro["senales"]):
        slot_top = base_top + i * senal_slot_h
        # Center image vertically in slot
        img_y = slot_top + (senal_slot_h - IMG_H) / 2
        img_y = max(slot_top, min(img_y, content_bot - IMG_H))

        img_x  = content_x3
        url    = senal["url"]
        img_file = senal["img"]
        img_path = os.path.join(SHOTS, img_file) if img_file else None

        if img_path and os.path.exists(img_path):
            add_image_hyperlink(slide, img_path, img_x, img_y, IMG_W, IMG_H, url)
        else:
            add_placeholder(slide, img_x, img_y, IMG_W, IMG_H, url)

        # Badge CLICK ME
        add_click_me_badge(slide, img_x, img_y, IMG_W)

        # Caption box to the right of image — Poppins 10pt white 170×35pt
        cap_x = img_x + IMG_W + img_cap_gap
        cap_y = img_y
        # Check if cap_x + cap_w_box overflows col3
        available_cap_w = (COL3_X + COL_W - col_pad) - cap_x
        if available_cap_w < Inches(1.0):
            # Place caption below image instead
            cap_x = img_x
            cap_y = img_y + IMG_H + Inches(0.04)
            cap_w_use = IMG_W
        else:
            cap_w_use = min(cap_w_box, available_cap_w)

        tb_cap = slide.shapes.add_textbox(cap_x, cap_y, cap_w_use, cap_h_box)
        tf = tb_cap.text_frame
        tf.word_wrap = True
        tf.auto_size = None
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        _set_line_spacing(p, 1.0)
        run = p.add_run()
        run.text = senal["caption"]
        run.font.name = FONT_SANS
        run.font.size = Pt(10)
        run.font.color.rgb = WHITE

    return slide


# -- Main ----------------------------------------------------------------------

def main():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H

    micro_idx = 0
    for macro_i, macro in enumerate(MACROS):
        build_macro_divider(prs, macro)
        for j in range(5):
            # Add needs to each micro from the editorial content
            m = MICROS[micro_idx].copy()
            needs_map = {
                0:  "CONTROL · MIEDO · SOLEDAD",
                1:  "DIGNIDAD · VACÍO · CONTROL",
                2:  "CULPA · RESENTIMIENTO · REPARACIÓN",
                3:  "SOLEDAD · PERTENENCIA · INVISIBILIDAD",
                4:  "CONTROL · SOLEDAD · CULPA",
                5:  "MIEDO · CULPA · CONTROL",
                6:  "VACÍO · CONTROL · SOLEDAD",
                7:  "CULPA · SOLEDAD · INVISIBILIDAD",
                8:  "CONTROL · MIEDO · VACÍO",
                9:  "VACÍO · CONTROL · SOLEDAD",
                10: "VACÍO · INVISIBILIDAD · CULPA",
                11: "SOLEDAD · INVISIBILIDAD · VACÍO",
                12: "SOLEDAD · VACÍO · CONTROL",
                13: "MIEDO · RESENTIMIENTO · CONTROL",
                14: "VACÍO · MIEDO · SOLEDAD",
            }
            m["needs"] = needs_map.get(micro_idx, "")
            build_micro_slide(prs, m)
            micro_idx += 1

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    prs.save(OUT)
    print(f"Saved: {OUT}")
    print(f"Total slides: {len(prs.slides)}")

    # Count real vs placeholder images
    real = placeholder = 0
    for m in MICROS:
        for s in m["senales"]:
            img_file = s.get("img")
            if img_file and os.path.exists(os.path.join(SHOTS, img_file)):
                real += 1
            else:
                placeholder += 1
    print(f"Señales con imagen real: {real}")
    print(f"Señales placeholder: {placeholder}")


if __name__ == "__main__":
    main()
