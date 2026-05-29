"""
build_trends_alimentacion.py
Montador Trends CC — Capítulo 04 ALIMENTACIÓN
Aplica las 7 reglas duras del aprendizajes-montador-trends-cc.md

REGLAS APLICADAS:
  1. Headline 20pt FIJO Instrument Serif UPPERCASE tracking 0 line-height 1.1. Sin auto-fit.
  2. Triggers stack vertical: cifra ARRIBA 64pt → gap 10pt → caja desc 170×35pt Poppins 10pt → gap 6pt → fuente 7pt. Gap 24pt entre triggers.
  3. Fotos señales 95×140pt EXACTO. Gap 24pt entre fotos. Caption 170×35pt al lado (gap 8pt).
  4. NO 3 needs en el slide. Eliminadas.
  5. Hashtags 16pt Instrument Serif Regular (NO 23pt).
  6. Padding mínimo entre bloques en col-left: 24pt entre headline→fenómeno→hashtags.
  7. NO placeholders "CAPTURA MANUAL". Solo fotos reales. Si falta PNG → raise.
"""

from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree

# ─── PATHS ────────────────────────────────────────────────────────────────────
BASE  = Path("/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC")
SHOTS = BASE / "screenshots" / "trends-alimentacion"
OUT   = BASE / "outputs" / "trends-alimentacion-forecast.pptx"

# ─── CANVAS ───────────────────────────────────────────────────────────────────
prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)

SLIDE_W = prs.slide_width    # 9144000 EMU ≈ 960pt @ 72dpi
SLIDE_H = prs.slide_height   # 6858000 EMU ≈ 540pt

# ─── COLOURS ──────────────────────────────────────────────────────────────────
C_BG    = RGBColor(0x0D, 0x0D, 0x0D)
C_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
C_GREY_A0 = RGBColor(0xA0, 0xA0, 0xA0)
C_GREY_66 = RGBColor(0x66, 0x66, 0x66)
C_RED   = RGBColor(0xFF, 0x2D, 0x2D)
C_TAB_BG = RGBColor(0xE8, 0xE8, 0xE8)
C_SEP   = RGBColor(0xFF, 0xFF, 0xFF)

# ─── FONTS ────────────────────────────────────────────────────────────────────
FONT_SERIF = "Instrument Serif"
FONT_SANS  = "Poppins"

# ─── TYPE SIZES ───────────────────────────────────────────────────────────────
PT_HEADLINE   = Pt(20)    # Regla 1 — FIJO
PT_HASHTAGS   = Pt(16)    # Regla 5
PT_BODY_10    = Pt(10)
PT_LABEL_8    = Pt(8)
PT_SOURCE_7   = Pt(7)
PT_STAT       = Pt(64)    # Regla 2
PT_BADGE      = Pt(8)
PT_TAB        = Pt(8)
PT_MACRO_DIV  = Pt(100)
PT_TAGLINE    = Pt(24)
PT_MACRO_LBL  = Pt(14)

# ─── LAYOUT (all in EMU via Pt()) ─────────────────────────────────────────────
MARGIN_L = Pt(28)

# Column x-positions and widths
COL_W_L  = Pt(286)   # ~33%
COL_W_C  = Pt(300)   # ~34%
COL_W_R  = Pt(286)   # ~33%

COL_L_X  = MARGIN_L
SEP1_X   = COL_L_X + COL_W_L + Pt(8)
COL_C_X  = SEP1_X + Pt(10)
SEP2_X   = COL_C_X + COL_W_C + Pt(8)
COL_R_X  = SEP2_X + Pt(10)

# Regla 3: photos 95×140pt EXACTO
PHOTO_W  = Pt(95)
PHOTO_H  = Pt(140)
PHOTO_GAP = Pt(24)   # Regla 6

# Regla 2: trigger block dims
STAT_H       = Pt(72)
DESC_W       = Pt(170)
DESC_H       = Pt(35)
SRC_H        = Pt(12)
STAT_DESC_GAP = Pt(10)   # Regla 6
DESC_SRC_GAP  = Pt(6)    # Regla 6
TRIGGER_GAP   = Pt(24)   # Regla 6

# Tab + labels
TAB_H          = Pt(20)
TAB_TO_LABELS  = Pt(18)   # Regla 6
LABEL_H        = Pt(14)
LABEL_TO_HLINE = Pt(6)
HLINE_TO_CONTENT = Pt(16) # Regla 6

# Col-left gaps (Regla 6)
HL_BOX_H        = Pt(64)   # headline text box height
GAP_HL_PHENOM   = Pt(24)   # headline → label FENÓMENO
GAP_LBL_BODY    = Pt(6)    # label → body text
PHENOM_BOX_H    = Pt(72)   # body fenómeno
GAP_PHENOM_HT   = Pt(24)   # body → label HASHTAGS
HT_BOX_H        = Pt(42)   # hashtags box


# ─── HELPERS ──────────────────────────────────────────────────────────────────

def add_bg(slide):
    sp = slide.shapes.add_shape(1, Pt(0), Pt(0), SLIDE_W, SLIDE_H)
    sp.fill.solid()
    sp.fill.fore_color.rgb = C_BG
    sp.line.fill.background()
    slide.shapes._spTree.remove(sp._element)
    slide.shapes._spTree.insert(2, sp._element)


def add_tb(slide, text, x, y, w, h,
           font=FONT_SANS, size=Pt(10), bold=False, italic=False,
           color=C_WHITE, align=PP_ALIGN.LEFT,
           line_spacing=1.0, uppercase=False, wrap=True):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tb.word_wrap = wrap
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.auto_size = None
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    r = p.add_run()
    r.text = text.upper() if uppercase else text
    r.font.name  = font
    r.font.size  = size
    r.font.bold  = bold
    r.font.italic = italic
    r.font.color.rgb = color
    return tb


def add_sep_h(slide, x, y, w):
    """Thin horizontal separator rectangle ~15% white."""
    sp = slide.shapes.add_shape(1, x, y, w, Pt(0.5))
    sp.fill.solid()
    sp.fill.fore_color.rgb = C_SEP
    sp.line.fill.background()
    _set_alpha(sp._element.spPr.solidFill, 15000)


def add_sep_v(slide, x, y, h):
    """Thin vertical separator rectangle ~15% white."""
    sp = slide.shapes.add_shape(1, x, y, Pt(0.5), h)
    sp.fill.solid()
    sp.fill.fore_color.rgb = C_SEP
    sp.line.fill.background()
    _set_alpha(sp._element.spPr.solidFill, 15000)


def _set_alpha(solid_fill_el, val):
    if solid_fill_el is None:
        return
    for tag in (qn('a:srgbClr'), qn('a:sysClr'), qn('a:schemeClr')):
        clr = solid_fill_el.find(tag)
        if clr is not None:
            alpha = etree.SubElement(clr, qn('a:alpha'))
            alpha.set('val', str(val))
            return


def add_image_badge(slide, img_path, x, y, w, h, url):
    """Add image at exact dims with red badge + hyperlink."""
    if not Path(img_path).exists():
        raise FileNotFoundError(
            f"PNG faltante: {img_path}. Devolver al scrapper. NO placeholder."
        )
    pic = slide.shapes.add_picture(str(img_path), x, y, w, h)
    # Hyperlink
    if url:
        try:
            rId = slide.part.relate_to(
                url,
                "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
                is_external=True
            )
            hlinkClick = etree.SubElement(
                pic._element.nvPicPr.cNvPr,
                qn('a:hlinkClick')
            )
            hlinkClick.set(qn('r:id'), rId)
        except Exception:
            pass
    # Badge CLICK ME
    bw = Pt(50)
    bh = Pt(14)
    bx = x + w - bw
    by = y
    sp = slide.shapes.add_shape(1, bx, by, bw, bh)
    sp.fill.solid()
    sp.fill.fore_color.rgb = C_RED
    sp.line.fill.background()
    tf = sp.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "CLICK ME"
    r.font.name  = FONT_SANS
    r.font.size  = PT_BADGE
    r.font.bold  = True
    r.font.color.rgb = C_WHITE


# ─── MACRO DIVIDER ────────────────────────────────────────────────────────────

def build_macro_divider(num, name, tagline):
    sl = prs.slide_layouts[6]
    slide = prs.slides.add_slide(sl)
    add_bg(slide)

    cx = SLIDE_W // 2

    # Label "MACRO N"
    lw, lh = Pt(100), Pt(20)
    add_tb(slide, f"MACRO {num}",
           cx - lw // 2, Pt(185), lw, lh,
           font=FONT_SANS, size=PT_MACRO_LBL, bold=True,
           color=C_GREY_A0, align=PP_ALIGN.CENTER, uppercase=True)

    # Macro name 100pt Instrument Serif UPPERCASE
    nw, nh = Pt(920), Pt(200)
    nx, ny = cx - nw // 2, Pt(210)
    tb = add_tb(slide, name,
                nx, ny, nw, nh,
                font=FONT_SERIF, size=PT_MACRO_DIV,
                color=C_WHITE, align=PP_ALIGN.CENTER, uppercase=True)
    tb.text_frame.paragraphs[0].line_spacing = 0.95

    # Tagline Instrument Serif Italic 24pt
    tw, th = Pt(820), Pt(50)
    ty = ny + nh - Pt(70)
    add_tb(slide, f'"{tagline}"',
           cx - tw // 2, ty, tw, th,
           font=FONT_SERIF, size=PT_TAGLINE, italic=True,
           color=C_GREY_A0, align=PP_ALIGN.CENTER)


# ─── MICRO SLIDE ──────────────────────────────────────────────────────────────

def build_micro(macro_num, macro_name, micro_id,
                headline, fenomeno, hashtags,
                triggers, signals):
    """
    One micro-trend slide. 7 reglas duras aplicadas.
    signals: list of {png, caption, source, url} — 2 or 3 real PNGs.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide)

    # ── TAB ROW ──────────────────────────────────────────────────────────────
    tab_y = Pt(16)

    # "MACRO N" filled
    t1w, t1h = Pt(58), TAB_H
    sp1 = slide.shapes.add_shape(1, COL_L_X, tab_y, t1w, t1h)
    sp1.fill.solid(); sp1.fill.fore_color.rgb = C_TAB_BG
    sp1.line.fill.background()
    tf1 = sp1.text_frame; tf1.word_wrap = False
    p1 = tf1.paragraphs[0]; p1.alignment = PP_ALIGN.CENTER
    r1 = p1.add_run()
    r1.text = f"MACRO {macro_num}"
    r1.font.name = FONT_SANS; r1.font.size = PT_TAB
    r1.font.bold = True; r1.font.color.rgb = RGBColor(0x11,0x11,0x11)

    # Macro name outline tab
    t2x = COL_L_X + t1w + Pt(4)
    t2w, t2h = Pt(220), TAB_H
    sp2 = slide.shapes.add_shape(1, t2x, tab_y, t2w, t2h)
    sp2.fill.background()
    sp2.line.color.rgb = RGBColor(0x55,0x55,0x55); sp2.line.width = Pt(0.5)
    tf2 = sp2.text_frame; tf2.word_wrap = False
    p2 = tf2.paragraphs[0]; p2.alignment = PP_ALIGN.CENTER
    r2 = p2.add_run()
    r2.text = macro_name.upper()
    r2.font.name = FONT_SANS; r2.font.size = PT_TAB
    r2.font.bold = False; r2.font.color.rgb = C_GREY_A0

    # ── LABELS ───────────────────────────────────────────────────────────────
    lbl_y = tab_y + TAB_H + TAB_TO_LABELS

    for txt, lx, lw in [
        ("DEFINICIÓN", COL_L_X, COL_W_L),
        ("TRIGGERS",   COL_C_X, COL_W_C),
        ("SEÑALES",    COL_R_X, COL_W_R),
    ]:
        add_tb(slide, txt, lx, lbl_y, lw, LABEL_H,
               font=FONT_SANS, size=PT_LABEL_8, bold=True,
               color=C_GREY_A0, uppercase=True)

    # ── HORIZONTAL SEPARATOR ─────────────────────────────────────────────────
    hline_y = lbl_y + LABEL_H + LABEL_TO_HLINE
    sep_w   = SLIDE_W - MARGIN_L * 2
    add_sep_h(slide, COL_L_X, hline_y, sep_w)

    # Content starts here
    content_y = hline_y + HLINE_TO_CONTENT
    content_h = SLIDE_H - content_y - Pt(14)

    # ── VERTICAL SEPARATORS ──────────────────────────────────────────────────
    add_sep_v(slide, SEP1_X, hline_y - Pt(2), content_h + Pt(16))
    add_sep_v(slide, SEP2_X, hline_y - Pt(2), content_h + Pt(16))

    # ══════════════════════════════════════════════════════════════════════════
    # COL-LEFT: DEFINICIÓN
    # ══════════════════════════════════════════════════════════════════════════
    cy = content_y
    cw = COL_W_L - Pt(10)

    # HEADLINE — Regla 1: 20pt FIJO
    hl_tb = slide.shapes.add_textbox(COL_L_X, cy, cw, HL_BOX_H)
    hl_tb.word_wrap = True
    tf_hl = hl_tb.text_frame
    tf_hl.word_wrap = True
    tf_hl.auto_size = None
    p_hl = tf_hl.paragraphs[0]
    p_hl.line_spacing = 1.1
    r_hl = p_hl.add_run()
    r_hl.text = headline.upper()
    r_hl.font.name  = FONT_SERIF
    r_hl.font.size  = PT_HEADLINE   # 20pt — Regla 1, NO auto-fit
    r_hl.font.bold  = False
    r_hl.font.color.rgb = C_WHITE

    cy += HL_BOX_H + GAP_HL_PHENOM  # Regla 6: 24pt

    # Label EL FENÓMENO
    add_tb(slide, "EL FENÓMENO", COL_L_X, cy, cw, Pt(12),
           font=FONT_SANS, size=PT_LABEL_8, bold=True,
           color=C_GREY_A0, uppercase=True)
    cy += Pt(12) + GAP_LBL_BODY  # Regla 6: 6pt

    # Body fenómeno — Poppins Regular 10pt blanco line-spacing 1.0
    add_tb(slide, fenomeno, COL_L_X, cy, cw, PHENOM_BOX_H,
           font=FONT_SANS, size=PT_BODY_10, color=C_WHITE, line_spacing=1.0)
    cy += PHENOM_BOX_H + GAP_PHENOM_HT  # Regla 6: 24pt

    # Label HASHTAGS
    add_tb(slide, "HASHTAGS", COL_L_X, cy, cw, Pt(12),
           font=FONT_SANS, size=PT_LABEL_8, bold=True,
           color=C_GREY_A0, uppercase=True)
    cy += Pt(12) + GAP_LBL_BODY

    # Hashtags — Regla 5: 16pt Instrument Serif Regular
    ht_tb = slide.shapes.add_textbox(COL_L_X, cy, cw, HT_BOX_H)
    ht_tb.word_wrap = True
    tf_ht = ht_tb.text_frame
    tf_ht.word_wrap = True
    tf_ht.auto_size = None
    p_ht = tf_ht.paragraphs[0]
    p_ht.line_spacing = 1.0
    r_ht = p_ht.add_run()
    r_ht.text = hashtags
    r_ht.font.name  = FONT_SERIF   # NOT Poppins — Regla 5
    r_ht.font.size  = PT_HASHTAGS  # 16pt — Regla 5
    r_ht.font.bold  = False
    r_ht.font.color.rgb = C_WHITE

    # NO 3 Needs — Regla 4

    # ══════════════════════════════════════════════════════════════════════════
    # COL-CENTER: TRIGGERS — stack vertical (Regla 2)
    # Cifra ARRIBA → gap 10pt → caja desc 170×35pt ABAJO → gap 6pt → fuente 7pt
    # Gap 24pt ENTRE triggers
    # ══════════════════════════════════════════════════════════════════════════
    ty = content_y
    for i, trig in enumerate(triggers):
        # CIFRA / STAT ARRIBA — Instrument Serif 64pt
        st_tb = slide.shapes.add_textbox(COL_C_X, ty, COL_W_C - Pt(6), STAT_H)
        st_tb.word_wrap = False
        tf_st = st_tb.text_frame
        tf_st.word_wrap = False
        tf_st.auto_size = None
        p_st = tf_st.paragraphs[0]
        p_st.line_spacing = 1.0
        r_st = p_st.add_run()
        r_st.text = trig["stat"]
        r_st.font.name  = FONT_SERIF
        r_st.font.size  = PT_STAT   # 64pt — Regla 2
        r_st.font.bold  = False
        r_st.font.color.rgb = C_WHITE

        ty += STAT_H + STAT_DESC_GAP  # gap 10pt — Regla 6

        # CAJA DESC ABAJO — Poppins 10pt blanco W170×H35pt (Regla 2)
        add_tb(slide, trig["desc"],
               COL_C_X, ty, DESC_W, DESC_H,
               font=FONT_SANS, size=PT_BODY_10,
               color=C_WHITE, line_spacing=1.0)
        ty += DESC_H + DESC_SRC_GAP  # gap 6pt — Regla 6

        # Fuente inline 7pt #666
        add_tb(slide, trig.get("source", "").upper(),
               COL_C_X, ty, DESC_W, SRC_H,
               font=FONT_SANS, size=PT_SOURCE_7,
               color=C_GREY_66, uppercase=False)
        ty += SRC_H

        # Gap ENTRE triggers — Regla 6: 24pt
        if i < len(triggers) - 1:
            ty += TRIGGER_GAP

    # ══════════════════════════════════════════════════════════════════════════
    # COL-RIGHT: SEÑALES — 95×140pt EXACTO (Regla 3)
    # Gap 24pt entre fotos. Caption 170×35pt al lado (gap 8pt).
    # Regla 7: solo fotos reales, raise si falta PNG
    # ══════════════════════════════════════════════════════════════════════════
    sy = content_y
    cap_x = COL_R_X + PHOTO_W + Pt(8)   # 8pt gap foto→caption (Regla 6)
    cap_w = Pt(170)

    for j, sig in enumerate(signals):
        png_path = SHOTS / Path(sig["png"]).name
        # Regla 7: NO placeholder, raise se falta PNG
        add_image_badge(slide, png_path,
                        COL_R_X, sy, PHOTO_W, PHOTO_H,
                        url=sig.get("url", ""))

        # Caption 170×35pt Poppins 10pt blanco
        add_tb(slide, sig.get("caption", ""),
               cap_x, sy, cap_w, DESC_H,
               font=FONT_SANS, size=PT_BODY_10,
               color=C_WHITE, line_spacing=1.0)

        # Source inline 7pt #666
        add_tb(slide, sig.get("source", "").upper(),
               cap_x, sy + DESC_H + DESC_SRC_GAP, cap_w, SRC_H,
               font=FONT_SANS, size=PT_SOURCE_7,
               color=C_GREY_66, uppercase=False)

        sy += PHOTO_H + PHOTO_GAP  # gap 24pt — Regla 3 + 6


# ══════════════════════════════════════════════════════════════════════════════
# CONTENT DATA
# ══════════════════════════════════════════════════════════════════════════════

MACROS_DATA = [
    {"num": 1, "name": "INVENTOLOGÍA DE LA ADULTEZ",
     "tagline": "Un mundo en crisis está reescribiendo qué significa ser adulto y formar familia."},
    {"num": 2, "name": "LOS HERNÁNDEZ ARE PROMPTED",
     "tagline": "El dominicano ya entró al mundo prompteado. Solo no lo nombra así."},
    {"num": 3, "name": "ALGORITMO DEL HOGAR",
     "tagline": "El feed se sentó en la mesa y nadie le ofreció silla."},
]

MICROS_DATA = [
    # ── MACRO 1 ──────────────────────────────────────────────────────────────
    {
        "macro_num": 1, "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "micro_id": "1.1",
        "headline": "La generación sin tiempo entre semana descubrió que dos horas el domingo le devuelven la semana entera.",
        "fenomeno": "El joven dominicano prepara comidas el domingo para ahorrar tiempo, comer mejor y controlar lo que ingiere. No es dieta — es autonomía. El meal prep entra como ritual de adultez sin mamá-cocinera detrás.",
        "hashtags": "#MealPrepDominicano · #DomingoDePrep · #ControlDeLoQueComo · #ComidaDeLaSemana",
        "triggers": [
            {"stat": "US$36B",  "desc": "Mercado global meal prep en 2026, CAGR 9.84% hasta 2035.", "source": "Market Reports World · 2026"},
            {"stat": "48%",     "desc": "De adultos ya practica meal prep; 62% de profesionales >8h/día cita falta de tiempo.", "source": "HelloFresh State of Cooking · 2025"},
            {"stat": "4 días",  "desc": "Creadora RD @morechulaa documenta prep de 4 días con tuppers etiquetados.", "source": "TikTok @morechulaa · 2025"},
        ],
        "signals": [
            {"png": "macro-1-1-tiktok-morechulaa-mealprep.png",
             "caption": "Creadora @morechulaa — meal prep RD 4 días, tuppers + etiquetas por día.",
             "source": "TikTok @morechulaa · 2025",
             "url": "https://www.tiktok.com/@morechulaa/video/7636986702262717704"},
            {"png": "macro-1-1-tiktok-viviankh-mealprep.png",
             "caption": "@viviank.h — 10 sándwiches + 9 porciones en freezer, meal prep 3 semanas.",
             "source": "TikTok @viviank.h · 2025",
             "url": "https://www.tiktok.com/@viviank.h/video/7620501104765177108"},
            {"png": "macro-1-0-mktreports-mealprep-market.png",
             "caption": "Market Reports World: mercado meal prep US$36,433M globales en 2026.",
             "source": "Market Reports World · 2026",
             "url": "https://www.marketreportsworld.com/market-reports/meal-prep-market-14713709"},
        ],
    },
    {
        "macro_num": 1, "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "micro_id": "1.2",
        "headline": "Las empresas descubrieron que si el empleado come bien al mediodía rinde mejor en la tarde — y el menú de almuerzo se volvió beneficio.",
        "fenomeno": "El trabajador de 8-5 está harto de comer calentado. Fripick deja que la empresa pague la comida y la descuente en quincena. La comida del mediodía dejó de ser problema individual — ahora es categoría B2B.",
        "hashtags": "#LunchMenuRD · #AlmuerzoDeTrabajo · #MenúDelDía · #PrecioAccesible · #NegocioOyó",
        "triggers": [
            {"stat": "+13% YoY", "desc": "Tráfico restauración LATAM en horario almuerzo con shoulder hour pricing.", "source": "OpenTable / QSR Magazine · 2026"},
            {"stat": "84%",      "desc": "De consumidores percibe precios de alimentos como 'altos'; 2/3 prefieren opciones más económicas.", "source": "Purdue University · 2025"},
            {"stat": "B2B RD",   "desc": "Fripick — plataforma de beneficios alimentarios corporativos con descuento de quincena.", "source": "Fripick.com · 2025"},
        ],
        "signals": [
            {"png": "macro-1-2-tiktok-toyantoja-noccila-lunch.png",
             "caption": "@toyantoja muestra lunch en Nocciola por menos de RD$500 — 'dato que vale oro'.",
             "source": "TikTok @toyantoja · 2025",
             "url": "https://www.tiktok.com/@toyantoja/video/7610215257000234247"},
            {"png": "macro-1-2-fripick-rd-brand.png",
             "caption": "Fripick RD — beneficio alimentario corporativo B2B, descuento en quincena.",
             "source": "Fripick · 2025",
             "url": "https://fripick.com"},
        ],
    },
    {
        "macro_num": 1, "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "micro_id": "1.3",
        "headline": "Te crió con miedo a lo 'malo' y ahora comer se siente como culpa. TikTok escuchó el término y lo convirtió en trend con millones de views.",
        "fenomeno": "La mamá que controlaba cada bocado crió hijas con relación rota con el plato. La almond mom no es solo un meme — es una cadena generacional. La adultez de esa hija inventa otra forma de comer sin la voz de mamá auditando.",
        "hashtags": "#AlmondMom · #TraumasDietéticos · #ComerConCulpa · #LaVozDeMamá",
        "triggers": [
            {"stat": "30M",           "desc": "Americanos desarrollarán un trastorno alimentario en su vida; 2da enfermedad mental más mortal.", "source": "ANAD / ABC News · 2025"},
            {"stat": "42%",           "desc": "De niñas de 1°-3° quiere ser más delgada; 81% de niños de 10 años teme engordar.", "source": "ANAD Statistics · 2025"},
            {"stat": "\"almond mom\"","desc": "Hashtag viral — rutina heredada: suplementos, restricción, sin cuestionar.", "source": "TikTok · 2025"},
        ],
        "signals": [
            {"png": "macro-1-3-tiktok-lielle-almondmom.png",
             "caption": "@Lielle & Dee — POV rutina heredada #almondmom: suplementos, restricción, sin cuestionamiento.",
             "source": "TikTok @liellewaldman17 · 2025",
             "url": "https://www.tiktok.com/@liellewaldman17/video/7617943870797630750"},
            {"png": "macro-1-3-tiktok-nourvilaa-almondmom.png",
             "caption": "@nour vilà — versión LATAM del trauma dietético heredado de mamá, #almondmum.",
             "source": "TikTok @nourvilaa · 2025",
             "url": "https://www.tiktok.com/@nourvilaa/video/7642383470026657046"},
        ],
    },
    {
        "macro_num": 1, "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "micro_id": "1.4",
        "headline": "La diferencia entre un domingo con familia y uno solo se mide en una pregunta: ¿qué vamos a comer?",
        "fenomeno": "Para familias grandes el domingo es sancocho, mesa llena, todos. Para el foráneo que vive solo es el día más difícil. Videollama a mamá en Bonao mientras come delivery — para sentir el domingo.",
        "hashtags": "#DomingoSolo · #AlmuerzoDeFamilia · #SancochoDelDomingo · #ForáneoEnLaCapital",
        "triggers": [
            {"stat": "45%",  "desc": "De hogares come junto menos que hace una década; 84% querría compartir más comidas.", "source": "Simirity / FMI Foundation · 2025"},
            {"stat": "17%",  "desc": "De dominicanos no comparte horas de comida — el foráneo en cuartito de Naco, delivery en mano.", "source": "Código Casa 2025 · P25"},
            {"stat": "2025", "desc": "World Happiness Report: compartir comidas se vincula con conectividad social y bienestar.", "source": "World Happiness Report · 2025"},
        ],
        "signals": [
            {"png": "macro-1-4-tiktok-josheilyn-foranea-capital.png",
             "caption": "@Josheilyn — 'yo amo estar en mi hogar los domingos' — foránea RD en la capital.",
             "source": "TikTok @josheilyndls1 · 2025",
             "url": "https://www.tiktok.com/@josheilyndls1/video/7549991019169811768"},
            {"png": "macro-1-4-tiktok-mariannycorderoo-domingo.png",
             "caption": "@mariannycorderoo — domingo solo en Bogotá, tostada con #amorpropio.",
             "source": "TikTok @mariannycorderoo · 2025",
             "url": "https://www.tiktok.com/@mariannycorderoo/video/7643570804885572882"},
            {"png": "macro-1-4-tiktok-macaseason-domingo-familiar.png",
             "caption": "@María Camila — el ritual completo del domingo familiar como contraste.",
             "source": "TikTok @macaseason · 2025",
             "url": "https://www.tiktok.com/@macaseason/video/7625031259835665685"},
        ],
    },
    {
        "macro_num": 1, "macro_name": "INVENTOLOGÍA DE LA ADULTEZ",
        "micro_id": "1.5",
        "headline": "PedidosYa es la app #1 de food en RD: el adulto joven ya no decide qué cocinar entre semana, decide qué pedir — y esa es su nueva forma de ser adulto.",
        "fenomeno": "La adultez tradicional cocinaba todos los días. La adultez 2026 delega el jueves a una app. No es flojera — es renegociación del rol en una economía donde el tiempo cuesta más que la comida.",
        "hashtags": "#PedidosYaRD · #DeliveryEsMiMamá · #AdultoQueNoCocina · #JuevesDeApp",
        "triggers": [
            {"stat": "21.7K",    "desc": "Descargas semanales pico de PedidosYa en RD — Q1 2025; app #1 food & drink iOS.", "source": "Sensor Tower · Q1 2025"},
            {"stat": "+50%",     "desc": "Precios de alimentos RD entre 2019 y 2025 — el delivery se vuelve cálculo costo-tiempo.", "source": "BCRD / Dominican Today · 2026"},
            {"stat": "100% app", "desc": "Primer supermercado 100% online abre en Santo Domingo — la grocería migra a app.", "source": "St Kitts Nevis Observer · 2025"},
        ],
        "signals": [
            {"png": "macro-1-5-sensortower-pedidosya-rd-chart.png",
             "caption": "Sensor Tower: PedidosYa #1 food delivery RD — 13K-21.7K descargas semanales Q1 2025.",
             "source": "Sensor Tower · Q1 2025",
             "url": "https://sensortower.com/blog/2025-q1-unified-top-5-food%20delivery%20services-units-do-63da96fbe1714cfff1c1e5a1"},
            {"png": "macro-1-5-pedidosya-country-selector.png",
             "caption": "PedidosYa — selector de países con RD listada + badges App Store / Google Play.",
             "source": "PedidosYa · 2026",
             "url": "https://www.pedidosya.com"},
            {"png": "macro-1-5-stkitts-online-super-sd.png",
             "caption": "Primer supermercado 100% online en Santo Domingo — la grocería migra a app.",
             "source": "St Kitts Nevis Observer · 2025",
             "url": "https://www.thestkittsnevisobserver.com/first-online-only-supermarket-opens-in-santo-domingo/"},
        ],
    },
    # ── MACRO 2 ──────────────────────────────────────────────────────────────
    {
        "macro_num": 2, "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "micro_id": "2.1",
        "headline": "Una foto de tu plato no sabe lo que comes. Pero el algoritmo te convence de que sí — y le crees más a la app que a tu propio cuerpo.",
        "fenomeno": "Las apps de conteo calórico pasaron de herramienta a obsesión. El algoritmo 'te ayuda a comer mejor' pero se convierte en la voz que condena cada nutriente. El número en pantalla pesa más que la sensación de saciedad.",
        "hashtags": "#AppQueEnfermó · #MyFitnessPalToxic · #AlgoritmoDeMiDieta · #ComerConMiedo",
        "triggers": [
            {"stat": "180M",       "desc": "Usuarios MyFitnessPal; 75% de pacientes con trastorno alimentario la usaba.", "source": "GripRoom / PMC NLM · 2026"},
            {"stat": "73%",        "desc": "De pacientes con trastorno creyó que la app contribuyó al desarrollo del mismo.", "source": "PMC NLM · 2026"},
            {"stat": "\"gateway\"","desc": "Apps con IA de reconocimiento por foto como gateway a trastorno, especialmente en perfeccionistas.", "source": "Sage Journals / Ohio State · 2026"},
        ],
        "signals": [
            {"png": "macro-2-1-myfitnesspal-app-ui.png",
             "caption": "UI MyFitnessPal: 976 cal + macro breakdown — 'Nutrition tracking for real life'.",
             "source": "MyFitnessPal · 2026",
             "url": "https://www.myfitnesspal.com"},
            {"png": "macro-2-1-flinders-fitnessapp-disorder.png",
             "caption": "Flinders University: mujer con teléfono — fitness apps fuelling disordered eating.",
             "source": "Flinders University · Feb 2025",
             "url": "https://news.flinders.edu.au/blog/2025/02/22/fitness-apps-fuelling-disordered-eating/"},
        ],
    },
    {
        "macro_num": 2, "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "micro_id": "2.2",
        "headline": "Antes mamá decidía qué había de comer. Hoy lo decide el For You Page — y de paso te vende los ingredientes en el mismo scroll.",
        "fenomeno": "El joven dominicano abre TikTok antes de abrir el refrigerador. Las recetas virales compiten con la tradición oral heredada. 6pm: scroll 4 min → screenshot → chat con pareja → supermercado con lista específica.",
        "hashtags": "#TikTokRecetas · #ForYouPageDeCocina · #RecetaViralVsAbuela · #AlgoritmoDeAlmuerzo",
        "triggers": [
            {"stat": "índice 42",  "desc": "Pico de contenido food en TikTok en enero 2026 — la plataforma como primer recetario.", "source": "Accio / TikTok Food Trends · 2026"},
            {"stat": "US$759M",    "desc": "GMV food en TikTok Shop 2025 — food es 13.6% del volumen total.", "source": "Capital One Shopping · 2025"},
            {"stat": "2×",         "desc": "Marcas grandes casi duplicaron ventas en TikTok Shop en 2025.", "source": "Modern Retail · 2025"},
        ],
        "signals": [
            {"png": "macro-2-2-tiktokshop-food-gmv.png",
             "caption": "TikTok es el nuevo recetario Y el nuevo supermercado — food 13.6% del GMV.",
             "source": "Resourcera · 2026",
             "url": "https://resourcera.com/data/social/tiktok-shop-statistics/"},
            {"png": "macro-2-2-modernretail-tiktokshop-brands.png",
             "caption": "Modern Retail: marcas grandes casi duplicaron ventas en TikTok Shop en 2025.",
             "source": "Modern Retail · 2025",
             "url": "https://www.modernretail.co/technology/sales-from-major-brands-on-tiktok-shop-nearly-doubled-in-2025-drawing-ulta-and-sally-beauty/"},
            {"png": "macro-2-2-cropink-social-food-stats.png",
             "caption": "Cropink: 74% usa redes para decidir qué/dónde comer; 50% reporta influencia directa.",
             "source": "Cropink · 2026",
             "url": "https://cropink.com/restaurant-social-media-statistics"},
        ],
    },
    {
        "macro_num": 2, "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "micro_id": "2.3",
        "headline": "El truco de poner un video para que el niño coma se convirtió en condición — el iPad es la única forma de que el plato baje.",
        "fenomeno": "El niño no come sin el iPad. La pantalla dejó de ser acompañamiento y se volvió condición. Mamá pone Cocomelon; niño come pollo en piloto automático; mesa familiar dura 14 minutos en silencio. Comió. Eso cuenta.",
        "hashtags": "#iPadKid · #PantallaMientrasCome · #NetflixYCena · #ComerSinPantalla",
        "triggers": [
            {"stat": "40%",   "desc": "De niños tiene iPad a los 2 años; 2.6 hrs/día promedio — solo 1% cumple límites.", "source": "Common Sense Media · 2025"},
            {"stat": "2026",  "desc": "Comer con pantalla desconecta señales de hambre/saciedad y aumenta consumo de chatarra.", "source": "ScienceDirect / Business Standard · 2026"},
            {"stat": "LATAM", "desc": "UNICEF Kids Online: exposición infantil a pantallas más temprana y menos mediada que promedios.", "source": "UNICEF Kids Online · 2025"},
        ],
        "signals": [
            {"png": "macro-2-3-tiktok-ipadkid-debate.png",
             "caption": "TikTok viral: 'Kids and iPads at the table… yes or no?' — debate sobre pantallas en mesa familiar.",
             "source": "TikTok @sextedmyboss · 2025",
             "url": "https://www.tiktok.com/@sextedmyboss/video/7475054384771075350"},
            {"png": "macro-2-3-k12dive-csm-screentimekids.png",
             "caption": "K12 Dive / CSM 2025: niño con tablet — 'Half of young children own a cell phone or tablet'.",
             "source": "K12 Dive / CSM · 2025",
             "url": "https://www.k12dive.com/news/half-of-young-children-own-a-cell-phone-or-tablet/741318/"},
            {"png": "macro-2-3-newsmedical-screentime-proxy.png",
             "caption": "News Medical: GLP-1 altera apetito y comportamiento — señal de medicalización del comer.",
             "source": "News Medical · 2026",
             "url": "https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx"},
        ],
    },
    {
        "macro_num": 2, "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "micro_id": "2.4",
        "headline": "El consumidor sano se pega un sensor de glucosa por dos semanas y descubre que la uva le sube más el azúcar que el helado. La nutrición ya es dato en tiempo real.",
        "fenomeno": "Los wearables de glucosa OTC salieron del nicho diabético y entraron al consumer health. El 'comer bien' dejó de ser opinión — ahora es métrica continua. El glucómetro contradice a la abuela. Gana el glucómetro.",
        "hashtags": "#LingoRD · #SensorDeGlucosa · #ComerConDato · #MetabolicAge · #ElPlatoYElGráfico",
        "triggers": [
            {"stat": "US$80B",        "desc": "Mercado wearables y health tracking 2024 — proyecta US$200B+ para 2030.", "source": "Statista · 2025"},
            {"stat": "OTC",           "desc": "Abbott Lingo: CGM sin prescripción expande a Android dic 2025; en Walmart y Amazon.", "source": "Abbott Newsroom · 2025"},
            {"stat": "#glucosegoddess","desc": "Jessie Inchauspé cruza cientos de millones de views; 'glucose hacks' como género.", "source": "TikTok · 2025"},
        ],
        "signals": [
            {"png": "macro-2-4-hellolingo-cgm-hero.png",
             "caption": "Abbott Lingo hero — mujer con sensor en brazo + 'My glucose, my insights'. CGM OTC.",
             "source": "Abbott Lingo · 2025",
             "url": "https://www.hellolingo.com"},
            {"png": "macro-2-4-scripps-cgm-sensor-arm.png",
             "caption": "Scripps News: brazo con sensor CGM — 'CGMs in vogue' para consumidor no-diabético.",
             "source": "Scripps News · 2025",
             "url": "https://www.scrippsnews.com/health/continuous-glucose-monitors-are-in-vogue-but-do-you-really-need-to-track-your-blood-sugar"},
        ],
    },
    {
        "macro_num": 2, "macro_name": "LOS HERNÁNDEZ ARE PROMPTED",
        "micro_id": "2.5",
        "headline": "Una creadora cocina en vivo, te muestra el producto, lo agregas al carrito sin salir del feed. El supermercado se volvió streaming.",
        "fenomeno": "Live shopping pasó del nicho beauty al supermercado. Food es 13.6% del GMV de TikTok Shop. El próximo carrito del dominicano será un live stream — no un walk-in. Vió, comió, compró. En menos de 4 minutos.",
        "hashtags": "#TikTokShopFood · #CocinaEnVivo · #CarritoDelFeed · #CompraLoQueCocinas",
        "triggers": [
            {"stat": "US$64.3B",  "desc": "GMV total TikTok Shop 2025; food US$759.84M; ticket promedio food shopper US$43.20.", "source": "Capital One Shopping / Resourcera · 2025"},
            {"stat": "+84% YoY", "desc": "Live shopping creció 84% en 2025; conversión live 6.1% vs feed 4.7%.", "source": "Modern Retail / Resourcera · 2026"},
            {"stat": "100% app", "desc": "Primer supermercado 100% online en Santo Domingo — grocery digital prepara terreno.", "source": "St Kitts Nevis Observer · 2025"},
        ],
        "signals": [
            {"png": "macro-2-5-modernretail-tiktokshop-2025.png",
             "caption": "Modern Retail: marcas grandes duplicaron ventas TikTok Shop 2025; food es categoría #1 del live.",
             "source": "Modern Retail · 2025",
             "url": "https://www.modernretail.co/technology/sales-from-major-brands-on-tiktok-shop-nearly-doubled-in-2025-drawing-ulta-and-sally-beauty/"},
            {"png": "macro-2-5-resourcera-tiktokshop-stats.png",
             "caption": "Resourcera: GMV US$64.3B, ticket food US$43.20, live shopping +84% YoY.",
             "source": "Resourcera · 2026",
             "url": "https://resourcera.com/data/social/tiktok-shop-statistics/"},
        ],
    },
    # ── MACRO 3 ──────────────────────────────────────────────────────────────
    {
        "macro_num": 3, "macro_name": "ALGORITMO DEL HOGAR",
        "micro_id": "3.1",
        "headline": "Ver lo que otros comen se convirtió en uno de los formatos más consumidos de internet. Ya no es comida — es identidad.",
        "fenomeno": "'What I Eat in a Day' explota no por curiosidad culinaria — por validación. Ver lo que come otro para confirmar, comparar o inspirarse. El plato ajeno es espejo. Y juez.",
        "hashtags": "#QuéComoEnUnDía · #WhatIEatInADay · #ComidaParaVer · #DíaDeComidaRD",
        "triggers": [
            {"stat": "74%",      "desc": "De personas usa redes para decidir qué/dónde comer; 50% reporta influencia directa.", "source": "Cropink · 2026"},
            {"stat": "top 2026", "desc": "WIEIAD entre top food trends 2026 — engagement positivo y negativo que el algoritmo premia.", "source": "Chowhound TikTok Trends · 2026"},
            {"stat": "2026",     "desc": "Whole Foods: bowl colorido como 'comer bien aspiracional' que WIEIAD replica.", "source": "VegNews · Oct 2025"},
        ],
        "signals": [
            {"png": "macro-3-1-tiktok-wieiad-hanfoodfit.png",
             "caption": "@han | macro friendly food — WIEIAD aspiracional con #wieiad #8020rule; el formato que el feed distribuye.",
             "source": "TikTok @hanfoodfit · 2025",
             "url": "https://www.tiktok.com/@hanfoodfit/video/7493474947029880086"},
            {"png": "macro-3-1-vegnews-food-trend-hero.png",
             "caption": "VegNews: bowl proteína + grains + vegetales — imagen del 'comer bien aspiracional 2026'.",
             "source": "VegNews · 2025",
             "url": "https://vegnews.com/fiber-whole-foods-2026-top-trend"},
            {"png": "macro-3-1-cropink-social-food-decisions.png",
             "caption": "Cropink: 74% usa redes para decidir qué/dónde comer — el feed como nutricionista.",
             "source": "Cropink · 2026",
             "url": "https://cropink.com/restaurant-social-media-statistics"},
        ],
    },
    {
        "macro_num": 3, "macro_name": "ALGORITMO DEL HOGAR",
        "micro_id": "3.2",
        "headline": "El mukbang nació porque hay gente que come sola y prefiere ver a alguien comer antes que comer en silencio.",
        "fenomeno": "Nació en Corea como compañía virtual. Hoy es negocio millonario. El dominicano lo consume porque la mesa vacía duele — y una pantalla llena el silencio del comedor. La cena ya viene con co-cenador incluido.",
        "hashtags": "#MukbangLatino · #ComerSoloPeroNoTanto · #SoledadEnLaMesa · #CenarConPantalla",
        "triggers": [
            {"stat": "5.3M",   "desc": "#mukbang supera 5.3M videos en 2025; top creadores generan hasta US$10K/mes.", "source": "Distraction Magazine / PMC · 2025"},
            {"stat": "68.5%",  "desc": "De jóvenes universitarias ve videos de comida regularmente; vínculo con efecto parasocial en soledad.", "source": "Western Gazette / PMC · 2026"},
            {"stat": ">2B",    "desc": "Views de Nickocado Avocado en YouTube — mukbang como nuevo co-comensal digital.", "source": "YouTube · 2025"},
        ],
        "signals": [
            {"png": "macro-3-2-youtube-mukbang-search-grid.png",
             "caption": "Grid YouTube 'mukbang' — thumbnails de comida extrema y ASMR con millones de vistas.",
             "source": "YouTube · 2026",
             "url": "https://www.youtube.com/results?search_query=mukbang"},
        ],
    },
    {
        "macro_num": 3, "macro_name": "ALGORITMO DEL HOGAR",
        "micro_id": "3.3",
        "headline": "Cuando todo lo demás está fuera de control, la cocina es el único sitio donde lo que hago sí sale como quiero.",
        "fenomeno": "Bajo burnout y presión social, adultos jóvenes descubrieron que cocinar y hornear son terapia real. No es hobbyismo — es el único espacio donde lo que controlas eres tú. El horno escucha mejor que el psicólogo en lista de espera.",
        "hashtags": "#CocinaComoTerapia · #HornearParaDesestresarse · #LoveLanguageCocina · #Repostería",
        "triggers": [
            {"stat": "dopamina", "desc": "Hornear activa rutas de dopamina y reduce cortisol — equivalente a mindfulness clínico.", "source": "Kaiser Permanente / NeuroLaunch · 2026"},
            {"stat": "2026",     "desc": "Ola de cancelaciones de delivery + vuelta a la cocina como anti-ansiedad digital.", "source": "EditorialGe / Cooking as Therapy · 2026"},
            {"stat": "#terapia", "desc": "#cookingastherapy + #reposteriaterapia — creadoras LATAM documentan cocina como bienestar.", "source": "TikTok · 2025"},
        ],
        "signals": [
            {"png": "macro-3-3-tiktok-natalie-stressbaking.png",
             "caption": "@chef_natalie_ — 'stress baking is my form of therapy' #bakingtiktok #bakingtherapy.",
             "source": "TikTok @chef_natalie_ · 2025",
             "url": "https://www.tiktok.com/@chef_natalie_/video/7569545767090703647"},
            {"png": "macro-3-3-newsmedical-cooking-proxy.png",
             "caption": "News Medical: jeringa GLP-1 + headline — cocina como contrapunto analógico a la farmacología.",
             "source": "News Medical · 2026",
             "url": "https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx"},
        ],
    },
    {
        "macro_num": 3, "macro_name": "ALGORITMO DEL HOGAR",
        "micro_id": "3.4",
        "headline": "El FOMO de bajar de peso llegó a su versión más extrema: eliminar todo lo que no sea animal. Los análisis de sangre cuentan otra historia.",
        "fenomeno": "Joe Rogan lo popularizó, los influencers lo viralizaron, el que lleva años sin bajar de peso lo consideró. Solo carne, mantequilla y huevo. El algoritmo lo distribuye más rápido que la evidencia clínica que lo contradice.",
        "hashtags": "#DietaCarnívora · #SoloCarneMantequillaYHuevo · #FOMODeBajarDePeso · #CarnivoreVsColesterol",
        "triggers": [
            {"stat": "2.6M",     "desc": "#carnivore supera 2.6M publicaciones en Instagram a noviembre 2025.", "source": "ResearchGate / Fox News · 2025"},
            {"stat": "LDL +37%", "desc": "LDL promedio sube de 126 a 172 mg/dL en seguidores; caso reportado 163→365.", "source": "Nutrients Journal · Jan 2026"},
            {"stat": "\"Year of the Fiber\"", "desc": "Whole Foods 2026: mainstream pivota a fibra + longevity mientras carnivore escala.", "source": "VegNews / Whole Foods · 2026"},
        ],
        "signals": [
            {"png": "macro-3-4-tiktok-carnivore-steakbuttergal.png",
             "caption": "@Steakandbuttergal | Carnivore — la creadora más viral de la dieta carnívora: solo carne + mantequilla.",
             "source": "TikTok @steakandbuttergal · 2025",
             "url": "https://www.tiktok.com/@steakandbuttergal/video/7577437952679087374"},
            {"png": "macro-3-4-vegnews-protein-fiber-trend.png",
             "caption": "VegNews: bowl colorido del pivot fibra 2026 — contraste con la tabla de bistec del carnivore feed.",
             "source": "VegNews · 2025",
             "url": "https://vegnews.com/fiber-whole-foods-2026-top-trend"},
        ],
    },
    {
        "macro_num": 3, "macro_name": "ALGORITMO DEL HOGAR",
        "micro_id": "3.5",
        "headline": "GLP-1 silencia el 'food noise' del cerebro. La nueva conversación sobre comer no es qué cocinar — es si lo deseo o solo me acordé que existía.",
        "fenomeno": "Ozempic y Mounjaro reescriben la relación con la comida: ya no se trata de fuerza de voluntad, sino de farmacología que apaga el ruido mental. El feed normaliza la conversación; el endocrinólogo no está en el loop.",
        "hashtags": "#FoodNoise · #OzempicDiary · #SinHambreSinAnsiedad · #GLP1RD · #LaCabezaSinComida",
        "triggers": [
            {"stat": "58%",        "desc": "Siente menos hambre con GLP-1; 64% se llena antes; 21-23% reporta cambios de sabor — EASD n=411.", "source": "EASD 2025 / News-Medical · 2025"},
            {"stat": "#foodnoise", "desc": "Viralizado por usuarias de GLP-1 documentando cambio cognitivo — decenas de millones de views.", "source": "TikTok · 2025"},
            {"stat": "2026",       "desc": "Whole Foods contrapunto: longevidad y fibra como aspiracional opuesto al cuerpo medicado.", "source": "Whole Foods 2026 / VegNews · 2026"},
        ],
        "signals": [
            {"png": "macro-3-5-sciam-ozempic-food-noise.png",
             "caption": "Scientific American: ilustración surrealista — cabeza con comida flotando, 'Ozempic Quiets Food Noise'.",
             "source": "Scientific American · Jun 2024",
             "url": "https://www.scientificamerican.com/article/ozempic-quiets-food-noise-in-the-brain-but-how/"},
            {"png": "macro-3-5-newsmedical-glp1-appetite.png",
             "caption": "News Medical: jeringa semaglutide — 58% menos hambre según EASD 2025.",
             "source": "News Medical · 2026",
             "url": "https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx"},
            {"png": "macro-3-5-tiktok-glp1-foodnoise.png",
             "caption": "@JanelleRohner — responde sobre food noise; #glp1community con millones de views en 2025.",
             "source": "TikTok @janellerohner · 2025",
             "url": "https://www.tiktok.com/@janellerohner/video/7564545141835418911"},
        ],
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# BUILD DECK — 18 slides (3 dividers + 15 micros)
# ══════════════════════════════════════════════════════════════════════════════

micro_idx = 0
for macro in MACROS_DATA:
    build_macro_divider(macro["num"], macro["name"], macro["tagline"])
    for _ in range(5):
        m = MICROS_DATA[micro_idx]
        build_micro(
            macro_num=m["macro_num"],
            macro_name=m["macro_name"],
            micro_id=m["micro_id"],
            headline=m["headline"],
            fenomeno=m["fenomeno"],
            hashtags=m["hashtags"],
            triggers=m["triggers"],
            signals=m["signals"],
        )
        micro_idx += 1

OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(str(OUT))
print(f"SAVED: {OUT}")
print(f"SLIDES: {len(prs.slides)}")
