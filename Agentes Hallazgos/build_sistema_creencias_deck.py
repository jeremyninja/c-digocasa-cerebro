#!/usr/bin/env python3
"""
build_sistema_creencias_deck.py
================================
Deck sistema-de-creencias-deck-flat.pptx desde cero con python-pptx.
16 slides — set editorial cerrado sistema-de-creencias-hallazgos-editados.md (11 hallazgos).

Distribución por tensión:
  T1 — El cuerpo legal y el cuerpo del deseo (H01, H02)
       H01: cuanti 3 stats + Consumer Voice → 2 slides
       H02: cuanti 1 stat + Consumer Voice  → 2 slides
       Subtotal: 4 slides

  T2 — La fe como infraestructura (H03, H04)
       H03: cuanti 3 stats + Consumer Voice → 2 slides
       H04: cuanti 2 stats + Consumer Voice → 2 slides
       Subtotal: 4 slides

  T3 — El país que no mira a todos (H05, H06)
       H05: solo-cuanti 3 stats           → 1 slide
       H06: cuanti 2 stats + Consumer Voice → 2 slides
       Subtotal: 3 slides

  T4 — La violencia que no tiene nombre (H07, H08)
       H07: solo-cuanti 2 stats           → 1 slide
       H08: solo-cuali 1 verbatim         → 1 slide
       Subtotal: 2 slides

  T5 — La equidad pendiente (H09, H10, H11)
       H09: solo-cuanti 2 stats           → 1 slide
       H10: solo-cuanti 2 stats           → 1 slide
       H11: solo-cuanti 2 stats           → 1 slide
       Subtotal: 3 slides

TOTAL: 16 slides

Specs visuales (aprendizajes-montador-cc.md § 3.9 — v3, feedback Jeremy mayo 2026):
  Slide: 1920×1080 px = 18,288,000 × 10,287,000 EMU
  1px = 9525 EMU
  Fonts: Instrument Serif (headlines, stats, verbatims) + Poppins (cuerpo, atribución, source)
  Fondo: #000000 negro plano (NO masterslide)
  Cards: rgba(0,0,0,0.45) MSO_SHAPE.ROUNDED_RECTANGLE adj=0.05
  Stat number: 180px → 135pt, Instrument Serif italic
  Verbatim: 50px → 37.5pt, Instrument Serif regular, comillas «»
  Headlines: auto-size px por largo de texto, MAYÚSCULAS, kerning 0
  Source: Poppins italic 16px → 12pt, gris #9B9B9B
"""

from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.enum.shapes import MSO_SHAPE
from lxml import etree
import os

# ── Conversión px → EMU ────────────────────────────────────────────────────────
PX = 9525  # 1 px @ 96 dpi = 9525 EMU

def px(n):
    return Emu(int(n * PX))

# ── Dimensiones del slide ──────────────────────────────────────────────────────
SLIDE_W_PX = 1920
SLIDE_H_PX = 1080
SLIDE_W = px(SLIDE_W_PX)
SLIDE_H = px(SLIDE_H_PX)

# ── Colores ────────────────────────────────────────────────────────────────────
BLACK     = RGBColor(0x00, 0x00, 0x00)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
GREY_SEP  = RGBColor(0x2E, 0x2E, 0x2E)
GREY_SOFT = RGBColor(0x9B, 0x9B, 0x9B)

# ── Tipografías ────────────────────────────────────────────────────────────────
FONT_HEADLINE = "Instrument Serif"
FONT_BODY     = "Poppins"

def pt_from_px(px_val):
    return round(px_val * 0.75, 1)

# Fuentes en pt
STAT_NUMBER_PT  = pt_from_px(180)   # 135.0 pt
STAT_DESC_PT    = pt_from_px(22)    # 16.5 pt
VERBATIM_PT     = pt_from_px(50)    # 37.5 pt
ATTRIBUTION_PT  = pt_from_px(22)    # 16.5 pt
SOURCE_PT       = pt_from_px(16)    # 12.0 pt
CV_HEADER_PT    = pt_from_px(16)    # 12.0 pt

# Dimensiones de elementos en px
STAT_BOX_W_1STAT  = 822
STAT_BOX_W_2STATS = 880
STAT_BOX_W_3STATS = 560
STAT_BOX_H        = 238

CV_CARD_W = 1637
CV_CARD_H = 485

STAT_TOP_PX = 500

# ── helpers ────────────────────────────────────────────────────────────────────

def new_prs():
    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H
    return prs


def blank_slide(prs):
    layout = prs.slide_layouts[6]  # Blank
    slide  = prs.slides.add_slide(layout)
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = BLACK
    return slide


def _set_kern(r_elem):
    rpr = r_elem.find(qn('a:rPr'))
    if rpr is not None:
        rpr.set('kern', '0')
        rpr.set('spc', '0')


def add_textbox(slide, left_px, top_px, width_px, height_px,
                text, font_name, font_size_pt,
                bold=False, italic=False, color=WHITE,
                align=PP_ALIGN.LEFT, word_wrap=True):
    txBox = slide.shapes.add_textbox(
        px(left_px), px(top_px), px(width_px), px(height_px)
    )
    tf = txBox.text_frame
    tf.word_wrap = word_wrap
    tf.margin_left   = Emu(0)
    tf.margin_right  = Emu(0)
    tf.margin_top    = Emu(0)
    tf.margin_bottom = Emu(0)
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.name   = font_name
    run.font.size   = Pt(font_size_pt)
    run.font.bold   = bold
    run.font.italic = italic
    run.font.color.rgb = color
    _set_kern(run._r)
    return txBox


def add_rich_textbox(slide, left_px, top_px, width_px, height_px,
                     runs, align=PP_ALIGN.LEFT, word_wrap=True):
    txBox = slide.shapes.add_textbox(
        px(left_px), px(top_px), px(width_px), px(height_px)
    )
    tf = txBox.text_frame
    tf.word_wrap = word_wrap
    tf.margin_left   = Emu(0)
    tf.margin_right  = Emu(0)
    tf.margin_top    = Emu(0)
    tf.margin_bottom = Emu(0)
    p = tf.paragraphs[0]
    p.alignment = align
    for r in runs:
        run = p.add_run()
        run.text = r['text']
        run.font.name   = r.get('font_name', FONT_BODY)
        run.font.size   = Pt(r.get('font_size_pt', STAT_DESC_PT))
        run.font.bold   = r.get('bold', False)
        run.font.italic = r.get('italic', False)
        run.font.color.rgb = r.get('color', WHITE)
        _set_kern(run._r)
    return txBox


def pick_headline_size_px(chars):
    if chars <= 30:
        return 110
    elif chars <= 44:
        return 88
    elif chars <= 65:
        return 64
    elif chars <= 85:
        return 52
    else:
        return 42


def add_headline(slide, text_plain, text_italic=""):
    full_text = text_plain + text_italic
    chars     = len(full_text.strip())
    size_px   = pick_headline_size_px(chars)
    size_pt   = pt_from_px(size_px)

    txBox = slide.shapes.add_textbox(
        px(100), px(100), px(1720), px(300)
    )
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.margin_left   = Emu(0)
    tf.margin_right  = Emu(0)
    tf.margin_top    = Emu(0)
    tf.margin_bottom = Emu(0)

    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER

    if text_plain:
        run = p.add_run()
        run.text = text_plain.upper()
        run.font.name   = FONT_HEADLINE
        run.font.size   = Pt(size_pt)
        run.font.bold   = False
        run.font.italic = False
        run.font.color.rgb = WHITE
        _set_kern(run._r)

    if text_italic:
        run2 = p.add_run()
        run2.text = text_italic.upper()
        run2.font.name   = FONT_HEADLINE
        run2.font.size   = Pt(size_pt)
        run2.font.bold   = False
        run2.font.italic = True
        run2.font.color.rgb = WHITE
        _set_kern(run2._r)

    return txBox


def add_source(slide, source_text):
    add_textbox(
        slide,
        left_px=0, top_px=990,
        width_px=1920, height_px=50,
        text=source_text,
        font_name=FONT_BODY, font_size_pt=SOURCE_PT,
        italic=True, color=GREY_SOFT,
        align=PP_ALIGN.CENTER
    )


def add_vertical_separator(slide, x_px, y_top_px, height_px):
    line = slide.shapes.add_shape(
        1,  # RECTANGLE
        px(x_px - 1), px(y_top_px),
        px(2), px(height_px)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = GREY_SEP
    line.line.fill.background()


def make_card_rgba_45(slide, left_px, top_px, width_px, height_px):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        px(left_px), px(top_px),
        px(width_px), px(height_px)
    )
    shape.adjustments[0] = 0.05
    shape.line.fill.background()
    shape.fill.solid()
    shape.fill.fore_color.rgb = BLACK

    sp_elem = shape._element
    spPr = sp_elem.find(qn('p:spPr'))
    if spPr is not None:
        solidFill = spPr.find(qn('a:solidFill'))
        if solidFill is None:
            solidFill = etree.SubElement(spPr, qn('a:solidFill'))
        for child in list(solidFill):
            solidFill.remove(child)
        srgbClr = etree.SubElement(solidFill, qn('a:srgbClr'))
        srgbClr.set('val', '000000')
        alpha = etree.SubElement(srgbClr, qn('a:alpha'))
        alpha.set('val', '45000')

    return shape


def make_run(text, bold=False, italic=False,
             size_pt=None, color=WHITE, font_name=FONT_BODY):
    return {
        'text': text,
        'font_name': font_name,
        'font_size_pt': size_pt if size_pt is not None else STAT_DESC_PT,
        'bold': bold,
        'italic': italic,
        'color': color
    }


def add_card(slide, quote_text, attribution,
             left_px, top_px, card_w_px, card_h_px,
             verbatim_size_pt=None):
    if verbatim_size_pt is None:
        verbatim_size_pt = VERBATIM_PT

    make_card_rgba_45(slide, left_px, top_px, card_w_px, card_h_px)

    full_quote = f"«{quote_text}»"

    pad_h = 80
    pad_v = 60
    text_w = card_w_px - (pad_h * 2)
    text_h = card_h_px - (pad_v * 2)

    txBox = slide.shapes.add_textbox(
        px(left_px + pad_h), px(top_px + pad_v),
        px(text_w), px(text_h)
    )
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.margin_left   = Emu(0)
    tf.margin_right  = Emu(0)
    tf.margin_top    = Emu(0)
    tf.margin_bottom = Emu(0)

    p1 = tf.paragraphs[0]
    p1.alignment = PP_ALIGN.CENTER
    run_q = p1.add_run()
    run_q.text = full_quote
    run_q.font.name   = FONT_HEADLINE
    run_q.font.size   = Pt(verbatim_size_pt)
    run_q.font.italic = False
    run_q.font.bold   = False
    run_q.font.color.rgb = WHITE
    _set_kern(run_q._r)

    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(10)
    run_a = p2.add_run()
    run_a.text = f"— {attribution}"
    run_a.font.name   = FONT_BODY
    run_a.font.size   = Pt(ATTRIBUTION_PT)
    run_a.font.italic = True
    run_a.font.bold   = False
    run_a.font.color.rgb = WHITE
    _set_kern(run_a._r)

    return txBox


def stat_x_centers(n_stats):
    w = SLIDE_W_PX
    if n_stats == 1:
        return [w // 2]
    elif n_stats == 2:
        return [w // 3, (w * 2) // 3]
    else:
        return [w // 4, w // 2, (w * 3) // 4]


def stat_box_width(n_stats):
    if n_stats == 1:
        return STAT_BOX_W_1STAT
    elif n_stats == 2:
        return STAT_BOX_W_2STATS
    else:
        return STAT_BOX_W_3STATS


def add_stat_block(slide, stat_value, desc_runs, x_center_px, n_stats):
    box_w = stat_box_width(n_stats)
    box_h = STAT_BOX_H

    box_left = x_center_px - (box_w // 2)
    box_top  = STAT_TOP_PX

    num_h = 200
    add_textbox(
        slide,
        left_px=box_left, top_px=box_top,
        width_px=box_w, height_px=num_h,
        text=stat_value,
        font_name=FONT_HEADLINE, font_size_pt=STAT_NUMBER_PT,
        italic=True, color=WHITE,
        align=PP_ALIGN.CENTER
    )

    desc_top = box_top + num_h + 20
    add_rich_textbox(
        slide,
        left_px=box_left, top_px=desc_top,
        width_px=box_w, height_px=180,
        runs=desc_runs,
        align=PP_ALIGN.CENTER
    )


# ── layouts de slides ──────────────────────────────────────────────────────────

def build_hallazgo_slide(prs, headline_plain, headline_italic,
                          stats, source_text):
    slide = blank_slide(prs)
    add_headline(slide, headline_plain, headline_italic)

    n = len(stats)
    xs = stat_x_centers(n)

    sep_top_px    = STAT_TOP_PX - 20
    sep_height_px = STAT_BOX_H + 40

    if n >= 2:
        x_sep1 = (xs[0] + xs[1]) // 2
        add_vertical_separator(slide, x_sep1, sep_top_px, sep_height_px)
    if n == 3:
        x_sep2 = (xs[1] + xs[2]) // 2
        add_vertical_separator(slide, x_sep2, sep_top_px, sep_height_px)

    for i, stat in enumerate(stats):
        add_stat_block(slide, stat['value'], stat['desc_runs'], xs[i], n)

    add_source(slide, source_text)
    return slide


def build_consumer_voice_slide(prs, quote, attribution):
    slide = blank_slide(prs)

    add_textbox(
        slide,
        left_px=0, top_px=80,
        width_px=1920, height_px=50,
        text="CONSUMER VOICE",
        font_name=FONT_BODY, font_size_pt=CV_HEADER_PT,
        color=GREY_SOFT, align=PP_ALIGN.CENTER
    )

    card_left = (SLIDE_W_PX - CV_CARD_W) // 2
    card_top  = 220

    add_card(
        slide,
        quote_text=quote,
        attribution=attribution,
        left_px=card_left, top_px=card_top,
        card_w_px=CV_CARD_W, card_h_px=CV_CARD_H
    )

    return slide


def build_cuali_slide(prs, headline_plain, headline_italic, verbatims, source_text):
    slide = blank_slide(prs)
    add_headline(slide, headline_plain, headline_italic)

    n = len(verbatims)
    card_left = (SLIDE_W_PX - CV_CARD_W) // 2

    if n == 1:
        card_h   = 485
        gap      = 0
        verb_pt  = VERBATIM_PT
        y_start  = 430
    elif n == 2:
        card_h   = 290
        gap      = 30
        verb_pt  = pt_from_px(38)
        y_start  = 380
    else:
        card_h   = 200
        gap      = 25
        verb_pt  = pt_from_px(32)
        y_start  = 360

    for i, v in enumerate(verbatims):
        y_card = y_start + i * (card_h + gap)
        add_card(
            slide,
            quote_text=v['quote'],
            attribution=v['attribution'],
            left_px=card_left, top_px=y_card,
            card_w_px=CV_CARD_W, card_h_px=card_h,
            verbatim_size_pt=verb_pt
        )

    add_source(slide, source_text)
    return slide


# ── Datos del set editorial ────────────────────────────────────────────────────

def build_deck():
    prs = new_prs()

    # ─────────────────────────────────────────────────────────────────────────
    # TENSIÓN 1 — El cuerpo legal y el cuerpo del deseo
    # H01: derechos patrimoniales vs adopción — 3 stats + verbatim → 2 slides
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 01 — H01 Hallazgo cuanti (3 stats)
    # Headline: "El país aprueba la propiedad compartida, rechaza la adopción 2 a 1.
    #            Para las parejas del mismo sexo, lo que el derecho no da, tampoco lo puede quitar nadie."
    # 159 chars → >85 → 42px
    # Stats:
    #   40%  (39.8% → 40%)  muy de acuerdo con propiedad compartida
    #   48%  (47.8% → 48%)  muy de acuerdo con acceso salud familiar
    #   30%  (30.4% → 30%)  muy de acuerdo con préstamo bancario mancomunado
    build_hallazgo_slide(
        prs,
        headline_plain="El país aprueba la propiedad compartida, rechaza la adopción 2 a 1. ",
        headline_italic="Para las parejas del mismo sexo, lo que el derecho no da, tampoco lo puede quitar nadie.",
        stats=[
            {
                'value': '40%',
                'desc_runs': [
                    make_run('está muy de acuerdo con que una pareja del mismo sexo compre '),
                    make_run('propiedad', bold=True),
                    make_run(' juntos — ítem de mayor aprobación de Q55. En el extremo, 61.8% rechaza la adopción legal.')
                ]
            },
            {
                'value': '48%',
                'desc_runs': [
                    make_run('muy de acuerdo con acceso a '),
                    make_run('servicios de salud familiar', bold=True),
                    make_run(' como beneficiarios mutuos, frente a 26.2% en desacuerdo. Salud: más apoyo que lo bancario.')
                ]
            },
            {
                'value': '30%',
                'desc_runs': [
                    make_run('muy de acuerdo con '),
                    make_run('préstamo bancario mancomunado', bold=True),
                    make_run(', pero 37.8% sigue en desacuerdo. El derecho más técnico tampoco alcanza mayoría.')
                ]
            }
        ],
        source_text="Source: Código Casa — Estudio cuantitativo + cualitativo 2025 · Q55 · Base 500."
    )

    # Slide 02 — H01 Consumer Voice
    build_consumer_voice_slide(
        prs,
        quote='Aquí usted no tiene familia, usted vive y convive con un amiguito o una amiguita. Jurídicamente eso no existe. Tú no existes para nada. Tú tienes un problema de violencia de género en personas del mismo sexo que viven juntas, y eso se califica como una riña, no como violencia de género.',
        attribution='Familia Homoparental'
    )

    # ─────────────────────────────────────────────────────────────────────────
    # H02: "Respeto pero no comparto" — 1 stat + verbatim → 2 slides
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 03 — H02 Hallazgo cuanti (1 stat)
    # Headline: 170 chars → >85 → 42px
    # Stat: 60.4% → 60% (entero)
    build_hallazgo_slide(
        prs,
        headline_plain="El límite del respeto dominicano siempre es el mismo: los niños. ",
        headline_italic="Hay quienes son parte de una pareja del mismo sexo y aun así dicen que ese no es un ambiente para un hijo.",
        stats=[
            {
                'value': '60%',
                'desc_runs': [
                    make_run('está en desacuerdo con que una pareja del mismo sexo sea reconocida legalmente como '),
                    make_run('padres o madres', bold=True),
                    make_run(' de un mismo hijo. Ítem Q55 reconocimiento legal parentalidad.')
                ]
            }
        ],
        source_text="Source: Código Casa — Estudio cuantitativo + cualitativo 2025 · Q55, Q56 · Base 500."
    )

    # Slide 04 — H02 Consumer Voice
    build_consumer_voice_slide(
        prs,
        quote='De la dos y de la cuatro, respeto su decisión pero no la comparto. Últimamente se está viviendo en una época moderna en la cual quieren imponer eso... hacerlo como normal, algo que no es normal, porque la palabra de Dios dice que hombre y mujer, no las dos personas del mismo sexo.',
        attribution='Familia Monoparental'
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TENSIÓN 2 — La fe como infraestructura
    # H03: fe como refugio × brecha género/NSE — 3 stats + verbatim → 2 slides
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 05 — H03 Hallazgo cuanti (3 stats)
    # Headline: 152 chars → >85 → 42px
    # Stats:
    #   64%  (64.0% → 64%)  siempre recurre a la fe
    #   71%  (70.8% → 71%)  mujeres vs 53.3% hombres
    #   73%  (72.7% → 73%)  estrato D
    build_hallazgo_slide(
        prs,
        headline_plain="64% recurre siempre a la fe en momentos de dificultad. ",
        headline_italic="Ese 64% no es parejo: es más mujer, más bajo el nivel socioeconómico, más alta la dependencia.",
        stats=[
            {
                'value': '64%',
                'desc_runs': [
                    make_run('marca “Siempre” recurrir a la '),
                    make_run('religión o espiritualidad', bold=True),
                    make_run(' como refugio en momentos de dificultad. Solo 6.6% dice nunca. Q57, Base 500.')
                ]
            },
            {
                'value': '71%',
                'desc_runs': [
                    make_run('de las '),
                    make_run('mujeres', bold=True),
                    make_run(' recurre siempre a la fe, vs 53.3% de los hombres. Brecha de género: 17.5 puntos. Q57 × sexo.')
                ]
            },
            {
                'value': '73%',
                'desc_runs': [
                    make_run('del '),
                    make_run('estrato D', bold=True),
                    make_run(' recurre siempre, vs 52.8% del estrato C+ y 61.5% del estrato C. A menor NSE, mayor dependencia espiritual.')
                ]
            }
        ],
        source_text="Source: Código Casa — Estudio cuantitativo + cualitativo 2025 · Q57, Q57 × D2, Q57 × D6 · Base 500."
    )

    # Slide 06 — H03 Consumer Voice
    build_consumer_voice_slide(
        prs,
        quote='He buscado ayuda profesional para tratar esas cosas... ¿Qué también yo hago? Me refugio mucho en Dios, en la oración. Tener una conexión con Dios para mí es importante, dejarle las cosas a él, que él se encargue, porque hay días que tú dices yo no puedo más y Dios se encarga.',
        attribution='Familia Biparental con Hijos Adultos'
    )

    # ─────────────────────────────────────────────────────────────────────────
    # H04: religiosidad de baja institución — 2 stats + verbatim → 2 slides
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 07 — H04 Hallazgo cuanti (2 stats)
    # Headline: 162 chars → >85 → 42px
    # Stats:
    #   31%  (30.8% → 31%)  creyente ocasional
    #   30%  (30.2% → 30%)  muy practicante y activo  — usamos el dato como es
    #   NOTA: headline ya declara los dos datos; las cajas desglosarán distribución
    #   2 stats → cajas de 880px, posición 1/3 y 2/3
    build_hallazgo_slide(
        prs,
        headline_plain="El dominicano cree, pero no en institución. 30.8% es creyente ocasional, 28.8% espiritual sin práctica regular. ",
        headline_italic="Solo 30.2% se declara muy practicante y activo.",
        stats=[
            {
                'value': '31%',
                'desc_runs': [
                    make_run('es '),
                    make_run('creyente ocasional', bold=True),
                    make_run(', 30.2% muy practicante y activo, 28.8% espiritual sin práctica regular. La relación con la fe se reparte en tercios. Q58, Base 500.')
                ]
            },
            {
                'value': '8%',
                'desc_runs': [
                    make_run('queda fuera de la órbita espiritual: 6.8% sin afiliación ni práctica, 1.2% no creyente. El país mantiene casi por completo algún vínculo con '),
                    make_run('lo espiritual', bold=True),
                    make_run(' — la fractura es de práctica, no de fe.')
                ]
            }
        ],
        source_text="Source: Código Casa — Estudio cuantitativo + cualitativo 2025 · Q58 · Base 500."
    )

    # Slide 08 — H04 Consumer Voice
    build_consumer_voice_slide(
        prs,
        quote='Yo soy básicamente la nota discordante de ese entorno... yo no me rijo por la línea en la que va mi familia, sin embargo yo respeto lo que yo vi, yo entiendo que esa es la manera en la que las familias funcionan.',
        attribution='Familia Mixta'
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TENSIÓN 3 — El país que no mira a todos
    # H05: inclusión discapacidad × NSE y edad — 3 stats, solo-cuanti → 1 slide
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 09 — H05 Hallazgo solo-cuanti (3 stats)
    # Headline: 161 chars → >85 → 42px
    # Stats:
    #   54%  (54.2% → 54%)  muy baja la inclusión de discapacidad en comunidad
    #   62%  (61.8% → 62%)  comunidad no nada preparada para incluir
    #   72%  (71.5% → 72%)  estrato D considera no preparada
    build_hallazgo_slide(
        prs,
        headline_plain="54.2% califica de muy baja la inclusión de discapacidad en su comunidad. ",
        headline_italic="En el estrato D, el 71.5% dice que la comunidad no está nada preparada para incluirla.",
        stats=[
            {
                'value': '54%',
                'desc_runs': [
                    make_run('califica de '),
                    make_run('muy baja', bold=True),
                    make_run(' la inclusión de personas con discapacidad en su comunidad; solo 19.0% la califica de muy alta. Q61, Base 500.')
                ]
            },
            {
                'value': '62%',
                'desc_runs': [
                    make_run('cree que su comunidad no está '),
                    make_run('nada preparada', bold=True),
                    make_run(' para incluir personas neurodivergentes o con discapacidad; solo 12.0% la ve muy preparada. Q63, Base 500.')
                ]
            },
            {
                'value': '72%',
                'desc_runs': [
                    make_run('del '),
                    make_run('estrato D', bold=True),
                    make_run(' considera la comunidad no preparada, vs 70.6% de los mayores de 55. La exclusión percibida crece con la vulnerabilidad.')
                ]
            }
        ],
        source_text="Source: Código Casa — Estudio cuantitativo 2025 · Q61, Q63, Q63 × D6, Q63 × D5 · Base 500."
    )

    # ─────────────────────────────────────────────────────────────────────────
    # H06: polarización espejo orientación sexual × género — 2 stats + verbatim → 2 slides
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 10 — H06 Hallazgo cuanti (2 stats)
    # Headline: 162 chars → >85 → 42px
    # Stats:
    #   37%  (36.8% → 37%)  muy cómodo, 35% (34.8% → 35%) nada cómodo
    #   40%  (40.3% → 40%)  mujeres muy cómodas, 40% (39.5% → 40%) hombres nada cómodos
    build_hallazgo_slide(
        prs,
        headline_plain="Hablar de orientación sexual en familia parte al país en dos. El hombre se inclina al silencio; ",
        headline_italic="la mujer, a la conversación — por casi 20 puntos de diferencia.",
        stats=[
            {
                'value': '37%',
                'desc_runs': [
                    make_run('se siente '),
                    make_run('muy cómodo', bold=True),
                    make_run(' hablando de orientación sexual o identidad de género en familia, y 34.8% nada cómodo. La distribución nacional es casi espejo. Q64, Base 500.')
                ]
            },
            {
                'value': '40%',
                'desc_runs': [
                    make_run('de las '),
                    make_run('mujeres', bold=True),
                    make_run(' tiene "muy cómoda" como respuesta top; 39.5% de los hombres tiene "nada cómodo" como respuesta top. El género invierte el polo dominante.')
                ]
            }
        ],
        source_text="Source: Código Casa — Estudio cuantitativo + cualitativo 2025 · Q64, Q64 × D2 · Base 500."
    )

    # Slide 11 — H06 Consumer Voice
    build_consumer_voice_slide(
        prs,
        quote='Si tú vives con una pareja gay, depende de la educación que tú le des. Viene de la educación... porque si tú te reprimes a no, no, yo no voy a poder porque yo soy lo que soy, es gay, entonces el muchacho después lo que me va a reclamar por eso.',
        attribution='Familia Homoparental'
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TENSIÓN 4 — La violencia que no tiene nombre
    # H07: violencia económica vs física — 2 stats, solo-cuanti → 1 slide
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 12 — H07 Hallazgo solo-cuanti (2 stats)
    # Headline: 181 chars → >85 → 42px
    # Stats:
    #   20%  (20.2% → 20%)  violencia económica
    #   17%  (17.4% → 17%)  violencia emocional/psicológica
    #   NOTE: headline declara el triple, las cajas desglosan el ranking
    build_hallazgo_slide(
        prs,
        headline_plain="La violencia que más pesa en el hogar dominicano no es la de los golpes: 20.2% reporta violencia económica, casi triplicando a la física. ",
        headline_italic="El control del dinero es el primer arma.",
        stats=[
            {
                'value': '20%',
                'desc_runs': [
                    make_run('señala la '),
                    make_run('violencia económica', bold=True),
                    make_run(' —restricción del acceso al dinero, control financiero— como el tipo de violencia experimentada con mayor frecuencia en los últimos 3 años. La física: 7.6%.')
                ]
            },
            {
                'value': '17%',
                'desc_runs': [
                    make_run('reporta '),
                    make_run('violencia emocional o psicológica', bold=True),
                    make_run('. Sumadas, la económica y la emocional (37.6%) más que cuadruplican a la física (7.6%). Q67, Base 500.')
                ]
            }
        ],
        source_text="Source: Código Casa — Estudio cuantitativo 2025 · Q67 · Base 500."
    )

    # ─────────────────────────────────────────────────────────────────────────
    # H08: transmisión intergeneracional del golpe — solo-cuali 1 verbatim → 1 slide
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 13 — H08 Card cualitativa (1 verbatim)
    # Headline: 158 chars → >85 → 42px
    build_cuali_slide(
        prs,
        headline_plain="Hay hogares donde el golpe se aprende como respuesta al amor. ",
        headline_italic="La madre lo sabe: si su hija ve que el esposo la golpea, la hija entiende que así se quiere.",
        verbatims=[
            {
                'quote': 'Si por ejemplo yo, si mi esposo me golpea, o sea aunque yo le diga a mi hija, mira tú no puedes dejar que nadie te golpea, ella entiende que si él, que es mi esposo, me quiere y me golpea, es una respuesta al amor. Entonces, es como que eso es parte de la educación.',
                'attribution': 'Familia Extendida'
            }
        ],
        source_text="Source: Código Casa — Estudio cualitativo 2025 · Q67 · Base cualitativa: 11 grupos de enfoque."
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TENSIÓN 5 — La equidad pendiente
    # H09: padres presentes — 2 stats, solo-cuanti → 1 slide
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 14 — H09 Hallazgo solo-cuanti (2 stats)
    # Headline: 160 chars → >85 → 42px
    # Stats:
    #   63%  (62.6% → 63%)  padres más presentes
    #   13%  (12.8% → 13%)  flexibilidad laboral
    build_hallazgo_slide(
        prs,
        headline_plain="62.6% pide una sola cosa para la equidad familiar: que los padres estén más presentes. ",
        headline_italic="Las reformas laborales y la paridad salarial no aparecen en el radar.",
        stats=[
            {
                'value': '63%',
                'desc_runs': [
                    make_run('considera que el cambio social más urgente para la equidad familiar es que los '),
                    make_run('padres estén más presentes', bold=True),
                    make_run(' en la crianza y las tareas del hogar. TOP-1 con margen amplio. Q66, Base 500.')
                ]
            },
            {
                'value': '13%',
                'desc_runs': [
                    make_run('elige '),
                    make_run('flexibilidad laboral para ambos padres', bold=True),
                    make_run(' y apenas 2.8% que la maternidad no implique retroceso profesional. Lo estructural queda cinco veces por debajo de lo presencial.')
                ]
            }
        ],
        source_text="Source: Código Casa — Estudio cuantitativo 2025 · Q66 · Base 500."
    )

    # ─────────────────────────────────────────────────────────────────────────
    # H10: vejez digna como cheque — 2 stats, solo-cuanti → 1 slide
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 15 — H10 Hallazgo solo-cuanti (2 stats)
    # Headline: 152 chars → >85 → 42px
    # Stats:
    #   74%  (73.8% → 74%)  pensiones
    #   32%  (32.2% → 32%)  prevención abandono/soledad
    build_hallazgo_slide(
        prs,
        headline_plain="73.8% pide pensiones para que los mayores vivan con dignidad. ",
        headline_italic="El respeto, la compañía y el cuidado emocional llegan después. Lo primero es el cheque.",
        stats=[
            {
                'value': '74%',
                'desc_runs': [
                    make_run('cree que lo que más falta para la dignidad de la tercera edad son '),
                    make_run('pensiones o apoyos económicos suficientes', bold=True),
                    make_run('. Le sigue acceso a salud con 53.4%. TOP-1 absoluto. Q69, Base 500.')
                ]
            },
            {
                'value': '32%',
                'desc_runs': [
                    make_run('elige prevención del '),
                    make_run('abandono, la soledad y el maltrato', bold=True),
                    make_run(' (quinto lugar con 32.2%) y sólo 32.4% el respeto y reconocimiento familiar. Lo emocional pesa la mitad que lo económico.')
                ]
            }
        ],
        source_text="Source: Código Casa — Estudio cuantitativo 2025 · Q69 · Base 500."
    )

    # ─────────────────────────────────────────────────────────────────────────
    # H11: discriminación — 2 stats, solo-cuanti → 1 slide
    # ─────────────────────────────────────────────────────────────────────────

    # Slide 16 — H11 Hallazgo solo-cuanti (2 stats)
    # Headline: 145 chars → >85 → 42px
    # Stats:
    #   91%  (91.2% → 91%)  no fue discriminado
    #   2.8% mantiene decimal (1 dígito antes del punto) / 1.8% también
    build_hallazgo_slide(
        prs,
        headline_plain="91.2% dice no haber sido discriminado en 3 años. ",
        headline_italic="Lo poco que sí se reporta tiene cara: color de piel y cabello concentran casi todos los casos.",
        stats=[
            {
                'value': '91%',
                'desc_runs': [
                    make_run('declara no haber sido víctima de '),
                    make_run('discriminación', bold=True),
                    make_run(' en los últimos 3 años por raza, color de piel, etnia, nacionalidad, orientación sexual o religión. Q60, Base 500.')
                ]
            },
            {
                'value': '2.8%',
                'desc_runs': [
                    make_run('reporta discriminación por '),
                    make_run('color de piel', bold=True),
                    make_run(' (n=14) y 1.8% por cabello (n=9). El cuerpo racializado concentra lo poco que se declara. Cifras sobre n=500 total.')
                ]
            }
        ],
        source_text="Source: Código Casa — Estudio cuantitativo 2025 · Q60 · Base 500."
    )

    # ── Guardar ────────────────────────────────────────────────────────────────
    output_path = "/home/user/c-digocasa-cerebro/Agentes Hallazgos/sistema-de-creencias-deck-flat.pptx"
    prs.save(output_path)
    print(f"GUARDADO: {output_path}")
    print(f"Total slides: {len(prs.slides)}")

    # Verificación de specs
    print("\n── Verificación specs ──────────────────────────────────────────────────")
    print(f"Slide size: {prs.slide_width} × {prs.slide_height} EMU")
    print(f"  = {prs.slide_width / PX:.0f}px × {prs.slide_height / PX:.0f}px")
    expected_w = 1920 * PX
    expected_h = 1080 * PX
    ok = prs.slide_width == Emu(expected_w) and prs.slide_height == Emu(expected_h)
    print(f"  Slide size OK: {ok}")
    print(f"Stat number size: {STAT_NUMBER_PT}pt ({STAT_NUMBER_PT/0.75:.0f}px)")
    print(f"Stat desc size:   {STAT_DESC_PT}pt ({STAT_DESC_PT/0.75:.0f}px)")
    print(f"Verbatim size:    {VERBATIM_PT}pt ({VERBATIM_PT/0.75:.0f}px)")
    print(f"Attribution size: {ATTRIBUTION_PT}pt ({ATTRIBUTION_PT/0.75:.0f}px)")
    print(f"Source size:      {SOURCE_PT}pt ({SOURCE_PT/0.75:.0f}px)")
    print("Cards: rgba(0,0,0,0.45) via MSO_SHAPE.ROUNDED_RECTANGLE + XML alpha=45000")
    print("Headlines >85 chars → 42px (31.5pt)")
    print("Comillas españolas «...» en todos los verbatims")
    print("Kerning 0 en todo el deck")
    print("NO masterslide — fondo negro plano")

    return output_path


if __name__ == "__main__":
    build_deck()
