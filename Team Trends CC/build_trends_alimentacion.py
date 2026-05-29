#!/usr/bin/env python3
"""
Build script — Trend Forecast ALIMENTACIÓN
Capítulo 04 · Código Casa · NINJA Thinking

REGLAS DURAS (aprendizajes-montador-trends-cc.md):
1. Headline 20pt FIJO — NO 42-50pt, NO auto-fit
2. Triggers: cifra ARRIBA, caja descriptiva ABAJO (stack vertical, NO side-by-side)
3. Fotos señales: 110×162pt EXACTO (NO 149×220pt)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml
import lxml.etree as etree

# ─── PATHS ───────────────────────────────────────────────────────────────────
BASE = "/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC"
SCREENSHOTS = os.path.join(BASE, "screenshots/trends-alimentacion")
OUT_PPTX = os.path.join(BASE, "outputs/trends-alimentacion-forecast.pptx")

# ─── COLORS ──────────────────────────────────────────────────────────────────
C_BG       = RGBColor(0x0D, 0x0D, 0x0D)
C_WHITE    = RGBColor(0xFF, 0xFF, 0xFF)
C_GRAY     = RGBColor(0xA0, 0xA0, 0xA0)
C_DARK     = RGBColor(0x66, 0x66, 0x66)
C_RED      = RGBColor(0xFF, 0x2D, 0x2D)
C_TABFILL  = RGBColor(0xE8, 0xE8, 0xE8)
C_BLACK    = RGBColor(0x00, 0x00, 0x00)
C_PLACEHOLDER = RGBColor(0x22, 0x22, 0x22)

# ─── DIMENSIONS ──────────────────────────────────────────────────────────────
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# Grid in points (960pt wide × 540pt tall)
MARGIN_LEFT   = Pt(28)
MARGIN_TOP    = Pt(28)
MARGIN_RIGHT  = Pt(28)
CONTENT_W     = Pt(960 - 56)   # 904pt
CONTENT_H     = Pt(540 - 56)   # 484pt

# Column widths
COL_LEFT_W    = Pt(int(904 * 0.33))   # ~298pt
COL_CENTER_W  = Pt(int(904 * 0.34))   # ~307pt
COL_RIGHT_W   = Pt(int(904 * 0.33))   # ~298pt

COL_LEFT_X    = MARGIN_LEFT
COL_CENTER_X  = MARGIN_LEFT + COL_LEFT_W + Pt(3)
COL_RIGHT_X   = COL_CENTER_X + COL_CENTER_W + Pt(3)

# Vertical layout anchors
TAB_Y         = MARGIN_TOP
TAB_H         = Pt(20)
LABEL_Y       = TAB_Y + TAB_H + Pt(4)
LABEL_H       = Pt(12)
HLINE_Y       = LABEL_Y + LABEL_H
CONTENT_TOP   = HLINE_Y + Pt(8)

# Photo dimensions — RULE 3: 110×162pt EXACTO
PHOTO_W       = Pt(110)
PHOTO_H       = Pt(162)
PHOTO_GAP     = Pt(8)   # 3×162+2×8=502pt, start at MARGIN_TOP(28) → bottom=530 < 540 OK
CAPTION_W     = Pt(170)
CAPTION_H     = Pt(35)
CAPTION_OFFSET_X = Pt(8)

# Trigger layout — RULE 2: stat ARRIBA, caja ABAJO
STAT_H        = Pt(82)
DESC_W        = Pt(170)
DESC_H        = Pt(35)
SOURCE_H      = Pt(12)
TRIGGER_GAP   = Pt(5)


# ─── HELPERS ─────────────────────────────────────────────────────────────────

def add_bg(slide, color=C_BG):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_rect(slide, x, y, w, h, fill_color=None, line_color=None):
    shape = slide.shapes.add_shape(
        1,  # RECTANGLE
        left=int(x), top=int(y), width=int(w), height=int(h)
    )
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = int(Pt(1))
    else:
        shape.line.fill.background()
    return shape


def add_text_box(slide, x, y, w, h, text, font_name, font_size, color,
                 bold=False, italic=False, align=PP_ALIGN.LEFT,
                 word_wrap=True, line_spacing=None, uppercase=False):
    txBox = slide.shapes.add_textbox(int(x), int(y), int(w), int(h))
    txBox.word_wrap = word_wrap
    tf = txBox.text_frame
    tf.word_wrap = word_wrap
    tf.auto_size = None
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.alignment = align
    if line_spacing is not None:
        p.line_spacing = line_spacing

    run = p.add_run()
    run.text = text.upper() if uppercase else text
    run.font.name = font_name
    run.font.size = int(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txBox


def add_line(slide, x1, y1, x2, y2, color, width=Pt(1)):
    connector = slide.shapes.add_connector(1, int(x1), int(y1), int(x2), int(y2))
    connector.line.color.rgb = color
    connector.line.width = int(width)
    return connector


def add_picture_safe(slide, img_path, x, y, w, h):
    if img_path and os.path.isfile(img_path):
        try:
            pic = slide.shapes.add_picture(img_path, int(x), int(y), int(w), int(h))
            return pic, True
        except Exception:
            pass
    # Placeholder
    shape = add_rect(slide, x, y, w, h,
                     fill_color=C_PLACEHOLDER,
                     line_color=RGBColor(0x33, 0x33, 0x33))
    add_text_box(slide,
                 x + Pt(4), y + int(h / 2) - Pt(10),
                 w - Pt(8), Pt(20),
                 "CAPTURA MANUAL — JEREMY",
                 "Poppins", Pt(8), C_DARK,
                 bold=True, align=PP_ALIGN.CENTER)
    return shape, False


def add_hyperlink_to_shape(shape, url):
    if not url:
        return
    try:
        sp = shape._element
        # Try pic first, then sp
        nvPicPr = sp.find('.//' + qn('p:nvPicPr'))
        nvSpPr  = sp.find('.//' + qn('p:nvSpPr'))
        nvPr = None
        if nvPicPr is not None:
            nvPr = nvPicPr.find(qn('p:nvPr'))
        elif nvSpPr is not None:
            nvPr = nvSpPr.find(qn('p:nvPr'))
        if nvPr is None:
            return
        slide_part = shape.part
        rId = slide_part.relate_to(
            url,
            'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',
            is_external=True
        )
        hlinkClick = parse_xml(
            f'<a:hlinkClick xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"'
            f' xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
            f' r:id="{rId}"/>'
        )
        nvPr.append(hlinkClick)
    except Exception:
        pass


def add_badge(slide, photo_x, photo_y, photo_w):
    """Add red CLICK ME badge at top-right corner of photo."""
    badge_w = Pt(42)
    badge_h = Pt(14)
    badge_x = photo_x + photo_w - badge_w
    badge_y = photo_y
    add_rect(slide, badge_x, badge_y, badge_w, badge_h, fill_color=C_RED)
    add_text_box(slide, badge_x, badge_y, badge_w, badge_h,
                 "CLICK ME", "Poppins", Pt(7), C_WHITE,
                 bold=True, align=PP_ALIGN.CENTER)


# ─── SLIDE BUILDERS ──────────────────────────────────────────────────────────

def build_divider(prs, macro_num, macro_name, tagline):
    """Macro divider slide — name only, no content."""
    slide_layout = prs.slide_layouts[6]  # blank
    slide = prs.slides.add_slide(slide_layout)
    add_bg(slide)

    label_h   = Pt(22)
    gap1      = Pt(16)
    name_h    = Pt(115)
    gap2      = Pt(14)
    tagline_h = Pt(40)
    total_h   = label_h + gap1 + name_h + gap2 + tagline_h

    block_top = Pt(540 / 2) - total_h / 2

    # MACRO N label
    add_text_box(slide,
                 x=Pt(0), y=block_top,
                 w=Pt(960), h=label_h,
                 text=f"MACRO {macro_num}",
                 font_name="Poppins", font_size=Pt(14),
                 color=C_GRAY, bold=True,
                 align=PP_ALIGN.CENTER, uppercase=True)

    # Macro name — Instrument Serif 100pt
    add_text_box(slide,
                 x=Pt(80), y=block_top + label_h + gap1,
                 w=Pt(800), h=name_h,
                 text=macro_name,
                 font_name="Instrument Serif", font_size=Pt(100),
                 color=C_WHITE, bold=False,
                 align=PP_ALIGN.CENTER, uppercase=True)

    # Tagline — Instrument Serif Italic 24pt
    add_text_box(slide,
                 x=Pt(80), y=block_top + label_h + gap1 + name_h + gap2,
                 w=Pt(800), h=tagline_h,
                 text=f'"{tagline}"',
                 font_name="Instrument Serif", font_size=Pt(24),
                 color=C_GRAY, bold=False, italic=True,
                 align=PP_ALIGN.CENTER)

    return slide


def build_micro(prs, macro_num, macro_name,
                headline, fenomeno, hashtags, needs,
                triggers, signals):
    """
    Micro slide — 3 columns.

    RULE 1: headline 20pt FIJO
    RULE 2: triggers — stat ARRIBA, caja ABAJO (stack vertical)
    RULE 3: photos 110×162pt EXACTO
    """
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    add_bg(slide)

    inner_left_w = COL_LEFT_W - Pt(8)
    inner_center_w = COL_CENTER_W - Pt(10)

    # ── TABS ─────────────────────────────────────────────────────────────
    tab_macro_w = Pt(58)
    tab_name_w  = Pt(185)

    add_rect(slide, COL_LEFT_X, TAB_Y, tab_macro_w, TAB_H, fill_color=C_TABFILL)
    add_text_box(slide, COL_LEFT_X, TAB_Y, tab_macro_w, TAB_H,
                 f"MACRO {macro_num}", "Poppins", Pt(7.5),
                 C_BLACK, bold=True, align=PP_ALIGN.CENTER, uppercase=True)

    tab_name_x = COL_LEFT_X + tab_macro_w + Pt(4)
    add_rect(slide, tab_name_x, TAB_Y, tab_name_w, TAB_H,
             fill_color=None,
             line_color=RGBColor(0x55, 0x55, 0x55))
    add_text_box(slide, tab_name_x + Pt(4), TAB_Y, tab_name_w - Pt(8), TAB_H,
                 macro_name, "Poppins", Pt(7.5),
                 C_GRAY, bold=False, align=PP_ALIGN.LEFT, uppercase=True)

    # ── COLUMN LABELS ────────────────────────────────────────────────────
    add_text_box(slide, COL_LEFT_X, LABEL_Y, inner_left_w, LABEL_H,
                 "DEFINICIÓN", "Poppins", Pt(8),
                 C_GRAY, bold=True, uppercase=True)
    add_text_box(slide, COL_CENTER_X, LABEL_Y, inner_center_w, LABEL_H,
                 "TRIGGERS", "Poppins", Pt(8),
                 C_GRAY, bold=True, uppercase=True)
    add_text_box(slide, COL_RIGHT_X, LABEL_Y, COL_RIGHT_W - Pt(8), LABEL_H,
                 "SEÑALES", "Poppins", Pt(8),
                 C_GRAY, bold=True, uppercase=True)

    # ── DIVIDERS ─────────────────────────────────────────────────────────
    line_color = RGBColor(0x20, 0x20, 0x20)
    total_w = COL_LEFT_W + Pt(3) + COL_CENTER_W + Pt(3) + COL_RIGHT_W
    # Horizontal
    add_line(slide,
             MARGIN_LEFT, HLINE_Y,
             MARGIN_LEFT + total_w, HLINE_Y,
             color=line_color)
    # Vertical 1
    vx1 = COL_CENTER_X - Pt(2)
    add_line(slide, vx1, LABEL_Y, vx1, Pt(540) - MARGIN_TOP, color=line_color)
    # Vertical 2
    vx2 = COL_RIGHT_X - Pt(2)
    add_line(slide, vx2, LABEL_Y, vx2, Pt(540) - MARGIN_TOP, color=line_color)

    # ═══════════════════════════════════════════════════════════════════════
    # COL-LEFT: DEFINICIÓN
    # ═══════════════════════════════════════════════════════════════════════
    cy = CONTENT_TOP

    # HEADLINE — RULE 1: 20pt FIJO, Instrument Serif UPPERCASE, word-wrap
    headline_box_h = Pt(72)
    add_text_box(slide, COL_LEFT_X, cy, inner_left_w, headline_box_h,
                 headline,
                 "Instrument Serif", Pt(20),
                 C_WHITE, bold=False, italic=False,
                 align=PP_ALIGN.LEFT, word_wrap=True,
                 uppercase=True)
    cy += headline_box_h + Pt(6)

    # EL FENÓMENO label
    add_text_box(slide, COL_LEFT_X, cy, inner_left_w, Pt(12),
                 "EL FENÓMENO", "Poppins", Pt(8),
                 C_GRAY, bold=True, uppercase=True)
    cy += Pt(14)

    # Body — Poppins 10pt white
    add_text_box(slide, COL_LEFT_X, cy, inner_left_w, Pt(88),
                 fenomeno, "Poppins", Pt(10),
                 C_WHITE, word_wrap=True, line_spacing=1.0)
    cy += Pt(88) + Pt(8)

    # HASHTAGS label
    add_text_box(slide, COL_LEFT_X, cy, inner_left_w, Pt(12),
                 "HASHTAGS", "Poppins", Pt(8),
                 C_GRAY, bold=True, uppercase=True)
    cy += Pt(14)

    # Hashtags — Instrument Serif 23pt (NEVER Poppins)
    if isinstance(hashtags, list):
        hashtag_str = " · ".join(hashtags)
    else:
        hashtag_str = hashtags
    add_text_box(slide, COL_LEFT_X, cy, inner_left_w, Pt(52),
                 hashtag_str, "Instrument Serif", Pt(23),
                 C_WHITE, word_wrap=True)
    cy += Pt(52) + Pt(6)

    # 3 NEEDS label
    add_text_box(slide, COL_LEFT_X, cy, inner_left_w, Pt(12),
                 "3 NEEDS", "Poppins", Pt(8),
                 C_GRAY, bold=True, uppercase=True)
    cy += Pt(14)

    # Needs — Instrument Serif 28pt UPPERCASE
    if isinstance(needs, list):
        needs_str = " · ".join(needs)
    else:
        needs_str = needs
    add_text_box(slide, COL_LEFT_X, cy, inner_left_w, Pt(40),
                 needs_str, "Instrument Serif", Pt(28),
                 C_WHITE, bold=False, uppercase=True, word_wrap=True)

    # ═══════════════════════════════════════════════════════════════════════
    # COL-CENTER: TRIGGERS
    # RULE 2: cifra ARRIBA, caja descriptiva ABAJO — pure stack vertical
    # ═══════════════════════════════════════════════════════════════════════
    ty = CONTENT_TOP

    for trig in triggers[:3]:
        stat_text   = trig.get("stat", "")
        desc_text   = trig.get("desc", "")
        source_text = trig.get("source", "")

        # Font size for stat based on length
        slen = len(stat_text)
        if slen <= 4:
            stat_pt = Pt(80)
        elif slen <= 8:
            stat_pt = Pt(64)
        elif slen <= 12:
            stat_pt = Pt(48)
        else:
            stat_pt = Pt(36)

        # CIFRA/STAT ARRIBA
        add_text_box(slide, COL_CENTER_X, ty,
                     inner_center_w, STAT_H,
                     stat_text, "Instrument Serif", stat_pt,
                     C_WHITE, bold=False, italic=False,
                     align=PP_ALIGN.LEFT, word_wrap=True)
        ty += STAT_H

        # CAJA DESCRIPTIVA ABAJO — W170×H35pt, Poppins 10pt
        add_text_box(slide, COL_CENTER_X, ty,
                     DESC_W, DESC_H,
                     desc_text, "Poppins", Pt(10),
                     C_WHITE, word_wrap=True, line_spacing=1.0)
        ty += DESC_H + Pt(2)

        # FUENTE INLINE — Poppins 7pt #666
        if source_text:
            add_text_box(slide, COL_CENTER_X, ty,
                         inner_center_w, SOURCE_H,
                         source_text.upper(),
                         "Poppins", Pt(7), C_DARK)
        ty += SOURCE_H + TRIGGER_GAP

    # ═══════════════════════════════════════════════════════════════════════
    # COL-RIGHT: SEÑALES
    # RULE 3: 3 fotos 110×162pt EXACTO + caption 170×35pt al lado
    # Math: 3×162 + 2×8 = 502pt, starting at MARGIN_TOP(28) → bottom=530pt < 540pt OK
    # ═══════════════════════════════════════════════════════════════════════
    sy = MARGIN_TOP

    for sig in signals[:3]:
        img_path    = sig.get("path", "")
        caption_txt = sig.get("caption", "")
        source_txt  = sig.get("source", "")
        url         = sig.get("url", "")

        # FOTO 110×162pt
        pic, found = add_picture_safe(slide, img_path,
                                      COL_RIGHT_X, sy,
                                      PHOTO_W, PHOTO_H)
        if url:
            add_hyperlink_to_shape(pic, url)

        # BADGE "CLICK ME"
        add_badge(slide, COL_RIGHT_X, sy, PHOTO_W)

        # CAPTION BOX at side — W170×H35pt, Poppins 10pt
        cap_x = COL_RIGHT_X + PHOTO_W + CAPTION_OFFSET_X
        add_text_box(slide, cap_x, sy,
                     CAPTION_W, CAPTION_H,
                     caption_txt, "Poppins", Pt(10),
                     C_WHITE, word_wrap=True, line_spacing=1.0)

        # Source inline under caption
        if source_txt:
            add_text_box(slide, cap_x, sy + CAPTION_H + Pt(2),
                         CAPTION_W, SOURCE_H,
                         source_txt.upper(),
                         "Poppins", Pt(7), C_DARK)

        sy += PHOTO_H + PHOTO_GAP

    return slide


# ─── DATA ────────────────────────────────────────────────────────────────────

MACRO_1 = {
    "num": 1,
    "name": "INVENTOLOGÍA DE LA ADULTEZ",
    "tagline": "Un mundo en crisis está reescribiendo qué significa ser adulto y formar familia."
}

MACRO_2 = {
    "num": 2,
    "name": "LOS HERNÁNDEZ ARE PROMPTED",
    "tagline": "El dominicano ya entró al mundo prompteado. Solo no lo nombra así."
}

MACRO_3 = {
    "num": 3,
    "name": "ALGORITMO DEL HOGAR",
    "tagline": "El feed se sentó en la mesa y nadie le ofreció silla."
}


def p(filename):
    return os.path.join(SCREENSHOTS, filename)


SLIDES_DATA = [
    # ── MACRO 1 DIVIDER ──────────────────────────────────────────────────
    {"type": "divider", **MACRO_1},

    # ── MICRO 1.1 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 1,
        "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "headline": "La generación sin tiempo entre semana descubrió que dos horas el domingo le devuelven la semana entera.",
        "fenomeno": "El joven dominicano prepara comidas el domingo para ahorrar tiempo, comer mejor y controlar lo que ingiere. No es dieta — es autonomía. El meal prep entra como ritual de adultez sin mamá-cocinera detrás.",
        "hashtags": ["#MealPrepDominicano", "#DomingoDePrep", "#ControlDeLoQueComo", "#AdultoJovenRD", "#ComidaDeLaSemana"],
        "needs": ["CONTROL", "MIEDO", "SOLEDAD"],
        "triggers": [
            {"stat": "US$36B", "desc": "Mercado global de meal prep en 2026, CAGR 9.84% hasta 2035.", "source": "Market Reports World · 2026"},
            {"stat": "48%", "desc": "De adultos ya practica meal prep; 62% cita falta de tiempo como driver principal.", "source": "HelloFresh State of Home Cooking · 2025"},
            {"stat": "@morechulaa", "desc": "Creadora RD documenta meal prep de 4 días — tuppers etiquetados por día de la semana.", "source": "TikTok @morechulaa · 2025"},
        ],
        "signals": [
            {"path": p("macro-1-1-tiktok-morechulaa-mealprep.png"),
             "caption": "Creadora dominicana @morechulaa: meal prep 4 días con tuppers etiquetados por día.",
             "source": "TikTok @morechulaa · 2025",
             "url": "https://www.tiktok.com/@morechulaa/video/7636986702262717704"},
            {"path": p("macro-1-1-tiktok-viviankh-mealprep.png"),
             "caption": "@viviank.h documenta 10 sándwiches + 9 porciones congeladas — meal prep de 3 semanas.",
             "source": "TikTok @viviank.h · 2025",
             "url": "https://www.tiktok.com/@viviank.h/video/7620501104765177108"},
            {"path": p("macro-1-0-mktreports-mealprep-market.png"),
             "caption": "Chart: mercado global meal prep US$36,433M en 2026, CAGR 9.84% hasta 2035.",
             "source": "Market Reports World · 2026",
             "url": "https://www.marketreportsworld.com/market-reports/meal-prep-market-14713709"},
        ]
    },

    # ── MICRO 1.2 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 1,
        "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "headline": "Las empresas descubrieron que si el empleado come bien al mediodía rinde mejor en la tarde — y el menú de almuerzo se volvió beneficio.",
        "fenomeno": "Fripick deja que la empresa pague la comida y la descuente en quincena. La comida del mediodía dejó de ser problema individual del empleado — ahora es categoría B2B.",
        "hashtags": ["#LunchMenuRD", "#AlmuerzoDeTrabajo", "#MenúDelDía", "#PrecioAccesible", "#NegocioOyó"],
        "needs": ["DIGNIDAD", "VACÍO", "CONTROL"],
        "triggers": [
            {"stat": "+13%", "desc": "Tráfico YoY en restauración LATAM en horario almuerzo con shoulder hour pricing.", "source": "OpenTable Dining Trends / QSR Magazine · 2025"},
            {"stat": "84%", "desc": "Percibe los precios de alimentos como \"altos\"; dos tercios prefieren opciones más económicas.", "source": "Purdue University / Family Dinner Project · 2025"},
            {"stat": "Fripick", "desc": "Plataforma RD de beneficios alimentarios corporativos B2B operando con descuento de quincena.", "source": "Fripick.com · 2025"},
        ],
        "signals": [
            {"path": p("macro-1-2-tiktok-toyantoja-noccila-lunch.png"),
             "caption": "@toyantoja muestra lunch completo en Nocciola por menos de RD$500 — dato que \"vale oro\".",
             "source": "TikTok @toyantoja · 2025",
             "url": "https://www.tiktok.com/@toyantoja/video/7610215257000234247"},
            {"path": p("macro-1-2-fripick-rd-brand.png"),
             "caption": "Fripick RD — beneficio alimentario corporativo B2B, descuento directo en quincena.",
             "source": "Fripick · 2025",
             "url": "https://fripick.com"},
            {"path": None,
             "caption": "Inflación alimentaria RD: precios subieron 50% entre jul 2019 y jul 2025; 8.03% interanual ene 2026.",
             "source": "BCRD / Dominican Today · 2026",
             "url": ""},
        ]
    },

    # ── MICRO 1.3 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 1,
        "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "headline": "Te crió con miedo a lo \"malo\" y ahora comer se siente como culpa. TikTok escuchó el término y lo convirtió en trend con millones de views.",
        "fenomeno": "La mamá que controlaba cada bocado crió hijas con relación rota con el plato. La almond mom no es solo un meme — es una cadena generacional. El trauma tiene hashtag ahora.",
        "hashtags": ["#AlmondMom", "#TraumasDietéticos", "#ComerConCulpa", "#GeneraciónSinRefresco", "#LaVozDeMamá"],
        "needs": ["CULPA", "RESENTIMIENTO", "REPARACIÓN"],
        "triggers": [
            {"stat": "30M", "desc": "Americanos desarrollarán un trastorno alimentario en su vida. 2a enfermedad mental más mortal.", "source": "ANAD / ABC News · 2025"},
            {"stat": "42%", "desc": "De niñas de 1°-3° quiere ser más delgada; 81% de niños de 10 años teme engordar.", "source": "ANAD Statistics · 2025"},
            {"stat": "#almondmom", "desc": "Hashtag viral con millones de views — trauma dietético heredado como contenido de TikTok.", "source": "TikTok · 2025"},
        ],
        "signals": [
            {"path": p("macro-1-3-tiktok-lielle-almondmom.png"),
             "caption": "@Lielle & Dee recrea rutina matutina bajo #almondmom — suplementos, restricción heredada sin cuestionamiento.",
             "source": "TikTok @liellewaldman17 · 2025",
             "url": "https://www.tiktok.com/@liellewaldman17/video/7617943870797630750"},
            {"path": p("macro-1-3-tiktok-nourvilaa-almondmom.png"),
             "caption": "@nour vilà — versión francesa/LATAM del trauma dietético heredado de mamá bajo #almondmum.",
             "source": "TikTok @nourvilaa · 2025",
             "url": "https://www.tiktok.com/@nourvilaa/video/7642383470026657046"},
            {"path": None,
             "caption": "ANAD 2025: 30M americanos desarrollarán un trastorno alimentario — 2da enfermedad mental más mortal.",
             "source": "ANAD · 2025",
             "url": ""},
        ]
    },

    # ── MICRO 1.4 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 1,
        "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "headline": "La diferencia entre un domingo con familia y uno solo se mide en una pregunta: ¿qué vamos a comer?",
        "fenomeno": "Para el foráneo que vive solo, el domingo es el día más difícil — sin ritual, sin mesa, con delivery en la cama. La mesa familiar se volvió FaceTime con plato distinto a cada lado.",
        "hashtags": ["#DomingoSolo", "#AlmuerzoDeFamilia", "#SancochoDelDomingo", "#ForáneoEnLaCapital", "#SinMesaNoHayDomingo"],
        "needs": ["SOLEDAD", "PERTENENCIA", "INVISIBILIDAD"],
        "triggers": [
            {"stat": "45%", "desc": "De hogares come junto menos que hace una década; 84% querría compartir más comidas.", "source": "Simirity / FMI Foundation · 2025"},
            {"stat": "84%", "desc": "Querría más comidas familiares; 62% de padres no logra cenar con la frecuencia deseada.", "source": "FMI Foundation · 2026"},
            {"stat": "17%", "desc": "De familias dominicanas no comparte las horas de comida — el foráneo es ese porcentaje.", "source": "Código Casa · P25 · 2024"},
        ],
        "signals": [
            {"path": p("macro-1-4-tiktok-josheilyn-foranea-capital.png"),
             "caption": "@Josheilyn de los Santos — \"yo amo estar en mi hogar los domingos\" — foránea RD en la capital.",
             "source": "TikTok @josheilyndls1 · 2025",
             "url": "https://www.tiktok.com/@josheilyndls1/video/7549991019169811768"},
            {"path": p("macro-1-4-tiktok-mariannycorderoo-domingo.png"),
             "caption": "@mariannycorderoo — domingo solo en Bogotá preparándose una tostada con #amorpropio.",
             "source": "TikTok @mariannycorderoo · 2025",
             "url": "https://www.tiktok.com/@mariannycorderoo/video/7643570804885572882"},
            {"path": p("macro-1-4-tiktok-macaseason-domingo-familiar.png"),
             "caption": "@María Camila — el domingo familiar completo; contraste con el domingo solo del foráneo.",
             "source": "TikTok @macaseason · 2025",
             "url": "https://www.tiktok.com/@macaseason/video/7625031259835665685"},
        ]
    },

    # ── MICRO 1.5 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 1,
        "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "headline": "PedidosYa es la app #1 de food en RD: el adulto joven ya no decide qué cocinar entre semana, decide qué pedir — y esa es su nueva forma de ser adulto.",
        "fenomeno": "La adultez tradicional cocinaba todos los días. La adultez 2026 delega el jueves a una app. No es flojera — es renegociación del rol de \"buen adulto\" en una economía donde el tiempo cuesta más que la comida.",
        "hashtags": ["#PedidosYaRD", "#DeliveryEsMiMamá", "#AdultoQueNoCocina", "#JuevesDeApp", "#ComerSinCocinar"],
        "needs": ["CONTROL", "SOLEDAD", "CULPA"],
        "triggers": [
            {"stat": "#1", "desc": "PedidosYa app #1 food & drink iOS en RD con 13K-21.7K descargas semanales Q1 2025.", "source": "Sensor Tower · Q1 2025"},
            {"stat": "50%", "desc": "Subida de precios alimentos en RD entre jul 2019 y jul 2025 — delivery se vuelve cálculo costo-tiempo.", "source": "BCRD / Dominican Today · 2026"},
            {"stat": "Online", "desc": "Primer supermercado 100% online abre en Santo Domingo — la grocería migra a app.", "source": "St Kitts Nevis Observer · 2025"},
        ],
        "signals": [
            {"path": p("macro-1-5-pedidosya-country-selector.png"),
             "caption": "Pantalla PedidosYa con República Dominicana listada + badges App Store y Google Play.",
             "source": "PedidosYa · 2026",
             "url": "https://www.pedidosya.com"},
            {"path": p("macro-1-5-sensortower-pedidosya-rd-chart.png"),
             "caption": "Bar chart Sensor Tower: PedidosYa #1 en descargas food delivery RD, Q1 2025.",
             "source": "Sensor Tower · Q1 2025",
             "url": "https://sensortower.com"},
            {"path": p("macro-1-5-stkitts-online-super-sd.png"),
             "caption": "Primer supermercado 100% online que abre en Santo Domingo — la grocería migra a app.",
             "source": "St Kitts Nevis Observer · 2025",
             "url": "https://www.thestkittsnevisobserver.com/first-online-only-supermarket-opens-in-santo-domingo/"},
        ]
    },

    # ── MACRO 2 DIVIDER ──────────────────────────────────────────────────
    {"type": "divider", **MACRO_2},

    # ── MICRO 2.1 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 2,
        "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "headline": "Una foto de tu plato no sabe lo que comes. Pero el algoritmo te convence de que sí — y le crees más a la app que a tu propio cuerpo.",
        "fenomeno": "Las apps de conteo calórico pasaron de herramienta a obsesión. El algoritmo que \"te ayuda a comer mejor\" se convierte en la voz que condena cada nutriente. El número en pantalla pesa más que la sensación de saciedad.",
        "hashtags": ["#AppQueEnfermó", "#MyFitnessPalToxic", "#AlgoritmoDeMiDieta", "#ContarCalorías", "#ComerConMiedo"],
        "needs": ["MIEDO", "CULPA", "CONTROL"],
        "triggers": [
            {"stat": "180M", "desc": "Usuarios de MyFitnessPal; 75% de pacientes con trastorno alimentario la usaba.", "source": "GripRoom / PMC NLM · 2026"},
            {"stat": "73%", "desc": "De pacientes con trastorno alimentario creyó que la app contribuyó a su desarrollo.", "source": "PMC NLM · 2026"},
            {"stat": "#toxic", "desc": "#myfitnesspaltoxic y #calorietracking — creadoras documentan recuperación de relación rota con apps.", "source": "TikTok · 2025-2026"},
        ],
        "signals": [
            {"path": p("macro-2-1-myfitnesspal-app-ui.png"),
             "caption": "Mockup MyFitnessPal: 976 cal + macro breakdown del día — \"Nutrition tracking for real life\".",
             "source": "MyFitnessPal · 2026",
             "url": "https://www.myfitnesspal.com"},
            {"path": None,
             "caption": "PMC NLM 2026: apps con IA de reconocimiento por foto funcionan como gateway a trastorno alimentario.",
             "source": "Sage Journals / Ohio State · 2024-2026",
             "url": ""},
            {"path": None,
             "caption": "Búsqueda TikTok: \"MyFitnessPal ruined me\" — backlash de creadoras documentando recuperación.",
             "source": "TikTok · 2025-2026",
             "url": ""},
        ]
    },

    # ── MICRO 2.2 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 2,
        "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "headline": "Antes mamá decidía qué había de comer. Hoy lo decide el For You Page — y de paso te vende los ingredientes en el mismo scroll.",
        "fenomeno": "El joven dominicano abre TikTok antes de abrir el refrigerador. Las recetas virales compiten con la tradición oral heredada — y en muchos hogares jóvenes el algoritmo está ganando.",
        "hashtags": ["#TikTokRecetas", "#ForYouPageDeCocina", "#RecetaViralVsAbuela", "#QuéComiHoy", "#AlgoritmoDeAlmuerzo"],
        "needs": ["VACÍO", "CONTROL", "SOLEDAD"],
        "triggers": [
            {"stat": "42", "desc": "Índice pico de contenido food en TikTok en enero 2026 — plataforma como primer recetario.", "source": "Accio / TikTok Food Trends · 2026"},
            {"stat": "US$759M", "desc": "GMV food en TikTok Shop 2025 — food = 13.6% del volumen total de la plataforma.", "source": "Capital One Shopping · 2025"},
            {"stat": "2×", "desc": "Ventas de marcas grandes en TikTok Shop casi duplicaron en 2025.", "source": "Modern Retail · 2025"},
        ],
        "signals": [
            {"path": p("macro-2-2-tiktokshop-food-gmv.png"),
             "caption": "TikTok es el nuevo recetario Y el nuevo supermercado — food = 13.6% del GMV de TikTok Shop 2025.",
             "source": "Resourcera · 2026",
             "url": "https://resourcera.com/data/social/tiktok-shop-statistics/"},
            {"path": p("macro-2-2-modernretail-tiktokshop-brands.png"),
             "caption": "Modern Retail: ventas de marcas grandes en TikTok Shop casi duplicaron en 2025.",
             "source": "Modern Retail · 2025",
             "url": "https://www.modernretail.co/technology/sales-from-major-brands-on-tiktok-shop-nearly-doubled-in-2025-drawing-ulta-and-sally-beauty/"},
            {"path": None,
             "caption": "Fine Dining Lovers 2025: creadores latinos reconocidos como \"transmisión cultural adaptada a 2025\".",
             "source": "Fine Dining Lovers ES · 2025",
             "url": ""},
        ]
    },

    # ── MICRO 2.3 (iPad Kid — proxy) ─────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 2,
        "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "headline": "El truco de poner un video para que el niño coma se convirtió en condición — el iPad es la única forma de que el plato baje.",
        "fenomeno": "El niño no come sin el iPad. La pantalla dejó de ser acompañamiento y se volvió condición. La mesa familiar tiene un competidor que casi siempre gana.",
        "hashtags": ["#iPadKid", "#PantallaMientrasCome", "#NetflixYCena", "#MesaSinPantalla", "#ComerSinPantalla"],
        "needs": ["CULPA", "SOLEDAD", "INVISIBILIDAD"],
        "triggers": [
            {"stat": "40%", "desc": "De niños tiene iPad a los 2 años; 2.6 hrs/día promedio de pantalla; solo 1% cumple límites.", "source": "Common Sense Media · 2025"},
            {"stat": "2.6h", "desc": "Promedio diario de pantalla en niños; comer con pantalla desconecta señales de hambre/saciedad.", "source": "ScienceDirect / Business Standard · 2026"},
            {"stat": "UNICEF", "desc": "Kids Online: exposición infantil a pantallas más temprana y menos mediada en LATAM/RD.", "source": "UNICEF Kids Online · 2024-2025"},
        ],
        "signals": [
            {"path": p("macro-2-3-newsmedical-screentime-proxy.png"),
             "caption": "Proxy: inyección de semaglutide + headline sobre cómo la tech interviene en cómo comemos.",
             "source": "News Medical · 2026",
             "url": "https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx"},
            {"path": None,
             "caption": "CAPTURA MANUAL: búsqueda TikTok \"mi hijo no come sin tablet\" RD/LATAM — verbatim madres.",
             "source": "TikTok · 2025",
             "url": ""},
            {"path": None,
             "caption": "Common Sense Media 2025: 40% de niños tiene iPad a los 2 años — límites de pantalla incumplidos.",
             "source": "Common Sense Media · 2025",
             "url": ""},
        ]
    },

    # ── MICRO 2.4 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 2,
        "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "headline": "El consumidor sano se pega un sensor de glucosa por dos semanas y descubre que la uva le sube más el azúcar que el helado. La nutrición ya es dato en tiempo real.",
        "fenomeno": "Los wearables de glucosa OTC salieron del nicho diabético y entraron al consumer health. El \"comer bien\" dejó de ser opinión — ahora es métrica continua que cambia qué desayunas mañana.",
        "hashtags": ["#LingoRD", "#SensorDeGlucosa", "#ComerConDato", "#MetabolicAge", "#ElPlatoYElGráfico"],
        "needs": ["CONTROL", "MIEDO", "VACÍO"],
        "triggers": [
            {"stat": "US$80B", "desc": "Mercado de wearables y health tracking en 2024 → proyecta US$200B+ para 2030.", "source": "Statista · 2025"},
            {"stat": "Lingo", "desc": "Abbott Lingo (CGM sin prescripción) expande a Android dic 2025 — sensor 14 días en Walmart/Amazon.", "source": "Abbott Newsroom · 2025"},
            {"stat": "#glucose", "desc": "#glucosegoddess (Jessie Inchauspé) cruza cientos de millones de views — \"glucose hacks\" como género.", "source": "TikTok · 2025"},
        ],
        "signals": [
            {"path": p("macro-2-4-hellolingo-cgm-hero.png"),
             "caption": "Hero shot mujer con sensor Lingo en el brazo + \"My glucose, my insights\" — CGM OTC sin prescripción.",
             "source": "Abbott Lingo · 2025",
             "url": "https://www.hellolingo.com"},
            {"path": p("macro-2-4-scripps-cgm-sensor-arm.png"),
             "caption": "Foto AP: brazo con sensor de glucosa continuo — \"CGMs in vogue\" para consumidor no-diabético.",
             "source": "Scripps News / AP · 2025",
             "url": "https://www.scrippsnews.com/health/continuous-glucose-monitors-are-in-vogue-but-do-you-really-need-to-track-your-blood-sugar"},
            {"path": None,
             "caption": "Statista 2025: mercado wearables health tracking US$80B en 2024 hacia US$200B+ en 2030.",
             "source": "Statista · 2025",
             "url": ""},
        ]
    },

    # ── MICRO 2.5 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 2,
        "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "headline": "Una creadora cocina en vivo, te muestra el producto, lo agregas al carrito sin salir del feed. El supermercado se volvió streaming.",
        "fenomeno": "Live shopping pasó del nicho beauty al supermercado: snacks, salsas, kits de receta vendidos durante el video. Food es 13.6% del GMV de TikTok Shop. El próximo carrito del dominicano será un live stream.",
        "hashtags": ["#TikTokShopFood", "#CocinaEnVivo", "#CarritoDelFeed", "#LiveSnacks", "#CompraLoQueCocinas"],
        "needs": ["VACÍO", "CONTROL", "SOLEDAD"],
        "triggers": [
            {"stat": "US$64B", "desc": "GMV total TikTok Shop 2025 — food US$759.84M (13.6%), ticket promedio food shopper US$43.20.", "source": "Capital One Shopping / Resourcera · 2025"},
            {"stat": "+84%", "desc": "Live shopping creció 84% YoY en 2025; conversión live 6.1% vs feed 4.7%.", "source": "Resourcera · 2026"},
            {"stat": "2×", "desc": "Ventas de marcas grandes en TikTok Shop casi duplicaron en 2025.", "source": "Modern Retail · 2025"},
        ],
        "signals": [
            {"path": p("macro-2-5-modernretail-tiktokshop-2025.png"),
             "caption": "TikTok Shop visual — marcas grandes duplicaron ventas en 2025; food es categoría #1 del live shopping.",
             "source": "Modern Retail · 2025",
             "url": "https://www.modernretail.co/technology/sales-from-major-brands-on-tiktok-shop-nearly-doubled-in-2025-drawing-ulta-and-sally-beauty/"},
            {"path": p("macro-2-5-resourcera-tiktokshop-stats.png"),
             "caption": "Key Insights: GMV US$64.3B, ticket promedio food US$43.20, live shopping +84% YoY.",
             "source": "Resourcera · 2026",
             "url": "https://resourcera.com/data/social/tiktok-shop-statistics/"},
            {"path": p("macro-1-5-stkitts-online-super-sd.png"),
             "caption": "Primer supermercado 100% online en Santo Domingo — grocería digital prepara terreno para social commerce.",
             "source": "St Kitts Nevis Observer · 2025",
             "url": "https://www.thestkittsnevisobserver.com/first-online-only-supermarket-opens-in-santo-domingo/"},
        ]
    },

    # ── MACRO 3 DIVIDER ──────────────────────────────────────────────────
    {"type": "divider", **MACRO_3},

    # ── MICRO 3.1 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 3,
        "macro_name": "ALGORITMO DEL HOGAR",
        "headline": "Ver lo que otros comen se convirtió en uno de los formatos más consumidos de internet. Ya no es comida — es identidad.",
        "fenomeno": "\"What I Eat in a Day\" explota no por curiosidad culinaria — por validación. Ver lo que come otro para confirmar, comparar o inspirarse. El plato ajeno es espejo. Y juez.",
        "hashtags": ["#QuéComoEnUnDía", "#WhatIEatInADay", "#ComidaParaVer", "#AlimentaciónEnPantalla", "#DíaDeComidaRD"],
        "needs": ["VACÍO", "INVISIBILIDAD", "CULPA"],
        "triggers": [
            {"stat": "74%", "desc": "De personas usa redes para decidir qué o dónde comer; 50% dice que influyen directamente.", "source": "Cropink · 2026"},
            {"stat": "Top", "desc": "\"What I Eat in a Day\" entre top food trends 2026; formato genera engagement que el algoritmo premia.", "source": "Chowhound TikTok Trends · 2026"},
            {"stat": "2026", "desc": "Whole Foods predice year of the Fiber; protein-frenzy en backlash; bowl colorido como aspiracional.", "source": "VegNews / Whole Foods · 2026"},
        ],
        "signals": [
            {"path": p("macro-3-1-vegnews-food-trend-hero.png"),
             "caption": "Bowl proteína + grains + vegetales coloridos — el \"comer bien aspiracional 2026\" que WIEIAD replica.",
             "source": "VegNews · 2025",
             "url": "https://vegnews.com/fiber-whole-foods-2026-top-trend"},
            {"path": None,
             "caption": "Búsqueda TikTok: \"qué como en un día dominicana\" → adaptación local del formato WIEIAD.",
             "source": "TikTok · 2025-2026",
             "url": ""},
            {"path": None,
             "caption": "Cropink 2026: 74% usa redes para decidir qué comer; 50% dice que influyen directamente.",
             "source": "Cropink · 2026",
             "url": ""},
        ]
    },

    # ── MICRO 3.2 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 3,
        "macro_name": "ALGORITMO DEL HOGAR",
        "headline": "El mukbang nació porque hay gente que come sola y prefiere ver a alguien comer antes que comer en silencio.",
        "fenomeno": "Nació en Corea como compañía virtual. Hoy es negocio millonario. El dominicano lo consume porque la mesa vacía duele — y una pantalla llena el silencio del comedor.",
        "hashtags": ["#MukbangLatino", "#ComerSoloPeroNoTanto", "#AcompañamientoPorPantalla", "#SoledadEnLaMesa", "#CenarConPantalla"],
        "needs": ["SOLEDAD", "INVISIBILIDAD", "VACÍO"],
        "triggers": [
            {"stat": "5.3M", "desc": "#mukbang supera 5.3M videos en 2025; top creadores ganan hasta US$10K/mes.", "source": "Distraction Magazine / PMC · 2025"},
            {"stat": "2B+", "desc": "Nickocado Avocado supera 2B views en YouTube — mukbang como negocio millonario.", "source": "YouTube / PMC · 2025"},
            {"stat": "68.5%", "desc": "De jóvenes universitarias ve videos de comida regularmente; hasta 40 min/día — efecto parasocial.", "source": "Western Gazette / PMC · 2025-2026"},
        ],
        "signals": [
            {"path": p("macro-3-2-youtube-mukbang-search-grid.png"),
             "caption": "Grid resultados YouTube \"mukbang\" — thumbnails comida extrema, ASMR con millones de vistas.",
             "source": "YouTube · 2026",
             "url": "https://www.youtube.com/results?search_query=mukbang"},
            {"path": None,
             "caption": "PMC 2025: 68.5% de jóvenes ve videos de comida regularmente; vínculo con soledad y efecto parasocial.",
             "source": "Western Gazette / PMC · 2025-2026",
             "url": ""},
            {"path": None,
             "caption": "Distraction Magazine 2025: top mukbangers ganan hasta US$10K/mes — mukbang como negocio millonario.",
             "source": "Distraction Magazine · 2025",
             "url": ""},
        ]
    },

    # ── MICRO 3.3 (Cocina Terapia — proxy) ───────────────────────────────
    {
        "type": "micro",
        "macro_num": 3,
        "macro_name": "ALGORITMO DEL HOGAR",
        "headline": "Cuando todo lo demás está fuera de control, la cocina es el único sitio donde lo que hago sí sale como quiero.",
        "fenomeno": "Bajo burnout y presión social, adultos jóvenes descubrieron que cocinar y hornear son terapia real. No es hobbyismo — es el único espacio donde lo que controlas eres tú.",
        "hashtags": ["#CocinaComoTerapia", "#HornearParaDesestresarse", "#LoveLanguageCocina", "#Repostería", "#CocinaQueControlo"],
        "needs": ["SOLEDAD", "VACÍO", "CONTROL"],
        "triggers": [
            {"stat": "Dopamina", "desc": "Hornear activa rutas de dopamina y reduce cortisol — equivalente a mindfulness clínico.", "source": "Kaiser Permanente / NeuroLaunch / ICE · 2025-2026"},
            {"stat": "2026", "desc": "Ola de cancelaciones de delivery + vuelta a la cocina como anti-ansiedad digital.", "source": "EditorialGe / Cooking as Therapy · 2026"},
            {"stat": "GLP-1", "desc": "Medicalización del hambre crea contrapunto cultural: la cocina como ritual analógico.", "source": "News Medical · 2026"},
        ],
        "signals": [
            {"path": p("macro-3-3-newsmedical-cooking-proxy.png"),
             "caption": "Proxy: jeringa de medicamento + headline sobre cómo fármacos alteran el apetito — cocina como contrapunto.",
             "source": "News Medical · 2026",
             "url": "https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx"},
            {"path": None,
             "caption": "CAPTURA MANUAL: búsqueda Instagram #cookingastherapy — cocina como bienestar mental en creadoras LATAM.",
             "source": "TikTok / Instagram · 2025",
             "url": ""},
            {"path": None,
             "caption": "Kaiser Permanente: hornear activa dopamina y reduce cortisol equivalente a mindfulness clínico.",
             "source": "Kaiser Permanente / NeuroLaunch · 2025",
             "url": ""},
        ]
    },

    # ── MICRO 3.4 (Carnívora — proxy) ────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 3,
        "macro_name": "ALGORITMO DEL HOGAR",
        "headline": "El FOMO de bajar de peso llegó a su versión más extrema: eliminar todo lo que no sea animal. Los análisis de sangre cuentan otra historia.",
        "fenomeno": "Solo carne, mantequilla y huevo. El algoritmo lo distribuye más rápido que la evidencia clínica que lo contradice. El feed va más rápido que el cardiólogo.",
        "hashtags": ["#DietaCarnívora", "#SoloCarneMantequillaYHuevo", "#FOMODeBajarDePeso", "#ExtremoNutricional", "#CarnivoreVsColesterol"],
        "needs": ["MIEDO", "RESENTIMIENTO", "CONTROL"],
        "triggers": [
            {"stat": "2.6M", "desc": "#carnivore supera 2.6M publicaciones a noviembre 2025 — entre las dietas más comentadas.", "source": "ResearchGate / Fox News · 2025-2026"},
            {"stat": "LDL 172", "desc": "Revisión clínica Nutrients ene 2026: LDL promedio sube de 126 a 172 mg/dL en seguidores de carnivore.", "source": "Nutrients Journal · 2026"},
            {"stat": "Fibra", "desc": "Whole Foods predice 2026 = Year of the Fiber — mainstream pivota al opuesto mientras carnivore escala.", "source": "Whole Foods 2026 Trend Report · 2026"},
        ],
        "signals": [
            {"path": p("macro-3-4-vegnews-protein-fiber-trend.png"),
             "caption": "Hero food bowl — señal del pivot mainstream proteína→fibra, mientras carnivore escala en el algoritmo.",
             "source": "VegNews · 2025",
             "url": "https://vegnews.com/fiber-whole-foods-2026-top-trend"},
            {"path": None,
             "caption": "CAPTURA MANUAL: búsqueda YouTube/Instagram \"carnivore diet\" — thumbnails bistec + mantequilla + huevo.",
             "source": "TikTok / Instagram · 2025",
             "url": ""},
            {"path": None,
             "caption": "Nutrients Journal ene 2026: LDL promedio sube 126→172 mg/dL; caso reportado 163→365 en carnivore.",
             "source": "Nutrients Journal · 2026",
             "url": ""},
        ]
    },

    # ── MICRO 3.5 ────────────────────────────────────────────────────────
    {
        "type": "micro",
        "macro_num": 3,
        "macro_name": "ALGORITMO DEL HOGAR",
        "headline": "GLP-1 silencia el \"food noise\" del cerebro. La nueva conversación sobre comer no es qué cocinar — es si lo deseo o solo me acordé que existía.",
        "fenomeno": "Ozempic y Mounjaro reescriben la relación con la comida: ya no se trata de fuerza de voluntad, se trata de farmacología que apaga el ruido mental. El feed normaliza la conversación.",
        "hashtags": ["#FoodNoise", "#OzempicDiary", "#SinHambreSinAnsiedad", "#GLP1RD", "#LaCabezaSinComida"],
        "needs": ["VACÍO", "MIEDO", "SOLEDAD"],
        "triggers": [
            {"stat": "58%", "desc": "De usuarios GLP-1 siente menos hambre; 64% se llena antes; 21-23% reporta cambios de sabor.", "source": "EASD 2025 / News-Medical · 2025"},
            {"stat": "#foodnoise", "desc": "Hashtag viralizado por usuarias GLP-1 documentando cambio cognitivo — decenas de millones de views.", "source": "TikTok · 2025"},
            {"stat": "Longevity", "desc": "Whole Foods 2026: longevity y fibra como aspiracional opuesto al cuerpo medicado por GLP-1.", "source": "Whole Foods 2026 · 2026"},
        ],
        "signals": [
            {"path": p("macro-3-5-sciam-ozempic-food-noise.png"),
             "caption": "Ilustración surrealista: cabeza clásica con comida girando — \"Ozempic Quiets Food Noise in the Brain—But How?\"",
             "source": "Scientific American · Jun 2024",
             "url": "https://www.scientificamerican.com/article/ozempic-quiets-food-noise-in-the-brain-but-how/"},
            {"path": p("macro-3-5-newsmedical-glp1-appetite.png"),
             "caption": "Jeringa semaglutide — GLP-1 afecta apetito, estado de ánimo y comportamiento; 58% siente menos hambre.",
             "source": "News Medical · 2026",
             "url": "https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx"},
            {"path": None,
             "caption": "Búsqueda TikTok #foodnoise → top videos de usuarias GLP-1 documentando cambio cognitivo.",
             "source": "TikTok · 2025",
             "url": ""},
        ]
    },
]


# ─── BUILD ───────────────────────────────────────────────────────────────────

def main():
    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H

    for sd in SLIDES_DATA:
        if sd["type"] == "divider":
            build_divider(prs,
                          macro_num=sd["num"],
                          macro_name=sd["name"],
                          tagline=sd["tagline"])
        else:
            build_micro(prs,
                        macro_num=sd["macro_num"],
                        macro_name=sd["macro_name"],
                        headline=sd["headline"],
                        fenomeno=sd["fenomeno"],
                        hashtags=sd["hashtags"],
                        needs=sd["needs"],
                        triggers=sd["triggers"],
                        signals=sd["signals"])

    os.makedirs(os.path.dirname(OUT_PPTX), exist_ok=True)
    prs.save(OUT_PPTX)
    print(f"Saved: {OUT_PPTX}")
    print(f"Slides: {len(prs.slides)}")
    # Height check for photos
    three_photos_h = 3 * 162 + 2 * 8
    print(f"3-photo stack height check: 3×162 + 2×15 = {three_photos_h}pt (slide height 540pt) — {'OK' if three_photos_h <= 510 else 'OVERFLOW'}")


if __name__ == "__main__":
    main()
