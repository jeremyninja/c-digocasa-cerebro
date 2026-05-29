"""
trends_deck_engine.py — MOTOR CENTRAL DE LAYOUT del Team Trends CC.

═══════════════════════════════════════════════════════════════════════════════
ESTE ES EL "CSS" DEL TEAM TRENDS CC.
═══════════════════════════════════════════════════════════════════════════════
Todas las constantes de layout (posiciones, tamaños, gaps, colores, fuentes) y
todas las funciones de render viven AQUÍ y SOLO aquí. Cada capítulo
(build_trends_{capitulo}.py) importa este motor y le pasa únicamente DATOS:
los 3 dividers macro + los 15 micros + la carpeta de screenshots.

Cambiar una constante en este archivo re-renderiza TODOS los decks idénticos:
Educación, Consumos, Tecnología, Política, Alimentación y los que vengan.
NUNCA copies layout dentro de un build_trends_{capitulo}.py — solo datos.

Reglas duras de diseño: Team Trends CC/aprendizajes-montador-trends-cc.md
(headline 20pt fijo, triggers cifra-arriba, fotos 88×130pt, sin needs,
hashtags 16pt, padding mínimo, sin placeholders, validador de overflow).
═══════════════════════════════════════════════════════════════════════════════
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pathlib import Path
from lxml import etree
from pptx.oxml.ns import qn

# ─── Colours ──────────────────────────────────────────────────────────────────
C_BG        = RGBColor(0x0D, 0x0D, 0x0D)
C_WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
C_GREY      = RGBColor(0xA0, 0xA0, 0xA0)
C_DARK_GREY = RGBColor(0x66, 0x66, 0x66)
C_TAB_BG    = RGBColor(0xE8, 0xE8, 0xE8)
C_RED       = RGBColor(0xFF, 0x2D, 0x2D)
C_PLACEHLD  = RGBColor(0x1A, 0x1A, 0x1A)

# ─── Fuentes ────────────────────────────────────────────────────────────────────
F_SERIF   = "Instrument Serif"
F_SANS    = "Poppins"

# ─── Canvas (pt) ────────────────────────────────────────────────────────────────
SLIDE_W = 960.0   # 13.333 in
SLIDE_H = 540.0   # 7.5 in

# ─── Columnas ─────────────────────────────────────────────────────────────────
COL_LEFT_X  = 20.0;  COL_LEFT_W  = 290.0
COL_MID_X   = 330.0; COL_MID_W   = 290.0
COL_RIGHT_X = 640.0; COL_RIGHT_W = 300.0

# ─── Cabecera del slide micro ───────────────────────────────────────────────────
TAB_Y     = 10.0; TAB_H    = 22.0
LABELS_Y  = 50.0; LABELS_H = 14.0     # = TAB_Y + TAB_H + 18 (TAB_TO_LABELS)
HLINE_Y   = 68.0                      # = LABELS_Y + LABELS_H + 6
CONTENT_Y = 84.0                      # = HLINE_Y + 10 (LABELS_TO_CONTENT)

# ─── Col-left (DEFINICIÓN) ──────────────────────────────────────────────────────
HEADLINE_PT      = 20.0   # REGLA #1 — FIJO, sin auto-fit
HEADLINE_H       = 48.0
PHENOM_LABEL_Y   = CONTENT_Y + HEADLINE_H + 20.0
PHENOM_LABEL_H   = 14.0
PHENOM_BODY_Y    = PHENOM_LABEL_Y + PHENOM_LABEL_H + 6.0
PHENOM_BODY_H    = 84.0
HASH_LABEL_Y     = PHENOM_BODY_Y + PHENOM_BODY_H + 18.0
HASH_LABEL_H     = 14.0
HASH_BODY_Y      = HASH_LABEL_Y + HASH_LABEL_H + 6.0
HASH_BODY_H      = 52.0
PHENOM_PT        = 10.0   # body fenómeno
HASHTAG_PT       = 16.0   # REGLA #5 — NO 23pt
# (SIN 3 needs — REGLA #4)

# ─── Col-center (TRIGGERS) — REGLA #2 ───────────────────────────────────────────
STAT_PT          = 56.0   # cifra (NO 72pt)
STAT_W           = 170.0  # = ancho de la caja desc (NO ancho completo de columna)
STAT_H           = 56.0
STAT_TO_DESC_GAP = 18.0   # (NO 10pt)
DESC_W           = 170.0
DESC_H           = 35.0
DESC_PT          = 10.0
DESC_TO_SRC_GAP  = 6.0
SRC_PT           = 6.5
SRC_H            = 12.0
TRIGGER_GAP      = 28.0   # (NO 24pt)
# Block = 56+18+35+6+12 = 127pt; 3×127 + 2×28 = 437 → 84+437=521 < 540 ✓

# ─── Col-right (SEÑALES) — REGLA #3 ─────────────────────────────────────────────
PHOTO_W   = 88.0          # (NO 95, NO 110, NO 149)
PHOTO_H   = 130.0
PHOTO_GAP = 24.0
CAP_OFFSET_X = PHOTO_W + 8.0
CAP_W        = 162.0
CAP_H        = 35.0
CAP_PT       = 10.0
# 3×130 + 2×24 = 438 → 84+438=522 < 540 ✓

# ─── Badge ──────────────────────────────────────────────────────────────────────
BADGE_W = 38.0; BADGE_H = 11.0; BADGE_PT = 5.5

# ─── Divider macro ──────────────────────────────────────────────────────────────
DIV_LABEL_PT = 14.0; DIV_NAME_PT = 100.0; DIV_TAG_PT = 24.0

# ─── Validador de overflow — REGLA #8 ───────────────────────────────────────────
SAFE_MARGIN = 4.0


# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════
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
    spcPct.set('val', str(int(sp_pct * 1000)))

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
    cx = max(abs(x2-x1), 1); cy = max(abs(y2-y1), 1)
    lx = min(x1, x2);        ly = min(y1, y2)
    conn = slide.shapes.add_connector(1, emupt(lx), emupt(ly),
                                      emupt(lx+cx), emupt(ly+cy))
    conn.line.color.rgb = C_WHITE
    conn.line.width = Pt(1)
    solidFill = conn._element.find('.//' + qn('a:solidFill'))
    if solidFill is not None:
        srgb = solidFill.find(qn('a:srgbClr'))
        if srgb is not None:
            a_el = etree.SubElement(srgb, qn('a:alpha'))
            a_el.set('val', str(alpha_pct * 1000))


# ══════════════════════════════════════════════════════════════════════════════
# COMPONENTES DEL SLIDE MICRO
# ══════════════════════════════════════════════════════════════════════════════
def add_tabs(slide, macro_n, macro_name):
    add_rect(slide, COL_LEFT_X, TAB_Y, 58, TAB_H, fill=C_TAB_BG)
    _, tf = _tb(slide, COL_LEFT_X+4, TAB_Y+3, 52, TAB_H-4)
    _run(tf, macro_n, F_SANS, 7.5, bold=True, color=RGBColor(0,0,0))
    add_rect(slide, COL_LEFT_X+62, TAB_Y, 220, TAB_H, line_rgb=C_DARK_GREY)
    _, tf2 = _tb(slide, COL_LEFT_X+66, TAB_Y+3, 214, TAB_H-4)
    _run(tf2, macro_name.upper(), F_SANS, 7.5, color=C_GREY)

def add_col_labels(slide):
    for x, lbl in [(COL_LEFT_X, "DEFINICIÓN"),
                   (COL_MID_X,  "TRIGGERS"),
                   (COL_RIGHT_X,"SEÑALES")]:
        _, tf = _tb(slide, x, LABELS_Y, 200, LABELS_H)
        _run(tf, lbl, F_SANS, 8, bold=True, color=C_GREY)

def add_seps(slide):
    add_line_connector(slide, COL_MID_X-6,   LABELS_Y, COL_MID_X-6,   SLIDE_H-10)
    add_line_connector(slide, COL_RIGHT_X-6, LABELS_Y, COL_RIGHT_X-6, SLIDE_H-10)
    add_line_connector(slide, COL_LEFT_X,    HLINE_Y,  SLIDE_W-20,    HLINE_Y)

def add_col_left(slide, headline, fenomeno, hashtags):
    # HEADLINE — 20pt FIJO (REGLA #1)
    _, tf = _tb(slide, COL_LEFT_X, CONTENT_Y, COL_LEFT_W, HEADLINE_H)
    _run(tf, headline.upper(), F_SERIF, HEADLINE_PT, color=C_WHITE, sp_pct=110, tracking=0)
    # EL FENÓMENO
    _, tf2 = _tb(slide, COL_LEFT_X, PHENOM_LABEL_Y, COL_LEFT_W, PHENOM_LABEL_H)
    _run(tf2, "EL FENÓMENO", F_SANS, 8, bold=True, color=C_GREY)
    _, tf3 = _tb(slide, COL_LEFT_X, PHENOM_BODY_Y, COL_LEFT_W, PHENOM_BODY_H)
    _run(tf3, fenomeno, F_SANS, PHENOM_PT, color=C_WHITE, sp_pct=100)
    # HASHTAGS — 16pt (REGLA #5)
    _, tf4 = _tb(slide, COL_LEFT_X, HASH_LABEL_Y, COL_LEFT_W, HASH_LABEL_H)
    _run(tf4, "HASHTAGS", F_SANS, 8, bold=True, color=C_GREY)
    _, tf5 = _tb(slide, COL_LEFT_X, HASH_BODY_Y, COL_LEFT_W, HASH_BODY_H)
    _run(tf5, hashtags, F_SERIF, HASHTAG_PT, color=C_WHITE, sp_pct=100, tracking=0)
    # (SIN 3 needs — REGLA #4)

def add_col_center(slide, triggers):
    """3 triggers vertical: cifra ARRIBA, caja desc ABAJO (REGLA #2)."""
    y = CONTENT_Y
    for trig in triggers:
        _, tf_s = _tb(slide, COL_MID_X, y, STAT_W, STAT_H)
        _run(tf_s, trig['stat'], F_SERIF, STAT_PT, color=C_WHITE, sp_pct=100, tracking=0)
        y_d = y + STAT_H + STAT_TO_DESC_GAP
        _, tf_d = _tb(slide, COL_MID_X, y_d, DESC_W, DESC_H)
        _run(tf_d, trig['desc'], F_SANS, DESC_PT, color=C_WHITE, sp_pct=100)
        y_src = y_d + DESC_H + DESC_TO_SRC_GAP
        _, tf_src = _tb(slide, COL_MID_X, y_src, DESC_W, SRC_H)
        _run(tf_src, trig['source'].upper(), F_SANS, SRC_PT, color=C_DARK_GREY, sp_pct=100)
        y = y_src + SRC_H + TRIGGER_GAP

def _hyperlink_picture(slide, pic, url):
    rId = slide.part.relate_to(
        url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',
        is_external=True)
    nvPicPr = pic._element.find('.//' + qn('p:nvPicPr'))
    if nvPicPr is not None:
        cNvPr = nvPicPr.find(qn('p:cNvPr'))
        if cNvPr is not None:
            hl = etree.SubElement(cNvPr, qn('a:hlinkClick'))
            hl.set('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id', rId)

def add_col_right(slide, signals, screenshots_dir):
    """3 fotos 88×130pt + badge + caption (REGLA #3, #7)."""
    y = CONTENT_Y
    for sig in signals:
        png_path = Path(screenshots_dir) / sig['png']
        if png_path.exists():
            pic = slide.shapes.add_picture(str(png_path), emupt(COL_RIGHT_X), emupt(y),
                                           emupt(PHOTO_W), emupt(PHOTO_H))
            if sig.get('url'):
                _hyperlink_picture(slide, pic, sig['url'])
        else:
            # REGLA #7: cero placeholder "manual"; si falta PNG es un fallo de flujo
            raise FileNotFoundError(
                f"Falta screenshot: {png_path}\n"
                f"Devuelve al scrapper (no se permite placeholder manual)."
            )
        # Badge CLICK ME
        bx = COL_RIGHT_X + PHOTO_W - BADGE_W - 2
        by = y + 2
        add_rect(slide, bx, by, BADGE_W, BADGE_H, fill=C_RED)
        _, tb = _tb(slide, bx+2, by+1, BADGE_W-4, BADGE_H-2)
        _run(tb, "CLICK ME", F_SANS, BADGE_PT, bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)
        # Caption al lado
        cx = COL_RIGHT_X + CAP_OFFSET_X
        _, tf_c = _tb(slide, cx, y, CAP_W, CAP_H)
        _run(tf_c, sig['caption'], F_SANS, CAP_PT, color=C_WHITE, sp_pct=100)
        sy = y + CAP_H + 6
        if sy + SRC_H <= SLIDE_H:
            _, tf_s = _tb(slide, cx, sy, CAP_W, SRC_H)
            _run(tf_s, sig['source'].upper(), F_SANS, SRC_PT, color=C_DARK_GREY, sp_pct=100)
        y += PHOTO_H + PHOTO_GAP


# ══════════════════════════════════════════════════════════════════════════════
# SLIDES COMPLETOS
# ══════════════════════════════════════════════════════════════════════════════
def add_macro_divider(prs, num, name, tagline):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide)
    cy = SLIDE_H / 2
    lbl_h = 20.0; lbl_y = cy - 90.0
    _, tf_l = _tb(slide, 0, lbl_y, SLIDE_W, lbl_h)
    _run(tf_l, f"MACRO {num}", F_SANS, DIV_LABEL_PT, bold=True, color=C_GREY, align=PP_ALIGN.CENTER)
    name_h = 130.0; name_y = lbl_y + lbl_h + 24.0
    _, tf_n = _tb(slide, 20, name_y, SLIDE_W-40, name_h)
    _run(tf_n, name.upper(), F_SERIF, DIV_NAME_PT, color=C_WHITE, align=PP_ALIGN.CENTER, sp_pct=95, tracking=0)
    tag_h = 36.0; tag_y = name_y + name_h
    _, tf_t = _tb(slide, 20, tag_y, SLIDE_W-40, tag_h)
    _run(tf_t, f'"{tagline}"', F_SERIF, DIV_TAG_PT, italic=True, color=C_GREY, align=PP_ALIGN.CENTER)
    return slide

def add_micro(prs, micro, screenshots_dir):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide)
    add_tabs(slide, micro['macro_n'], micro['macro_name'])
    add_col_labels(slide)
    add_seps(slide)
    add_col_left(slide, micro['headline'], micro['fenomeno'], micro['hashtags'])
    add_col_center(slide, micro['triggers'])
    add_col_right(slide, micro['signals'], screenshots_dir)
    return slide


# ══════════════════════════════════════════════════════════════════════════════
# VALIDADOR DE OVERFLOW — REGLA #8 (OBLIGATORIO)
# ══════════════════════════════════════════════════════════════════════════════
def audit_overflow(prs):
    issues = []
    for idx, slide in enumerate(prs.slides, 1):
        for sh in slide.shapes:
            if sh.left is None or sh.top is None:
                continue
            x = Emu(sh.left).pt; y = Emu(sh.top).pt
            w = Emu(sh.width).pt  if sh.width  else 0
            h = Emu(sh.height).pt if sh.height else 0
            if y + h > SLIDE_H + SAFE_MARGIN:
                issues.append(f"  OVERFLOW BOTTOM slide {idx}: y={y:.1f} h={h:.1f} bottom={y+h:.1f} > {SLIDE_H}")
            if x + w > SLIDE_W + SAFE_MARGIN:
                issues.append(f"  OVERFLOW RIGHT slide {idx}: x={x:.1f} w={w:.1f} right={x+w:.1f} > {SLIDE_W}")
    return issues


# ══════════════════════════════════════════════════════════════════════════════
# API PRINCIPAL — lo único que llama cada build_trends_{capitulo}.py
# ══════════════════════════════════════════════════════════════════════════════
def build_deck(dividers, micros, screenshots_dir, output_path):
    """
    Construye el deck completo de 18 slides (3 dividers + 15 micros) aplicando
    el layout central. Corre el validador de overflow ANTES de guardar.

    dividers        : lista de 3 tuplas (num, NAME, tagline)
    micros          : lista de 15 dicts {macro_n, macro_name, headline, fenomeno,
                      hashtags, triggers[3], signals[3]}
    screenshots_dir : carpeta con los PNGs de las señales
    output_path     : ruta del .pptx de salida
    """
    assert len(dividers) == 3, f"Se esperan 3 dividers, llegaron {len(dividers)}"
    assert len(micros) == 15, f"Se esperan 15 micros, llegaron {len(micros)}"

    prs = Presentation()
    prs.slide_width  = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Orden: divider M1, 5 micros, divider M2, 5 micros, divider M3, 5 micros
    for macro_idx in range(3):
        d_num, d_name, d_tag = dividers[macro_idx]
        add_macro_divider(prs, d_num, d_name, d_tag)
        for micro in micros[macro_idx*5 : macro_idx*5 + 5]:
            add_micro(prs, micro, screenshots_dir)

    # REGLA #8 — validar overflow antes de guardar
    issues = audit_overflow(prs)
    if issues:
        print("FAIL — overflow detectado:")
        for it in issues:
            print(it)
        raise SystemExit("BUILD FALLIDO. Ajusta dims en el motor antes de entregar.")
    print(f"OK — {len(prs.slides)} slides sin overflow.")

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out))
    print(f"Guardado: {out}")
    return out
