"""
build_trends_alimentacion.py — Capítulo 04 ALIMENTACIÓN v3
Dimensiones corregidas per aprendizajes-montador-trends-cc.md (8 reglas duras).

KEY CHANGES v3 (fixes overflow):
- PHOTO_W=88pt, PHOTO_H=130pt (was 95×140)
- STAT_SIZE=56pt, STAT_W=170pt (was 72pt/294pt)
- STAT_TO_DESC_GAP=18pt (was 10pt)
- TRIGGER_GAP=28pt (was 24pt)
- LABELS_TO_CONTENT=10pt → content starts y=84pt (was 16pt/y=90)

Math proof (no overflow):
  Col-right: 3×130 + 2×24 = 438pt → 84+438=522 < 540 ✓  (18pt margin)
  Col-mid:   3×(56+18+35+6+12) + 2×28 = 3×127+56 = 437pt → 84+437=521 < 540 ✓  (19pt margin)
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pathlib import Path
from lxml import etree
from pptx.oxml.ns import qn

# ─── Canvas ───────────────────────────────────────────────────────────────────
prs = Presentation()
prs.slide_width  = Inches(13.333)   # 960pt
prs.slide_height = Inches(7.5)      # 540pt

BASE        = Path("/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC")
SCREENSHOTS = BASE / "screenshots" / "trends-alimentacion"

# ─── Colours ──────────────────────────────────────────────────────────────────
C_BG        = RGBColor(0x0D, 0x0D, 0x0D)
C_WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
C_GREY      = RGBColor(0xA0, 0xA0, 0xA0)
C_DARK_GREY = RGBColor(0x66, 0x66, 0x66)
C_TAB_BG    = RGBColor(0xE8, 0xE8, 0xE8)
C_RED       = RGBColor(0xFF, 0x2D, 0x2D)

# ─── Layout constants (pt) ────────────────────────────────────────────────────
SLIDE_W = 960.0
SLIDE_H = 540.0

COL_LEFT_X  = 20.0;  COL_LEFT_W  = 290.0
COL_MID_X   = 330.0; COL_MID_W   = 290.0
COL_RIGHT_X = 640.0; COL_RIGHT_W = 300.0

TAB_Y        = 10.0;  TAB_H    = 22.0
LABELS_Y     = 50.0;  LABELS_H = 14.0   # tab_y + tab_h + 18
HLINE_Y      = 68.0                      # labels_y + labels_h + 6
CONTENT_Y    = 84.0                      # hline_y + 10 (LABELS_TO_CONTENT=10) ← KEY FIX

# Col-left blocks
HEADLINE_H       = 48.0
PHENOM_LABEL_Y   = CONTENT_Y + HEADLINE_H + 20.0
PHENOM_LABEL_H   = 14.0
PHENOM_BODY_Y    = PHENOM_LABEL_Y + PHENOM_LABEL_H + 6.0
PHENOM_BODY_H    = 84.0
HASH_LABEL_Y     = PHENOM_BODY_Y + PHENOM_BODY_H + 18.0
HASH_LABEL_H     = 14.0
HASH_BODY_Y      = HASH_LABEL_Y + HASH_LABEL_H + 6.0
HASH_BODY_H      = 52.0

# Trigger dims (REGLA #2 — v3 values)
STAT_W           = 170.0
STAT_H           = 56.0
STAT_TO_DESC_GAP = 18.0
DESC_W           = 170.0
DESC_H           = 35.0
DESC_TO_SRC_GAP  = 6.0
SRC_H            = 12.0
TRIGGER_GAP      = 28.0
# Block = 56+18+35+6+12 = 127pt; 3×127 + 2×28 = 437pt → end=84+437=521 ✓

# Photo dims (REGLA #3 — v3 values)
PHOTO_W   = 88.0
PHOTO_H   = 130.0
PHOTO_GAP = 24.0
# 3×130 + 2×24 = 438pt → end=84+438=522 ✓ (18pt margin)

CAP_OFFSET_X = PHOTO_W + 8.0
CAP_W        = 162.0   # COL_RIGHT_W - PHOTO_W - 8 - 22 (right pad)
CAP_H        = 35.0

# ─── Helpers ──────────────────────────────────────────────────────────────────
def emupt(v): return int(v * 12700)

def add_bg(slide):
    sp = slide.shapes.add_shape(1, emupt(0), emupt(0), emupt(SLIDE_W), emupt(SLIDE_H))
    sp.fill.solid(); sp.fill.fore_color.rgb = C_BG
    sp.line.fill.background()

def add_rect(slide, x, y, w, h, fill=None, line_rgb=None, line_pt=0.75):
    sp = slide.shapes.add_shape(1, emupt(x), emupt(y), emupt(w), emupt(h))
    if fill:
        sp.fill.solid(); sp.fill.fore_color.rgb = fill
    else:
        sp.fill.background()
    if line_rgb:
        sp.line.color.rgb = line_rgb
        sp.line.width = Pt(line_pt)
    else:
        sp.line.fill.background()
    return sp

def _tb(slide, x, y, w, h):
    """Return (txBox, tf) with word_wrap on, auto_size off."""
    from pptx.enum.text import MSO_AUTO_SIZE
    box = slide.shapes.add_textbox(emupt(x), emupt(y), emupt(w), emupt(h))
    box.word_wrap = True
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    return box, tf

def _run(tf, text, fname, fsize, bold=False, italic=False, color=C_WHITE,
         align=PP_ALIGN.LEFT, sp_pct=100, tracking=0):
    para = tf.paragraphs[0]
    para.alignment = align
    pPr = para._p.get_or_add_pPr()
    lnSpc = pPr.find(qn('a:lnSpc'))
    if lnSpc is None:
        lnSpc = etree.SubElement(pPr, qn('a:lnSpc'))
    spcPct = lnSpc.find(qn('a:spcPct'))
    if spcPct is None:
        spcPct = etree.SubElement(lnSpc, qn('a:spcPct'))
    spcPct.set('val', str(sp_pct * 1000))

    run = para.add_run()
    run.text = text
    run.font.name = fname
    run.font.size = Pt(fsize)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    if tracking != 0:
        run._r.get_or_add_rPr().set('spc', str(tracking))
    return run

def add_line_connector(slide, x1, y1, x2, y2, alpha_pct=15):
    """Thin white line with alpha."""
    cx = max(abs(x2-x1), 1); cy = max(abs(y2-y1), 1)
    lx = min(x1,x2);          ly = min(y1,y2)
    conn = slide.shapes.add_connector(1, emupt(lx), emupt(ly),
                                      emupt(lx+cx), emupt(ly+cy))
    conn.line.color.rgb = C_WHITE
    conn.line.width = Pt(1)
    # apply alpha
    spTree = conn._element
    solidFill = spTree.find('.//' + qn('a:solidFill'))
    if solidFill is not None:
        srgb = solidFill.find(qn('a:srgbClr'))
        if srgb is not None:
            a_el = etree.SubElement(srgb, qn('a:alpha'))
            a_el.set('val', str(alpha_pct * 1000))

# ─── Slide components ─────────────────────────────────────────────────────────
def add_tabs(slide, macro_n, macro_name):
    # Filled tab MACRO N
    add_rect(slide, COL_LEFT_X, TAB_Y, 58, TAB_H, fill=C_TAB_BG)
    _, tf = _tb(slide, COL_LEFT_X+4, TAB_Y+3, 52, TAB_H-4)
    _run(tf, macro_n, "Poppins", 7.5, bold=True, color=RGBColor(0,0,0))

    # Outline tab MACRO NAME
    add_rect(slide, COL_LEFT_X+62, TAB_Y, 220, TAB_H, line_rgb=C_DARK_GREY)
    _, tf2 = _tb(slide, COL_LEFT_X+66, TAB_Y+3, 214, TAB_H-4)
    _run(tf2, macro_name.upper(), "Poppins", 7.5, color=C_GREY)

def add_col_labels(slide):
    for x, lbl in [(COL_LEFT_X, "DEFINICIÓN"),
                   (COL_MID_X,  "TRIGGERS"),
                   (COL_RIGHT_X,"SEÑALES")]:
        _, tf = _tb(slide, x, LABELS_Y, 200, LABELS_H)
        _run(tf, lbl, "Poppins", 8, bold=True, color=C_GREY)

def add_seps(slide):
    add_line_connector(slide, COL_MID_X-6, LABELS_Y, COL_MID_X-6, SLIDE_H-10)
    add_line_connector(slide, COL_RIGHT_X-6, LABELS_Y, COL_RIGHT_X-6, SLIDE_H-10)
    add_line_connector(slide, COL_LEFT_X, HLINE_Y, SLIDE_W-20, HLINE_Y)

def add_col_left(slide, headline, fenomeno, hashtags):
    # HEADLINE — 20pt FIJO (REGLA #1)
    _, tf = _tb(slide, COL_LEFT_X, CONTENT_Y, COL_LEFT_W, HEADLINE_H)
    _run(tf, headline.upper(), "Instrument Serif", 20,
         color=C_WHITE, sp_pct=110, tracking=0)

    # EL FENÓMENO label
    _, tf2 = _tb(slide, COL_LEFT_X, PHENOM_LABEL_Y, COL_LEFT_W, PHENOM_LABEL_H)
    _run(tf2, "EL FENÓMENO", "Poppins", 8, bold=True, color=C_GREY)

    # body fenómeno — Poppins 10pt
    _, tf3 = _tb(slide, COL_LEFT_X, PHENOM_BODY_Y, COL_LEFT_W, PHENOM_BODY_H)
    _run(tf3, fenomeno, "Poppins", 10, color=C_WHITE, sp_pct=100)

    # HASHTAGS label
    _, tf4 = _tb(slide, COL_LEFT_X, HASH_LABEL_Y, COL_LEFT_W, HASH_LABEL_H)
    _run(tf4, "HASHTAGS", "Poppins", 8, bold=True, color=C_GREY)

    # hashtags — Instrument Serif 16pt (REGLA #5)
    _, tf5 = _tb(slide, COL_LEFT_X, HASH_BODY_Y, COL_LEFT_W, HASH_BODY_H)
    _run(tf5, hashtags, "Instrument Serif", 16,
         color=C_WHITE, sp_pct=100, tracking=0)

def add_col_center(slide, triggers):
    """3 triggers vertical: stat 56pt ABOVE, desc 170×35 BELOW (REGLA #2)."""
    y = CONTENT_Y
    for trig in triggers:
        # STAT — 56pt, width=170
        _, tf_s = _tb(slide, COL_MID_X, y, STAT_W, STAT_H)
        _run(tf_s, trig['stat'], "Instrument Serif", 56,
             color=C_WHITE, sp_pct=100, tracking=0)

        # DESC box — 170×35
        y_d = y + STAT_H + STAT_TO_DESC_GAP
        _, tf_d = _tb(slide, COL_MID_X, y_d, DESC_W, DESC_H)
        _run(tf_d, trig['desc'], "Poppins", 10, color=C_WHITE, sp_pct=100)

        # SOURCE — 6.5pt #666
        y_src = y_d + DESC_H + DESC_TO_SRC_GAP
        _, tf_src = _tb(slide, COL_MID_X, y_src, DESC_W, SRC_H)
        _run(tf_src, trig['source'].upper(), "Poppins", 6.5,
             color=C_DARK_GREY, sp_pct=100)

        y = y_src + SRC_H + TRIGGER_GAP

def add_col_right(slide, signals):
    """3 photos 88×130pt + badge + caption (REGLA #3)."""
    y = CONTENT_Y
    for sig in signals:
        png_path = SCREENSHOTS / sig['png']
        if png_path.exists():
            pic = slide.shapes.add_picture(
                str(png_path),
                emupt(COL_RIGHT_X), emupt(y),
                emupt(PHOTO_W), emupt(PHOTO_H)
            )
            # Hyperlink on picture
            if sig.get('url'):
                rId = slide.part.relate_to(
                    sig['url'],
                    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',
                    is_external=True
                )
                nvPicPr = pic._element.find('.//' + qn('p:nvPicPr'))
                if nvPicPr is not None:
                    cNvPr = nvPicPr.find(qn('p:cNvPr'))
                    if cNvPr is not None:
                        hl = etree.SubElement(cNvPr, qn('a:hlinkClick'))
                        hl.set(
                            '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id',
                            rId
                        )
        else:
            add_rect(slide, COL_RIGHT_X, y, PHOTO_W, PHOTO_H,
                     fill=RGBColor(0x1A,0x1A,0x1A), line_rgb=C_DARK_GREY)

        # Badge CLICK ME
        bw, bh = 38.0, 11.0
        bx = COL_RIGHT_X + PHOTO_W - bw - 2
        by = y + 2
        add_rect(slide, bx, by, bw, bh, fill=C_RED)
        _, tb = _tb(slide, bx+2, by+1, bw-4, bh-2)
        _run(tb, "CLICK ME", "Poppins", 5.5, bold=True,
             color=C_WHITE, align=PP_ALIGN.CENTER)

        # Caption box alongside
        cx = COL_RIGHT_X + CAP_OFFSET_X
        _, tf_c = _tb(slide, cx, y, CAP_W, CAP_H)
        _run(tf_c, sig['caption'], "Poppins", 10, color=C_WHITE, sp_pct=100)

        # Source inline
        sy = y + CAP_H + 6
        if sy + SRC_H <= SLIDE_H:
            _, tf_s = _tb(slide, cx, sy, CAP_W, SRC_H)
            _run(tf_s, sig['source'].upper(), "Poppins", 6.5,
                 color=C_DARK_GREY, sp_pct=100)

        y += PHOTO_H + PHOTO_GAP

# ─── Macro divider ────────────────────────────────────────────────────────────
def add_macro_divider(num, name, tagline):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide)

    cy = SLIDE_H / 2
    lbl_h = 20.0; lbl_y = cy - 90.0
    _, tf_l = _tb(slide, 0, lbl_y, SLIDE_W, lbl_h)
    _run(tf_l, f"MACRO {num}", "Poppins", 14, bold=True,
         color=C_GREY, align=PP_ALIGN.CENTER)

    name_h = 130.0; name_y = lbl_y + lbl_h + 24.0
    _, tf_n = _tb(slide, 20, name_y, SLIDE_W-40, name_h)
    _run(tf_n, name.upper(), "Instrument Serif", 100,
         color=C_WHITE, align=PP_ALIGN.CENTER, sp_pct=95, tracking=0)

    tag_h = 36.0; tag_y = name_y + name_h
    _, tf_t = _tb(slide, 20, tag_y, SLIDE_W-40, tag_h)
    _run(tf_t, f'"{tagline}"', "Instrument Serif", 24, italic=True,
         color=C_GREY, align=PP_ALIGN.CENTER)

    return slide

# ─── Micro slide ──────────────────────────────────────────────────────────────
def add_micro(macro_n, macro_name, headline, fenomeno, hashtags, triggers, signals):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide)
    add_tabs(slide, macro_n, macro_name)
    add_col_labels(slide)
    add_seps(slide)
    add_col_left(slide, headline, fenomeno, hashtags)
    add_col_center(slide, triggers)
    add_col_right(slide, signals)
    return slide

# ══════════════════════════════════════════════════════════════════════════════
# CONTENT DATA
# ══════════════════════════════════════════════════════════════════════════════

M1_N = "MACRO 1"; M1_NAME = "INVENTOLOGÍA DE LA ADULTEZ"
M1_TAG = "Un mundo en crisis está reescribiendo qué significa ser adulto y formar familia."

M2_N = "MACRO 2"; M2_NAME = "LOS HERNÁNDEZ ARE PROMPTED"
M2_TAG = "El dominicano ya entró al mundo prompteado. Solo no lo nombra así."

M3_N = "MACRO 3"; M3_NAME = "ALGORITMO DEL HOGAR"
M3_TAG = "El feed se sentó en la mesa y nadie le ofreció silla."

MICROS = [
    # ── Macro 1 ──────────────────────────────────────────────────────────────
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="La generación sin tiempo entre semana descubrió que dos horas el domingo le devuelven la semana entera.",
         fenomeno="El joven dominicano prepara comidas el domingo para ahorrar tiempo, comer mejor y controlar lo que ingiere. No es dieta — es autonomía. El meal prep entra como ritual de adultez sin mamá-cocinera detrás.",
         hashtags="#MealPrepDominicano · #DomingoDePrep · #ControlDeLoQueComo",
         triggers=[
             dict(stat="US$36B",  desc="Mercado global de meal prep en 2026, CAGR 9.84% hasta 2035.", source="Market Reports World · 2026"),
             dict(stat="48%",     desc="De adultos ya practica meal prep; 62% de profesionales cita falta de tiempo como driver.", source="HelloFresh · 2025-2026"),
             dict(stat="4 días",  desc="@morechulaa documenta prep de 4 días con tuppers etiquetados por día de la semana.", source="TikTok @morechulaa · 2025"),
         ],
         signals=[
             dict(png="macro-1-1-tiktok-morechulaa-mealprep.png",
                  caption="@morechulaa muestra meal prep de 4 días — tuppers, arroz, proteína, etiquetas por día.",
                  source="TikTok @morechulaa · 2025",
                  url="https://www.tiktok.com/@morechulaa/video/7636986702262717704"),
             dict(png="macro-1-1-tiktok-viviankh-mealprep.png",
                  caption="@viviank.h documenta 10 sándwiches + 9 porciones congeladas — meal prep de 3 semanas.",
                  source="TikTok @viviank.h · 2025",
                  url="https://www.tiktok.com/@viviank.h/video/7620501104765177108"),
             dict(png="macro-1-0-mktreports-mealprep-market.png",
                  caption="Mercado global meal prep US$36,433M en 2026, CAGR 9.84% hasta 2035.",
                  source="Market Reports World · 2026",
                  url="https://www.marketreportsworld.com/market-reports/meal-prep-market-14713709"),
         ]),
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="Las empresas descubrieron que si el empleado come bien al mediodía rinde mejor en la tarde — y el menú de almuerzo se volvió beneficio.",
         fenomeno="El trabajador de 8-5 está harto de comer calentado. Fripick deja que la empresa pague la comida y la descuente en quincena. La comida del mediodía dejó de ser problema individual — ahora es categoría B2B.",
         hashtags="#LunchMenuRD · #AlmuerzoDeTrabajo · #NegocioOyó",
         triggers=[
             dict(stat="+13%",   desc="YoY tráfico en restaurantes LATAM con lunch menus de shoulder hour pricing.", source="OpenTable / QSR Magazine · 2025-2026"),
             dict(stat="84%",    desc="Percibe los precios de alimentos como 'altos'; dos tercios prefieren opciones económicas para el almuerzo.", source="Purdue / Family Dinner Project · 2025"),
             dict(stat="RD$425", desc="Ticket promedio almuerzo corporativo vía Fripick — descuento en quincena, llega caliente en 25 min.", source="Fripick.com · 2025"),
         ],
         signals=[
             dict(png="macro-1-2-tiktok-toyantoja-noccila-lunch.png",
                  caption="@toyantoja muestra lunch en Nocciola por menos de RD$500 — dato que 'vale oro' para el trabajador.",
                  source="TikTok @toyantoja · 2025",
                  url="https://www.tiktok.com/@toyantoja/video/7610215257000234247"),
             dict(png="macro-1-2-fripick-rd-brand.png",
                  caption="Fripick RD — beneficio alimentario corporativo B2B con descuento en quincena.",
                  source="Fripick · 2025",
                  url="https://fripick.com"),
             dict(png="macro-1-0-mktreports-mealprep-market.png",
                  caption="Inflación alimentaria RD 8.03% interanual ene 2026 — el delivery se vuelve cálculo costo-tiempo.",
                  source="BCRD / Dominican Today · 2026",
                  url="https://www.marketreportsworld.com/market-reports/meal-prep-market-14713709"),
         ]),
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="Te crió con miedo a lo 'malo' y ahora comer se siente como culpa. TikTok escuchó el término y lo convirtió en trend con millones de views.",
         fenomeno="La mamá que controlaba cada bocado crió hijas con relación rota con el plato. La almond mom no es solo un meme — es una cadena generacional. La adultez de esa hija inventa otra forma de comer sin la voz de mamá.",
         hashtags="#AlmondMom · #TraumasDietéticos · #ComerConCulpa",
         triggers=[
             dict(stat="30M",   desc="De americanos desarrollarán un trastorno alimentario en su vida — 2da enfermedad mental más mortal.", source="ANAD / ABC News · 2025"),
             dict(stat="42%",   desc="De niñas de 1°-3° quiere ser más delgada; 81% de niños de 10 años teme engordar.", source="ANAD Statistics · 2025"),
             dict(stat="LATAM", desc="@nour vilà lleva el trauma dietético al español bajo #almondmum — herencia sin cuestionamiento.", source="TikTok @nourvilaa · 2025"),
         ],
         signals=[
             dict(png="macro-1-3-tiktok-lielle-almondmom.png",
                  caption="@Lielle & Dee recrea rutina #almondmom — suplementos, restricción, rutina heredada sin cuestionar.",
                  source="TikTok @liellewaldman17 · 2025",
                  url="https://www.tiktok.com/@liellewaldman17/video/7617943870797630750"),
             dict(png="macro-1-3-tiktok-nourvilaa-almondmom.png",
                  caption="@nour vilà — #almondmum versión LATAM del trauma dietético en español/francés.",
                  source="TikTok @nourvilaa · 2025",
                  url="https://www.tiktok.com/@nourvilaa/video/7642383470026657046"),
             dict(png="macro-2-1-flinders-fitnessapp-disorder.png",
                  caption="Fitness apps fuelling disordered eating — foto editorial persona con teléfono, Flinders U. 2025.",
                  source="Flinders University · Feb 2025",
                  url="https://news.flinders.edu.au/blog/2025/02/22/fitness-apps-fuelling-disordered-eating/"),
         ]),
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="La diferencia entre un domingo con familia y uno solo se mide en una pregunta: ¿qué vamos a comer?",
         fenomeno="Para familias grandes el domingo es sancocho, mesa llena, todos. Para el foráneo que vive solo, es el día más difícil. La brecha no es nutricional — es emocional.",
         hashtags="#DomingoSolo · #ForáneoEnLaCapital · #SinMesaNoHayDomingo",
         triggers=[
             dict(stat="45%",   desc="De hogares come junto menos que hace una década; 84% querría compartir más comidas.", source="Simirity / FMI Foundation · 2025-2026"),
             dict(stat="17%",   desc="De familias dominicanas no comparte las horas de comida (P25 Código Casa).", source="Código Casa · 2025"),
             dict(stat="2025",  desc="World Happiness Report vincula compartir comidas con conectividad social y bienestar subjetivo.", source="World Happiness Report · 2025"),
         ],
         signals=[
             dict(png="macro-1-4-tiktok-josheilyn-foranea-capital.png",
                  caption="@Josheilyn — 'yo amo estar en mi hogar los domingos' — foránea RD viviendo en la capital.",
                  source="TikTok @josheilyndls1 · 2025",
                  url="https://www.tiktok.com/@josheilyndls1/video/7549991019169811768"),
             dict(png="macro-1-4-tiktok-mariannycorderoo-domingo.png",
                  caption="@mariannycorderoo — domingo solo en Bogotá con tostada y #amorpropio, ritual sin mesa familiar.",
                  source="TikTok @mariannycorderoo · 2025",
                  url="https://www.tiktok.com/@mariannycorderoo/video/7643570804885572882"),
             dict(png="macro-1-4-tiktok-macaseason-domingo-familiar.png",
                  caption="@María Camila — el ritual del domingo familiar completo como contraste al foráneo solo.",
                  source="TikTok @macaseason · 2025",
                  url="https://www.tiktok.com/@macaseason/video/7625031259835665685"),
         ]),
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="PedidosYa es la app #1 de food en RD: el adulto joven ya no decide qué cocinar entre semana, decide qué pedir — y esa es su nueva forma de ser adulto.",
         fenomeno="La adultez tradicional cocinaba todos los días. La adultez 2026 delega el jueves a una app. No es flojera — es renegociación del rol de 'buen adulto' donde el tiempo cuesta más que la comida.",
         hashtags="#PedidosYaRD · #DeliveryEsMiMamá · #AdultoQueNoCocina",
         triggers=[
             dict(stat="#1",    desc="PedidosYa en iOS food & drink RD; 13K-21.7K descargas semanales Q1 2025.", source="Sensor Tower · Q1 2025"),
             dict(stat="50%",   desc="Precios de alimentos RD subieron entre julio 2019 y julio 2025 — delivery se vuelve cálculo.", source="BCRD / Dominican Today · 2026"),
             dict(stat="100%",  desc="Online — primer supermercado 100% digital abre en Santo Domingo; la grocería migra a app.", source="St Kitts Nevis Observer · 2025"),
         ],
         signals=[
             dict(png="macro-1-5-pedidosya-country-selector.png",
                  caption="PedidosYa selector de países — RD listada con badges App Store y Google Play.",
                  source="PedidosYa · 2026",
                  url="https://www.pedidosya.com"),
             dict(png="macro-1-5-sensortower-pedidosya-rd-chart.png",
                  caption="Bar chart Sensor Tower: PedidosYa #1 en descargas food delivery RD Q1 2025.",
                  source="Sensor Tower · Q1 2025",
                  url="https://sensortower.com/blog/2025-q1-unified-top-5-food%20delivery%20services-units-do-63da96fbe1714cfff1c1e5a1"),
             dict(png="macro-1-5-stkitts-online-super-sd.png",
                  caption="Primer supermercado 100% online en Santo Domingo — la grocería migra a app.",
                  source="St Kitts Nevis Observer · 2025",
                  url="https://www.thestkittsnevisobserver.com/first-online-only-supermarket-opens-in-santo-domingo/"),
         ]),
    # ── Macro 2 ──────────────────────────────────────────────────────────────
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="Una foto de tu plato no sabe lo que comes. Pero el algoritmo te convence de que sí — y le crees más a la app que a tu propio cuerpo.",
         fenomeno="Las apps de conteo calórico pasaron de herramienta a obsesión. El algoritmo que 'te ayuda a comer mejor' se convierte en la voz que condena cada nutriente. El número en pantalla pesa más que la saciedad.",
         hashtags="#AppQueEnfermó · #MyFitnessPalToxic · #AlgoritmoDeMiDieta",
         triggers=[
             dict(stat="180M",  desc="Usuarios MyFitnessPal; 75% de pacientes con trastorno alimentario la usaba.", source="GripRoom / PMC NLM · 2026"),
             dict(stat="73%",   desc="De pacientes con trastorno creyó que la app contribuyó al desarrollo del mismo.", source="GripRoom / PMC NLM · 2026"),
             dict(stat="⚠",     desc="Apps con IA de reconocimiento por foto funcionan como 'gateway' a trastorno en perfeccionistas.", source="Sage Journals / Ohio State · 2024-2026"),
         ],
         signals=[
             dict(png="macro-2-1-myfitnesspal-app-ui.png",
                  caption="MyFitnessPal UI — 976 cal + macro breakdown. 'Nutrition tracking for real life'.",
                  source="MyFitnessPal · 2026",
                  url="https://www.myfitnesspal.com"),
             dict(png="macro-2-1-flinders-fitnessapp-disorder.png",
                  caption="Fitness apps fuelling disordered eating — Flinders University 2025.",
                  source="Flinders University · Feb 2025",
                  url="https://news.flinders.edu.au/blog/2025/02/22/fitness-apps-fuelling-disordered-eating/"),
             dict(png="macro-2-2-cropink-social-food-stats.png",
                  caption="74% usa redes para decidir qué comer — el feed como primer nutricionista.",
                  source="Cropink · 2026",
                  url="https://cropink.com/restaurant-social-media-statistics"),
         ]),
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="Antes mamá decidía qué había de comer. Hoy lo decide el For You Page — y de paso te vende los ingredientes en el mismo scroll.",
         fenomeno="El joven dominicano abre TikTok antes de abrir el refrigerador. Las recetas virales compiten con la tradición oral heredada — y en muchos hogares jóvenes el algoritmo está ganando.",
         hashtags="#TikTokRecetas · #ForYouPageDeCocina · #AlgoritmoDeAlmuerzo",
         triggers=[
             dict(stat="42",       desc="Índice de contenido food en TikTok enero 2026 — la plataforma como primer recetario.", source="Accio / TikTok Food Trends · 2026"),
             dict(stat="US$759M",  desc="GMV de food en TikTok Shop 2025 — integración receta → carrito en plataforma.", source="Capital One Shopping · 2025"),
             dict(stat="2×",       desc="Las marcas grandes casi duplicaron ventas en TikTok Shop en 2025.", source="Modern Retail · 2025"),
         ],
         signals=[
             dict(png="macro-2-2-tiktokshop-food-gmv.png",
                  caption="TikTok Shop: food = 13.6% del GMV total 2025. El supermercado vive dentro del feed.",
                  source="Resourcera · 2026",
                  url="https://resourcera.com/data/social/tiktok-shop-statistics/"),
             dict(png="macro-2-2-modernretail-tiktokshop-brands.png",
                  caption="Modern Retail: ventas de marcas grandes casi duplicaron en TikTok Shop 2025.",
                  source="Modern Retail · 2025",
                  url="https://www.modernretail.co/technology/sales-from-major-brands-on-tiktok-shop-nearly-doubled-in-2025-drawing-ulta-and-sally-beauty/"),
             dict(png="macro-2-2-cropink-social-food-stats.png",
                  caption="74% usa redes para decidir qué comer; 50% reporta influencia directa.",
                  source="Cropink · 2026",
                  url="https://cropink.com/restaurant-social-media-statistics"),
         ]),
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="El truco de poner un video para que el niño coma se convirtió en condición — el iPad es la única forma de que el plato baje.",
         fenomeno="El niño no come sin el iPad. El joven de 18 no cena sin Netflix. La pantalla dejó de ser acompañamiento y se volvió condición. La mesa familiar tiene un competidor que casi siempre gana.",
         hashtags="#iPadKid · #PantallaMientrasCome · #NetflixYCena",
         triggers=[
             dict(stat="40%",    desc="De niños tiene iPad a los 2 años; 2.6 hrs/día promedio; solo 1% cumple límites recomendados.", source="Common Sense Media · 2025"),
             dict(stat="2 años", desc="Edad a la que 4 de cada 10 niños ya tiene tablet según Census 2025 de Common Sense Media.", source="K12 Dive / CSM · 2025"),
             dict(stat="17%",    desc="De familias dominicanas no comparte las horas de comida — y donde sí comparten, la pantalla se sentó primero.", source="Código Casa · 2025"),
         ],
         signals=[
             dict(png="macro-2-3-tiktok-ipadkid-debate.png",
                  caption="TikTok debate viral: 'Kids and iPads at the table… yes or no?' — pantallas en la mesa.",
                  source="TikTok @sextedmyboss · 2025",
                  url="https://www.tiktok.com/@sextedmyboss/video/7475054384771075350"),
             dict(png="macro-2-3-k12dive-csm-screentimekids.png",
                  caption="'Half of young children own a cell phone or tablet' — foto editorial niño con tablet.",
                  source="K12 Dive / Common Sense Media · 2025",
                  url="https://www.k12dive.com/news/half-of-young-children-own-a-cell-phone-or-tablet/741318/"),
             dict(png="macro-2-3-newsmedical-screentime-proxy.png",
                  caption="GLP-1 altera apetito y comportamiento — proxy de la pantalla como mediador del comer.",
                  source="News Medical · 2026",
                  url="https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx"),
         ]),
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="El consumidor sano se pega un sensor de glucosa por dos semanas y descubre que la uva le sube más el azúcar que el helado. La nutrición ya es dato en tiempo real.",
         fenomeno="Los wearables de glucosa OTC (Lingo, Stelo) salieron del nicho diabético y entraron al consumer health. El 'comer bien' dejó de ser opinión — ahora es métrica continua.",
         hashtags="#LingoRD · #SensorDeGlucosa · #ComerConDato · #MetabolicAge",
         triggers=[
             dict(stat="US$80B",  desc="Mercado de wearables y health tracking en 2024; proyecta US$200B+ para 2030.", source="Statista · 2025"),
             dict(stat="14 días", desc="Abbott Lingo — CGM sin prescripción, biosensor de 14 días en Walmart y Amazon.", source="Abbott Newsroom · 2025"),
             dict(stat="OTC",     desc="FDA aprobó primeros CGMs OTC en 2024; expansión al consumidor no-diabético.", source="Scripps News · 2025"),
         ],
         signals=[
             dict(png="macro-2-4-hellolingo-cgm-hero.png",
                  caption="Abbott Lingo hero — mujer con sensor en brazo: 'My glucose, my insights'. CGM OTC.",
                  source="Abbott Lingo · 2025",
                  url="https://www.hellolingo.com"),
             dict(png="macro-2-4-scripps-cgm-sensor-arm.png",
                  caption="Foto AP: brazo con sensor de glucosa — 'CGMs in vogue' para consumidor no-diabético.",
                  source="Scripps News / AP · 2025",
                  url="https://www.scrippsnews.com/health/continuous-glucose-monitors-are-in-vogue-but-do-you-really-need-to-track-your-blood-sugar"),
             dict(png="macro-2-0-resourcera-tiktokshop-gmv.png",
                  caption="TikTok Shop Key Insights 2026: GMV US$64.3B — el contexto tech que rodea al wearable.",
                  source="Resourcera · 2026",
                  url="https://resourcera.com/data/social/tiktok-shop-statistics/"),
         ]),
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="Una creadora cocina en vivo, te muestra el producto, lo agregas al carrito sin salir del feed. El supermercado se volvió streaming.",
         fenomeno="Live shopping pasó del nicho beauty al supermercado: snacks, salsas, kits de receta vendidos durante el video. Food es 13.6% del GMV de TikTok Shop. El próximo carrito será un live stream.",
         hashtags="#TikTokShopFood · #CocinaEnVivo · #CarritoDelFeed",
         triggers=[
             dict(stat="US$64.3B", desc="GMV total TikTok Shop 2025; food = 13.6% = US$759.84M; ticket food US$43.20.", source="Capital One Shopping / Resourcera · 2025-2026"),
             dict(stat="+84%",     desc="Live shopping creció 84% YoY en 2025; conversión live 6.1% vs feed 4.7%.", source="Resourcera · 2026"),
             dict(stat="1er",      desc="Primer supermercado 100% online abre en Santo Domingo — grocery digital prepara terreno.", source="St Kitts Nevis Observer · 2025"),
         ],
         signals=[
             dict(png="macro-2-5-modernretail-tiktokshop-2025.png",
                  caption="Modern Retail: TikTok Shop 2025 — marcas grandes duplicaron ventas; food como categoría #1.",
                  source="Modern Retail · 2025",
                  url="https://www.modernretail.co/technology/sales-from-major-brands-on-tiktok-shop-nearly-doubled-in-2025-drawing-ulta-and-sally-beauty/"),
             dict(png="macro-2-5-resourcera-tiktokshop-stats.png",
                  caption="Resourcera: GMV US$64.3B + ticket food US$43.20 + live shopping +84% YoY.",
                  source="Resourcera · 2026",
                  url="https://resourcera.com/data/social/tiktok-shop-statistics/"),
             dict(png="macro-1-5-stkitts-online-super-sd.png",
                  caption="Primer super 100% online en Santo Domingo — la grocería dominicana migra a app.",
                  source="St Kitts Nevis Observer · 2025",
                  url="https://www.thestkittsnevisobserver.com/first-online-only-supermarket-opens-in-santo-domingo/"),
         ]),
    # ── Macro 3 ──────────────────────────────────────────────────────────────
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="Ver lo que otros comen se convirtió en uno de los formatos más consumidos de internet. Ya no es comida — es identidad.",
         fenomeno="'What I Eat in a Day' explota no por curiosidad culinaria — por validación. Ver lo que come otro para confirmar, comparar o inspirarse. El plato ajeno es espejo. Y juez.",
         hashtags="#QuéComoEnUnDía · #WhatIEatInADay · #AlimentaciónEnPantalla",
         triggers=[
             dict(stat="74%",  desc="De personas usa redes para decidir qué/dónde comer; 50% reporta influencia directa.", source="Cropink · 2026"),
             dict(stat="Top",  desc="'What I Eat in a Day' entre top food trends 2026; engagement que el algoritmo premia.", source="Chowhound / TikTok Trends · 2026"),
             dict(stat="2026", desc="Whole Foods predice bowl colorido como 'comer bien aspiracional' que WIEIAD replica.", source="VegNews · 2025"),
         ],
         signals=[
             dict(png="macro-3-1-tiktok-wieiad-hanfoodfit.png",
                  caption="@hanfoodfit — 'What I eat in a day, healthy and balanced' aspiracional #8020rule.",
                  source="TikTok @hanfoodfit · 2025",
                  url="https://www.tiktok.com/@hanfoodfit/video/7493474947029880086"),
             dict(png="macro-3-1-vegnews-food-trend-hero.png",
                  caption="Bowl proteína + grains + vegetales coloridos — 'comer bien aspiracional 2026' que WIEIAD replica.",
                  source="VegNews · 2025",
                  url="https://vegnews.com/fiber-whole-foods-2026-top-trend"),
             dict(png="macro-3-1-cropink-social-food-decisions.png",
                  caption="Cropink: 74% usa redes para decidir qué comer; el feed como nutricionista.",
                  source="Cropink · 2026",
                  url="https://cropink.com/restaurant-social-media-statistics"),
         ]),
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="El mukbang nació porque hay gente que come sola y prefiere ver a alguien comer antes que comer en silencio.",
         fenomeno="Nació en Corea como compañía virtual. Hoy es negocio millonario. El dominicano lo consume porque la mesa vacía duele — y una pantalla llena el silencio del comedor.",
         hashtags="#MukbangLatino · #ComerSoloPeroNoTanto · #SoledadEnLaMesa",
         triggers=[
             dict(stat="5.3M",  desc="#mukbang supera 5.3M videos en 2025; top creadores ganan hasta US$10K/mes.", source="Distraction Magazine / PMC · 2025"),
             dict(stat="68.5%", desc="De jóvenes universitarias ve videos de comida regularmente — vínculo parasocial como consuelo.", source="Western Gazette / PMC · 2025-2026"),
             dict(stat="2B+",   desc="Nickocado Avocado supera 2B views en YouTube — el mukbang como negocio millonario.", source="PMC · 2025"),
         ],
         signals=[
             dict(png="macro-3-2-youtube-mukbang-search-grid.png",
                  caption="Grid YouTube 'mukbang' — thumbnails comida extrema + ASMR con millones de vistas.",
                  source="YouTube · 2026",
                  url="https://www.youtube.com/results?search_query=mukbang"),
             dict(png="macro-3-1-tiktok-wieiad-hanfoodfit.png",
                  caption="@hanfoodfit — formato WIEIAD como compañía parasocial; el comer-en-pantalla.",
                  source="TikTok @hanfoodfit · 2025",
                  url="https://www.tiktok.com/@hanfoodfit/video/7493474947029880086"),
             dict(png="macro-3-3-newsmedical-cooking-proxy.png",
                  caption="Medicalización del hambre — GLP-1 crea contrapunto; el mukbang es el polo opuesto analógico.",
                  source="News Medical · 2026",
                  url="https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx"),
         ]),
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="Cuando todo lo demás está fuera de control, la cocina es el único sitio donde lo que hago sí sale como quiero.",
         fenomeno="Bajo burnout y presión social, adultos jóvenes descubrieron que cocinar y hornear son terapia real. No es hobbyismo — es el único espacio donde lo que controlas eres tú.",
         hashtags="#CocinaComoTerapia · #HornearParaDesestresarse · #LoveLanguageCocina",
         triggers=[
             dict(stat="↓",     desc="Hornear activa rutas de dopamina y reduce cortisol — equivalente a mindfulness clínico según Kaiser Permanente.", source="Kaiser Permanente / NeuroLaunch · 2025-2026"),
             dict(stat="2026",  desc="Ola de cancelaciones de delivery + vuelta a la cocina como anti-ansiedad digital.", source="EditorialGe / Cooking as Therapy · 2026"),
             dict(stat="GLP-1", desc="Medicalización del hambre (Ozempic) crea contrapunto cultural: la cocina como ritual analógico.", source="News Medical · 2026"),
         ],
         signals=[
             dict(png="macro-3-3-tiktok-natalie-stressbaking.png",
                  caption="@chef_natalie_ — 'stress baking is my form of therapy' #bakingtherapy #bakingtiktok.",
                  source="TikTok @chef_natalie_ · 2025",
                  url="https://www.tiktok.com/@chef_natalie_/video/7569545767090703647"),
             dict(png="macro-3-3-newsmedical-cooking-proxy.png",
                  caption="Jeringa semaglutide — GLP-1 altera apetito; la cocina como contrapunto analógico a la farmacología.",
                  source="News Medical · 2026",
                  url="https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx"),
             dict(png="macro-3-1-vegnews-food-trend-hero.png",
                  caption="Bowl aspiracional 2026 — cocinar para el feed y para el alma; el plato que también es estética.",
                  source="VegNews · 2025",
                  url="https://vegnews.com/fiber-whole-foods-2026-top-trend"),
         ]),
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="El FOMO de bajar de peso llegó a su versión más extrema: eliminar todo lo que no sea animal. Los análisis de sangre cuentan otra historia.",
         fenomeno="Joe Rogan lo popularizó, los influencers lo viralizaron. Solo carne, mantequilla y huevo. El algoritmo lo distribuye más rápido que la evidencia clínica que lo contradice.",
         hashtags="#DietaCarnívora · #FOMODeBajarDePeso · #CarnivoreVsColesterol",
         triggers=[
             dict(stat="2.6M",   desc="#carnivore supera 2.6M publicaciones en Instagram a noviembre 2025.", source="ResearchGate / Fox News · 2025-2026"),
             dict(stat="LDL +36",desc="LDL promedio sube de 126 a 172 mg/dL; un caso documentado pasó de 163 a 365.", source="Nutrients Journal · Ene 2026"),
             dict(stat="2026",   desc="Whole Foods predice 'Year of the Fiber' + flexitarian — mainstream pivota mientras carnivore escala.", source="Whole Foods / VegNews · 2026"),
         ],
         signals=[
             dict(png="macro-3-4-tiktok-carnivore-steakbuttergal.png",
                  caption="@Steakandbuttergal — #carnivorediet: la creadora más viral de solo carne + mantequilla + huevos.",
                  source="TikTok @steakandbuttergal · 2025",
                  url="https://www.tiktok.com/@steakandbuttergal/video/7577437952679087374"),
             dict(png="macro-3-4-vegnews-protein-fiber-trend.png",
                  caption="Bowl colorido aspiracional 2026 — pivot mainstream de proteína → fibra mientras carnivore escala.",
                  source="VegNews · 2025",
                  url="https://vegnews.com/fiber-whole-foods-2026-top-trend"),
             dict(png="macro-3-0-vegnews-wholefoods-fiber-2026.png",
                  caption="'Move Over Protein' — Whole Foods predice Año de la Fibra 2026 como contratendencia.",
                  source="VegNews · Oct 2025",
                  url="https://vegnews.com/fiber-whole-foods-2026-top-trend"),
         ]),
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="GLP-1 silencia el 'food noise' del cerebro. La nueva conversación sobre comer no es qué cocinar — es si lo deseo o solo me acordé que existía.",
         fenomeno="Ozempic y Mounjaro reescriben la relación con la comida: ya no se trata de fuerza de voluntad — se trata de farmacología que apaga el ruido mental. El feed normaliza la conversación.",
         hashtags="#FoodNoise · #OzempicDiary · #SinHambreSinAnsiedad · #GLP1RD",
         triggers=[
             dict(stat="58%",   desc="Siente menos hambre con GLP-1; 64% se llena antes; 21-23% reporta cambios de sabor.", source="EASD 2025 / News-Medical · 2025"),
             dict(stat="n=411", desc="Survey EASD Annual Meeting 2025 sobre impacto cognitivo del GLP-1 en el food noise.", source="EASD 2025"),
             dict(stat="🧠",    desc="Scientific American + Medscape documentan cómo GLP-1 reduce respuesta cerebral a comida.", source="Scientific American / Medscape · 2025"),
         ],
         signals=[
             dict(png="macro-3-5-sciam-ozempic-food-noise.png",
                  caption="SciAm: ilustración surrealista — cabeza clásica con comida girando. 'Ozempic Quiets Food Noise'.",
                  source="Scientific American · Jun 2024",
                  url="https://www.scientificamerican.com/article/ozempic-quiets-food-noise-in-the-brain-but-how/"),
             dict(png="macro-3-5-newsmedical-glp1-appetite.png",
                  caption="Jeringa semaglutide — 58% siente menos hambre con GLP-1; 64% se llena antes (EASD 2025).",
                  source="News Medical · 2026",
                  url="https://www.news-medical.net/health/How-GLP-1-Weight-Loss-Drugs-Affect-Appetite-Mood-and-Behavior.aspx"),
             dict(png="macro-3-5-tiktok-glp1-foodnoise.png",
                  caption="@JanelleRohner — responde sobre GLP-1 y food noise; #glp1community decenas de millones de views.",
                  source="TikTok @janellerohner · 2025",
                  url="https://www.tiktok.com/@janellerohner/video/7564545141835418911"),
         ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# BUILD
# ══════════════════════════════════════════════════════════════════════════════
DIVIDERS = [
    (1, M1_NAME, M1_TAG),
    (2, M2_NAME, M2_TAG),
    (3, M3_NAME, M3_TAG),
]
macro_divider_indices = [0, 5, 10]  # before micro indices 0-4, 5-9, 10-14

for div_pos, (d_num, d_name, d_tag) in zip(macro_divider_indices, DIVIDERS):
    pass  # we build sequentially below

# Build all 18 slides in order: divider, 5 micros, divider, 5 micros, ...
slide_num = 0
for macro_idx in range(3):
    d_num, d_name, d_tag = DIVIDERS[macro_idx]
    add_macro_divider(d_num, d_name, d_tag)
    for micro in MICROS[macro_idx*5 : macro_idx*5 + 5]:
        add_micro(micro['macro_n'], micro['macro_name'],
                  micro['headline'], micro['fenomeno'],
                  micro['hashtags'], micro['triggers'], micro['signals'])

# ══════════════════════════════════════════════════════════════════════════════
# OVERFLOW AUDIT — REGLA #8 OBLIGATORIO
# ══════════════════════════════════════════════════════════════════════════════
SLIDE_W_PT  = 960
SLIDE_H_PT  = 540
SAFE_MARGIN = 4   # pt tolerance

def audit_slide(slide, idx):
    issues = []
    for sh in slide.shapes:
        if sh.left is None or sh.top is None:
            continue
        x = Emu(sh.left).pt
        y = Emu(sh.top).pt
        w = Emu(sh.width).pt  if sh.width  else 0
        h = Emu(sh.height).pt if sh.height else 0
        if y + h > SLIDE_H_PT + SAFE_MARGIN:
            issues.append(
                f"  OVERFLOW BOTTOM slide {idx}: "
                f"shape y={y:.1f} h={h:.1f} bottom={y+h:.1f} > {SLIDE_H_PT}"
            )
        if x + w > SLIDE_W_PT + SAFE_MARGIN:
            issues.append(
                f"  OVERFLOW RIGHT slide {idx}: "
                f"shape x={x:.1f} w={w:.1f} right={x+w:.1f} > {SLIDE_W_PT}"
            )
    return issues

all_issues = []
for i, sl in enumerate(prs.slides):
    all_issues += audit_slide(sl, i+1)

if all_issues:
    print("FAIL — overflow detectado:")
    for it in all_issues:
        print(it)
    raise SystemExit("BUILD FALLIDO. Ajusta dims antes de entregar.")
else:
    print(f"OK — {len(prs.slides)} slides sin overflow.")

# ══════════════════════════════════════════════════════════════════════════════
# SAVE
# ══════════════════════════════════════════════════════════════════════════════
OUT = BASE / "outputs" / "trends-alimentacion-forecast.pptx"
OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(str(OUT))
print(f"Guardado: {OUT}")

# ── Debug: report bottom-most shape on slide 2 ──
sl2 = list(prs.slides)[1]
bottoms = []
for sh in sl2.shapes:
    if sh.top is None: continue
    y = Emu(sh.top).pt
    h = Emu(sh.height).pt if sh.height else 0
    bottoms.append((y+h, sh.name if hasattr(sh,'name') else '?'))
if bottoms:
    max_bot = max(b[0] for b in bottoms)
    print(f"Slide 2 — bottom-most shape ends at: {max_bot:.1f}pt  (margin={SLIDE_H_PT-max_bot:.1f}pt)")
