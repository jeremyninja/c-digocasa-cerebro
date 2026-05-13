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
| Hallazgo cuanti + 1 verbatim | **2 slides:** Slide A Hallazgo cuanti + Slide B Consumer Voice (1 verbatim en card). |
| Hallazgo solo cualitativo (sin cifra publicable, 1-3 verbatims) | **1 slide:** Card cualitativa (headline + 1-3 verbatims en cards estilo gris carbón dentro del mismo slide). |
| Hallazgo cuanti + cuali integrado | **1 slide:** stat grande + 1-2 cards de verbatim en el mismo slide (caso especial, solo si el editor lo entregó así). |

**Reglas operativas del formato flat (corregidas):**

1. **Consumer Voice = APOYO al cuanti, no narrativa expandida.** El slide Consumer Voice existe para **fortalecer el hallazgo cuantitativo del slide anterior** con UNA voz que literalice el dato. **1 verbatim por slide Consumer Voice — uno solo, el que mejor apoye al cuanti.** No 2, no 3. Si el set editorial entrega 2 verbatims para un hallazgo cuanti, el editor debe escoger cuál apoya mejor al stat y descartar el otro (o reservarlo para otro entregable). **Esto es decisión del editor, no del montador.**

2. **Múltiples verbatims (2-3) en un mismo slide = SOLO en dos casos:**
   - **Hallazgo solo-cuali** (sin stat publicable) — los 2-3 verbatims apilados como cards gris carbón dentro de un slide único con headline arriba.
   - **Hallazgo cuanti + cuali integrado en el mismo slide** — caso especial donde el stat grande y las quotes coexisten en el mismo slide porque el editor lo entregó así.

   **Nunca apilar 2 verbatims en un slide Consumer Voice tradicional** (slide que apoya un hallazgo cuanti de slide anterior). Esa fue una sobre-corrección de versiones previas.

3. **Data cualitativa = cards translúcidas negras** en todos los casos. Ya sea Consumer Voice (1 verbatim), card cualitativa pura (1-3 verbatims) o cuanti+cuali integrado — siempre el verbatim va en card con fill `rgba(0, 0, 0, 0.45)` (negro con opacidad 45%, NO `#2E2E2E` sólido) y border-radius 24px. Specs completas en sección 3.9. **Nunca verbatim flotando sobre fondo negro como texto centrado en grande sin card.**

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

## 3.9. CSS / decisiones de diseño NO NEGOCIABLES — specs en px (feedback Jeremy mayo 2026 — v3 con referencias visuales)

Estas reglas vienen de feedback EXPLÍCITO de Jeremy con referencias visuales y dimensiones medidas en Keynote. **Reemplazan TODA versión anterior.** Aplican a cualquier deck Código Casa formato flat.

**TODOS los tamaños están en píxeles asumiendo slide 1920×1080 px (Full HD widescreen).** No interpretes, no escales, no decidas. Aplica las dimensiones literales. Si algo no cabe, regresa al editor — no improvises.

### Configuración del slide

```css
.slide {
  width: 1920px;
  height: 1080px;
  background: #000000;           /* fondo negro plano — sin masterslide */
  font-family: 'Instrument Serif', 'Poppins';
  letter-spacing: 0;              /* kerning 0 en TODO el deck */
}
```

**python-pptx equivalente:**
```python
from pptx.util import Emu
# 1920px @ 96 dpi = 20 inches = 18,288,000 EMU
# 1080px @ 96 dpi = 11.25 inches = 10,287,000 EMU
prs.slide_width = Emu(18_288_000)
prs.slide_height = Emu(10_287_000)
# 1px = 9525 EMU @ 96 dpi
```

### CAJAS DE STAT (cifra grande + descripción)

```css
.stat-box {
  width: 822px;
  height: 238px;
  /* contenido: cifra grande + descripción debajo */
}

.stat-number {
  font-family: 'Instrument Serif';
  font-style: italic;
  font-weight: 400;
  font-size: 180px;             /* cifra dominante visualmente */
  color: #FFFFFF;
  text-align: center;
  /* enteros por defecto: 47.8% → 48%, 3.0% → 3%, 85.0% → 85% */
  /* decimal solo si: 1 dígito antes (8.7%, 5.5%) o brecha significativa (15.2pts) */
}

.stat-description {
  font-family: 'Poppins';
  font-weight: 400;
  font-size: 22px;
  line-height: 1.4;
  color: #FFFFFF;
  text-align: center;
  margin-top: 20px;
  /* bold selectivo en palabra clave (variable demográfica, concepto, cita) */
}

.stat-description strong {
  font-weight: 700;
}
```

### CARDS DE VERBATIM — fill negro opacidad 45% (CRÍTICO)

```css
.verbatim-card {
  background: rgba(0, 0, 0, 0.45);   /* NEGRO con 45% opacidad — NO #2E2E2E */
  border-radius: 24px;
  padding: 80px 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
```

**python-pptx equivalente para el fill translúcido (CRÍTICO — no usar #2E2E2E sólido):**
```python
from pptx.dml.color import RGBColor
from lxml import etree

shape.fill.solid()
shape.fill.fore_color.rgb = RGBColor(0x00, 0x00, 0x00)

# Aplicar opacidad 45% vía XML directo:
sp = shape.fill._xPr  # solid fill xml properties
nsmap = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
srgbClr = sp.find('.//a:srgbClr', nsmap)
alpha = etree.SubElement(srgbClr, '{http://schemas.openxmlformats.org/drawingml/2006/main}alpha')
alpha.set('val', '45000')  # 45000 = 45% en notación PPTX (de 0 a 100000)
```

**Border-radius (esquinas redondeadas) en python-pptx:**
```python
from pptx.shapes.autoshape import Shape
from pptx.enum.shapes import MSO_SHAPE
# Usar autoshape ROUNDED_RECTANGLE en lugar de RECTANGLE
shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
# Ajustar el adjustment del corner radius (default ~0.16):
shape.adjustments[0] = 0.10  # ~10% del lado más corto → border-radius ~24-32px
```

### VERBATIM dentro de la card

```css
.verbatim-text {
  font-family: 'Instrument Serif';
  font-weight: 400;
  font-style: normal;            /* NO italic */
  font-size: 50px;               /* texto grande para que respire */
  line-height: 1.3;
  color: #FFFFFF;
  text-align: center;
  /* comillas españolas angulares «...» — NO comillas curvas inglesas */
}

.verbatim-attribution {
  font-family: 'Poppins';
  font-style: italic;            /* atribución sí italic */
  font-weight: 400;
  font-size: 22px;
  color: #FFFFFF;
  text-align: center;
  margin-top: 30px;
  /* formato: "— Familia [tipología]" */
}
```

### HEADLINE (slide Hallazgo cuanti / Card cualitativa)

```css
.headline {
  position: absolute;
  top: 100px;
  left: 100px;
  width: 1720px;                  /* 1920 - 100*2 */
  
  font-family: 'Instrument Serif';
  font-weight: 400;
  text-align: center;
  text-transform: uppercase;
  color: #FFFFFF;
  letter-spacing: 0;
  line-height: 1.1;
  
  /* AUTO-SIZE según largo del texto: */
  /* ≤30 chars  → font-size: 110px */
  /* 31-44      → font-size: 88px */
  /* 45-65      → font-size: 64px */
  /* 66-85      → font-size: 52px */
  /* >85        → font-size: 42px */
}

.headline em {
  font-style: italic;             /* solo en frase del giro */
}
```

### SOURCE pie de página

```css
.source {
  position: absolute;
  bottom: 60px;
  left: 0;
  right: 0;
  
  font-family: 'Poppins';
  font-style: italic;
  font-size: 16px;
  color: #9B9B9B;                 /* gris claro, no blanco puro */
  text-align: center;
  /* formato: "Source: Código Casa — Estudio cuantitativo 2025 · P##, P## · Base 500." */
  /* UNA línea cubre TODAS las preguntas del slide */
}
```

### LAYOUTS POR TIPO DE SLIDE

#### Layout 1 — Slide Hallazgo cuanti con 1 stat

```
+----------------------------------------------+
|                                              |
|      [HEADLINE AUTO-SIZE, 1720px wide]      | <- top 100px
|                                              |
|                                              |
|          [STAT BOX 822x238 centered]         | <- top 500px, left (1920-822)/2 = 549px
|             cifra 180px                      |
|             descripción 22px                 |
|                                              |
|                                              |
|             [Source 16px]                    | <- bottom 60px
+----------------------------------------------+
```

#### Layout 2 — Slide Hallazgo cuanti con 2 stats

```
+----------------------------------------------+
|      [HEADLINE]                              |
|                                              |
|   [STAT 1]   │   [STAT 2]                    |
|   822x238    │   822x238                     | <- línea vertical #2E2E2E 1px entre los dos
|                                              |
|              [Source]                        |
+----------------------------------------------+

Posiciones:
- Stat 1: left 80px,  top 500px, width 822, height 238
- Línea separadora: left 945px, top 520px, width 1px, height 200, background #2E2E2E
- Stat 2: left 1018px, top 500px, width 822, height 238
```

NOTA: con 2 stats de 822px cada uno + margen, no caben los 2 enteros (822×2 + márgenes > 1920). En ese caso reduce las cajas proporcionalmente a `width: 880px` cada una (en lugar de 822) y centra el conjunto. O cambia a 700×238 para que entren ambas con respiro. El stat number se queda en 180px; solo la caja se ajusta. **Tamaño de cifra NUNCA cambia.**

#### Layout 3 — Slide Hallazgo cuanti con 3 stats

```
+----------------------------------------------+
|      [HEADLINE]                              |
|                                              |
| [STAT 1] │ [STAT 2] │ [STAT 3]              |
| ~560x238 │ ~560x238 │ ~560x238              | <- líneas verticales entre cada par
|                                              |
|              [Source]                        |
+----------------------------------------------+

Posiciones aproximadas:
- Stat 1: left 80px,  top 500px, width 560, height 238
- Separador 1: left 651px, top 520px, width 1, height 200
- Stat 2: left 680px, top 500px, width 560, height 238
- Separador 2: left 1251px, top 520px, width 1, height 200
- Stat 3: left 1280px, top 500px, width 560, height 238

NOTA: con 3 stats no caben de 822px cada uno. Se reducen a ~560×238. El stat number se queda en 180px (puede bajarse a 160px si el dato es de 4 chars como "12.8%").
```

#### Layout 4 — Slide Consumer Voice (apoya cuanti anterior — 1 verbatim solo)

```
+----------------------------------------------+
|                                              |
|              CONSUMER VOICE                  | <- top 80px, Poppins 16px gris #9B9B9B
|                                              |
|                                              |
|   ┌────────────────────────────────────┐    |
|   │                                      │    |
|   │      « Verbatim 50px Instrument     │    |
|   │        Serif regular blanco. »       │    |
|   │                                      │    | <- card 1637×485 px
|   │      — Familia [tipología]           │    |    fill rgba(0,0,0,0.45)
|   │                                      │    |    border-radius 24px
|   └────────────────────────────────────┘    |
|                                              |
|              [Source]                        |
+----------------------------------------------+

Posición de la card:
- left: (1920 - 1637) / 2 = 141px (centrada horizontalmente)
- top: 220px (debajo del header CONSUMER VOICE)
- width: 1637px
- height: 485px
```

#### Layout 5 — Slide Card cualitativa (solo-cuali — 1-3 verbatims apilados)

```
+----------------------------------------------+
|      [HEADLINE AUTO-SIZE]                    |
|                                              |
|   ┌────────────────────────────────────┐    |
|   │      « Verbatim 1 »                  │    |
|   │      — Familia [tipología]           │    | <- card 1 (1637×290 si hay 2-3 stacked)
|   └────────────────────────────────────┘    |
|                                              |
|   ┌────────────────────────────────────┐    |
|   │      « Verbatim 2 »                  │    | <- card 2
|   │      — Familia [otra tipología]      │    |
|   └────────────────────────────────────┘    |
|                                              |
|              [Source si aplica]              |
+----------------------------------------------+

Si hay 1 solo verbatim → 1 card de 1637×485 centrada (como Consumer Voice pero con headline arriba).
Si hay 2 verbatims → 2 cards de 1637×290 apiladas con 30px de gap entre cada una.
Si hay 3 verbatims → 3 cards de 1637×200 apiladas con 25px de gap.

Verbatim size dentro de cada card:
- 1 verbatim → 50px
- 2 verbatims → 38px
- 3 verbatims → 32px
```

#### Layout 6 — Slide cuali+cuanti integrado (1 stat + 1 verbatim en mismo slide)

**Caso especial: cuando un hallazgo tiene exactamente 1 stat + 1 verbatim y el editor decidió integrar.** Reduce el deck (1 slide en lugar de 2). Se ve como el slide de Conversación Digital pero adaptado.

```
+----------------------------------------------+
|      [HEADLINE AUTO-SIZE]                    |
|                                              |
|                                              |
|              ┌────────────────────────┐     |
|   [STAT]     │  « Verbatim »            │     |
|   822x480    │  — Familia [tipología]   │     | <- card 1100×480
|   margen     │                          │     |
|   centrado   └────────────────────────┘     |
|              │                                |
|              línea vertical #2E2E2E 1px        |
|                                              |
|              [Source]                        |
+----------------------------------------------+

Posiciones:
- Headline: top 80px, full width
- Stat box: left 80px, top 380px, width 560, height 480
- Línea vertical: left 680px, top 400px, width 1, height 440, background #2E2E2E
- Verbatim card: left 720px, top 380px, width 1100, height 480
  fill rgba(0,0,0,0.45), border-radius 24px
  Verbatim text 38-42px (más pequeño que en Consumer Voice puro porque la card es más estrecha)

Cuándo usar este layout vs Layout 1+4 separados:
- USAR layout 6 cuando: hallazgo tiene 1 solo stat + 1 verbatim, el editor lo entrega como bloque integrado, o cuando se quiere reducir conteo de slides.
- USAR layouts 1+4 separados cuando: hallazgo tiene 2 o 3 stats (no caben en mitad del slide).
```

### REGLAS GLOBALES (no negociables)

1. **Slide: 1920×1080 px.** Configurar el deck a este tamaño al inicio.
2. **Fondo negro plano `#000000`.** Sin masterslide decorativo. Jeremy aplica halos arcoíris, headers, logo, textura después.
3. **Cards: SIEMPRE `rgba(0, 0, 0, 0.45)` con border-radius 24px.** NO `#2E2E2E` sólido. NO opacidad 100%. NO sin border-radius.
4. **Verbatims: Instrument Serif regular (NO italic) con comillas españolas `«...»`.**
5. **Atribuciones: "— Familia [tipología]" en italic Poppins 22px.**
6. **Stats: redondeo a entero por defecto.** Decimal solo si 1 dígito antes (8.7%, 5.5%) o brecha (15.2 pts).
7. **NO cajas de "Pregunta P##. Base. Fuente" debajo de stats.** Solo cifra + descripción Poppins con bold. Metadata vive en Source pie.
8. **Kerning 0 en TODO el deck.** `letter-spacing: 0`.
9. **Sin elementos decorativos.** Solo líneas verticales `#2E2E2E` 1px entre stats. Nada más.
10. **Si algo no cabe en las dimensiones literales, regresar al editor.** NO improvisar el tamaño de cifras ni textos.

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

### Slide de Consumer Voice (1 verbatim que apoya el hallazgo cuanti anterior)

**Función del slide Consumer Voice:** apoyar y fortalecer el hallazgo cuantitativo del slide anterior con UNA voz que literalice el dato. No es para expandir narrativa ni para acumular quotes. Si el set editorial entrega 2 verbatims para un hallazgo cuanti, el editor debe escoger cuál apoya mejor al stat — el montador NO decide.

**Layout canónico (UNA sola card centrada):**

```
                     [CONSUMER VOICE]
              (header arriba, Poppins 10pt, gris suave)


       ┌──────────────────────────────────────────────┐
       │                                                │
       │                                                │
       │   « Verbatim grande en Instrument Serif       │
       │     regular blanco, comillas españolas. »      │
       │                                                │
       │                                                │
       │              — Familia [tipología]             │
       │                  (italic)                      │
       │                                                │
       └──────────────────────────────────────────────┘
```

**Especificaciones:**

**Esta sección es DESCRIPTIVA. Las specs canónicas en px están en la sección 3.9 (CSS / decisiones de diseño no negociables). Si hay conflicto entre esta sección y 3.9, manda 3.9.**

- **1 card centrada vertical y horizontalmente en el slide.** No múltiples cards apiladas en Consumer Voice. Solo una.
- **Header arriba:** texto `CONSUMER VOICE` en Poppins regular, mayúsculas, centrado horizontalmente, color gris suave `#9B9B9B`. Ver 3.9 para tamaño exacto en px.
- **Card del verbatim:** rectángulo con fill `rgba(0, 0, 0, 0.45)` (negro con opacidad 45%, NO `#2E2E2E` sólido), border-radius 24px, dimensiones 1637×485 px (ver 3.9).
- **Verbatim dentro de la card:**
  - **Instrument Serif regular** (NO italic), 50px (ver 3.9).
  - Color blanco `#FFFFFF`.
  - **Comillas españolas angulares `«...»`**, NO comillas curvas inglesas `"..."`.
  - Alineación centrada horizontalmente.
- **Atribución:** Poppins italic 22px, blanco, centrada debajo del verbatim dentro de la misma card. Formato: `— Familia [tipología]`.
- **Si el editor entrega 2 verbatims para un hallazgo cuanti** → regresa al editor para que escoja cuál apoya mejor el stat. Nunca apiles los 2 en un Consumer Voice. La regla de "múltiples verbatims apilados" aplica SOLO a slides solo-cuali (sin stat) — ver siguiente sección.

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
