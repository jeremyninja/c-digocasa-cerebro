# Aprendizajes del Montador de Trends CC

Lecciones acumuladas con Jeremy mientras se montan los Trend Forecasts
de Código Casa. Si una regla aparece aquí, es porque ya se corrigió al
menos una vez. **Si entra en conflicto con `.claude/agents/montador-trends-cc.md`,
estos aprendizajes ganan.**

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

**Fecha del aprendizaje:** 2026-05-29.

**Regla dura:**
- Cada trigger en col-center es un bloque vertical con dos elementos:
  1. **Cifra arriba** (Instrument Serif 64–72pt o keyword italic 32–40pt).
  2. **Caja descriptiva abajo** (W170pt × H35pt, Poppins 10pt blanco).
- **NUNCA side-by-side.** Stack vertical siempre.
- Debajo de la caja descriptiva va la fuente inline (Poppins 7pt #666).

---

## 3. FOTOS DE SEÑALES — 95×140pt (NO 110×162, NO 149×220)

**Fecha del aprendizaje:** 2026-05-29 (segunda corrección — el primer fix
a 110×162pt todavía chocaba con los otros elementos).

**Regla dura:**
- Cada foto de señal en col-right va **95×140pt EXACTO**.
- Ratio portrait preservado (95/140 = 0.679).
- 3 fotos × 140pt + 2 gaps × 24pt = 468pt total. Cabe holgado en los
  ~480pt útiles del slide.
- Badge "Click me" rojo `#FF2D2D` en esquina sup-der + hyperlink al URL
  + caja caption 170×35pt al lado.

**Por qué se redujo otra vez:**
A 110×162pt todavía dejaba poco aire entre filas y el caption se montaba
con el siguiente bloque.

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

## 6. RESPIRACIÓN — PADDING MÍNIMO ENTRE BLOQUES

**Fecha del aprendizaje:** 2026-05-29 ("los cuadros de texto se están
chocando uno con otro").

**Regla dura — gaps mínimos:**
- Entre tab MACRO y labels de columna: **18pt**
- Entre labels de columna y primer bloque de contenido: **16pt**
- Entre headline y label EL FENÓMENO: **24pt**
- Entre label y body fenómeno: **6pt**
- Entre body fenómeno y label HASHTAGS: **24pt**
- Entre label y hashtags: **6pt**
- Entre triggers verticales (col-center): **24pt**
- Entre cifra y caja descriptiva dentro del trigger: **10pt**
- Entre caja descriptiva y fuente inline: **6pt**
- Entre fotos verticales (col-right): **24pt**
- Entre foto y caja caption: **8pt** (caption al lado, no abajo)
- Entre caja caption y fuente inline: **6pt**

**Nada debe pegarse a otra cosa. Si un elemento no respeta el padding,
el montador rebobina y recalcula la altura del slide.**

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

Cada vez que el montador corra de aquí en adelante debe **leer este
archivo antes de generar el script** y aplicar las 7 reglas duras sin
excepción.
