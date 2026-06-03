# Aprendizajes del Montador de Trends CC

Lecciones acumuladas con Jeremy mientras se montan los Trend Forecasts
de Código Casa. Si una regla aparece aquí, es porque ya se corrigió al
menos una vez. **Si entra en conflicto con `.claude/agents/montador-trends-cc.md`,
estos aprendizajes ganan.**

---

## 0. EL MOTOR CENTRAL ES LA ÚNICA FUENTE DE LAYOUT (el "CSS")

**Fecha del aprendizaje:** 2026-05-29 ("¿cómo hago que todos los slides
queden así? no puedo cambiar slide por slide").

**Regla dura — arquitectura:**
- TODO el layout (constantes, posiciones, tamaños, gaps, fuentes, colores)
  y TODAS las funciones de render viven en **`Team Trends CC/trends_deck_engine.py`**.
- Cada capítulo `build_trends_{capitulo}.py` es **SOLO DATOS**: los 3 dividers
  + los 15 micros + la ruta de screenshots + 1 llamada a `build_deck(...)`.
- **NUNCA copies layout dentro de un build_trends_{capitulo}.py.** Si lo haces,
  rompes la regla: el día que Jeremy pida un cambio, habría que tocar 5+ archivos.
- Cambiar una constante en el motor re-renderiza TODOS los decks idénticos.
- El montador, cuando arme un capítulo nuevo, genera el archivo de datos e
  **importa el motor** — no reescribe el layout.

**API del motor:**
```python
from trends_deck_engine import build_deck
build_deck(DIVIDERS, MICROS, SCREENSHOTS_DIR, OUTPUT_PATH)
```
`build_deck` corre el validador de overflow (regla #8) automáticamente antes
de guardar. Si algo desborda, falla la build — no entrega deck roto.

---

## 1. HEADLINE DEL TREND — 20pt FIJO

**Fecha del aprendizaje:** 2026-05-29 (corrección de Jeremy "no sé cuántas
veces te tengo que decir").

**Regla dura:**
- Headline del trend (nombre del trend en col-left) va **20pt FIJO**.
- Fuente: Instrument Serif Regular UPPERCASE, tracking 0, line-height 1.1.
- **NO 42pt. NO 50pt. NO auto-fit. NO escalado por longitud del headline.**
- Si el headline no entra en la caja, el problema lo resuelve el editor
  recortando el copy — NO el montador subiendo el tamaño.

**Por qué pasaba el bug:**
La versión vieja del DS decía "Instrument Serif 42–50pt auto-fit". Esa
lógica "otherwise" se eliminó por completo. **Cero excepciones.**

---

## 2. TRIGGERS — CIFRA ARRIBA, TEXTO ABAJO (stack vertical)

**Fecha del aprendizaje:** 2026-05-29 (refinada).

**Regla dura:**
- Cada trigger en col-center es un bloque vertical con tres elementos:
  1. **Cifra arriba**: Instrument Serif **56pt** (no 72pt — demasiado
     dominante), caja height 56pt, **width 170pt** (igual a la caja
     desc, NO el ancho completo de la columna).
  2. **Caja descriptiva abajo**: W170pt × H35pt, Poppins 10pt blanco.
  3. **Fuente inline**: Poppins 7pt #666.
- Gaps: cifra → caja desc = **18pt** (NO 10pt — quedaba apelmazado).
  Caja desc → fuente = 6pt. Entre triggers = **28pt** (NO 24pt).
- **NUNCA side-by-side.** Stack vertical siempre.

**Por qué se ajustó:**
Stat 72pt + caja desc 10pt abajo se veía apelmazado. Reducir cifra a
56pt + abrir gap a 18pt da respiración real.

**Cálculo de altura:** trigger block = 56 + 18 + 35 + 6 + 12 = **127pt**.
3 × 127 + 2 × 28 = 437pt → arrancando en y=84 termina y=521 ✓ (19pt margin).

---

## 3. FOTOS DE SEÑALES — 88×130pt (NO 95×140, NO 110×162, NO 149×220)

**Fecha del aprendizaje:** 2026-05-29 (TERCERA corrección — el fix a
95×140pt todavía desbordaba el slide).

**Regla dura:**
- Cada foto de señal en col-right va **88×130pt EXACTO**.
- Ratio portrait preservado (88/130 ≈ 0.677).
- Layout: top de col-right content = y=84 (LABELS_TO_CONTENT = 10pt).
- 3 fotos × 130pt + 2 gaps × 24pt = 438pt → ends y=522 ✓ (18pt margin
  hasta el bottom del slide y=540).
- Badge "Click me" rojo `#FF2D2D` en esquina sup-der + hyperlink + caja
  caption 170×35pt al lado.

**Por qué se redujo otra vez:**
A 95×140pt con gap 24pt, 3 fotos arrancando en y=90 terminaban en y=558
→ **clipping de 18pt** del bottom del slide. Foto 3 quedaba cortada.

---

## 4. 3 NEEDS — ELIMINADAS DEL SLIDE

**Fecha del aprendizaje:** 2026-05-29.

**Regla dura:**
- **El slide de micro NO lleva las 3 needs.**
- Las needs del canon viven solo en el `.md` editorial como referencia
  interna; el deck no las muestra.
- Esto libera ~80pt verticales en col-left y permite respirar al resto.

**Implicancia para el editor cultural:**
El editor sigue redactando las 3 needs por micro en el `.md` editado
(las usa para anclar el ángulo emocional), pero el montador las **omite
del slide**.

---

## 5. HASHTAGS — 16pt (NO 23pt)

**Fecha del aprendizaje:** 2026-05-29.

**Regla dura:**
- Hashtags en col-left van **Instrument Serif Regular 16pt** (no 23pt).
- Tracking 0, color blanco, line-spacing 1.0.
- Más chicos para no competir con el headline 20pt ni con el body 10pt.

---

## 6. RESPIRACIÓN — PADDING MÍNIMO ENTRE BLOQUES (refinado)

**Fecha del aprendizaje:** 2026-05-29 (refinada tras inspección de
coordenadas reales — los cuadros se seguían chocando).

**Regla dura — gaps mínimos exactos:**
- Entre tab MACRO y labels de columna: **18pt**
- Entre labels de columna y línea horizontal: **6pt**
- Entre línea horizontal y primer bloque de contenido (`LABELS_TO_CONTENT`): **10pt** (NO 16pt — recortado para dar espacio al col-right)
- Entre headline y label EL FENÓMENO: **24pt**
- Entre label y body fenómeno: **6pt**
- Entre body fenómeno y label HASHTAGS: **24pt**
- Entre label y hashtags: **6pt**
- Entre triggers verticales (col-center): **28pt** (NO 24pt)
- Entre cifra y caja descriptiva dentro del trigger: **18pt** (NO 10pt)
- Entre caja descriptiva y fuente inline: **6pt**
- Entre fotos verticales (col-right): **24pt**
- Entre foto y caja caption: **8pt** (caption al lado, no abajo)
- Entre caja caption y fuente inline: **6pt**

**Nada debe pegarse a otra cosa.**

---

## 7. SCREENSHOTS FALTANTES — EL SCRAPPER RELLENA, NO HAY PLACEHOLDER MANUAL

**Fecha del aprendizaje:** 2026-05-29 ("necesito que tú hagas el esfuerzo
de hacer los screenshots, yo no puedo").

**Regla dura:**
- **El slide NUNCA lleva un placeholder "CAPTURA MANUAL — JEREMY"** ni
  similar. Si una señal no tiene PNG, el montador **detiene la build** y
  devuelve al scrapper.
- El scrapper debe encontrar **algún** visual relacionado usando estos
  fallbacks en orden:
  1. og:image del artículo principal de esa señal
  2. Hero image de la marca/plataforma mencionada (sitio oficial)
  3. Thumbnail de otro TikTok del mismo hashtag/tema
  4. Imagen de Wikipedia / Wikimedia Commons del concepto
  5. Captura headless de una página de Google Images filtrada por el
     concepto (último recurso, recortada a 596×880)
- **El placeholder LOGIN-REQUIRED queda DEPRECADO.** Si el scrapper
  agotó los 5 fallbacks sin encontrar nada, ese micro vuelve al editor
  para reescribir la prueba con otra señal cazable.

**Esto significa:**
El montador puede asumir que recibe **un PNG por cada slot de señal**.
Si no llega un PNG, el flow está incompleto — no es problema del montador.

---

## 8. VALIDADOR DE OVERFLOW — OBLIGATORIO ANTES DE DECLARAR ÉXITO

**Fecha del aprendizaje:** 2026-05-29 ("se están chocando los textos
DIOS MIO" — el montador reportó "todo OK" cuando había clipping real).

**Regla dura:**
Al final del script `build_trends_{capitulo}.py`, ANTES de declarar
el deck terminado, el montador corre este check:

```python
from pptx.util import Emu

SLIDE_W_PT = 960
SLIDE_H_PT = 540
SAFE_MARGIN_PT = 4   # tolerancia mínima

def audit_slide(slide, slide_idx):
    issues = []
    for sh in slide.shapes:
        if sh.left is None or sh.top is None:
            continue
        x = Emu(sh.left).pt
        y = Emu(sh.top).pt
        w = Emu(sh.width).pt if sh.width else 0
        h = Emu(sh.height).pt if sh.height else 0
        # overflow bottom
        if y + h > SLIDE_H_PT + SAFE_MARGIN_PT:
            issues.append(f"  OVERFLOW BOTTOM slide {slide_idx}: "
                          f"shape at y={y:.1f} h={h:.1f} → "
                          f"bottom={y+h:.1f} > {SLIDE_H_PT}")
        # overflow right
        if x + w > SLIDE_W_PT + SAFE_MARGIN_PT:
            issues.append(f"  OVERFLOW RIGHT slide {slide_idx}: "
                          f"shape at x={x:.1f} w={w:.1f} → "
                          f"right={x+w:.1f} > {SLIDE_W_PT}")
    return issues

all_issues = []
for i, sl in enumerate(prs.slides):
    all_issues += audit_slide(sl, i + 1)

if all_issues:
    print("FAIL — overflow detectado:")
    for it in all_issues:
        print(it)
    raise SystemExit("BUILD FALLIDO. Ajusta dims antes de entregar.")
else:
    print(f"OK — {len(prs.slides)} slides sin overflow.")
```

**El montador no entrega el deck hasta que el auditor diga OK.** Si
falla, ajusta dimensiones y reintenta — NO entrega un deck con clipping.

---

## 9. COL-LEFT CON FLOW DINÁMICO — el headline no se desborda sobre EL FENÓMENO

**Fecha del aprendizaje:** 2026-05-29 ("todo se está chocando" — el headline
de 20pt ocupaba 5-6 líneas pero su caja medía 48pt fija; el texto se
desbordaba HACIA ABAJO sobre EL FENÓMENO y el body).

**El bug oculto:** el validador de overflow medía COORDENADAS DE CAJA. La caja
del headline (48pt) no solapaba la de EL FENÓMENO. Pero el TEXTO renderizado
(110pt en 5 líneas) sí se salía de su caja y se montaba sobre lo de abajo.
Box-coords decían OK; el render decía choque.

**Regla dura:**
- Col-left FLUYE: cada bloque (headline → EL FENÓMENO → body → HASHTAGS label →
  hashtags) se posiciona debajo del anterior según su altura REAL estimada
  (`est_text_height`), no en una `y` fija.
- La caja del headline se dimensiona a las líneas que ocupa (estimación
  conservadora con `CW_SERIF_UPPER=0.62`). EL FENÓMENO siempre cae debajo.
- El validador ahora también detecta **solapamiento vertical en col-left**
  (no solo overflow de slide): si `bottom` de un bloque > `top` del siguiente,
  falla la build. El chequeo excluye la fila de tabs/labels (y < CONTENT_Y).

**Por qué importa:** medir solo cajas no basta. Hay que estimar el texto
renderizado y dejar que la columna fluya. Headlines largos (hasta ~6 líneas
a 20pt) ahora caben sin tocar nada.

---

## 10. TAB [MACRO N][NOMBRE] VA ARRIBA DEL HEADLINE (dentro del flow de col-left)

**Fecha del aprendizaje:** 2026-05-29 ("baja el macrotrend y tipo de trend,
mueve toda la caja y ponla arriba del headline").

**Regla dura:**
- La tab [MACRO N][NOMBRE MACRO] ya NO vive en la cabecera del slide (y=10).
  Ahora es el PRIMER elemento del flow de col-left, justo ARRIBA del headline.
- Orden col-left: DEFINICIÓN (label de columna) + línea → tab [MACRO N][NOMBRE]
  → headline → EL FENÓMENO → body → HASHTAGS → hashtags.
- Gap tab → headline: `GAP_TAB_TO_HL = 10pt`.
- La función es `_draw_tab(slide, y, macro_n, macro_name)` llamada dentro de
  `add_col_left`; `add_micro` ya NO llama un `add_tabs` separado.

**Ajuste de gaps que vino con esto:** bajar la tab empuja col-left ~32pt. Para
que los slides de headline largo (ej. Tecnología 3.2, ~10 líneas estimadas) no
desborden, se apretaron gaps: GAP_HL_TO_LABEL 20→14, GAP_BODY_TO_HASH 18→14.

**El validador ahora usa solape 2D (x Y y):** dos cajas lado a lado (las dos
mitades de la tab) NO cuentan como choque; solo si se solapan en ambos ejes.

---

## 11. CIFRAS 40pt + CAJA DE DESCRIPCIÓN DINÁMICA (fuente no choca)

**Fecha del aprendizaje:** 2026-05-29 ("cifras a 40pt; la caja de fuente de la
cifra ponla más abajo de la caja de explicación, que chocan").

**Regla dura:**
- Cifra del trigger: **40pt** Instrument Serif (NO 56, NO 72). `STAT_PT=40, STAT_H=46`.
- La caja de descripción se dimensiona al texto real (`est_text_height`), igual
  que el headline. La fuente cae SIEMPRE debajo del texto de la descripción,
  no de una caja fija de 35pt que el texto desbordaba.
- `STAT_TO_DESC_GAP=12`, `DESC_TO_SRC_GAP=12` (subió de 6), `TRIGGER_GAP=22`.
- El validador ahora cubre col-left **y col-center** (solape 2D x+y).

**Por qué chocaba:** la caja desc era fija (35pt) pero las descripciones de 3-4
líneas a 10pt medían ~50pt → el texto se salía y la fuente se le montaba encima.
Mismo patrón que el headline: medir el texto, no la caja.

---

## Cómo aplica el montador estos aprendizajes en el script

```python
# 1. HEADLINE — siempre 20pt
headline_tf.paragraphs[0].font.size = Pt(20)
headline_tf.paragraphs[0].font.name = "Instrument Serif"
headline_tf.word_wrap = True

# 2. TRIGGERS — stack vertical (cifra arriba, caja abajo)
TRIGGER_GAP = Pt(24)
STAT_TO_DESC_GAP = Pt(10)
DESC_TO_SOURCE_GAP = Pt(6)
for i, trigger in enumerate(triggers):
    y_base = TRIGGERS_TOP + i * (TRIGGER_BLOCK_HEIGHT + TRIGGER_GAP)
    add_stat(y=y_base, size=Pt(72))                       # ARRIBA
    add_desc_box(y=y_base + STAT_H + STAT_TO_DESC_GAP,
                 w=Pt(170), h=Pt(35), font="Poppins",
                 size=Pt(10))                              # ABAJO
    add_source(y=...)

# 3. FOTOS SEÑALES — 95×140pt con gap 24pt
PHOTO_W, PHOTO_H, PHOTO_GAP = Pt(95), Pt(140), Pt(24)

# 4. NO needs (eliminado)
# add_needs(...)  # ❌ NO

# 5. Hashtags 16pt
hashtags_tf.paragraphs[0].font.size = Pt(16)
hashtags_tf.paragraphs[0].font.name = "Instrument Serif"

# 6. Padding — usa constantes globales arriba del script
COL_GAP_HEADLINE_TO_PHENOMENON = Pt(24)
COL_GAP_PHENOMENON_TO_HASHTAGS = Pt(24)
TAB_TO_LABELS = Pt(18)
LABELS_TO_CONTENT = Pt(16)

# 7. Si falta un PNG, raise — NO placeholder manual
for signal in signals:
    if not Path(signal["png"]).exists():
        raise FileNotFoundError(
            f"Falta {signal['png']}. Devolver al scrapper, "
            f"NO usar placeholder CAPTURA MANUAL."
        )
```

---

## Histórico de corridas y qué falló

| Fecha | Capítulo | Bug detectado por Jeremy |
|-------|----------|--------------------------|
| 2026-05-29 v1 | Alimentación | Headline 42–50pt; triggers side-by-side; fotos 149×220pt desbordan → fix #1, #2, #3 |
| 2026-05-29 v2 | Alimentación | Bloques de texto chocados; hashtags muy grandes (23pt); 3 needs ocupan espacio innecesario; placeholder "CAPTURA MANUAL" no es aceptable → fix #4, #5, #6, #7 |
| 2026-05-29 v3 | Alimentación | Foto 3 desborda slide por 18pt (95×140 no fit); stat 72pt + caja desc 10pt abajo apelmaza; stat box 294pt vs caja desc 170pt rompe alineación; montador reportó "OK" con clipping real → fix #3 a 88×130, fix #2 cifra 56pt + gap 18pt + width 170pt match, fix #8 validador overflow obligatorio |

Cada vez que el montador corra de aquí en adelante debe **leer este
archivo antes de generar el script** y aplicar las 7 reglas duras sin
excepción.
