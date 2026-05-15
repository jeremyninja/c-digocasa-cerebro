# Aprendizajes operativos — Montador de Deck Código Casa MED

**Fuente:** `Documents/Cerebro/Código Casa/Conocimiento - Sets de datos/` (knowledge pack canónico, 7 archivos + scripts + deck de referencia + .txt de referencia).

**Para qué sirve:** el agente `montador-deck-cc` lee este archivo al arrancar para (a) localizar el knowledge pack en su ruta real, (b) tener una destilación operativa de las reglas absolutamente no negociables, y (c) saber a cuál archivo del pack ir para cada decisión específica.

**Cómo se usa:** este `.md` es el **índice + manifest de no-negociables**. No reemplaza al knowledge pack. Cuando hay conflicto, el knowledge pack manda. Cuando hay duda visual o de proceso, este archivo te dice a qué archivo del pack ir.

---

## 1. Ruta del knowledge pack

**Path real (úsala literal):**
`/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Conocimiento - Sets de datos/`

Contenido:

| Archivo | Cuándo lo lees |
|---|---|
| `README.md` | Primero. Marco general del pack. |
| `01_ESTRUCTURA_DEL_DECK.md` | Cuando necesitas saber qué tipo de slide es cuál y qué contiene cada uno |
| `02_DATA_SCHEMA.md` | Cuando necesitas mapear data del `.txt` MED al slide específico |
| `03_WORKFLOW_OPERATIVO.md` | Cuando vas a empezar el deck, para seguir las 7 fases en orden |
| `04_DECISIONES_DE_DISENO.md` | Cuando hay duda visual: tipografía, tamaños, paleta, kerning, sources |
| `05_EJEMPLO_TRABAJADO_T6.md` | Cuando necesitas un ejemplo end-to-end de cómo se llenó una tensión |
| `06_ERRORES_COMUNES.md` | Antes de QA, para no repetir lo que ya se aprendió |
| `txt_referencia_finanzas.txt` | Como ejemplo del formato del `.txt` MED de input |
| `deck_referencia_T6-10.pptx` | Como referencia visual final del look-and-feel |
| `scripts/` | Scripts python (apply_design_fixes.py, fix_hallazgo_text.py, build_cruce_slides.py) |

**Si la ruta no existe en sesión, detente y reporta antes de montar.** El knowledge pack es la fuente de verdad operativa; sin él, los slides salen distintos cada vez.

---

## 2. Lo más importante en una sola frase

> **El `.txt` es la fuente de verdad. Si algo no está en el `.txt`, no debe estar en el deck. Si algo está en el `.txt` y no está en el deck, es un dato faltante que hay que montar.**

Esto manda sobre cualquier ajuste editorial visual.

---

## 3. Las no-negociables del montador

Reglas que un agente apurado se salta. No se saltan:

### 3.1. Estructura de slides

**Formato MED canónico (5 tensiones × 8 slides = 40 slides):**
- Numeración: T1 = 1–8, T2 = 9–16, T3 = 17–24, T4 = 25–32, T5 = 33–40.
- Tipos por tensión: Intro → Hallazgo → Consumer Voice → Cruce de Data → Conversación Digital → Mapeo de Oportunidades → Kit de Respuesta de Marca → Caso Referencia.

**Formato flat / prueba de humo (1 hallazgo = 1 o 2 slides MÁXIMO):**

Esta es la regla corregida tras feedback de Jeremy en mayo 2026 (segunda iteración). **Reemplaza cualquier versión anterior del formato flat.**

Por hallazgo del set editorial:

| Tipo de hallazgo | Slides que produce |
|---|---|
| Hallazgo cuanti SIN verbatims (solo-cuanti) | **1 slide:** Hallazgo cuanti (headline + 1-3 stats). |
| Hallazgo cuanti + 1 verbatim | **2 slides:** Slide A Hallazgo cuanti + Slide B Consumer Voice (1 verbatim SUELTO sobre fondo negro, sin card, con header "CONSUMER VOICE" arriba). |
| Hallazgo solo cualitativo (sin cifra publicable, 1-3 verbatims) | **1 slide:** Card cualitativa (headline + 1-3 verbatims en cards estilo gris carbón dentro del mismo slide). |
| Hallazgo cuanti + cuali integrado | **1 slide:** stat grande + 1-2 cards de verbatim en el mismo slide (caso especial, solo si el editor lo entregó así). |

**Reglas operativas del formato flat (corregidas):**

1. **Consumer Voice = APOYO al cuanti, no narrativa expandida.** El slide Consumer Voice existe para **fortalecer el hallazgo cuantitativo del slide anterior** con UNA voz que literalice el dato. **1 verbatim por slide Consumer Voice — uno solo, el que mejor apoye al cuanti.** No 2, no 3. Si el set editorial entrega 2 verbatims para un hallazgo cuanti, el editor debe escoger cuál apoya mejor al stat y descartar el otro (o reservarlo para otro entregable). **Esto es decisión del editor, no del montador.**

2. **Múltiples verbatims (2-3) en un mismo slide = SOLO en dos casos:**
   - **Hallazgo solo-cuali** (sin stat publicable) — los 2-3 verbatims apilados como cards gris carbón dentro de un slide único con headline arriba.
   - **Hallazgo cuanti + cuali integrado en el mismo slide** — caso especial donde el stat grande y las quotes coexisten en el mismo slide porque el editor lo entregó así.

   **Nunca apilar 2 verbatims en un slide Consumer Voice tradicional** (slide que apoya un hallazgo cuanti de slide anterior). Esa fue una sobre-corrección de versiones previas.

3. **Data cualitativa en cards translúcidas negras — EXCEPTO Consumer Voice.** Los verbatims van en cards con fill `rgba(0, 0, 0, 0.45)` + outline blanco 1pt + border-radius 15pt en estos casos: slide solo-cuali (1-3 verbatims) y slide cuali+cuanti integrado. **EL SLIDE CONSUMER VOICE NO LLEVA CARD** — el verbatim va suelto sobre fondo negro, con header "CONSUMER VOICE" arriba como única pista contextual. Specs completas en sección 3.9 Layout 4 vs Layouts 5 y 6.

4. **Sin masterslides decorativos.** El montador entrega fondo negro `#000000` PLANO con texto blanco. Los halos arcoíris, "CÓDIGO CASA® - REPORTE" arriba izq, "NINJA THINKING" arriba der, logo Ninja abajo der, textura ruido, etc. son del masterslide que Jeremy aplica DESPUÉS sobre el PPTX entregado. No los montes ni los simules.

5. **Sin cajas de "Pregunta P##. Base: X. Fuente: archivo.md" debajo de cada stat.** Esa metadata técnica NO va al slide. El stat lleva: cifra grande arriba + descripción Poppins con bold selectivo debajo. Punto. La pregunta y la base quedan implícitas en el **Source pie de página** (centrado al pie del slide, Poppins italic 9pt) que sí lleva el formato `Source: Código Casa — Estudio cuantitativo 2025 · P##, P## · Base 500.` Una sola línea Source al pie cubre TODAS las preguntas del slide. No se repite por stat.

### 3.2. Tipografía
- **Headlines de Hallazgo y Cruce:** Instrument Serif, MAYÚSCULAS, centrado, italic en la frase del giro, kerning 0, auto-tamaño 30–70pt según largo.
- **Resto de headlines:** Instrument Serif 32pt, sentence case, split plain/italic.
- **Stats grandes:** Instrument Serif italic 96pt, máximo 3–4 caracteres.
- **Texto en cajas (descripciones, conclusiones, sources):** Poppins.
- **Verbatims Consumer Voice:** Instrument Serif uppercase con comillas curvas.

### 3.3. Auto-tamaño de headlines Hallazgo y Cruce

| Largo de headline | Tamaño | Líneas |
|---|---|---|
| <30 chars | 70pt | 1 |
| 30–44 | 55pt | 2 |
| 45–65 | 42pt | 2–3 |
| 66–85 | 36pt | 3 |
| >85 | 30pt | 3–4 |

### 3.4. Paleta
- Negro `#000000` — fondo
- Blanco `#FFFFFF` — texto, cifras, **todos los verbatims**
- Gris carbón `#2E2E2E` — cajas de quotes social listening, separadores
- Verde lima `#B8FF4D` — **SOLO** la cápsula "Tensión 0X" en Mapeo y Kit
- Azul oscuro `#1A1A2E` — caja Nueva Narrativa de Marca

**Verde lima nunca para texto.** Si lo encuentras en @usernames o headers, es bug → pasarlo a blanco.

### 3.5. Cifras (regla corregida tras feedback Jeremy mayo 2026)

**Stats grandes (Instrument Serif 96pt italic, slot de 3-4 caracteres):**
- **Redondear a entero cuando se puede.** `47.8%` → `48%`, `42.6%` → `43%`, `64.0%` → `64%`, `3.0%` → `3%`, `85.0%` → `85%`. **Esto contradice instrucciones previas — la regla del knowledge oficial es redondeo visual por consistencia.**
- **Decimales se mantienen cuando agregan información** que el redondeo borraría: cifras de 1 dígito antes del punto (`8.7%`, `4.4%`, `6.6%`), brechas matemáticamente significativas (`15.2 puntos`), ratios `2.3x`, `1.5x`.
- **Decimales en descripciones inline (Poppins 11pt):** siempre se mantienen exactos. `47.8% economía` en stat grande pasa a `48%`, pero `el 95.6% restante` en descripción se queda con decimal.
- **K/M para volúmenes grandes:** `1.25K`, `2.88M`, `7.4M`.
- **Si el stat grande no cabe a 96pt:** baja el tamaño de fuente; nunca cortes el dato.

**Reglas operativas para cuando hay varios stats en un slide:**
- Aplica criterio de consistencia visual al SET de stats del slide. Si los 3 stats son enteros limpios (`48%`, `46%`, `62%`), todos van en entero. Si uno requiere decimal por información (`8.7%`), considera si los otros lo mantienen para coherencia o si solo ese lo lleva.
- La regla manda sobre el knowledge histórico (que decía "no redondear nunca"): para el formato flat de Código Casa, **stat grande redondeado a entero por defecto, decimal solo si es informativamente necesario**.

### 3.6. Source — formato estándar
- Slides cuanti: `Source: Código Casa — Estudio cuantitativo 2025 · P##, P## · Base 500.`
- Slides Conv. Digital: `Ninja Social Listening Impact® — Data 01 sept – 31 dic 2025.`
- Mapeo / Kit / Caso: `Source: Ninja Thinking 2026`

### 3.7. Headers de intro
"TENSIÓN 0X · FINANZAS" → **"TENSIÓN 0X"** (sin pilar). Borrar todos los labels guía visibles ("/ HALLAZGO ·", "/ CRUCE ·", etc.).

### 3.8. Cruces vienen del `.txt` MED, no del cazador
Slides 4, 12, 20, 28, 36 (Cruce de Data) → la data **viene del bloque "CRUCE TENSIÓN X" del `.txt` MED**, no del output del cazador (que ya no entrega cruces como bloque). Si el `.txt` MED no tabuló el cruce, **escala al equipo de research o al cazador**. No improvisar desde la base sin validación.

---

## 3.9. CSS / decisiones de diseño NO NEGOCIABLES — specs medidas en Keynote (feedback Jeremy mayo 2026 — v4 con dimensiones EXACTAS)

Estas reglas vienen de feedback EXPLÍCITO de Jeremy con dimensiones medidas en Keynote sobre el slide real. **Reemplazan TODA versión anterior, incluyendo v3 de este documento.** Aplican a cualquier deck Código Casa formato flat.

**TODOS los tamaños están en pt asumiendo slide 1920×1080 (Full HD widescreen, unidad Keynote = pt nativo).** No interpretes, no escales, no decidas. Aplica las dimensiones literales. Si algo no cabe, regresa al editor — no improvises.

**Conversión rápida pt → EMU para python-pptx:**
- 1 pt = 12,700 EMU
- Slide 1920×1080 pt = 24,384,000 × 13,716,000 EMU. PERO el slide PPTX widescreen ya está configurado en EMU como 18,288,000 × 10,287,000 (que es 1920×1080 px @ 96 dpi).
- **Convención operativa**: 1 pt Keynote = 1 px @ 96 dpi en python-pptx. Es decir, si Jeremy dice 1637pt en Keynote, en python-pptx se usa `Emu(1637 * 9525)` (porque 1 px @ 96 dpi = 9525 EMU).
- Dimensiones canónicas: 1637pt = 15,592,425 EMU; 485pt = 4,619,625 EMU; 360pt = 3,429,000 EMU; 75pt = 714,375 EMU; 500pt = 4,762,500 EMU; 245pt = 2,333,250 EMU.

### Configuración del slide

```css
.slide {
  width: 1920pt;
  height: 1080pt;
  background: #000000;           /* fondo negro plano — sin masterslide */
  font-family: 'Instrument Serif', 'Poppins';
  letter-spacing: 0;              /* kerning 0 en TODO el deck */
}
```

**python-pptx equivalente:**
```python
from pptx.util import Emu
# 1920pt @ convención Keynote = 18,288,000 EMU (= 20 inches)
# 1080pt @ convención Keynote = 10,287,000 EMU (= 11.25 inches)
prs.slide_width = Emu(18_288_000)
prs.slide_height = Emu(10_287_000)
# 1pt Keynote = 9525 EMU
```

### NO SOURCE — eliminar pie de página

**NO se pone Source en NINGÚN slide.** La metadata (Pregunta P##, base, fuente) vive en el set editorial y en los archivos derivados, no en el slide. El deck va limpio sin pie de página técnico.

Esto elimina la línea Poppins italic 9pt que aparecía al pie en versiones anteriores. Si el slide necesita atribuirse a la fuente, eso se hace una sola vez al final del deck o en una slide aparte de créditos — no en cada slide.

### STAT BOXES — caja de descripción Poppins 10 cm × 3 cm (≈ 378×113pt) — v5

**v5 — feedback Jeremy 14-may-2026 (Pilar Mujer): reemplaza la versión anterior de 360×75pt + 16pt. La caja se mide en CENTÍMETROS, no pulgadas, no "auto-size". 10cm × 3cm fijo. Texto de la descripción a 13pt fijo. Headline del hallazgo a 50pt fijo (ver sección de Headlines más abajo).**

> ## ⚠ LECCIÓN OPERATIVA CRÍTICA (15-may-2026 — Pilares Creencias + Opiniones Políticas)
>
> **Si en el repo ya existe un `build_<pilar>_deck.py` de una corrida anterior, NO LO REUTILICES TAL CUAL.** El cazador puede generar un script con dimensiones desactualizadas si copia patrones de la corrida previa.
>
> **Antes de correr cualquier build script, verifica que estas 4 constantes existan con estos valores exactos:**
> ```python
> HEADLINE_PT     = 50           # fijo, no auto-size, no pick_headline_size_px()
> STAT_DESC_PT    = 13           # 13pt fijo (NO 16, NO 16.5, NO pt_from_px(22))
> STAT_BOX_W      = 378          # 10cm fijo para 1, 2 y 3 stats
> STAT_BOX_H      = 113          # 3cm fijo
> ```
>
> **Si encuentras alguna de estas variantes prohibidas, regenera el script o patcheálo ANTES de buildear:**
> - `STAT_BOX_W_1STAT = 822`, `STAT_BOX_W_2STATS = 880`, `STAT_BOX_W_3STATS = 560` ← v3 antigua
> - `STAT_BOX_H = 238` o `height_px=180` en la `add_rich_textbox` de descripción ← v3 antigua
> - `STAT_DESC_PT = 16` o `pt_from_px(22)` ← v3 antigua
> - `size_pt = pt_from_px(pick_headline_size_px(chars))` en `add_headline()` ← auto-size, v3 antigua. Reemplazar por `size_pt = HEADLINE_PT`.
>
> Esta lección nace de que el cazador, en Sistema de Creencias y Opiniones Políticas (re-run 15-may), reusó el script del run anterior y NO aplicó v5. Hubo que patchear post-hoc. **Próxima vez: aplicar v5 al construir el script desde el primer write, sin importar si hay un build_*.py previo en `Agentes Hallazgos/`.**

> ## ⚠ V6 — UPDATE 15-may-2026 (Consumer Voice + Cards cualitativas)
>
> **Verbatim Consumer Voice (Layout 4):** de **60pt → 50pt** Instrument Serif. Fijo, no auto-size, no negociable.
>
> **Cards cualitativas (Layout 5 y 6):** de 549×221pt → **567×227pt = 15cm × 6cm** fijo (en cm, no pulgadas, no pt arbitrarios).
> - 1 card centrada: left 676, top 426
> - 2 cards side by side: gap 80pt, conjunto centrado (start left 353, top 429)
> - 3 cards side by side: gap 36pt, conjunto centrado (start left 73, top 429)
>
> **Las constantes en el build script deben quedar:**
> ```python
> CV_VERBATIM_PT  = 50         # v6: era 60
> CARD_W          = 567        # v6: era 549 — 15 cm @ 96dpi
> CARD_H          = 227        # v6: era 221 — 6 cm @ 96dpi
> ```
>
> Si encuentras `CV_VERBATIM_PT = 60`, `CARD_W = 549`, `CARD_H = 221`, `pt_from_px(50) = 37.5pt` para verbatim CV, o `CV_CARD_W = 1637` usado como card cuali — todas son variantes prohibidas, regenera o patchea.

**La cifra grande Instrument Serif va aparte (encima de la caja de descripción). La "caja de texto del stat" se refiere a la caja de descripción Poppins debajo de la cifra.**

**Conversión operativa (cm → pt → EMU):**
- 10 cm = 378 pt (en sistema Keynote/python-pptx, 1pt = 1px @ 96 dpi; 1cm @ 96 dpi = 37.8 px)
- 3 cm = 113 pt
- En python-pptx: `Emu(378 * 9525)` para 10cm de ancho, `Emu(113 * 9525)` para 3cm de alto.

```css
.stat-number {
  font-family: 'Instrument Serif';
  font-style: italic;
  font-weight: 400;
  font-size: 180pt;             /* cifra dominante; se mantiene grande */
  color: #FFFFFF;
  text-align: center;
  /* enteros por defecto: 47.8% → 48%, 3.0% → 3%, 85.0% → 85% */
  /* decimal solo si: 1 dígito antes (8.7%, 5.5%) o brecha significativa (15.2pts) */
}

.stat-description {
  width: 378pt;                 /* CAJA DE TEXTO STAT — 10 cm exactos */
  height: 113pt;                /* 3 cm exactos */
  font-family: 'Poppins';
  font-weight: 400;
  font-size: 13pt;              /* v5 — antes 16pt */
  line-height: 1.4;
  color: #FFFFFF;
  text-align: center;
  /* bold selectivo en palabra clave */
}

.stat-description strong {
  font-weight: 700;
}
```

**Respiración entre stats — REGLA OPERATIVA NO NEGOCIABLE:**
- Las cajas de stats (cifra + descripción) NO se pegan unas con otras. Respiran visualmente con márgenes generosos.
- Con cajas a 378pt de ancho fijo, los gaps quedan holgados:
  - **1 stat:** caja centrada en el slide (left = (1920-378)/2 = 771pt).
  - **2 stats:** ancho total 756pt; queda 1164pt de aire — distribuye con gap mínimo de ~388pt entre cajas o repartido con márgenes laterales generosos.
  - **3 stats:** ancho total 1134pt; queda 786pt de aire — distribuye con gap mínimo de ~196pt entre cajas (margen lateral ≈ 196pt cada lado).
- **El ancho de la caja NO se reduce.** Si visualmente quedan muy juntas, agranda los gaps, NO comprimas las cajas. La caja de stat es 10cm × 3cm. Punto.
- La cifra grande Instrument Serif (180pt) va centrada arriba de su caja de descripción. Cifra y descripción se alinean horizontalmente. Verifica que la cifra grande no se desborde hacia los stats adyacentes — si choca, reduce la cifra ANTES que romper la dimensión de la caja.

### CARDS DE VERBATIM — fill negro opacidad 45% + outline blanco 1pt (CRÍTICO)

**TODAS las cards rounded edges del deck (solo-cuali, cuali+cuanti integrado) llevan:**
*Nota: el slide Consumer Voice NO lleva card — verbatim suelto sobre fondo negro. Ver Layout 4.*


- Fill `rgba(0, 0, 0, 0.45)` — negro con opacidad 45%.
- **Outline blanco 1pt** `#FFFFFF` weight 1pt — borde sutil que define el contorno de la card sobre fondo negro.
- Border-radius 15pt (esquinas redondeadas).

```css
.verbatim-card {
  background: rgba(0, 0, 0, 0.45);   /* NEGRO con 45% opacidad — NO #2E2E2E */
  border: 1pt solid #FFFFFF;          /* outline blanco 1pt — NUEVO */
  border-radius: 15pt;
  padding: 60pt 80pt;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
```

**python-pptx equivalente para el fill translúcido + outline blanco 1pt:**
```python
from pptx.dml.color import RGBColor
from pptx.util import Pt
from lxml import etree

# Fill negro 45% opacidad
shape.fill.solid()
shape.fill.fore_color.rgb = RGBColor(0x00, 0x00, 0x00)

sp = shape.fill._xPr
nsmap = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
srgbClr = sp.find('.//a:srgbClr', nsmap)
alpha = etree.SubElement(srgbClr, '{http://schemas.openxmlformats.org/drawingml/2006/main}alpha')
alpha.set('val', '45000')  # 45% = 45000 en notación PPTX

# Outline blanco 1pt — NUEVO
shape.line.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
shape.line.width = Pt(1)
```

**Border-radius 15pt en python-pptx:**
```python
from pptx.enum.shapes import MSO_SHAPE
shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
# adjustment ~0.05-0.06 para border-radius ~15pt en cards de 567×227 (v6)
shape.adjustments[0] = 0.06
```

### VERBATIM dentro de la card

```css
.verbatim-text {
  font-family: 'Instrument Serif';
  font-weight: 400;
  font-style: normal;            /* NO italic */
  font-size: 50pt;               /* v6 — feedback Jeremy 15-may-2026 (era 60pt) */
  line-height: 1.3;
  color: #FFFFFF;
  text-align: center;
  /* comillas españolas angulares «...» — NO comillas curvas inglesas */
  /* CENTRADO en el centro vertical y horizontal de la card */
}

.verbatim-attribution {
  font-family: 'Poppins';
  font-style: italic;            /* atribución sí italic */
  font-weight: 400;
  font-size: 20pt;               /* dimensión EXACTA Jeremy */
  color: #FFFFFF;
  text-align: center;
  margin-top: 30pt;
  /* formato: "— Familia [tipología]" */
}
```

### HEADLINE (slide Hallazgo cuanti / Card cualitativa)

```css
.headline {
  position: absolute;
  top: 100pt;
  left: 100pt;
  width: 1720pt;                  /* 1920 - 100*2 */
  
  font-family: 'Instrument Serif';
  font-weight: 400;
  font-size: 50pt;                /* dimensión EXACTA Jeremy — fijo, no auto-size */
  text-align: center;
  text-transform: uppercase;
  color: #FFFFFF;
  letter-spacing: 0;
  line-height: 1.1;
}

.headline em {
  font-style: italic;             /* solo en frase del giro */
}
```

**Headlines: 50pt fijo, centralizados.** Ya no hay auto-size por largo. Si el headline excede el ancho de la caja a 50pt, se permite multi-línea (line-height 1.1 mantiene apretado el bloque). Si es excesivamente largo y no cabe en 3-4 líneas, regresa al editor para acortar — no reduzcas el tamaño del headline.

### NO SOURCE (eliminado)

Ya no se incluye pie de página Source en ningún slide. Ver sección "NO SOURCE — eliminar pie de página" arriba.

### LAYOUTS POR TIPO DE SLIDE — dimensiones EXACTAS en pt

#### Layout 1 — Slide Hallazgo cuanti con 1 stat (v5)

```
+----------------------------------------------+
|                                              |
|      [HEADLINE 50pt, 1720pt wide]            | <- top 100pt
|                                              |
|                                              |
|             [CIFRA GRANDE 180pt]             | <- top 420pt, centrada
|                                              |
|       [CAJA DESCRIPCIÓN 378×113pt (10×3cm)]  | <- top 660pt, centrada
|                                              |
+----------------------------------------------+

Posiciones:
- Headline: left 100, top 100, width 1720, font 50pt
- Cifra 180pt: top 420, centrada horizontalmente
- Caja descripción: left (1920-378)/2 = 771, top 660, width 378, height 113, font 13pt
```

#### Layout 2 — Slide Hallazgo cuanti con 2 stats (v5)

```
+----------------------------------------------+
|      [HEADLINE 50pt]                         |
|                                              |
|   [CIFRA 1 180pt]      [CIFRA 2 180pt]       | <- top 420
|                                              |
|   [DESC 378×113pt]     [DESC 378×113pt]      | <- top 660
|                                              |
+----------------------------------------------+

Posiciones (2 stats con cajas fijas 10×3cm, gap 200pt para respirar generoso):
- Conjunto de 2 stats centrado: ancho total = 378 + 200 + 378 = 956pt
- Conjunto empieza en left (1920-956)/2 = 482pt
- Desc 1: left 482, top 660, width 378, height 113, font 13pt
- Desc 2: left 1060, top 660, width 378, height 113, font 13pt
- Cifra 1: top 420, centrada sobre Desc 1 (centro x = 671)
- Cifra 2: top 420, centrada sobre Desc 2 (centro x = 1249)

Línea separadora vertical opcional (#2E2E2E 1pt, alto 200pt): left 960, top 460.
```

#### Layout 3 — Slide Hallazgo cuanti con 3 stats (v5)

```
+----------------------------------------------+
|      [HEADLINE 50pt]                         |
|                                              |
| [CIFRA 1]    [CIFRA 2]    [CIFRA 3]          | <- top 420 (cifra a 150pt si necesita)
|                                              |
| [378×113pt]  [378×113pt]  [378×113pt]        | <- top 660
|                                              |
+----------------------------------------------+

Posiciones (3 stats con cajas fijas 10×3cm, gap 100pt para respirar):
- Conjunto total: 378*3 + 100*2 = 1334pt
- Conjunto empieza en left (1920-1334)/2 = 293pt
- Desc 1: left 293, top 660, width 378, height 113, font 13pt
- Desc 2: left 771, top 660 (gap 100pt después de 293+378=671)
- Desc 3: left 1249, top 660
- Cifras centradas sobre sus descripciones, top 420
- Si las cifras (a 180pt) chocan, reducir a 150pt — pero NUNCA reducir el tamaño de la caja de descripción (10×3cm es fijo).

Líneas separadoras (#2E2E2E 1pt, alto 200pt): left 721 y 1199, top 460.
```

#### Layout 4 — Slide Consumer Voice (apoya cuanti anterior — 1 verbatim SUELTO, sin card)

**CRÍTICO (feedback Jeremy v6): el slide Consumer Voice NO lleva card.** El verbatim va suelto sobre fondo negro plano. La única pista contextual es el header "CONSUMER VOICE" arriba. Esto diferencia visualmente el Consumer Voice (verbatim que apoya cuanti, sin contenedor) de las cards cualitativas (verbatim en bloque cerrado, con outline).

```
+----------------------------------------------+
|                                              |
|              CONSUMER VOICE                  | <- top 80pt, Poppins 14pt gris #9B9B9B
|                                              |
|                                              |
|                                              |
|     « Verbatim 50pt Instrument Serif (v6)  | <- texto suelto, sin card
|       regular blanco, comillas               |    centrado vertical y horizontal
|       españolas «...». »                     |    sobre fondo negro del slide
|                                              |
|         — Familia [tipología]                | <- Poppins italic 20pt blanco
|                                              |
|                                              |
+----------------------------------------------+

Specs del slide Consumer Voice (sin card):

- Fondo: negro plano #000000 (sin masterslide).
- Header: "CONSUMER VOICE" en Poppins regular 14pt mayúsculas, color gris #9B9B9B, centrado horizontalmente, top ~80pt.
- Verbatim: Instrument Serif regular **50pt (v6)** blanco, comillas españolas «...», centrado horizontalmente.
  - Texto bloque ocupa ~1637pt de ancho máximo (left 141, ancho 1637, alto auto según longitud).
  - Centrado vertical aproximado: top ~350-400pt según longitud.
  - Multi-línea con line-height 1.3.
- Atribución: Poppins italic 20pt blanco, "— Familia [tipología]", centrada horizontalmente, ~60pt debajo del último renglón del verbatim.

NO se monta:
- NO card de fondo (sin rectángulo `rgba(0,0,0,0.45)`, sin outline, sin border-radius).
- NO source pie de página.
- NO masterslide decorativo (Jeremy lo aplica después).
```

#### Layout 5 — Slide Card cualitativa (solo-cuali — 1-3 cards SIDE BY SIDE)

**REGLA CLAVE: las cards múltiples van LADO A LADO (side by side), no apiladas verticalmente.**

```
+----------------------------------------------+
|      [HEADLINE 50pt]                         |
|                                              |
|                                              |
|   ┌─────────────┐    ┌─────────────┐         |
|   │ Verbatim 1  │    │ Verbatim 2  │         | <- cards side by side
|   │ Familia A   │    │ Familia B   │         |    v6: 567×227 pt = 15×6 cm cada una
|   └─────────────┘    └─────────────┘         |
|                                              |
+----------------------------------------------+

Card cualitativa — DIMENSIONES CANÓNICAS v6 (15-may-2026 Jeremy):
- width: 567pt (= 15 cm @ 96 dpi)
- height: 227pt (= 6 cm @ 96 dpi)
- border-radius: 15pt
- fill: rgba(0, 0, 0, 0.45) (negro 45% opacidad)
- outline: 1pt blanco #FFFFFF
- padding: 30pt lados, 30pt arriba/abajo

> ⚠ **v6 update — 15-may-2026:** las cards cualitativas pasan de 567×227pt (v6: 15×6cm) (medidas previas) a **567×227pt (15×6cm fijo)**. Ya no se interpreta — la caja se mide en CENTÍMETROS. Aplica a Layouts 5 y 6.

Posiciones canónicas (todas side by side):

1 verbatim — slide solo-cuali centrado en slide completo:
- left (1920-567)/2 = 676.5pt, top (1080-227)/2 = 426.5pt, width 567, height 227

2 verbatims (side by side):
- gap entre cards: 80pt
- Conjunto total: 567*2 + 80 = 1214pt
- Empieza en left (1920-1214)/2 = 353pt
- Card 1: left 353, top 429, width 567, height 227
- Card 2: left 1000, top 429, width 567, height 227

3 verbatims (side by side):
- gap entre cards: 36pt
- Conjunto total: 567*3 + 36*2 = 1773pt
- Empieza en left (1920-1773)/2 = 73pt
- Card 1: left 73, top 429
- Card 2: left 676, top 429
- Card 3: left 1279, top 429

TEXTO DENTRO de la card cualitativa (canónico v6):
- Verbatim: Poppins 15pt blanco, comillas españolas «...», centrado vertical y horizontalmente.
- Atribución: Poppins italic 12-13pt, blanco, centrada debajo del verbatim.
- Padding: 30pt arriba/abajo, 30pt lados.
- **IMPORTANTE:** el texto dentro de cards cualitativas es Poppins, NO Instrument Serif. Esto las diferencia visualmente del slide Consumer Voice (donde el verbatim sí va en Instrument Serif **50pt v6**, era 60pt).
```

#### Layout 6 — Slide cuali + cuanti integrado en mismo slide (1-3 stats + cards lado a lado)

**Caso: hallazgo tiene cuanti + cuali y se monta TODO en un mismo slide en lugar de 2 slides separados.** Layout que combina cifras + cajas de descripción 360×75pt + cards cualitativas 567×227pt (v6: 15×6cm).

```
+----------------------------------------------+
|      [HEADLINE 50pt]                         |
|                                              |
|   [CIFRA]     ┌─────────────┐                |
|   180pt       │ « Verbatim »│                |
|               │ Familia X   │                |
|   [DESC       └─────────────┘                |
|   360×75pt]                                  |
|                                              |
+----------------------------------------------+

POSICIONES CANÓNICAS para 1 stat + 1 verbatim (medidas por Jeremy en Keynote):
- Headline: left 100, top 100, width 1720, font-size 50pt
- Cifra grande: posición a la izquierda del slide, font-size 180pt
- Caja descripción: 360×75pt centrada debajo de la cifra, Poppins 16pt
- Card cualitativa a la derecha:
  · left: 748pt
  · top: 403pt
  · width: 549pt
  · height: 221pt
  · fill rgba(0,0,0,0.45)
  · outline blanco 1pt
  · border-radius 15pt
  · Texto: Poppins 15pt blanco, comillas «...», centrado
  · Atribución: Poppins italic 12-13pt centrada debajo del verbatim

Para 1 stat + 2 verbatims:
- Mantén el stat (cifra + caja descripción) a la izquierda
- Pon 2 cards cualitativas a la derecha, side by side: cada una 567×227pt (v6: 15×6cm)
- Si no caben con respiro, regresa al editor — no comprimas

Para 2 stats + 1 verbatim:
- 2 stats a la izquierda (cifras y descripciones lado a lado o apiladas)
- 1 card cualitativa 567×227pt (v6: 15×6cm) a la derecha
- Si queda muy apretado → regresa al editor para repartir en 2 slides

REGLA: si el layout integrado no respira (cajas pegadas, texto solapado), DESCARTA el integrado y monta como 2 slides separados (Hallazgo cuanti + Consumer Voice). No fuerces.
```

### REGLAS GLOBALES (no negociables — versión consolidada)

1. **Slide: 1920×1080 pt** (configurar el deck a 18,288,000×10,287,000 EMU al inicio).
2. **Fondo negro plano `#000000`.** Sin masterslide decorativo. Jeremy aplica halos arcoíris, headers, logo, textura después.
3. **Cards de verbatim (solo en Layouts 5 y 6): `rgba(0, 0, 0, 0.45)` + outline blanco 1pt + border-radius 15pt.** NO `#2E2E2E` sólido. EL SLIDE CONSUMER VOICE (Layout 4) NO LLEVA CARD — verbatim suelto sobre fondo negro.
4. **Verbatims en Consumer Voice (Layout 4 — slide dedicado, SIN card):** Instrument Serif regular 60pt (NO italic) con comillas españolas `«...»`, suelto sobre fondo negro. Atribución Poppins italic 20pt centrada debajo. Header "CONSUMER VOICE" Poppins 14pt gris #9B9B9B arriba.
5. **Verbatims en cards cualitativas (Layouts 5 y 6 — con card):** Poppins 15pt con comillas españolas `«...»`. Atribución Poppins italic 12-13pt. Card 567×227pt (v6: 15×6cm) con fill 45% opacidad + outline blanco 1pt + border-radius 15pt.
6. **Headlines: 50pt fijo Instrument Serif MAYÚSCULAS centralizados.** Sin auto-size. Italic solo en frase del giro.
7. **Cifras grandes: 180pt Instrument Serif italic blanco.** Redondeo a entero por defecto (47.8 → 48); decimal solo si 1 dígito antes (5.5%, 8.7%) o brecha matemática (15.2 pts).
8. **Caja de descripción de stat: 360×75pt Poppins 16pt** blanco con bold selectivo.
9. **Consumer Voice: verbatim suelto centrado en slide, ancho máximo del bloque ~1637pt.** Sin contenedor visual.
10. **Card cualitativa: 567×227pt (v6: 15×6cm) side by side** (no apiladas verticalmente). Posición canónica en cuali+cuanti integrado: X 748, Y 403.
11. **Atribuciones: "— Familia [tipología]"** en italic Poppins.
12. **NO SOURCE en ningún slide.** Pie de página técnico eliminado.
13. **NO cajas "Pregunta P##. Base. Fuente"** debajo de stats.
14. **Kerning 0** en TODO el deck (`letter-spacing: 0`).
15. **Sin elementos decorativos.** Solo líneas verticales `#2E2E2E` 1pt entre stats grandes cuando hay 2-3.
16. **Respiración: 120pt mínimo entre 2 stats, 80pt entre 3 stats.** Si chocan, reduce ancho del contenido antes de comprimir gaps; si aún no respira, regresa al editor.
17. **Si algo no cabe en las dimensiones literales, regresar al editor.** NO improvisar tamaños.

### Lo que el montador NO pone en el slide (el masterslide lo agrega después)

- **Halos arcoíris arriba** del slide — los aplica Jeremy con masterslide.
- **"CÓDIGO CASA® - REPORTE"** arriba izquierda — masterslide.
- **"NINJA THINKING"** arriba derecha — masterslide.
- **Logo Ninja** abajo derecha — masterslide.
- **Textura ruido / grain** sobre el fondo — masterslide.

El montador entrega **fondo negro plano** con los elementos de contenido (headline, stats, cards) y nada más. Jeremy aplica el masterslide al final.

### Sin elementos decorativos en el contenido

- NO ornamentos visuales, NO viñetas, NO iconografía decorativa.
- Líneas separadoras verticales finas (1px gris `#2E2E2E`) **SÍ se permiten** entre stats grandes cuando hay 2 o 3 stats en fila — siguen el patrón visual del deck de referencia.
- NO líneas separadoras horizontales entre headline y stats, ni entre stats y atribución.

### Slide de Hallazgo cuanti

**Layout canónico (ver referencia visual de Jeremy mayo 2026):**

```
       [HEADLINE EN MAYÚSCULAS, INSTRUMENT SERIF, CENTRADO ARRIBA]
       [auto-size 30-90pt según largo]


       [STAT 1]    │    [STAT 2]    │    [STAT 3]
        96pt       │     96pt        │     96pt
       (entero)    │    (entero)     │    (entero o decimal si aplica)

   [desc1: reg]    │   [desc2]       │   [desc3]
   [BOLD palabra]  │   [BOLD]        │   [BOLD]
   [reg cierre]    │                 │

                          [Source pie de página]
```

**Especificaciones:**

- **Headline:** Instrument Serif MAYÚSCULAS centrado horizontalmente, posicionado arriba del slide (1" del top aprox), kerning 0. Auto-size según la tabla de sección 3.3 (≤30 chars → 70pt, 30-44 → 55pt, 45-65 → 42pt, 66-85 → 36pt, >85 → 30pt). **Italic selectivo en la frase del giro.**
- **Stats grandes:** Instrument Serif italic 96pt, distribuidos uniformemente a lo ancho del slide. Si hay 1 stat → centrado. Si hay 2 stats → posiciones a 1/3 y 2/3 del ancho (NO en extremos). Si hay 3 stats → a 1/4, 1/2, 3/4 del ancho. **Bordes verticales finos `#2E2E2E` 1px entre stat y stat.**
- **Descripciones (debajo de cada stat):** Poppins regular 11pt, con **bold selectivo en la palabra clave** (variable demográfica, concepto destacado o cita textual). Patrón `[regular] [BOLD palabra] [regular cierre]`. Color blanco.
- **NO cajas de "Pregunta P##. Base. Fuente" debajo de cada stat.** Esa metadata vive solo en el Source pie de página. El stat se queda limpio: cifra grande + descripción Poppins con bold selectivo. Nada más debajo.
- **Source pie de página:** Poppins italic 9pt al pie del slide, centrado, blanco/gris claro. Formato `Source: Código Casa — Estudio cuantitativo 2025 · P##, P## · Base 500.` UNA sola línea cubre TODAS las preguntas del slide.

### Slide de Consumer Voice (1 verbatim SUELTO, sin card — feedback Jeremy v6)

**Función del slide Consumer Voice:** apoyar y fortalecer el hallazgo cuantitativo del slide anterior con UNA voz que literalice el dato. No es para expandir narrativa ni para acumular quotes. Si el set editorial entrega 2 verbatims para un hallazgo cuanti, el editor debe escoger cuál apoya mejor al stat — el montador NO decide.

**REGLA CRÍTICA: el slide Consumer Voice NO lleva card.** El verbatim va suelto sobre fondo negro plano, con el header "CONSUMER VOICE" arriba. Esto contradice versiones previas (v3, v4, v5) donde el Consumer Voice sí llevaba card 1637×485pt. **A partir de v6, sin card.**

**Layout canónico (verbatim suelto sobre fondo negro):**

```
                     [CONSUMER VOICE]
              (header arriba, Poppins 14pt, gris #9B9B9B)



     « Verbatim grande en Instrument Serif
       regular blanco, comillas españolas. »
       (texto suelto sobre fondo negro,
        SIN card, SIN outline)



              — Familia [tipología]
                  (Poppins italic 20pt)
```

**Especificaciones (sin card):**

- **Fondo del slide:** negro plano `#000000`. Sin masterslide.
- **Header:** "CONSUMER VOICE" en Poppins regular 14pt MAYÚSCULAS, centrado horizontalmente, color gris suave `#9B9B9B`, posicionado a top ~80pt.
- **Verbatim:** Instrument Serif regular 60pt blanco, comillas españolas `«...»`, centrado horizontalmente sobre fondo negro. Multi-línea con line-height 1.3.
  - Ancho máximo del bloque de texto: ~1637pt (left 141, ancho 1637).
  - Posición vertical: centrado vertical en el slide (top aprox 350-400pt según longitud).
- **Atribución:** Poppins italic 20pt blanco, formato `— Familia [tipología]`, centrada horizontalmente, ~60pt debajo del último renglón del verbatim.

**Lo que NO se monta en el slide Consumer Voice:**
- NO card de fondo (sin rectángulo translúcido, sin outline, sin border-radius).
- NO source pie de página.
- NO masterslide decorativo.

**Diferencia visual entre Consumer Voice y card cualitativa (importante):**
- **Consumer Voice (Layout 4):** verbatim SUELTO sobre fondo negro. Header "CONSUMER VOICE" arriba. Sin contenedor visual. El verbatim domina el slide.
- **Card cualitativa (Layout 5 y 6):** verbatim DENTRO de card 567×227pt (v6: 15×6cm) con fill `rgba(0,0,0,0.45)` + outline blanco 1pt + border-radius 15pt. Headline arriba (no header "CONSUMER VOICE"). Texto interno en Poppins 15pt (no Instrument Serif).

Esto separa dos modos visuales: Consumer Voice = pausa tipográfica grande, sola. Card cualitativa = bloque contenido side by side con otros bloques.

- **Si el editor entrega 2 verbatims para un hallazgo cuanti** → regresa al editor para que escoja cuál apoya mejor el stat. Nunca apiles los 2 en un Consumer Voice. La regla de "múltiples verbatims" aplica SOLO a slides solo-cuali (sin stat), y ahí van en cards side by side — ver Layout 5.

### Slide de Card cualitativa (hallazgo solo-cuali, sin stat publicable)

Layout idéntico al Consumer Voice, pero con headline arriba en lugar del header "CONSUMER VOICE":

```
       [HEADLINE EN MAYÚSCULAS INSTRUMENT SERIF, AUTO-SIZE]


       ┌──────────────────────────────────────────────┐
       │   « Verbatim 1 »                              │
       │              — Familia [tipología]             │
       └──────────────────────────────────────────────┘
       
       ┌──────────────────────────────────────────────┐
       │   « Verbatim 2 »                              │
       │              — Familia [tipología]             │
       └──────────────────────────────────────────────┘
```

Cards con fill `rgba(0, 0, 0, 0.45)` (negro 45% opacidad, NO `#2E2E2E` sólido) y border-radius 24px. Verbatim Instrument Serif regular blanco con comillas españolas. Atribución italic Poppins. Mismo patrón visual que Consumer Voice. **Dimensiones exactas en sección 3.9 según número de verbatims apilados.**

### Atribuciones — terminología canónica

- **"Familia [tipología]"** en lugar de "Grupo [tipología]". Atribución en **italic Poppins**.
- Tipologías canónicas:
  - Familia biparental con hijos pequeños
  - Familia biparental con hijos adultos
  - Familia monoparental
  - Familia sin hijos
  - Familia sin hijos con mascota
  - Familia homoparental
  - Familia mixta
  - Familia extendida

### Comillas

- **Verbatims en slides:** comillas españolas angulares `«...»` siempre.
- Comillas inline dentro de descripciones de stat: comillas curvas estándar `"..."` o españolas si el quote es largo.
- En XML python-pptx van como caracteres Unicode `«` (U+00AB) y `»` (U+00BB).

### Tipografía consolidada

| Elemento | Familia | Tamaño | Peso | Italic |
|---|---|---|---|---|
| Headlines Hallazgo / Card cualitativa | Instrument Serif | 30-90pt auto | regular | selectivo en giro |
| Stats grandes | Instrument Serif | 96pt | regular | sí |
| Descripciones de stat | Poppins | 11pt | regular + bold selectivo | no |
| Header "CONSUMER VOICE" | Poppins | 10pt | regular | no |
| Verbatim en card | Instrument Serif | 28-42pt según largo | regular | NO |
| Atribución "— Familia X" | Poppins | 13pt | regular | sí |
| Source pie de página | Poppins | 9pt | regular | sí |

---

## 4. Los 10 errores comunes que NO se repiten

Resumen operativo de `06_ERRORES_COMUNES.md`:

1. **Inventar oraciones editoriales en conclusiones.** Si una oración no está en el hallazgo editado, no va al slide.
2. **Mantener decimales innecesarios en stats grandes.** Stat grande redondeado a entero por defecto (47.8% → 48%, 3.0% → 3%, 85.0% → 85%). Decimal solo si tiene 1 dígito antes (8.7%) o es brecha (15.2 pts).
3. **Cambiar palabras del hallazgo "porque suenan mejor".** Sin razón visual o de claridad, mantén el original.
4. **Recortar comillas mal.** La frase completa va dentro de las comillas tal como está en el hallazgo editado.
5. **Dejar placeholders sin llenar.** Identifica TODOS y rellénalos. Si no se puede, escala.
6. **Confundir placeholder de imagen con elemento de diseño.** `[ AGREGAR IMAGEN ]` en Caso Referencia NO lo llena el montador (lo hace cuenta o creativo).
7. **Verbatims en verde lima.** Pasar siempre a blanco.
8. **Labels guía visibles** (`/ HALLAZGO ·`) — borrar todas.
9. **Decimales gigantes en stats.** "26.1%" se desborda → "26%".
10. **Mezclar 2 quotes en 1.** No mash-up. La quote del hallazgo editado va tal cual.
11. **Separar verbatims múltiples en slides distintos.** Si un hallazgo tiene 2 o 3 verbatims, TODOS van en UN solo slide Consumer Voice como cards apiladas. NUNCA se separan.
12. **Verbatim como texto centrado grande sobre fondo negro.** Los verbatims siempre van en CARDS de fondo gris carbón `#2E2E2E` con border-radius, no como texto suelto.
13. **Headlines pequeños (15-30pt).** El headline manda visualmente. Aplica auto-size del knowledge: ≤30 chars → 70pt, 30-44 → 55pt, 45-65 → 42pt, 66-85 → 36pt, >85 → 30pt mínimo.
14. **2 stats en los extremos del slide.** Cuando solo hay 2 stats, posiciónalos a 1/3 y 2/3 del ancho del slide, NO en los extremos (deja hueco visual).
15. **Comillas curvas inglesas en verbatims.** Los verbatims usan comillas españolas angulares `«...»`, no `"..."`.
16. **Atribución "Grupo X".** El nombre canónico es "Familia X" en italic Poppins, no "Grupo X".
17. **Montar masterslide decorativo.** Halos arcoíris, "CÓDIGO CASA® - REPORTE", logo Ninja, textura — todo eso lo aplica Jeremy con masterslide después. Entrega fondo negro plano.
18. **Líneas separadoras horizontales** — no se ponen. Líneas verticales finas `#2E2E2E` entre stats SÍ se permiten.
19. **Verbatim Consumer Voice en italic.** El verbatim dentro de la card va en Instrument Serif REGULAR, no italic. Solo la atribución va en italic.
20. **Conclusión italic / insight debajo de los stats.** La fuerza editorial vive en el headline. Si el editor entregó conclusión italic separada, fundirla en el headline o descartar.

---

## 5. Skills que el montador invoca (orden de operaciones)

Antes de montar:

1. **Knowledge pack completo** — ruta arriba. Lee al menos `README.md`, `03_WORKFLOW_OPERATIVO.md` y `04_DECISIONES_DE_DISENO.md` antes de tocar PPTX.
2. **Este archivo** (`aprendizajes-montador-cc.md`) — destilado de no-negociables.
3. **Skill `pptx`** (de `/mnt/skills/public/pptx/SKILL.md`) — manipulación PPTX.
4. **Scripts del knowledge pack** (`apply_design_fixes.py`, `fix_hallazgo_text.py`, `build_cruce_slides.py`) — automatizar fixes globales.
5. **`graphic-designer-senior`** — solo si hay duda real de jerarquía visual o composición.
6. **`frontend-design`** — solo si hay que construir desde cero un componente visual.

Si un recurso no está disponible en sesión, opera con las reglas de este archivo + las del agente. **El knowledge pack es no negociable**: si no se puede leer, detente y reporta.

---

## 6. Cuándo escalar y NO improvisar

- El `.txt` MED no incluye el cruce de una tensión que el editor marcó como "hallazgo nacido de cruce" → pedir al cazador la tabla cruzada de soporte.
- Un cruce existe en el `.txt` pero al ponerlo en el slide no aporta visualmente → consultar con cazador y editor antes de cambiarlo.
- El cliente pidió un slide nuevo que rompe el formato 8-slides → escalar al PM.
- Una cifra no cuadra entre el hallazgo editado y el `.txt` → regresar al cazador antes de montar.
- Hay menos de 5 hallazgos editados (mínimo para deck MED de 5 tensiones) → pedir al cazador que destrabe más.

---

## 6.bis El montador NO decide contenido — solo diseño visual

**Regla operativa central del flujo Código Casa:** el montador recibe del editor un set **CERRADO** y arma slides. Si llega ambigüedad de contenido, el montador **regresa al editor** — no decide él.

**Lo que el montador SÍ decide (diseño visual, sin tocar contenido):**

- Tamaño de fuente para que el decimal exacto quepa en la caja (NUNCA redondear el dato).
- Layout de cajas de stats (1, 2 o 3 cajas según número de stats que entregó el editor).
- Kerning, leading, paleta, tipografía según knowledge pack.
- Posición de elementos en el slide.
- Quiebre de línea del headline para que la línea corte bonita (sin cambiar palabras del headline).
- Bold selectivo en una palabra clave dentro de la descripción de stat (recurso visual menor).
- Tamaño de la card cualitativa, fill, transparencia, border-radius.

**Lo que el montador NO decide (es trabajo del editor — regresa si llega ambiguo):**

- **Fusionar dos hallazgos en un slide.** Si el editor entrega H08 y H09 separados, monta dos bloques. Si el editor decidió fusionarlos, monta uno. No "decide tú si conviene fusionar".
- **Verificar atribución de Speaker.** Si el editor publicó "Grupo Monoparental" sin letra, monta así. Si publicó letra, monta letra. No "verifica tú la diarización antes de poner el slide".
- **Decidir qué cifra entra al deck.** Las cifras que llegan al editor llegan auditadas. El montador no las descarta ni las reemplaza.
- **Editar verbatims.** El verbatim del editor entra tal cual al slide — sin reescribir, sin recortar, sin agregar puntuación. Solo limpieza visual (comillas curvas, espaciado).
- **Completar cuerpos de texto.** Si una descripción de stat está incompleta, el montador regresa al editor — no la completa él.
- **Decidir si un hallazgo es solo-cuanti o solo-cuali.** Si el editor entregó solo-cuali, monta como card cualitativa. Si entregó cuanti + verbatim, monta hallazgo cuanti + slide consumer voice. No "decide tú si vale la pena el verbatim".
- **Resolver caveats T2.** Si el editor pasó una cifra T2 con caveat, el montador la incluye con caveat declarado o (si el editor decidió no incluirla) la excluye. No "decide tú si confías en la cifra T2".
- **Decidir el conteo final de slides.** Si el editor entregó 14 hallazgos, el deck tiene los slides que corresponden a 14 hallazgos. No "consolida en 10 si crees que se ve mejor".

**Cuándo el montador regresa al editor (no improvisa):**

- Verbatim que no se entiende solo en el slide → regresa al editor para que lo pula o agregue contexto.
- Stat con descripción que se cae a media frase → regresa al editor.
- Hallazgo donde no queda claro si es cuanti+cuali o solo-cuali → regresa al editor.
- Headline con split plain/italic ambiguo → regresa al editor.
- Atribución que dice "verificar letra" → regresa al editor (es decisión editorial, no visual).

**Tono operativo del montador:** ejecutor visual de un set cerrado. El montador es la última manos antes de Keynote — su trabajo es traducir contenido a slides con la línea gráfica Código Casa. No es editor, no es analista. Si encuentra algo que requiere decisión de contenido, no la toma — regresa al editor.

**Por qué esta regla existe:** el montador no tiene contexto del corpus (cuestionario, derivados, transcripciones). Si decide contenido, lo decide a ciegas — y la decisión se ve en el deck. La separación de roles existe para que cada agente cierre su pase con lo que sí domina. El montador domina diseño; contenido se queda en el editor.

---

## 7. Lo que SÍ se puede editorializar visualmente

- Bajar el tamaño de fuente del stat grande para que el decimal exacto quepa (NUNCA redondear el dato).
- Acortar la conclusión del hallazgo si no cabe en 2 líneas (NUNCA extender).
- Ajustar el split plain/italic del headline para que la línea quiebre bonita (sin cambiar palabras).
- Bold selectivo en una palabra clave dentro de la descripción de stat.
- Decidir qué 3 stats narrativos extraer de la tabla del cruce (criterio editorial — ver Fase 4 del workflow).

Nada más.

---

## 8. Checklist final antes de entregar deck

- [ ] 40 slides exactos (5 tensiones × 8) o el número correcto si es deck parcial
- [ ] Los 5 slides intro dicen solo "TENSIÓN 0X" (sin "· PILAR")
- [ ] Ningún slide tiene labels guía "/ HALLAZGO ·" / "/ CRUCE ·"
- [ ] Los 5 slides Hallazgo tienen 3 stats con cifra **exacta** del hallazgo editado (decimal exacto en TODAS las cifras, sin redondear)
- [ ] Los 5 slides Cruce tienen 3 stats narrativos reales (no placeholders) y headline en MAYÚSCULAS centrado auto-tamaño
- [ ] Los 5 slides Conv. Digital tienen verbatims en BLANCO
- [ ] Kerning 0 en todo el deck
- [ ] Slides Caso Referencia tienen placeholder de imagen (lo llena cuenta)
- [ ] Sources en formato estándar
- [ ] PDF generado y revisado slide por slide
- [ ] Grid de thumbnails generado (opcional pero útil)

Si algún punto falla, no entregues — corrige primero.

---

## 9. Tono operativo del reporte de cierre

Sobrio, técnico, ejecutivo. Cuando termines, entregas:

1. El `.pptx` final
2. El PDF de QA
3. Reporte de cambios:
   - Slides que cambiaron significativamente
   - Slides que solo cambiaron cosméticamente
   - Slides que no se tocaron
   - Cualquier flag o limitación que el cliente deba conocer

No vendas el trabajo. Reporta los hechos.
