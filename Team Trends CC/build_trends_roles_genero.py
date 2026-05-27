#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trends Forecast — Roles de Género (Código Casa / NINJA Thinking)
Montador-trends-cc · 18 slides · DS Trends CC
Layout: 3 columnas oscuro #0D0D0D, Instrument Serif + Poppins.
"""

import os
from pathlib import Path

from pptx import Presentation
from pptx.util import Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

# ─────────────────────────────────────────────────────────────
# Constantes globales
# ─────────────────────────────────────────────────────────────

BASE = Path("/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC")
SCREENSHOTS = BASE / "screenshots" / "trends-roles-genero"
OUTPUT_PPTX = BASE / "outputs" / "trends-roles-genero-forecast.pptx"

# Canvas 1440 x 810 pt → 16:9 widescreen (1 pt = 1/72")
SLIDE_W_PT = 1440
SLIDE_H_PT = 810

# Colores
BG_DARK = RGBColor(0x0D, 0x0D, 0x0D)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GRAY_LABEL = RGBColor(0xA0, 0xA0, 0xA0)
GRAY_SRC = RGBColor(0x66, 0x66, 0x66)
RED_BADGE = RGBColor(0xFF, 0x2D, 0x2D)
LINE_WHITE_6 = RGBColor(0x29, 0x29, 0x29)  # ~6% white over black

FONT_SERIF = "Instrument Serif"
FONT_SANS = "Poppins"

# Layout 3 columnas
MARGIN_X = 48
MARGIN_Y = 48
GUTTER = 32
COL_W = (SLIDE_W_PT - 2 * MARGIN_X - 2 * GUTTER) / 3  # ~432pt each
COL_LEFT_X = MARGIN_X
COL_CENTER_X = MARGIN_X + COL_W + GUTTER
COL_RIGHT_X = MARGIN_X + 2 * (COL_W + GUTTER)

TOP_TAB_Y = MARGIN_Y
LABEL_Y = MARGIN_Y + 36
LINE_H_Y = LABEL_Y + 16
CONTENT_Y = LINE_H_Y + 18
CONTENT_H = SLIDE_H_PT - CONTENT_Y - MARGIN_Y

# Imagen señal
IMG_W = 149
IMG_H = 220

# ─────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────

def add_rect(slide, x, y, w, h, fill_color, line_color=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Pt(x), Pt(y), Pt(w), Pt(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill_color
    if line_color is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line_color
        shp.line.width = Pt(0.5)
    shp.shadow.inherit = False
    return shp


def add_line(slide, x1, y1, x2, y2, color=LINE_WHITE_6, weight=0.75):
    line = slide.shapes.add_connector(1, Pt(x1), Pt(y1), Pt(x2), Pt(y2))
    line.line.color.rgb = color
    line.line.width = Pt(weight)
    return line


def add_text(
    slide, x, y, w, h, text, font=FONT_SANS, size=8, bold=False, italic=False,
    color=WHITE, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=1.0,
    upper=False, tracking=None,
):
    tb = slide.shapes.add_textbox(Pt(x), Pt(y), Pt(w), Pt(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = anchor

    if isinstance(text, str):
        paragraphs = text.split("\n")
    else:
        paragraphs = text  # list of strings

    for i, line in enumerate(paragraphs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        run = p.add_run()
        run.text = line.upper() if upper else line
        f = run.font
        f.name = font
        f.size = Pt(size)
        f.bold = bold
        f.italic = italic
        f.color.rgb = color
        if tracking is not None:
            # tracking in 1/100 pt units via XML spc attribute
            rPr = run._r.get_or_add_rPr()
            rPr.set("spc", str(int(tracking)))
    return tb


def add_image(slide, path, x, y, w, h, hyperlink=None):
    if path and Path(path).exists():
        pic = slide.shapes.add_picture(str(path), Pt(x), Pt(y), Pt(w), Pt(h))
        if hyperlink:
            pic.click_action.hyperlink.address = hyperlink
        return pic
    else:
        # placeholder
        ph = add_rect(slide, x, y, w, h, BG_DARK, line_color=LINE_WHITE_6)
        return ph


def add_click_badge(slide, x_right, y_top):
    """Badge 'Click me' rojo en esquina superior derecha de una imagen."""
    bw, bh = 56, 16
    bx = x_right - bw + 8  # offset right:-8
    by = y_top - 8  # offset top:-8
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Pt(bx), Pt(by), Pt(bw), Pt(bh))
    rect.fill.solid()
    rect.fill.fore_color.rgb = RED_BADGE
    rect.line.fill.background()
    rect.shadow.inherit = False
    tf = rect.text_frame
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = "CLICK ME"
    run.font.name = FONT_SANS
    run.font.size = Pt(7)
    run.font.bold = True
    run.font.color.rgb = WHITE


def add_placeholder_pending(slide, x, y, w, h, url=None):
    ph = add_rect(slide, x, y, w, h, BG_DARK, line_color=LINE_WHITE_6)
    add_text(
        slide, x, y + h/2 - 12, w, 24,
        "CAPTURA MANUAL — JEREMY",
        font=FONT_SANS, size=8, bold=True, color=GRAY_SRC,
        align=PP_ALIGN.CENTER, upper=True,
    )
    if url:
        ph.click_action.hyperlink.address = url


def add_macro_tab(slide, x, y, text, w=COL_W):
    """Tab 'MACRO N | NOMBRE MACRO' arriba de col-left."""
    add_text(
        slide, x, y, w, 14,
        text,
        font=FONT_SANS, size=8, bold=True, color=WHITE,
        upper=True, tracking=150,
    )


def add_column_label(slide, x, y, text, w=COL_W):
    add_text(
        slide, x, y, w, 12,
        text,
        font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL,
        upper=True, tracking=100,
    )


def slide_chrome(slide, macro_tab_text):
    """Background, tab, labels, lines comunes a slides de micro."""
    # fondo
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.fill.background()
    bg.shadow.inherit = False
    # mover al fondo
    spTree = bg._element.getparent()
    spTree.remove(bg._element)
    spTree.insert(2, bg._element)

    # tab macro
    add_macro_tab(slide, COL_LEFT_X, TOP_TAB_Y, macro_tab_text)

    # labels columnas
    add_column_label(slide, COL_LEFT_X, LABEL_Y, "DEFINICIÓN")
    add_column_label(slide, COL_CENTER_X, LABEL_Y, "TRIGGERS")
    add_column_label(slide, COL_RIGHT_X, LABEL_Y, "SEÑALES")

    # línea horizontal bajo labels
    add_line(slide, MARGIN_X, LINE_H_Y, SLIDE_W_PT - MARGIN_X, LINE_H_Y)

    # 2 líneas verticales entre columnas
    v1_x = COL_LEFT_X + COL_W + GUTTER/2
    v2_x = COL_CENTER_X + COL_W + GUTTER/2
    add_line(slide, v1_x, CONTENT_Y - 12, v1_x, SLIDE_H_PT - MARGIN_Y)
    add_line(slide, v2_x, CONTENT_Y - 12, v2_x, SLIDE_H_PT - MARGIN_Y)


# ─────────────────────────────────────────────────────────────
# Data structures: editorial -> slides
# ─────────────────────────────────────────────────────────────

# Helper para señal
def S(label, caption, src, screenshot, url):
    return {
        "label": label, "caption": caption, "src": src,
        "screenshot": screenshot, "url": url,
    }

def T(keyword, stat, desc, src):
    return {"keyword": keyword, "stat": stat, "desc": desc, "src": src}


MACROS = [
    {
        "n": 1,
        "name": "INVENTOLOGÍA DE LA ADULTEZ",
        "tab": "MACRO 1 | INVENTOLOGÍA",
        "tagline": "“Un mundo en crisis está reescribiendo qué significa ser adulto y formar familia.”",
        "behavior": (
            "El guion heredado — él provee, ella sostiene — se cae a pedazos porque ya no cuadra con el banco "
            "ni con el censo. La mujer dominicana firmó contrato laboral [80% de nuevos empleos formales] sin "
            "romper el contrato doméstico. La adultez de género se está inventando en el espacio entre el "
            "“ambos” del discurso y la mujer batida del verbatim."
        ),
        "triggers": [
            T("“ambos”", "74.8%", "afirma que el rol del hombre y la mujer ha cambiado “Mucho” — pero P15/P33 desmiente tarea por tarea: la mujer sigue cargando 60/40 en lavar, cocinar, planchar y limpiar.", "Código Casa · 2024"),
            T("“ratio 59%”", "44,349 / 26,210", "matrimonios contra divorcios en 2024 — el ratio más alto del registro RD.", "ONE vía Listín Diario · 2025"),
            T("“nuevas adultas”", "80%+", "de los nuevos empleos formales en RD los toman mujeres de 25-39 años.", "BCRD vía N.com.do · 2025"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Lyn (@madresrealesrd) articula “CargaMentalMaterna” en español RD. Cara local de la brecha declarado-vivido.",
              "TikTok @madresrealesrd · 2024",
              "macro-1-1-tiktok-madres-reales-rd-carga-mental.png",
              "https://www.tiktok.com/@madresrealesrd/video/7262536453459086597"),
            S("TREND",
              "ONE — divorcios crecieron de 12,821 (2001) a 28,694 (2021): +124% en 20 años, oficial.",
              "Blog ONE · 2024-2025",
              "macro-1-5-one-blog-divorcios.png",
              "http://blog.one.gob.do/index.php/divorcios-en-aumento-que-esta-pasando-con-los-matrimonios-en-la-republica-dominicana/"),
            S("INNOVACIÓN",
              "Familia Feliz reconoce 2,160 mujeres con vivienda propia — el Estado nombra a la jefa de hogar como sujeto de política.",
              "Presidencia RD · 2024",
              "macro-1-3-presidencia-familia-feliz.png",
              "https://presidencia.gob.do/noticias/familia-feliz-ha-beneficiado-2160-mujeres-con-la-asignacion-de-una-vivienda-propia-y-digna"),
        ],
    },
    {
        "n": 2,
        "name": "LOS HERNÁNDEZ ARE PROMPTED",
        "tab": "MACRO 2 | HERNÁNDEZ PROMPTED",
        "tagline": "“El dominicano ya entró al mundo prompteado. Solo no lo nombra así.”",
        "behavior": (
            "La IA entró a la economía doméstica como la tercera adulta que la mujer no tenía. Si ella carga "
            "60/40 sin ayuda visible y el marido “ayuda cuando uno le dice”, el prompt aparece como el primer "
            "aliado que no necesita ser dirigido — recuerda, anticipa, redacta. Y del lado masculino también "
            "entró: papás dominicanos preguntan a la pantalla lo que jamás dijeron en voz alta."
        ),
        "triggers": [
            T("“72% usa IA”", "9 / 19", "RD es “adoptante en acción” en el índice ILIA — 44.96/100 — ranked 9 de 19 países LATAM.", "IRIS / CEPAL · 2025"),
            T("“ChatGPT mom”", "52.4%", "de usuarios activos de ChatGPT en junio 2025 tienen nombres femeninos (vs 17.6% al lanzamiento).", "Axios · 2025-09-30"),
            T("“97% mental load”", "97%", "Lilian Schmidt (Zurich) reduce 97% de su mental load usando ChatGPT — “AI is the third supporter”.", "Mother.ly · 2025"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Red Uno Bolivia — niña pide a ChatGPT que haga su tarea “como si fuera yo”. El prompt entró al pupitre LATAM.",
              "TikTok @redunotv · 2025",
              "macro-2-1-tiktok-nina-chatgpt-tarea-redunotv.png",
              "https://www.tiktok.com/@redunotv/video/7524731891031870726"),
            S("TREND",
              "Axios — la IA mainstream se hizo herramienta de mamá antes que de oficinista. Curva de feminización más limpia de la era reciente.",
              "Axios · 2025-09-30",
              "macro-2-1-axios-chatgpt-feminizado.png",
              "https://www.axios.com/2025/09/30/chatgpt-pulse-ai-assistant-moms"),
            S("INNOVACIÓN",
              "Mother.ly — Lilian Schmidt y la IA como “third supporter” de la familia. Caso editorial que las marcas IA todavía no convirtieron en campaña.",
              "Mother.ly · 2025",
              "macro-2-0-motherly-ai-mental-load.png",
              "https://www.mother.ly/parenting/how-ai-is-helping-this-mom-reduce-mental-load/"),
        ],
    },
    {
        "n": 3,
        "name": "ALGORITMO DEL HOGAR",
        "tab": "MACRO 3 | ALGORITMO DEL HOGAR",
        "tagline": "“El feed se sentó en la mesa y nadie le ofreció silla.”",
        "behavior": (
            "La misma casa dominicana ve dos feeds distintos. Ella: clean girl, tradwife evangélica, momfluencer. "
            "Él: Andrew Tate doblado al español, “high value males”, manosphere. Ambos algoritmos venden el rol "
            "tradicional como producto premium — uno como estética aspiracional, otro como reclamo identitario. "
            "El conflicto de género de 2026 no es marido vs mujer. Es algoritmo de ella vs algoritmo de él."
        ),
        "triggers": [
            T("“4x misoginia”", "4×", "aumento en contenido misógino sugerido por TikTok a perfiles jóvenes masculinos en solo 5 días.", "El Nacional · 2025"),
            T("“tradwife LATAM”", "50%", "de hombres jóvenes confía en al menos un influencer manosphere — Equimundo State of American Men.", "19th News · 2025-06"),
            T("“DadTok hispano”", "+3.8M", "views — #TribuDePapas, 10 cuentas mexicanas de papás viralizando tareas domésticas.", "Univision · 2024"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Andrew Tate doblado al español (@highvaluemales). El manosphere entró al feed hispano joven sin barrera de idioma.",
              "TikTok @highvaluemales · 2022-2025",
              "macro-3-2-tiktok-andrew-tate-espanol.png",
              "https://www.tiktok.com/@highvaluemales/video/7115901381503978758"),
            S("TREND",
              "The 19th — “Algoritmos, alpha males y tradwives”: el feed polariza a la pareja desde adentro del mismo hogar.",
              "The 19th · 2025-06",
              "macro-3-2-19thnews-alpha-males.png",
              "https://19thnews.org/2025/06/internet-culture-algorithms-alpha-males-tradwives/"),
            S("INNOVACIÓN",
              "Univision — #TribuDePapas. Cluster mexicano de papás que viralizan tareas. Contrapunto hispano al manosphere.",
              "Univision · 2024",
              "macro-3-4-univision-tribudepapas.png",
              "https://www.univision.com/entretenimiento/cultura-pop/tiktok-hombres-normalizan-laborales-hogar-paternidad"),
        ],
    },
]


# ─────────────────────────────────────────────────────────────
# Micros — 15 entries
# ─────────────────────────────────────────────────────────────

MICROS = [
    # ─── MACRO 1
    {
        "macro": 0,  # index in MACROS
        "code": "1.1",
        "headline": "AMBOS DICE LA BOCA, ELLA HACE LA CASA",
        "tagline": "“La equidad se declara en encuesta y se desmiente en la cocina.”",
        "fenomeno": (
            "Pregúntale al dominicano cómo se reparten las tareas y va a decir “ambos”. Pregúntaselo tarea por "
            "tarea y la respuesta cambia de país. En P15 más de la mitad dice “de los dos”. En P33, granular, "
            "salta a “más la mujer” en todas — con brechas que pasan los 20 puntos. La equidad llegó al discurso "
            "como una palabra de moda, pero todavía no llegó a la pila de ropa. Y entre esos dos pisos vive Lyn "
            "de @madresrealesrd nombrándolo en cámara: carga mental materna."
        ),
        "hashtags": "#cargamental · #defaultparent · #cargamentalmaterna · #ambosencomillas · #mamabatida",
        "hero_stat": ("66.6% vs 54.8%", "“Más la mujer” cocinar (P33) vs. “Ambos” cocinar (P15) — brecha 20+ puntos.", "Código Casa · 2024"),
        "triggers": [
            T("“ambos”", "P15: 54.8%", "declara “Ambos” cocinar, lavar, limpiar.", "Código Casa · 2024"),
            T("“más la mujer”", "P33: 66.6%", "desmiente granular — “Más la mujer” en cocinar, lavar, limpiar.", "Código Casa · 2024"),
            T("“default parent”", "4 fases", "del trabajo mental [anticipar, identificar, decidir, monitorear] recaen sobre la mujer aunque se “delegue”.", "ASR vía Alter Mutua · 2024"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Lyn (@madresrealesrd) — primera huella RD nombrando “CargaMentalMaterna” en español dominicano.",
              "TikTok @madresrealesrd · 2024",
              "macro-1-1-tiktok-madres-reales-rd-carga-mental.png",
              "https://www.tiktok.com/@madresrealesrd/video/7262536453459086597"),
            S("TREND",
              "Mother.ly — Default Parent Syndrome se viraliza en TikTok 2025: la mamá queda “primera en la fila” sin acuerdo.",
              "Mother.ly · 2025",
              "macro-1-1-motherly-default-parent.png",
              "https://www.mother.ly/news/viral-trending/default-parent-resentment/"),
            S("INNOVACIÓN",
              "Pequefelicidad — “La carga mental: lo que no se ve sí existe”. Concepto académico convertido en pieza viral hispana.",
              "TikTok @pequefelicidad · 2024",
              "macro-1-1-tiktok-pequefelicidad-carga-mental.png",
              "https://www.tiktok.com/@pequefelicidad/video/7371433274381487392"),
        ],
    },
    {
        "macro": 0, "code": "1.2",
        "headline": "LA PLANCHA TIENE GÉNERO",
        "tagline": "“Hay TikToks para todo. Pero no hay TikToks de la plancha.”",
        "fenomeno": (
            "La lavadora eliminó el lavadero. El microondas relevó el sancocho de los lunes. Uber Eats sustituyó "
            "la cocina de los miércoles. Pero la plancha no la tocó nadie. Es la única tarea del hogar dominicano "
            "donde “Mujer” le gana a “Ambos” — 54.2% contra 44%, y el hombre desaparece a 1.8%. Y cuando vas a "
            "buscar la huella viral del tema en TikTok hispano, no hay nada. La tarea más extrema de inequidad "
            "doméstica del país es tan invisible que ni el meme se atrevió."
        ),
        "hashtags": "#planchar · #cargainvisible · #tareasdecasa · #wifedoesitall · #dailychores",
        "hero_stat": ("1.8%", "de hombres dominicanos plancha. La única tarea de P15 donde “Mujer” le gana a “Ambos”.", "Código Casa · 2024"),
        "triggers": [
            T("“1.8% hombre”", "54.2% / 1.8%", "mujer planchando vs hombre planchando. La brecha más cruda del cuestionario.", "Código Casa · 2024"),
            T("“yo no plancho”", "0", "menciones de planchar como tarea masculina en 11 focus groups Código Casa.", "FG · 2024"),
            T("“huella viral nula”", "0", "videos hispanos verificables sobre planchar como tema de género. La plancha no produce contenido porque no tiene reclamo.", "Team Trends CC · 2026"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Pequefelicidad — la lógica de “lo que no se ve no se redistribuye” aplica exactamente a la plancha.",
              "TikTok @pequefelicidad · 2024",
              "macro-1-1-tiktok-pequefelicidad-carga-mental.png",
              "https://www.tiktok.com/@pequefelicidad/video/7371433274381487392"),
            S("TREND",
              "Alter Mutua — las 4 fases del trabajo mental femenino. Por qué tareas crónicas como planchar no se redistribuyen aunque se “comparta” la casa.",
              "Alter Mutua · 2024-2025",
              "macro-1-1-altermutua-carga-mental.png",
              "https://www.altermutua.com/es/la-carga-mental-en-las-mujeres/"),
            S("INNOVACIÓN",
              "Pipedrive — carga mental como vocabulario de negocio. Argumento para marcas de electrodomésticos y servicios de planchado.",
              "Pipedrive · 2024-2025",
              "macro-1-1-pipedrive-carga-mental.png",
              "https://www.pipedrive.com/es/blog/carga-mental"),
        ],
    },
    {
        "macro": 0, "code": "1.3",
        "headline": "LA JEFA DEL HOGAR ES UNA SOLA MUJER",
        "tagline": "“Ser madre soltera dejó de ser excepción para volverse estructura del país.”",
        "fenomeno": (
            "Una de cada tres familias dominicanas la lidera una mujer sola. La monoparentalidad ya no es la nota "
            "al pie del censo: es columna del censo. La familia papá-mamá-hijos dejó de ser mayoría estadística. "
            "El Estado, que tarda en nombrar lo evidente, finalmente lo nombró: Bono Madre, Bono Mujer, Familia "
            "Feliz. La política pública llegó tarde, pero llegó. La economía privada todavía no aterriza."
        ),
        "hashtags": "#madresoltera · #jefadehogar · #mompreneur · #bonomadre · #familiamonoparental",
        "hero_stat": ("41%", "de hogares en el programa Familia Feliz son monoparentales. 2,160 mujeres con vivienda propia.", "Presidencia RD · 2024"),
        "triggers": [
            T("“familia feliz”", "2,160", "mujeres beneficiadas con vivienda propia — 41% de hogares del programa son monoparentales.", "Presidencia RD · 2024"),
            T("“bono mujer”", "RD$1,500M", "presupuestados para jefas de hogar — Bono Mujer / Bono Madre institucionalizado.", "Ministerio de la Mujer · 2024"),
            T("“batallas invisibles”", "—", "reportaje El Intermediario sobre madres solteras RD: ausencia económica del padre, manutención débil.", "El Intermediario · 2025-11"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Lyn (@madresrealesrd) — la mamá habla en primera persona sin la teatralización de las momfluencers extranjeras.",
              "TikTok @madresrealesrd · 2024",
              "macro-1-1-tiktok-madres-reales-rd-carga-mental.png",
              "https://www.tiktok.com/@madresrealesrd/video/7262536453459086597"),
            S("TREND",
              "El Intermediario — “Las batallas invisibles de madres solteras en RD”. Reportaje 2025 que nombra el sistema.",
              "El Intermediario · 2025-11",
              "macro-1-3-elintermediario-madres-solteras.png",
              "https://elintermediario.com.do/2025/11/02/las-batallas-invisibles-de-madres-solteras-en-la-republica-dominicana/"),
            S("INNOVACIÓN",
              "Familia Feliz — el Estado nombra a la jefa de hogar como sujeto de política habitacional. Las marcas todavía no lo nombran como sujeto de compra.",
              "Presidencia RD · 2024",
              "macro-1-3-presidencia-familia-feliz.png",
              "https://presidencia.gob.do/noticias/familia-feliz-ha-beneficiado-2160-mujeres-con-la-asignacion-de-una-vivienda-propia-y-digna"),
        ],
    },
    {
        "macro": 0, "code": "1.4",
        "headline": "HEREDA MI ESPOSA: EL CUIDADO QUE NADIE VOTÓ",
        "tagline": "“El plan de retiro del adulto mayor dominicano se llama nuera.”",
        "fenomeno": (
            "73% de los dominicanos dice que no convive con nadie mayor. Pero RD entra a 2031 como sociedad "
            "envejecida [>14% de 60+] y a 2050 con uno de cada cinco habitantes pasado los 60. El cuidado de "
            "mayores existe pero está sumergido — se delega a la nuera, a la hija, a la hermana, en silencio. "
            "El Estado apenas en 2024 certificó la primera promoción de 90 cuidadoras formales con CONAPE."
        ),
        "hashtags": "#cuidadora · #elderlycare · #nuerasinpaga · #sandwichgeneration · #cuidalacuidadora",
        "hero_stat": ("2031", "RD entra como sociedad envejecida — >14% de la población con 60+ años. Sin sistema público de cuidados.", "Iberoamérica Mayores · 2025"),
        "triggers": [
            T("“78% sin mayores”", "78% / 64.6%", "mujeres vs hombres que dicen no convivir con nadie mayor. Cuando aplica, ella asume.", "Código Casa · 2024"),
            T("“RD envejece”", "21%", "de la población RD tendrá más de 60 años para 2050. Carga de cuidados crece sin sistema público.", "Iberoamérica Mayores · 2025-06"),
            T("“cuidadora formal”", "90", "cuidadoras certificadas CONAPE/Supérate/INFOTEP: RD$30,000 + seguridad social, 8 horas en casa.", "Listín Diario · 2024-12"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Lyn (@madresrealesrd) — la mujer carga lo que la casa heredada no redistribuyó. Aplica también al cuidado de mayores.",
              "TikTok @madresrealesrd · 2024",
              "macro-1-1-tiktok-madres-reales-rd-carga-mental.png",
              "https://www.tiktok.com/@madresrealesrd/video/7262536453459086597"),
            S("TREND",
              "Iberoamérica Mayores — RD será “sociedad envejecida” para 2031. El dato demográfico que la cuanti todavía no captura.",
              "Iberoamérica Mayores · 2025-06-30",
              "macro-1-4-iberoamerica-mayores-rd.png",
              "https://iberoamericamayores.org/2025/06/30/republica-dominicana-trayectorias-y-desafios-en-los-cuidados-de-larga-duracion-para-personas-mayores/"),
            S("INNOVACIÓN",
              "CONAPE — primera promoción de 90 cuidadoras certificadas. Política pública que reconoce a la cuidadora como trabajadora.",
              "Listín Diario · 2024-12-05",
              "macro-1-4-listin-cuidadoras-conape.png",
              "https://listindiario.com/la-republica/sector-salud/20241205/cuidaran-adultos-mayores-casas-ocho-horas_836458.html"),
        ],
    },
    {
        "macro": 0, "code": "1.5",
        "headline": "DIVORCIO LA NORMA, MATRIMONIO LA ANOMALÍA",
        "tagline": "“En RD el contrato matrimonial se renegocia cada siete años — si es que llega.”",
        "fenomeno": (
            "Por cada 100 matrimonios firmados en 2024, 60 terminaron en divorcio. Es el ratio más alto del registro "
            "y subió 124% desde 2001. Y en 2025 los matrimonios cayeron otro 8.7%. El contrato matrimonial dejó "
            "de ser predictor confiable de hogar — se volvió una herramienta más, opcional, revisable, terminable. "
            "La mujer se casa más joven que el hombre y se divorcia primero."
        ),
        "hashtags": "#divorcioRD · #coparenting · #exmarido · #papáfindesemana · #exitstrategy",
        "hero_stat": ("59%", "ratio divorcios/matrimonios RD 2024. El más alto del registro histórico.", "ONE vía Listín Diario · 2025"),
        "triggers": [
            T("“ratio 59%”", "44,349 / 26,210", "matrimonios vs divorcios en 2024. Desde 2021 supera el 60%.", "ONE vía Listín Diario · 2025"),
            T("“+124% divorcios”", "12,821 → 28,694", "divorcios crecieron 124% en 20 años (2001-2021).", "Blog ONE · 2024-2025"),
            T("“ella se casa primero”", "—", "las mujeres se casan más jóvenes que los hombres en RD — y suelen divorciarse primero.", "El Día · 2024"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Bloomberg Línea — el frame regional: en paralelo al divorcio masivo, una porción busca volver al “para toda la vida” como rebeldía.",
              "Bloomberg Línea · 2024-2025",
              "macro-3-0-bloomberg-tradwife-latam.png",
              "https://www.bloomberglinea.com/economia/tradwife-o-esposas-tradicionales-que-tan-real-es-la-tendencia-para-mujeres-de-latam/"),
            S("TREND",
              "Listín — matrimonios vs divorcios 2024 RD. La cifra dura con fuente oficial.",
              "Listín Diario · 2025-06-01",
              "macro-1-0-listin-divorcios-2024.png",
              "https://listindiario.com/la-republica/ciudad/20250601/2024-registraron-44-349-matrimonios-26-210-divorcios_859974.html"),
            S("INNOVACIÓN",
              "El Día — mujeres se casan más jóvenes que los hombres en RD. La que entra primero al matrimonio es la que sale primero.",
              "El Día RD · 2024",
              "macro-1-5-eldia-mujeres-jovenes-casan.png",
              "https://eldia.com.do/mujeres-se-casan-mas-jovenes-que-los-hombres-en-rd/"),
        ],
    },
    # ─── MACRO 2
    {
        "macro": 1, "code": "2.1",
        "headline": "CHATGPT, MI SEGUNDA ADULTA",
        "tagline": "“La coadulta que el matrimonio no produjo, la entregó OpenAI.”",
        "fenomeno": (
            "La mujer dominicana le delegó al prompt lo que su esposo no acaba de cargar. Menú semanal con "
            "presupuesto RD$5,000. Lista de útiles. Mensaje a la maestra sin tono acusatorio. Regalo de la sobrina. "
            "El prompt no se ofende cuando se le repite, no olvida cumpleaños. Para junio 2025 más de la mitad "
            "de los usuarios activos de ChatGPT ya tenían nombres femeninos. AI is the third supporter."
        ),
        "hashtags": "#chatgptmom · #aimomhack · #mentalloadhack · #promptdemama · #mividaconchatgpt",
        "hero_stat": ("52.4%", "de usuarios activos de ChatGPT con nombres femeninos en junio 2025 (vs 17.6% al lanzamiento).", "Axios · 2025-09-30"),
        "triggers": [
            T("“chatgpt mom”", "52.4%", "usuarios activos con nombres femeninos en junio 2025. La IA mainstream se feminizó.", "Axios · 2025-09-30"),
            T("“third supporter”", "97%", "Lilian Schmidt reduce 97% de mental load con ChatGPT: comidas, regalos, rutinas.", "Mother.ly · 2025"),
            T("“ya es mamá”", "—", "Merca 2.0, Independent Español, Infobae cubren “madre viral por usar ChatGPT para criar”.", "Merca 2.0 / Independent · 2025"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Red Uno Bolivia — niña delega tarea a ChatGPT, mamá observa, suegra ya no opina. Adopción IA en hogar LATAM.",
              "TikTok @redunotv · 2025",
              "macro-2-1-tiktok-nina-chatgpt-tarea-redunotv.png",
              "https://www.tiktok.com/@redunotv/video/7524731891031870726"),
            S("TREND",
              "Axios — 52.4% vs 17.6%. La curva de feminización más limpia de la era reciente.",
              "Axios · 2025-09-30",
              "macro-2-1-axios-chatgpt-feminizado.png",
              "https://www.axios.com/2025/09/30/chatgpt-pulse-ai-assistant-moms"),
            S("INNOVACIÓN",
              "Merca 2.0 — “ChatGPT ya es mamá”. Caso editorial hispano listo para referenciar; las marcas IA todavía no nombran a este segmento.",
              "Merca 2.0 · 2025",
              "macro-2-1-merca20-chatgpt-mama.png",
              "https://www.merca20.com/chatgpt-ya-es-mama-asi-ayuda-a-una-madre-a-criar-a-su-hijo-mientras-ella-descansa/"),
        ],
    },
    {
        "macro": 1, "code": "2.2",
        "headline": "LA PELEA QUE CHATGPT REESCRIBIÓ",
        "tagline": "“Antes del WhatsApp acusatorio, una pasada por el prompt.”",
        "fenomeno": (
            "Antes de mandarle el mensaje difícil al marido, ella le pide a ChatGPT que “lo diga sin sonar agresiva”. "
            "El prompt se volvió filtro de pareja. Ya no se tira el texto en caliente; se pasa primero por una IA "
            "que suaviza, ordena y borra los signos de exclamación. La mediación se privatizó y se automatizó. "
            "La pelea entra con la voz de ella y sale con la voz del prompt."
        ),
        "hashtags": "#promptparapareja · #chatgptcouples · #reescribelo · #aitherapist · #mediadoraIA",
        "hero_stat": ("47%", "de usuarios fuertes de IA se sienten más confiados al usarla en momentos de inseguridad para decidir.", "Accenture · 2025-10"),
        "triggers": [
            T("“filtro de pareja”", "47%", "usuarios fuertes de IA más confiados al usarla en momentos de inseguridad para decidir.", "Accenture · 2025-10"),
            T("“eye-opening”", "—", "Newsweek + Mother.ly: mamá overwhelmed encuentra “eye-opening solution” en ChatGPT como mediador.", "Newsweek · 2025"),
            T("“mom hack”", "52.4%", "usuarios ChatGPT con nombres femeninos. Uso emocional crece en paralelo al doméstico.", "Axios · 2025-09-30"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Red Uno Bolivia — el LLM entra como tercero en relaciones que antes eran cara a cara.",
              "TikTok @redunotv · 2025",
              "macro-2-1-tiktok-nina-chatgpt-tarea-redunotv.png",
              "https://www.tiktok.com/@redunotv/video/7524731891031870726"),
            S("TREND",
              "Newsweek — mom overwhelmed mental load encuentra “eye-opening solution”. Caso editorial que valida frame mediación-IA.",
              "Newsweek · 2025",
              "macro-2-1-newsweek-mom-mental-load.png",
              "https://www.newsweek.com/mom-overwhelmed-mental-load-finds-solution-2091525"),
            S("INNOVACIÓN",
              "Independent Español — madre viral por pedir ayuda a ChatGPT para criar. Cobertura hispana, no se siente importado.",
              "Independent Español · 2025",
              "macro-2-1-independent-mom-chatgpt.png",
              "https://www.independentespanol.com/estilo/chatgpt-consejos-paternidad-madres-inteligencia-artificial-b2803910.html"),
        ],
    },
    {
        "macro": 1, "code": "2.3",
        "headline": "EL CRONOGRAMA QUE NADIE FIRMÓ",
        "tagline": "“El acuerdo de equidad lo emitió un LLM, no la pareja.”",
        "fenomeno": (
            "ChatGPT le genera al hombre el cronograma de tareas equitativas que la mujer venía pidiendo hace años. "
            "Cuando lo pide ella, suena a reclamo. Cuando lo escribe el LLM, suena a hoja de Excel. La pareja se "
            "sienta con el prompt y le dice “divídenos las tareas según tiempo libre real, no según género”. "
            "Imprimen el output. Lo pegan en la nevera. La autoridad del cronograma viene de afuera."
        ),
        "hashtags": "#choreschedule · #contratomatrimonio · #cronogramadetareas · #aiarbitro · #dividirporIA",
        "hero_stat": ("47%", "de usuarios fuertes de IA se sienten más confiados al usarla en momentos de inseguridad para decidir.", "Accenture · 2025-10"),
        "triggers": [
            T("“árbitro IA”", "47%", "más confianza al usar IA en decisiones difíciles. La autoridad neutral que la pareja no encuentra adentro.", "Accenture · 2025-10"),
            T("“default parent”", "viral 2025", "Default Parent Syndrome generó demanda explícita de soluciones estructuradas para equidad doméstica.", "Mother.ly · 2025"),
            T("“roles negociados”", "FG-04", "“Yo quiero definir unos roles para a veces aligerar la carga” — Código Casa confirma demanda local.", "Código Casa · 2024"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Mother.ly — Lilian Schmidt y la IA que estructura la operación doméstica completa. Caso modelo del cronograma firmado por el LLM.",
              "Mother.ly · 2025",
              "macro-2-0-motherly-ai-mental-load.png",
              "https://www.mother.ly/parenting/how-ai-is-helping-this-mom-reduce-mental-load/"),
            S("TREND",
              "Axios — feminización ChatGPT. Indicador estructural de quién está mandando los prompts de organización doméstica.",
              "Axios · 2025-09-30",
              "macro-2-1-axios-chatgpt-feminizado.png",
              "https://www.axios.com/2025/09/30/chatgpt-pulse-ai-assistant-moms"),
            S("INNOVACIÓN",
              "Merca 2.0 — ChatGPT como mamá. Frame editorial que pavimenta audiencia para “operating system familiar”.",
              "Merca 2.0 · 2025",
              "macro-2-1-merca20-chatgpt-mama.png",
              "https://www.merca20.com/chatgpt-ya-es-mama-asi-ayuda-a-una-madre-a-criar-a-su-hijo-mientras-ella-descansa/"),
        ],
    },
    {
        "macro": 1, "code": "2.4",
        "headline": "LA TÍA QUE NO TIENE: CHATGPT CRIANDO",
        "tagline": "“La red familiar se mudó. El prompt no.”",
        "fenomeno": (
            "La mujer dominicana que migró del barrio, vive en SD a 40 minutos de su mamá y no tiene tía a la "
            "mano, le pregunta a ChatGPT lo que antes le preguntaba a la comadre. El hogar pasó de 4–5 personas "
            "(2005) a 2–3 (2022). La red intergeneracional se desarmó sin reemplazo. La IA llegó a ocupar la "
            "silla de la tía que ya no vive cerca. No con cariño. Con respuesta inmediata a las 11pm."
        ),
        "hashtags": "#mamasinred · #mividaenchatgpt · #parentingsolo · #aigrandma · #nuevocomadrazgo",
        "hero_stat": ("4–5 → 2–3", "personas en el hogar dominicano (2005 → 2022). La red intergeneracional ya no convive.", "ONE ENHOGAR"),
        "triggers": [
            T("“hogar encogido”", "4–5 → 2–3", "personas por hogar RD (2005 → 2022). La comadre real ya no vive en la casa.", "ONE ENHOGAR"),
            T("“third supporter”", "97%", "Lilian Schmidt reduce 97% mental load con ChatGPT como “tercera adulta”.", "Mother.ly · 2025"),
            T("“chatgpt mamá”", "—", "Merca 2.0 + Independent Español documentan adopción hispana del frame “mamá viral por usar IA para criar”.", "Merca 2.0 / Independent · 2025"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Red Uno Bolivia — visualiza el hueco que llena el prompt en hogares sin red.",
              "TikTok @redunotv · 2025",
              "macro-2-1-tiktok-nina-chatgpt-tarea-redunotv.png",
              "https://www.tiktok.com/@redunotv/video/7524731891031870726"),
            S("TREND",
              "Independent Español — madre viral ChatGPT. Sustitución de red familiar por LLM con cobertura editorial hispana.",
              "Independent Español · 2025",
              "macro-2-1-independent-mom-chatgpt.png",
              "https://www.independentespanol.com/estilo/chatgpt-consejos-paternidad-madres-inteligencia-artificial-b2803910.html"),
            S("INNOVACIÓN",
              "Merca 2.0 — “ChatGPT ya es mamá”. Frame listo para retail infantil, telemedicina pediátrica, edtech.",
              "Merca 2.0 · 2025",
              "macro-2-1-merca20-chatgpt-mama.png",
              "https://www.merca20.com/chatgpt-ya-es-mama-asi-ayuda-a-una-madre-a-criar-a-su-hijo-mientras-ella-descansa/"),
        ],
    },
    {
        "macro": 1, "code": "2.5",
        "headline": "EL PAPÁ QUE ANTES NO PREGUNTABA",
        "tagline": "“La pantalla es el primer lugar donde admite que no sabe.”",
        "fenomeno": (
            "El hombre dominicano que nunca preguntó cómo educar a un hijo le pregunta a ChatGPT sin que su esposa "
            "se entere. La pantalla es el primer espacio donde puede decir “no sé” sin perder cara. Pregunta cómo "
            "hablar de sexualidad con un hijo de 11. Cómo apoyar a una hija con su primer período. Y mientras él "
            "pregunta en privado, Quique Rosas (Mx, 1.2M) modela paternidad activa en público."
        ),
        "hashtags": "#padreprompted · #papápresente · #nuevapaternidad · #dadchatgpt · #manualpapas",
        "hero_stat": ("50%", "de hombres jóvenes confía en al menos un influencer manosphere. La brecha de fuentes confiables.", "Equimundo / 19th News · 2025"),
        "triggers": [
            T("“no sé sin testigo”", "—", "la masculinidad RD vive crisis de información paterna — el hombre tradicionalmente no consulta ni admite vulnerabilidad.", "Código Casa + Vargas · 2024"),
            T("“manosphere first”", "~50%", "de hombres jóvenes confía en al menos un influencer manosphere — brecha de fuentes confiables.", "19th News · 2025-06"),
            T("“dadtok hispano”", "1.2M", "followers de Quique Rosas — “Aprendiendo a ser papá”, modelo público hispano de paternidad activa.", "TikTok @soyquiquerosas · 2023-2024"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Quique Rosas — “Aprendiendo a ser papá”. 1.2M followers. El modelo hispano público de paternidad activa.",
              "TikTok @soyquiquerosas · 2023",
              "macro-2-5-tiktok-quique-aprendiendo-papa.png",
              "https://www.tiktok.com/@soyquiquerosas/video/7229104569165597958"),
            S("TREND",
              "Mother.ly — la IA como third supporter. Aplica también del lado del papá que aprende sin testigos.",
              "Mother.ly · 2025",
              "macro-2-0-motherly-ai-mental-load.png",
              "https://www.mother.ly/parenting/how-ai-is-helping-this-mom-reduce-mental-load/"),
            S("INNOVACIÓN",
              "Axios — feminización ChatGPT. El papá callado está dentro del 47% restante, aprendiendo sin contarle a nadie.",
              "Axios · 2025-09-30",
              "macro-2-1-axios-chatgpt-feminizado.png",
              "https://www.axios.com/2025/09/30/chatgpt-pulse-ai-assistant-moms"),
        ],
    },
    # ─── MACRO 3
    {
        "macro": 2, "code": "3.1",
        "headline": "TRADWIFE CON SAZÓN EVANGÉLICA",
        "tagline": "“La mujer dominicana no se llama tradwife. Se llama esposa virtuosa.”",
        "fenomeno": (
            "El frame tradwife llegó a Hispanoamérica, pero RD no lo importó con su nombre original. Lo "
            "cristianizó. Lo que en TikTok anglo se llama tradwife — mujer que cocina desde cero, sumisión "
            "bíblica, marido proveedor — en feed hispano se llama “esposa virtuosa”, “mujer Proverbios 31”, "
            "“ama de casa con clase”. La rebeldía del 2026 contra el feminismo cansado no se viste con ropa "
            "de los 50 — se viste con cita bíblica."
        ),
        "hashtags": "#esposavirtuosa · #mujerproverbios31 · #stayathomewife · #esposacristiana · #tradwife",
        "hero_stat": ("RoRo + Omi", "Las dos caras hispanas del frame tradwife — España secular y evangélica panamericana. Sin nombrarlo así.", "TikTok · 2024-2025"),
        "triggers": [
            T("“esposa virtuosa”", "Prov 31:10", "@disciple_omi y @soy.valioso predican el rol esposa con cita bíblica — currículum oculto evangélico.", "TikTok · 2024-2025"),
            T("“faith family femininity”", "—", "Boldlatina: Latina tradwives redefinen debate de roles con conexión evangélica/católica explícita.", "Boldlatina · 2024-2025"),
            T("“neoliberal choice”", "—", "Bloomberg Línea: tradwife en LATAM articulado con lógica neoliberal de “libre elección”.", "Bloomberg Línea · 2024-2025"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "@disciple_omi — “El valor de una esposa virtuosa según Proverbios 31:10-12”. Currículum oculto evangélico en español.",
              "TikTok @disciple_omi · 2025",
              "macro-3-1-tiktok-mujer-virtuosa-disciple-omi.png",
              "https://www.tiktok.com/@disciple_omi/video/7581944388549496077"),
            S("TREND",
              "El Mundo — RoRo López Bueno: 22 años, cocina y edita libros para su novio. La cara hispana del trend tradwife global.",
              "TikTok @elmundo.es · 2024-07",
              "macro-3-1-tiktok-roro-tradwife.png",
              "https://www.tiktok.com/@elmundo.es/video/7395159521426967841"),
            S("INNOVACIÓN",
              "Boldlatina — “Faith, Family and Femininity”. Frame editorial para marcas que quieran hablarle al segmento sin equivocarse de tono.",
              "Boldlatina · 2024-2025",
              "macro-3-1-boldlatina-latina-tradwives.png",
              "https://www.boldlatina.com/faith-family-and-femininity-latina-tradwives-redefine-the-gender-roles-debate/"),
        ],
    },
    {
        "macro": 2, "code": "3.2",
        "headline": "EL ALGORITMO QUE LE HABLA AL HIJO VARÓN",
        "tagline": "“Mientras mami vigila lo que ve Lulú, el feed de Zahir ya tomó decisión.”",
        "fenomeno": (
            "Las mamás dominicanas vigilan con lupa el feed de las hijas — clean girl, body image, predadores. "
            "Mientras tanto, el feed del hijo varón ya entró a la manosphere sin permiso de nadie. Tate doblado al "
            "español, “high value males”, sigma rules, “redpill 101”. En 5 días un perfil nuevo masculino joven "
            "recibe 4x más contenido misógino sugerido por TikTok. El currículum oculto digital lo arma un "
            "algoritmo que premia indignación de género."
        ),
        "hashtags": "#manosphere · #alphamale · #sigmamale · #redpill · #radicalizaciondigital",
        "hero_stat": ("4×", "más contenido misógino sugerido por TikTok a perfiles jóvenes masculinos en solo 5 días.", "El Nacional · 2025"),
        "triggers": [
            T("“4x en 5 días”", "4×", "aumento contenido misógino sugerido por TikTok a perfiles jóvenes masculinos en 5 días.", "El Nacional · 2025"),
            T("“tate español”", "—", "@highvaluemales + @andrew.tate.espanol confirman Tate dentro del feed hispano joven sin fricción de idioma.", "TikTok · 2022-2025"),
            T("“marbella hub”", "—", "OCCRP: Marbella hotspot de influencers manosphere alineados con Tate. Geografía hispanoparlante.", "OCCRP · 2024-2025"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "@highvaluemales — Andrew Tate doblado al español. Evidencia directa del manosphere en feed hispano joven.",
              "TikTok @highvaluemales · 2022-2025",
              "macro-3-2-tiktok-andrew-tate-espanol.png",
              "https://www.tiktok.com/@highvaluemales/video/7115901381503978758"),
            S("TREND",
              "The 19th — “Algoritmos, alpha males y tradwives”. Cifra Equimundo 50%. Frame editorial más afilado del 2025.",
              "The 19th · 2025-06",
              "macro-3-2-19thnews-alpha-males.png",
              "https://19thnews.org/2025/06/internet-culture-algorithms-alpha-males-tradwives/"),
            S("INNOVACIÓN",
              "OCCRP — Marbella manosphere hub. España como puente cultural hacia el hijo dominicano.",
              "OCCRP · 2024-2025",
              "macro-3-2-occrp-marbella-manosphere.png",
              "https://www.occrp.org/en/feature/sun-cigars-and-sexism-how-spains-marbella-became-a-hotspot-for-manosphere-influencers"),
        ],
    },
    {
        "macro": 2, "code": "3.3",
        "headline": "STAY-AT-HOME GIRLFRIEND CON DELIVERY",
        "tagline": "“La fantasía de no trabajar la consume la mujer que trabaja para todos.”",
        "fenomeno": (
            "El feed feminizado le vende a la mujer joven la fantasía de no trabajar y cuidar la casa con estética "
            "clean girl. Morning routine de 20 minutos. Skincare. Tender la cama con cojines. La realidad RD impone "
            "otro guion: 53.5% participación laboral femenina y cargando la casa además. La SAHG se consume como "
            "ASMR de descanso imaginado por mujeres que entran a la oficina a las 8am. Lo aspiracional es la pausa."
        ),
        "hashtags": "#stayathomegirlfriend · #cleangirl · #sahg · #thatgirl · #softlife",
        "hero_stat": ("53.5%", "participación laboral femenina RD vs 78.3% masculina. La fantasía choca con la realidad económica.", "Banco Mundial · 2024"),
        "triggers": [
            T("“soft life”", "53.5% / 78.3%", "participación laboral femenina vs masculina RD. La pausa es lujo, no rol.", "Banco Mundial · 2024"),
            T("“girlboss → SAHG”", "Sage 2025", "“From girlboss to #stayathomegirlfriend”: paper académico que nombra y legitima el frame.", "Sage Journals · 2025"),
            T("“ASMR aspiracional”", "—", "@aliyahwears + @lexiixi sostienen el cluster SAHG global con estética clean girl.", "TikTok · 2023-2025"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "@aliyahwears — “Day in the life of a stay-home girlfriend”. Referente global con estética que ya viaja al For You dominicano.",
              "TikTok @aliyahwears · 2023",
              "macro-3-3-tiktok-sahg-aliyah.png",
              "https://www.tiktok.com/@aliyahwears/video/7275392594656496938"),
            S("TREND",
              "Sage — “Romanticisation of domestic labour on TikTok”. Paper Isabel Sykes 2025 que legitima el frame como objeto de estudio.",
              "Sage Journals · 2025",
              "macro-3-3-sage-stayathomegirlfriend.png",
              "https://journals.sagepub.com/doi/10.1177/13675494241285643"),
            S("INNOVACIÓN",
              "@lexiixi — Morning routine SAHG. ASMR aspiracional del “no trabajar”. Útil para bienestar, skincare, delivery doméstico.",
              "TikTok @lexiixi · 2025",
              "macro-3-3-tiktok-sahg-lexiixi-morning.png",
              "https://www.tiktok.com/@lexiixi/video/7548267212381900045"),
        ],
    },
    {
        "macro": 2, "code": "3.4",
        "headline": "#DADTOK: EL PAPÁ QUE GRABA LA CRIANZA",
        "tagline": "“El #DadTok hispano existe. RD aún no produce sus propios Quiques.”",
        "fenomeno": (
            "En México, Quique Rosas tiene 1.2M followers grabando paternidad activa — cocina, peina niñas, "
            "limpia la casa. Univision le dedicó un feature a #TribuDePapas (+3.8M views). El #DadTok hispano "
            "ya armó cluster con creadores rentables. Y RD no produjo todavía sus Quiques. Hay un nicho enorme "
            "abierto: el creador masculino dominicano que normalice tareas y crianza con tracción local."
        ),
        "hashtags": "#dadtok · #paternidadactiva · #papápresente · #tribudepapás · #papásrd",
        "hero_stat": ("1.2M / 0", "followers de Quique Rosas en MX vs creadores DadTok dominicanos con tracción comparable.", "Team Trends CC · 2026"),
        "triggers": [
            T("“tribu de papás”", "+3.8M", "views #TribuDePapas (Mx): 10 cuentas de papás viralizan tareas domésticas.", "Univision · 2024"),
            T("“quique rosas”", "1.2M", "followers — “¿Por qué limpio la casa? Las relaciones funcionan porque las personas están dispuestas a hacerlas funcionar.”", "TikTok @soyquiquerosas · 2024"),
            T("“gap local”", "0", "creadores RD masculinos en #DadTok con tracción comparable. Cluster sin nombre local — ventana abierta.", "Team Trends CC · 2026"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "Quique Rosas — “¿Por qué limpio la casa?”. Verbatim oro: el papá hispano que normaliza la tarea con argumento, no con disculpa.",
              "TikTok @soyquiquerosas · 2024",
              "macro-3-4-tiktok-quique-limpiar-casa.png",
              "https://www.tiktok.com/@soyquiquerosas/video/7380877040385346822"),
            S("TREND",
              "Univision — #TribuDePapas. Cobertura del cluster mexicano con dato +3.8M views; argumenta caso de mercado.",
              "Univision · 2024",
              "macro-3-4-univision-tribudepapas.png",
              "https://www.univision.com/entretenimiento/cultura-pop/tiktok-hombres-normalizan-laborales-hogar-paternidad"),
            S("INNOVACIÓN",
              "Quique Rosas — “Día como papá primerizo”. Formato replicable que una marca RD (banca, retail infantil) podría financiar.",
              "TikTok @soyquiquerosas · 2024",
              "macro-3-4-tiktok-quique-rosas-papa-primerizo.png",
              "https://www.tiktok.com/@soyquiquerosas/video/7351217922259340549"),
        ],
    },
    {
        "macro": 2, "code": "3.5",
        "headline": "LA SUEGRA SE LLAMA ALGORITMO",
        "tagline": "“La autoridad doméstica migró de la familia política al For You.”",
        "fenomeno": (
            "Lo que antes definía la suegra — cómo se cuida un bebé, qué se cocina, cómo se trata al marido — "
            "ahora lo define la momfluencer. Las mamás dominicanas siguen 20+ creadoras extranjeras, aplican "
            "rutinas que no calzan con el clima local, y entran en choque con la suegra real cuando coinciden "
            "el sábado. La intergeneracionalidad perdió frente al algoritmo personalizado. Y el algoritmo no "
            "opina por amor — opina por engagement."
        ),
        "hashtags": "#momfluencer · #mamastips · #momtok · #crianzatok · #consejosdemamá",
        "hero_stat": ("15%", "de consumidores globales compra productos puramente porque son tendencia en TikTok.", "SAP Emarsys · 2025-10"),
        "triggers": [
            T("“suegra fuera”", "4–5 → 2–3", "personas por hogar RD (2005-2022). La suegra ya no convive con la nuera.", "ONE ENHOGAR"),
            T("“tiktok jurado”", "15%", "consumidores globales compra por trend TikTok puro. Autoridad de feed > autoridad familiar.", "SAP Emarsys · 2025-10"),
            T("“feed segmentado”", "4×", "contenido sugerido por algoritmo en perfiles segmentados por género en 5 días.", "El Nacional · 2025"),
        ],
        "proofs": [
            S("PRUEBA TIKTOK",
              "@disciple_omi — la momfluencer evangélica como nueva autoridad sobre rol esposa. Sustituye el sermón presencial de la suegra.",
              "TikTok @disciple_omi · 2025",
              "macro-3-1-tiktok-mujer-virtuosa-disciple-omi.png",
              "https://www.tiktok.com/@disciple_omi/video/7581944388549496077"),
            S("TREND",
              "El Nacional — el mismo motor que polariza hombres también personaliza autoridad doméstica femenina.",
              "El Nacional · 2025",
              "macro-3-0-elnacional-tiktok-misogino.png",
              "https://www.elnacional.cat/es/sociedad/tiktok-impulsa-contenido-misogino-extremo-entre-hombres-jovenes_1154811_102.html"),
            S("INNOVACIÓN",
              "Boldlatina — frame editorial que muestra cómo se construye una momfluencer-suegra hispana en 2025.",
              "Boldlatina · 2024-2025",
              "macro-3-1-boldlatina-latina-tradwives.png",
              "https://www.boldlatina.com/faith-family-and-femininity-latina-tradwives-redefine-the-gender-roles-debate/"),
        ],
    },
]


# ─────────────────────────────────────────────────────────────
# Slide builders
# ─────────────────────────────────────────────────────────────

prs = Presentation()
prs.slide_width = Pt(SLIDE_W_PT)
prs.slide_height = Pt(SLIDE_H_PT)
blank = prs.slide_layouts[6]


def render_proof(slide, x, y, proof, is_pending=False):
    """Render a single proof (label, image, badge, caption, source) starting at (x,y).
    Returns Y position after rendering."""
    cur = y
    # Label
    add_text(slide, x, cur, COL_W, 12, proof["label"],
             font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
    cur += 16

    # image area
    img_path = SCREENSHOTS / proof["screenshot"]
    if is_pending or not img_path.exists():
        add_placeholder_pending(slide, x, cur, IMG_W, IMG_H, url=proof.get("url"))
    else:
        add_image(slide, str(img_path), x, cur, IMG_W, IMG_H, hyperlink=proof.get("url"))
    # badge
    add_click_badge(slide, x + IMG_W, cur)
    cur += IMG_H + 8

    # caption
    add_text(slide, x, cur, COL_W, 60, proof["caption"],
             font=FONT_SANS, size=8, color=WHITE, line_spacing=1.0)
    cur += 56

    # source inline
    add_text(slide, x, cur, COL_W, 10, proof["src"],
             font=FONT_SANS, size=6.5, color=GRAY_SRC, upper=True, tracking=150)
    cur += 14
    return cur


def render_trigger(slide, x, y, trig):
    cur = y
    # Keyword italic serif
    add_text(slide, x, cur, COL_W, 28, f'“{trig["keyword"].strip("“”")}”' if not trig["keyword"].startswith("“") else trig["keyword"],
             font=FONT_SERIF, size=22, italic=True, color=WHITE, line_spacing=1.0)
    cur += 28
    # stat
    add_text(slide, x, cur, COL_W, 22, trig["stat"],
             font=FONT_SERIF, size=18, color=WHITE, line_spacing=1.0)
    cur += 22
    # desc body
    add_text(slide, x, cur, COL_W, 60, trig["desc"],
             font=FONT_SANS, size=8, color=WHITE, line_spacing=1.0)
    cur += 48
    # source
    add_text(slide, x, cur, COL_W, 10, trig["src"],
             font=FONT_SANS, size=6.5, color=GRAY_SRC, upper=True, tracking=150)
    cur += 16
    return cur


def build_macro_intro_slide(macro):
    slide = prs.slides.add_slide(blank)
    slide_chrome(slide, macro["tab"])

    # ── col-left: tagline + behavior
    cy = CONTENT_Y
    # Headline = macro name
    add_text(slide, COL_LEFT_X, cy, COL_W, 80, macro["name"],
             font=FONT_SERIF, size=44, color=WHITE, upper=True, line_spacing=0.95)
    cy += 110
    # tagline italic
    add_text(slide, COL_LEFT_X, cy, COL_W, 80, macro["tagline"],
             font=FONT_SERIF, size=20, italic=True, color=WHITE, line_spacing=1.1)
    cy += 80
    # label "EL COMPORTAMIENTO"
    add_text(slide, COL_LEFT_X, cy, COL_W, 12, "EL COMPORTAMIENTO",
             font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
    cy += 14
    add_text(slide, COL_LEFT_X, cy, COL_W, 240, macro["behavior"],
             font=FONT_SANS, size=8, color=WHITE, line_spacing=1.0)

    # ── col-center: 3 triggers
    cy = CONTENT_Y
    add_text(slide, COL_CENTER_X, cy, COL_W, 12, "3 TRIGGERS",
             font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
    cy += 18
    for t in macro["triggers"]:
        cy = render_trigger(slide, COL_CENTER_X, cy, t) + 16

    # ── col-right: 3 proofs
    cy = CONTENT_Y
    add_text(slide, COL_RIGHT_X, cy, COL_W, 12, "3 PRUEBAS",
             font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
    cy += 18
    # Para macro intro mostramos 1 prueba grande con foto y 2 más compactas debajo
    p = macro["proofs"][0]
    cy = render_proof(slide, COL_RIGHT_X, cy, p)
    cy += 10
    # 2 proofs sin foto, solo label + caption + src
    for p in macro["proofs"][1:]:
        add_text(slide, COL_RIGHT_X, cy, COL_W, 12, p["label"],
                 font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
        cy += 14
        add_text(slide, COL_RIGHT_X, cy, COL_W, 50, p["caption"],
                 font=FONT_SANS, size=8, color=WHITE, line_spacing=1.0)
        cy += 48
        add_text(slide, COL_RIGHT_X, cy, COL_W, 10, p["src"],
                 font=FONT_SANS, size=6.5, color=GRAY_SRC, upper=True, tracking=150)
        cy += 18


def build_micro_slide(micro):
    macro = MACROS[micro["macro"]]
    slide = prs.slides.add_slide(blank)
    slide_chrome(slide, macro["tab"])

    # ── col-left: headline + tagline + EL FENÓMENO + HASHTAGS
    cy = CONTENT_Y
    # micro code small label
    add_text(slide, COL_LEFT_X, cy, COL_W, 12, f"MICRO {micro['code']}",
             font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
    cy += 14
    # Headline 50pt - puede ocupar varias líneas
    add_text(slide, COL_LEFT_X, cy, COL_W, 200, micro["headline"],
             font=FONT_SERIF, size=42, color=WHITE, upper=True, line_spacing=0.95)
    cy += 180
    # Tagline
    add_text(slide, COL_LEFT_X, cy, COL_W, 60, micro["tagline"],
             font=FONT_SERIF, size=18, italic=True, color=WHITE, line_spacing=1.05)
    cy += 70

    # EL FENÓMENO label
    add_text(slide, COL_LEFT_X, cy, COL_W, 12, "EL FENÓMENO",
             font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
    cy += 14
    add_text(slide, COL_LEFT_X, cy, COL_W, 160, micro["fenomeno"],
             font=FONT_SANS, size=8, color=WHITE, line_spacing=1.0)
    cy += 150

    # HASHTAGS
    add_text(slide, COL_LEFT_X, cy, COL_W, 12, "HASHTAGS",
             font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
    cy += 14
    add_text(slide, COL_LEFT_X, cy, COL_W, 60, micro["hashtags"],
             font=FONT_SERIF, size=14, color=WHITE, line_spacing=1.1)

    # ── col-center: hero stat + 3 triggers
    cy = CONTENT_Y
    add_text(slide, COL_CENTER_X, cy, COL_W, 12, "HERO + TRIGGERS",
             font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
    cy += 16
    # Hero stat
    hero_stat = micro["hero_stat"]
    # Decidir tamaño hero
    hero_size = 96 if micro["code"] in {"1.1", "1.2", "2.1", "3.1", "3.2"} else 72
    add_text(slide, COL_CENTER_X, cy, COL_W, 120, hero_stat[0],
             font=FONT_SERIF, size=hero_size, color=WHITE, line_spacing=0.95)
    cy += hero_size + 10
    add_text(slide, COL_CENTER_X, cy, COL_W, 50, hero_stat[1],
             font=FONT_SANS, size=8, color=WHITE, line_spacing=1.0)
    cy += 40
    add_text(slide, COL_CENTER_X, cy, COL_W, 10, hero_stat[2],
             font=FONT_SANS, size=6.5, color=GRAY_SRC, upper=True, tracking=150)
    cy += 20

    # 3 triggers compactos
    for t in micro["triggers"]:
        cy = render_trigger(slide, COL_CENTER_X, cy, t) + 8

    # ── col-right: 3 SEÑALES con fotos
    cy = CONTENT_Y
    # Top 2 proofs en una fila + 1 abajo? No: layout vertical compacto
    # Renderizamos las 3 en columna con tamaño 149x180 (un poco más bajo para caber)
    # Pero la regla pide 149x220 exacto. Vamos con 149x150 para tres en columna sin overflow? Eso rompe regla.
    # Mejor: dos filas de proofs. Fila 1: 1 proof grande 149x220. Fila 2: 2 proofs lado a lado más pequeños.
    p0 = micro["proofs"][0]
    is_pending_p0 = "[SCREENSHOT PENDIENTE" in p0.get("caption", "")
    # Label + image grande
    add_text(slide, COL_RIGHT_X, cy, COL_W, 12, p0["label"],
             font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
    cy += 14
    img_path = SCREENSHOTS / p0["screenshot"]
    if img_path.exists():
        add_image(slide, str(img_path), COL_RIGHT_X, cy, IMG_W, IMG_H, hyperlink=p0.get("url"))
    else:
        add_placeholder_pending(slide, COL_RIGHT_X, cy, IMG_W, IMG_H, url=p0.get("url"))
    add_click_badge(slide, COL_RIGHT_X + IMG_W, cy)
    # caption al lado derecho de la foto
    cap_x = COL_RIGHT_X + IMG_W + 14
    cap_w = COL_W - IMG_W - 14
    add_text(slide, cap_x, cy, cap_w, 180, p0["caption"],
             font=FONT_SANS, size=8, color=WHITE, line_spacing=1.0)
    add_text(slide, cap_x, cy + 180, cap_w, 12, p0["src"],
             font=FONT_SANS, size=6.5, color=GRAY_SRC, upper=True, tracking=150)
    cy += IMG_H + 16

    # Fila inferior: proofs 1 y 2 lado a lado, tamaño compacto
    proofs_below = micro["proofs"][1:3]
    small_w = (COL_W - 12) / 2
    # Mantener ratio aprox 149:220, escalando proporcional
    small_img_w = small_w
    small_img_h = small_img_w * (IMG_H / IMG_W)
    # No demasiado alto; restringimos
    if small_img_h > 160:
        small_img_h = 160
        small_img_w = small_img_h * (IMG_W / IMG_H)
    for i, p in enumerate(proofs_below):
        px = COL_RIGHT_X + i * (small_w + 12)
        add_text(slide, px, cy, small_w, 12, p["label"],
                 font=FONT_SANS, size=8, bold=True, color=GRAY_LABEL, upper=True, tracking=100)
        ipath = SCREENSHOTS / p["screenshot"]
        iy = cy + 14
        if ipath.exists():
            add_image(slide, str(ipath), px, iy, small_img_w, small_img_h, hyperlink=p.get("url"))
        else:
            add_placeholder_pending(slide, px, iy, small_img_w, small_img_h, url=p.get("url"))
        add_click_badge(slide, px + small_img_w, iy)
        # caption corto debajo
        cy_cap = iy + small_img_h + 8
        cap_text = p["caption"]
        # truncar si muy largo
        if len(cap_text) > 160:
            cap_text = cap_text[:157] + "…"
        add_text(slide, px, cy_cap, small_w, 60, cap_text,
                 font=FONT_SANS, size=7, color=WHITE, line_spacing=1.0)
        add_text(slide, px, cy_cap + 56, small_w, 10, p["src"],
                 font=FONT_SANS, size=6.5, color=GRAY_SRC, upper=True, tracking=150)


# ─────────────────────────────────────────────────────────────
# Build deck
# ─────────────────────────────────────────────────────────────

# Slide 1: Macro 1 intro
build_macro_intro_slide(MACROS[0])
# Slides 2-6: micros 1.1..1.5
for m in [x for x in MICROS if x["macro"] == 0]:
    build_micro_slide(m)
# Slide 7: Macro 2 intro
build_macro_intro_slide(MACROS[1])
# Slides 8-12: micros 2.1..2.5
for m in [x for x in MICROS if x["macro"] == 1]:
    build_micro_slide(m)
# Slide 13: Macro 3 intro
build_macro_intro_slide(MACROS[2])
# Slides 14-18: micros 3.1..3.5
for m in [x for x in MICROS if x["macro"] == 2]:
    build_micro_slide(m)

OUTPUT_PPTX.parent.mkdir(parents=True, exist_ok=True)
prs.save(str(OUTPUT_PPTX))

print(f"OK · {len(prs.slides)} slides → {OUTPUT_PPTX}")
