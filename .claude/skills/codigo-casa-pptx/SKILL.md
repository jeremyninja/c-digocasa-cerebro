---
name: codigo-casa-pptx
description: Sistema completo para generar presentaciones PPTX de Código Casa / Ninja Thinking. Mapea contenido textual a slides con la línea gráfica exacta del estudio. Usa python-pptx + assets visuales reales.
type: skill
trigger: Cuando el usuario pida crear slides, presentaciones o montar capítulos de Código Casa en PPTX
---

# Código Casa PPTX — Sistema de Presentaciones

> Skill operativo para generar presentaciones .pptx que replican la línea gráfica de Código Casa / Ninja Thinking. El usuario da texto + información, este skill define la estructura y genera el archivo.

---

## REGLAS CRÍTICAS

1. **NUNCA proceder solo si no puedes replicar un gráfico.** Si un gráfico requiere capacidades que python-pptx no tiene (gradientes complejos, efectos especiales), DETENTE y ofrece alternativas.
2. **Siempre ofrecer caminos alternativos** cuando hay limitación técnica.
3. **Mantener estructuras idénticas** entre slides del mismo tipo. La repetición es ley.
4. **Títulos SIEMPRE en Instrument Serif.** Sin excepción.
5. **Las portadas de capítulo las pone Jeremy a mano.** No generarlas automáticamente.
6. **Los masterslides con texturas son imágenes de fondo reales**, no colores sólidos.

---

## INVENTARIO DE ASSETS

### Ubicación Base
```
/Users/jeremyrodriguez/Downloads/Código Casa/Gráfica/
```

### Tipografías
| Fuente | Uso | Archivo | Pesos |
|--------|-----|---------|-------|
| **Instrument Serif** | Títulos, headlines, tensiones | `Instrument_Serif/InstrumentSerif-Regular.ttf` | Regular, Italic |
| **Poppins** | Body text, datos, cuadros de texto | Sistema (Google Font) | Light, Regular, Medium, SemiBold, Bold |

### Texturas de Fondo (Dust/Grain)
Para slides de **contenido/desarrollo** — fondo negro con textura film grain:
```
Dust texture/01.png    Dust texture/06.png
Dust texture/02.png    Dust texture/09.png
Dust texture/03.png    Dust texture/010.png
Dust texture/04.png    Dust texture/011.png
Dust texture/05.png    Dust texture/012.png
```
**Uso:** Se aplica como imagen de fondo full-bleed en slides de contenido. Todas son texturas oscuras con partículas de polvo/grano estilo film vintage.

### Texturas de Color (Conectores/Transiciones)
Para slides que **dividen temas e introducen tensiones**:
```
Color textures/542f0792-23cb-4d1c-a261-7e9a0a69ad00.jpg   (grainy gradient)
Color textures/750506b6-ece0-4505-95c5-7dbf41d18c57.jpg
Color textures/785bf498-7f65-4c41-a187-69beabad83d6.jpg
Color textures/7f445da4-31bb-466c-8ca8-b5be32971dd2.jpg
Color textures/9e7d60b0-36c1-4f84-a35d-7c74423f6e50.jpg
Color textures/abstract-gradient-background-with-grainy-effect.jpg  (rosa/teal)
Color textures/c3c2c966-f12d-40b9-9f87-dff183477a5a.jpg
Color textures/d55b6eb1-83e4-4079-bf28-9334b65a48d1.jpg
Color textures/e75f55c9-8d19-4401-a6f9-8a5a54bd294b.jpg
```

### Gradientes Holográficos (Conectores especiales)
Para slides de **transición de alto impacto**:
```
Gradients finales/DESIGN-SYNDROME-HOLOGRAPHIX-TEXTURE-GENERATOR-V2*.jpg
```
31 variantes — texturas oscuras con esferas/luces holográficas neón.

### Upper Bar (Barra Superior)
```
Upper bar.png  (96KB — barra horizontal delgada, gradiente rainbow holográfico con grain)
```
**Uso:** Va en la parte SUPERIOR de TODOS los slides de contenido. Es la firma visual de la presentación.

### Logos y Emojis
```
Emojis + logos/mask white ninja.png    → Máscara ninja blanca (para fondos oscuros)
Emojis + logos/icon.png                → Máscara ninja negra (para fondos claros)
Emojis + logos/ninja white.png         → Logo ninja completo blanco
Emojis + logos/ninja black.png         → Logo ninja completo negro
Emojis + logos/data.png                → Emoji data
Emojis + logos/dominican.png           → Emoji bandera dominicana
Emojis + logos/eyes.png                → Emoji ojos
Emojis + logos/fire.png                → Emoji fuego
Emojis + logos/heart.png               → Emoji corazón
Emojis + logos/message.png             → Emoji mensaje
Emojis + logos/reach.png               → Emoji alcance
Emojis + logos/shopcar.png             → Emoji carrito de compras
Emojis + logos/warning.png             → Emoji advertencia
```

### Logos Principales
```
Ninja logo blanco.png   (326KB — logo Ninja completo, fondo transparente, blanco)
Ninja logo negro.png    (251KB — logo Ninja completo, fondo transparente, negro)
Logo Final/             (carpeta con versiones editables)
```

### Branding Reference
```
Branding Código Casa.pdf  (127KB — guía de branding)
```

---

## FORMATO ESTÁNDAR (SPECS EXACTAS v3 — UI pulido)

### Principios UI
- **Respiración mín 4cm** entre bloques de composición
- **Simple balance, contraste, centralización** en todas las composiciones
- **Títulos de slides de contenido: 30pt centrados** (data highlight, social listening, verdades, oportunidades, caso, kit)
- **Connectors: 45pt centrados** (excepción documentada)
- **Trends: 20pt** (excepción documentada — ver sección Trends)
- **Headers 7pt** (ambos lados)

### MANDATO OFICIAL — Connectors (slides de transición)

- **Fondo:** `Gradients finales/DESIGN-SYNDROME-HOLOGRAPHIX-TEXTURE-GENERATOR-V2-23.jpg` full-bleed
- **Firmas arriba (SÍ se aplican):** header de 2 lados a 7pt Poppins blanco, misma spec que content slides
- **NO llevan:** upper bar rainbow, máscara en esquina
- **Text box headline:** **width 25cm × height 8cm**, centrado horizontalmente en el slide
- **Headline:** Instrument Serif Regular + Italic mix, **45pt centrado**
- **Máscara CC:** centrada bottom, ratio 1.17:1

### REGLA GLOBAL — COLOR DE ACENTO

🚫 **PROHIBIDO usar verde lima / verde neón** (`#B8FF4A` o similares)
✅ **Color de acento único: BLANCO** (`#FFFFFF`)

Todos los labels, números decorativos, dots, flechas, bordes de frames, dividers, pills — **siempre blanco**. El color viene del fondo (dust texture, gradientes de connectors) y del contraste blanco sobre negro. No se introducen colores de marca adicionales.

### REGLA GLOBAL — TÍTULOS POR SECCIÓN

Los títulos NO son uniformes en toda la presentación. Cada sección tiene su tamaño correcto:

| Sección | Tamaño | Fuente | Notas |
|---------|--------|--------|-------|
| Slides de contenido (data, verdades, oportunidades, caso, kit) | **30pt** | Instrument Serif | Base estándar |
| Connectors / transición | **45pt** | Instrument Serif Regular+Italic mix | Excepción documentada |
| Trends Development — headline col 1 | **20pt** | Poppins Bold UPPERCASE | Excepción documentada (layout denso 3col) |
| Números hero en data highlight | **90pt** (3col) / **110pt** (2col) | Instrument Serif **Italic** | No son títulos, son datos |
| Números en trends col 2 | **48pt** | Instrument Serif **Italic** | Stats de tendencias |
| Números en Espacios Vacíos | **48pt** | Instrument Serif **Italic** | Cards territorios |

### ROUNDED EDGES — Estándar Único

- **Cards, contenedores, rectángulos:** `adjustments[0] = 0.08`
- **Pills** (labels bordeados): `adjustments[0] = 0.5` (max rounded, son pequeños)
- **Nunca mezclar valores distintos** en un mismo slide para cards

### MANDATO OFICIAL — Trends Development ("Trend en un Headline")

Layout **3 columnas verticales** — narrativa + stats + proof placeholder. Cada macro tendencia = 1 slide.

**Chrome estándar:** dust 15% + upper bar + firmas 7pt + máscara bottom-right (igual que slides de contenido).

---

**Columna 1 — Narrativa** (x: 1.5cm → 10.5cm, width: 9cm)

- **Headline:** Poppins Bold **20pt** UPPERCASE blanco, 2 líneas word-wrap (y=3cm, height=2.5cm)
  - Ejemplo: "UN MUNDO EN CRISIS ESTÁ REESCRIBIENDO QUÉ SIGNIFICA SER ADULTO"
- **Gap 1.5cm** vacío
- **3 bloques narrativa** stacked (y=7cm → 16.5cm), cada uno ~3cm altura:
  - Label italic 11pt gris claro: `The context` / `The contrast` / `The transformation`
  - Gap interno 0.3cm
  - Paragraph Poppins Regular **9pt** blanco, 3-4 líneas
  - Gap vertical entre bloques: 0.5cm

**Columna 2 — Stats** (x: 12cm → 21cm, width: 9cm)

- **3 stats stacked** (y=3cm → 16.5cm). Por stat:
  - Número Instrument Serif Italic **48pt** blanco, LEFT aligned
  - Height box: 1.9cm (fórmula pt × 0.039)
  - Gap interno 0.6cm
  - Descripción Poppins Regular **9pt** blanco, 3-4 líneas (height ~1.7cm)
- Gap vertical entre stats: 0.8cm

**Columna 3 — The Proof** (x: 22.5cm → 33cm, width: 10.5cm)

- Card contenedor: y=2.5cm, height=13cm
- `ROUNDED_RECTANGLE` con `adjustments[0]=0.08`
- Fill `#1A1A1A`, border `#333` 1pt
- Label "The proof" top-left interior (+0.6cm, +0.6cm): Poppins Regular 12pt blanco
- Interior reservado para gráfico / imagen / screenshot de TikTok / prueba visual

**Footer (específico de trends):**
- **Source:** `Source: Trends Hunting — Código Casa 2026 | Ninja Thinking`
- Italic 8pt gris claro, bottom-left (y≈17.5cm)
- **NUNCA** usar el source del estudio cuantitativo/cualitativo en trends (estos usan fuente propia de trend hunting)
- Máscara CC bottom-right (estándar)

---

### EXCEPCIONES TIPOGRÁFICAS EN TRENDS

Estas tallas son **excepciones documentadas** al estándar global:

| Elemento | Estándar global | Trends |
|----------|-----------------|--------|
| Título/Headline | 30pt | **20pt** |
| Body / análisis / descripción | 11-14pt | **9pt** |

**Razón:** Los slides de trends cargan 3 bloques narrativos + 3 stats + proof card en una sola vista. El layout denso requiere tipografía más compacta para mantener respiración y jerarquía. El headline 20pt es suficiente porque vive en columna estrecha de 9cm — visualmente compite bien con los números serif 48pt de la columna 2.

### MANDATO OFICIAL — Espacios Vacíos (12 territorios en 4 slides)

Cada slide: **3 cards horizontales**, total 12 cards.

**Título (y=2cm, 30pt centrado):**
- "ESPACIOS VACÍOS" (Poppins Bold + Instrument Serif Italic mix)
- Subtítulo (y=3.7cm): "Que ninguna marca está habitando — N/4" Poppins Italic 12pt gris

**Cards (y=5.5cm, height=9.5cm):**
- Margen lateral slide: 3cm cada lado
- Gap entre cards: 0.8cm
- Ancho card: `(SLIDE_W - 6cm - 1.6cm) / 3` ≈ 8.9cm
- Rounded 0.08, fill `#1A1A1A`, border `#2A2A2A`

**Contenido card:**
- Número Instrument Serif Italic 48pt blanco (y=+0.8cm)
- Separador fino 1.5cm × 0.03cm gris `#666` (y=+3.3cm)
- Título UPPERCASE Poppins Bold 13pt blanco (y=+3.8cm)
- Descripción Poppins Regular 10pt gris claro (y=+5.8cm)

### MANDATO OFICIAL — Caso Referencia

Layout **2 columnas** con foto izquierda + texto derecha:

```
[header chrome]

              CASO REFERENCIA  (label blanco 10pt bold centrado)

  ┌──────────────────────┐   Headline italic 30pt (Instrument Serif)
  │                      │   "Frase hook del caso."
  │                      │
  │   [FOTO DEL CASO]    │   MARCA · FECHA (9pt gris bold)
  │   frame con dashed   │
  │   border gris        │   Descripción del caso en Poppins 13pt blanco
  │                      │   (párrafo de 3-5 líneas)
  │                      │
  │                      │
  └──────────────────────┘

                                                  Source: Ninja Thinking
```

**Specs:**
- Margen lateral: 3cm cada lado
- Gap entre columnas: 1.2cm
- Ancho columna: `(SLIDE_W - 3cm*2 - 1.2cm) / 2` ≈ 13.7cm
- Altura columna: ~11cm (y=3.5 a 14.5cm)
- Frame foto: `ROUNDED_RECTANGLE` con `adjustments[0] = 0.08`, borde `#333333` dashed 1pt, fill `#1A1A1A`
- Placeholder text centrado en frame: "[ INSERTAR FOTO DEL CASO ]" 11pt gris bold
- Divider blanco: rectángulo 3cm × 0.03cm
- Headline texto: Instrument Serif Italic 24pt, LEFT aligned
- Brand label: Poppins Bold 9pt gris, UPPERCASE
- Descripción: Poppins Regular 13pt blanco

### MANDATO OFICIAL — Framework Toolkit de Marca (Kit de Respuesta)

Layout vertical con flujo **entrada → proceso → salida**:

```
[header chrome]

              TÍTULO "KIT DE RESPUESTA"  (30pt centrado, mix Regular+Italic)
              Subtítulo italic pequeño

  ┌────────────────────────────────────────────┐
  │              SITUACIÓN                     │  ← banda horizontal full-width (con 4cm margin)
  │   Desde la tensión identificada...         │
  └────────────────────────────────────────────┘
                        ↓ (flecha blanca)
  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │   01     │  │   02     │  │   03     │       ← 3 ingredientes en cards
  │  LABEL   │  │  LABEL   │  │  LABEL   │
  │  desc    │  │  desc    │  │  desc    │
  └──────────┘  └──────────┘  └──────────┘
                        ↓
  ┌────────────────────────────────────────────┐
  │       NUEVA NARRATIVA DE MARCA             │  ← output banda
  │  [Tu marca] quiere [rol] pero sabe que     │
  │  [oportunidad] por eso [transformación]    │
  └────────────────────────────────────────────┘

[source bottom]
```

**Elementos visuales:**
- Todas las cajas usan `card()` con roundness 0.08
- Banda de entrada/salida: width = SLIDE_W - 8cm (4cm margin cada lado)
- 3 cards ingredientes: ~8.5cm width cada uno, gap 0.6cm
- Flechas "↓" en blanco, 18pt, centradas
- Números 01/02/03 en Instrument Serif Italic 32pt blanco
- Labels en Poppins Bold 10pt blanco
- Descripciones en Poppins Regular 9pt gris claro
- Fórmula final: variables `[ ]` en Instrument Serif Italic 16pt blanco, conectores en Poppins Regular 13pt gris

### MANDATO OFICIAL — Estadísticas (número + contexto)

**NÚMERO**
- Fuente: Instrument Serif Italic
- Tamaño: **90pt** (3 columnas) / **110pt** (2 columnas)
- Color: `#FFFFFF`
- Box height: **3.5cm** (3 col, 90pt) / **4.3cm** (2 col, 110pt)
- Alineación: centrada horizontal, vertical **TOP** (anchor)
- Width: ancho completo de la columna

⚠️ **NOTA TÉCNICA — Aire muerto con anchor=TOP**
Con `anchor=TOP`, el glyph arranca en el borde superior del box, pero el box típicamente se dimensiona más alto que el glyph real. Ese espacio vacío entre el bottom del glyph y el bottom del box se traduce en padding invisible que empuja el texto de contexto hacia abajo, creando la sensación de "gap demasiado grande" incluso cuando el gap definido es correcto (0.85cm).

**Regla:** el `num_h` debe aproximarse al alto real del glyph, no al alto teórico del box. Fórmula empírica con Instrument Serif Italic:
- `num_h ≈ pt_size × 0.039 cm` (factor derivado de ~3.5cm para 90pt y ~4.3cm para 110pt)
- Para otros tamaños: 60pt → 2.3cm, 72pt → 2.8cm, 130pt → 5.1cm

**GAP**
- Separación vertical número → caja de texto: **0.85cm**
- Height vacío, sin contenido

**CAJA DE TEXTO (contexto)**
- Width: **7cm**
- Height: **4cm**
- Centrada horizontalmente dentro de la columna
- Fuente: Poppins Regular
- Tamaño: **10pt** (3 col) / **11pt** (2 col)
- Color: `#FFFFFF`
- Alineación: centrada
- Word wrap: ON
- Márgenes internos: 0

**LÍNEA SEPARADORA (entre números)**
- Altura: **5cm**
- Width: ~0.02cm (visual ≈ 0.5pt)
- Color: `#999999`
- Posición: centrada verticalmente sobre el bloque del número
- Entre cada par de columnas

### Máscara CC (aspect ratio crítico)
- Ratio: **1.17:1** (width:height) — NO distorsionar
- Bottom-right: height 1.0cm, width 1.17cm, margen 0.80cm
- Center-bottom (connectors): height 1.2cm, width 1.40cm

### Dust texture
- Opacidad **15%** (NO 85%) — textura sutil apenas perceptible
- Sobre fondo negro puro #000000

---


- **Dimensiones:** 16:9 (33.867cm x 19.05cm / 13.333in x 7.5in)
- **Márgenes:** 0.80cm desde bordes para elementos de chrome (header/footer/máscara)

### HEADER (todos los slides de desarrollo, NO connectors)
- **Posición vertical:** 0.85cm debajo del top bar (gradient rainbow queda en el top 0-~0.3cm)
- **Lado izquierdo:** `CÓDIGO CASA® - [NOMBRE CAPITULO]`
  - Ej: `CÓDIGO CASA® - BOOKLET`, `CÓDIGO CASA® - FAMILIA E IDENTIDAD`
- **Lado derecho:** `NINJA THINKING`
- **Estilo ambos:** 7pt, Poppins Regular, UPPERCASE, color blanco
- **Separación de bordes:** 0.80cm desde izq y der

### FONDO
- **Slides de desarrollo:** `Dust texture/04.png` con opacidad 15% sobre fondo negro `#000000`
  - Ruta: `/Users/jeremyrodriguez/Downloads/Código Casa/Gráfica/Dust texture/04.png`
- **Connectors de tensiones:** `Gradients finales/DESIGN-SYNDROME-HOLOGRAPHIX-TEXTURE-GENERATOR-V2-23.jpg`
  - Full-bleed, sin dust texture, sin top bar, sin header

### TOP BAR (gradient rainbow)
- Va en slides de desarrollo, **NO** en connectors
- Imagen: `Upper bar.png` full-width en y=0

### FOOTER
- **Máscara CC:** bottom-right, 0.80cm de ambos bordes (inferior y derecho)
  - Ruta: `/Users/jeremyrodriguez/Downloads/Código Casa/Gráfica/Logo Final/Mascara CC.png`
  - Tamaño: ~0.9-1.0cm de alto
- **Source line:** bottom-left, Poppins Regular 7pt, color gris claro con baja opacidad

### TIPOGRAFÍA — REGLA CLAVE ACTUALIZADA
- **Números hero (48%, 89%, 38%, 258, 1.3M):** Instrument Serif **Italic**, NO Poppins Bold
  - Tamaños: 96-120pt para números grandes
- **Títulos con énfasis mixto:** Combinar Instrument Serif Regular + Italic en misma línea
  - Ej: `PARA EL DOMINICANO LA CRIANZA ES *COLECTIVA*, NO NUCLEAR`
  - Las palabras importantes en italic funcionan como acento conceptual
- **Body text:** Poppins Regular, 11-14pt, blanco o gris claro
- **Labels/pills:** Poppins Medium/SemiBold, UPPERCASE, 10-11pt, bordered

### ELEMENTOS RECURRENTES
- **Pill label** (ej: "CONVERSACIÓN DIGITAL"): borde 1px gris, padding ~12px horizontal, rounded 20px, centrado arriba
- **Data card** (pricing, trends): rounded rectangle con borde sutil, fondo levemente más claro que el dust, padding interno generoso
- **Verbatim card**: fondo gris oscuro, green dot (●) + nombre bold + plataforma Regular + quote italic pequeño

---

## ANATOMÍA DE UN SLIDE DE CONTENIDO

Cada slide de desarrollo/contenido tiene estas capas (de abajo hacia arriba):

```
CAPA 1 (fondo):     Dust texture (imagen full-bleed, negro con grain)
CAPA 2 (barra):     Upper bar.png (barra delgada en el TOP, full width)
CAPA 3 (watermark):  Ninja mask + "/ código casa" (esquina superior, sobre la barra)
                     O bien: "CÓDIGO CASA® - [SECCIÓN] NINJA THINKING"
CAPA 4 (contenido):  Títulos, textos, datos, gráficos
CAPA 5 (source):     Línea de fuente en la parte inferior
```

### Watermark / Marca de Agua
- Posición: parte superior, generalmente alineado izquierda o sobre la upper bar
- Texto pattern: `CÓDIGO CASA® - [NOMBRE SECCIÓN] NINJA THINKING`
- Variantes por sección:
  - Booklet general: `CÓDIGO CASA® - BOOKLET NINJA THINKING`
  - Spot de tendencias: `CÓDIGO CASA® - SPOT DE TENDENCIAS`
  - Por código específico: `>/ Código Familia [Nombre]`
- Fuente: Poppins Regular, tamaño pequeño (~8-9pt), color blanco con opacidad baja

### Source / Fuente
- Posición: bottom de la slide
- Texto pattern: `Source: Código Casa: Estudio cuantitativo y cualitativo familias dominicanas 2024 | 500 personas | +70 horas de grupos focales`
- Fuente: Poppins Regular, ~7-8pt, color gris claro/blanco con baja opacidad

---

## TIPOGRAFÍA — ESCALAS POR SECCIÓN

> Las escalas son PER-SECCIÓN. No existe una escala global única. Usar la tabla de la sección que corresponde.

### Instrument Serif — Usos reales
| Sección | Elemento | Tamaño | Peso |
|---------|----------|--------|------|
| Content slides (data, verdades, kit, etc.) | Título principal | **30pt** | Regular |
| Connectors | Headline central | **45pt** | Regular + Italic mix |
| Caso referencia | Frase hook | **24pt** | Italic |
| Kit de respuesta | Números 01/02/03 | **32pt** | Italic |
| Data highlight | **Número hero** (48%, 89%, 258…) | **90pt** (3col) / **110pt** (2col) | **Italic** |
| Trends col 2 | Stats número | **48pt** | Italic |
| Espacios Vacíos | Número de territorio | **48pt** | Italic |

### Poppins — Usos reales
| Sección | Elemento | Tamaño | Peso |
|---------|----------|--------|------|
| Todos | Header firmas (izq/der) | **7pt** | Regular |
| Todos | Source line | **7-8pt** | Regular/Italic |
| Content slides | Body text / análisis | **11-14pt** | Regular |
| Trends col 1 | Headline UPPERCASE | **20pt** | Bold |
| Trends col 1 | Body análisis | **9pt** | Regular |
| Trends col 1 | Labels italic (The context…) | **11pt** | Italic |
| Trends col 3 | "The proof" label | **12pt** | Regular |
| Data highlight | Contexto bajo número | **10pt** (3col) / **11pt** (2col) | Regular |
| Cards / Espacios Vacíos | Título UPPERCASE | **13pt** | Bold |
| Cards / Espacios Vacíos | Descripción | **10pt** | Regular |
| Pill labels | Tags bordeados | **10-11pt** | Medium/SemiBold |

---

## PALETA DE COLORES

### Colores Base
| Color | Hex | Uso |
|-------|-----|-----|
| Negro fondo | `#0A0A0A` - `#111111` | Background principal (+ dust texture) |
| Blanco | `#FFFFFF` | Texto principal, títulos |
| Gris claro | `#CCCCCC` - `#999999` | Texto secundario, captions |
| Gris medio | `#666666` | Elementos terciarios |

### Colores de las texturas (solo referencia visual)
Los colores existen únicamente dentro de las texturas holográficas y gradientes — **no se aplican directamente** a texto, bordes ni elementos UI:
| Color | Rango | Dónde aparece |
|-------|-------|---------------|
| Rosa/Magenta | `#FF1493` - `#FF69B4` | Dentro de gradientes connectors |
| Cyan/Teal | `#00CED1` - `#008B8B` | Dentro de gradientes connectors |
| Amarillo | `#FFD700` - `#FFA500` | Dentro de gradientes connectors |
| Violeta | `#8A2BE2` - `#9400D3` | Dentro de gradientes holográficos |

🚫 **Verde neón (`#B8FF4A`, `#ADFF2F`) — PROHIBIDO.** No aparece en ningún elemento generado por código.

---

## CATÁLOGO DE TIPOS DE SLIDE

### TIPO 1: CHAPTER DIVIDER (Portada de Capítulo)
**Jeremy las hace a mano.** No generar automáticamente.
- Fondo: textura de color o gradiente holográfico
- Contenido: título grande + número de capítulo
- Ejemplo: "Los códigos" + "4"

### TIPO 2: CONTENT DEVELOPMENT (Desarrollo de Contenido)
**Slide estándar de contenido. El más común.**
```
┌─────────────────────────────────────────┐
│ [========= UPPER BAR ===========]       │  ← Upper bar full width
│ 🥷 / código casa - [sección]             │  ← Watermark
│                                         │
│ TÍTULO EN INSTRUMENT SERIF              │  ← 36-48pt, blanco
│                                         │
│ Párrafo de contenido en Poppins.        │  ← 14-16pt, gris claro
│ Aquí va el desarrollo del texto.        │
│                                         │
│                                         │
│ Source: Código Casa...                  │  ← 7-8pt, gris
└─────────────────────────────────────────┘
  Fondo: Dust texture (negro grain)
```

### TIPO 3: DATA HIGHLIGHT (Dato Destacado)
**Para números hero con contexto.**
```
┌─────────────────────────────────────────┐
│ [========= UPPER BAR ===========]       │
│ CÓDIGO CASA® - BOOKLET NINJA THINKING   │
│                                         │
│ HEADLINE EN INSTRUMENT SERIF            │  ← 28-36pt
│ (Frase provocativa / tensión)           │
│                                         │
│     48%              89%                │  ← Instrument Serif Italic 90-110pt
│  Contexto del     Contexto del          │  ← Poppins Regular 10-11pt, caja 7cm×4cm
│  dato aquí        dato aquí             │
│                                         │
│ Source: ...                             │
└─────────────────────────────────────────┘
  Fondo: Dust texture
```
**Layout:** Los números pueden ir:
- Lado a lado (2 datos)
- Uno grande centrado (1 dato hero)
- Grid de 3-4 datos (múltiples métricas)

### TIPO 4: TENSION STATEMENT (Frase de Tensión)
**Slide de alto impacto con frase provocativa.**
```
┌─────────────────────────────────────────┐
│ [========= UPPER BAR ===========]       │
│ CÓDIGO CASA® - BOOKLET NINJA THINKING   │
│                                         │
│ Tensión 01                              │  ← Poppins Medium, 12pt
│                                         │
│ EN RD "MAMÁ Y PAPÁ" ES EL IDEAL        │  ← Instrument Serif 36pt
│ "ABUELA, TÍA Y NANA" ES LA REALIDAD    │  ← centrado o izquierda
│                                         │
│ Aquí no cría la familia nuclear,        │  ← Poppins Italic 16pt
│ cría la red                             │
│                                         │
└─────────────────────────────────────────┘
  Fondo: Dust texture
```

### TIPO 5: CHART / DATA VISUALIZATION
**Slide con gráfico cuantitativo.**
```
┌─────────────────────────────────────────┐
│ [========= UPPER BAR ===========]       │
│ CÓDIGO CASA® - BOOKLET NINJA THINKING   │
│                                         │
│ [TÍTULO PEQUEÑO O PREGUNTA]             │  ← Poppins Medium 12pt
│                                         │
│ ┌─────────────────────────────────┐     │
│ │                                 │     │
│ │     [GRÁFICO / CHART]          │     │  ← Área de gráfico
│ │                                 │     │
│ └─────────────────────────────────┘     │
│                                         │
│ Source: ...                             │
└─────────────────────────────────────────┘
  Fondo: Dust texture
```

**IMPORTANTE sobre gráficos:**
- python-pptx puede generar: bar charts, line charts, pie charts, area charts, scatter plots
- python-pptx NO puede generar: stacked bars con colores custom complejos, treemaps, sankeys, chord diagrams
- Si el gráfico requerido NO se puede hacer en python-pptx:
  1. Ofrecerlo como SVG/HTML generado aparte (con codigo-casa-data-viz skill)
  2. Crear un placeholder con los datos visibles para que Jeremy inserte el gráfico
  3. Generar la imagen del gráfico con otra herramienta y embeber como imagen

### TIPO 6: DIGITAL CONVERSATION (Social Listening)
**Para datos de conversación digital / social listening.**
```
┌─────────────────────────────────────────┐
│ [========= UPPER BAR ===========]       │
│ CÓDIGO CASA® - BOOKLET NINJA THINKING   │
│                                         │
│ CONVERSACIÓN DIGITAL                    │  ← Instrument Serif 28pt
│                                         │
│ [Frase insight principal]               │  ← Poppins SemiBold 18pt
│                                         │
│   258          1.3M        53%          │  ← Instrument Serif Italic 90pt
│   MENCIONES    ALCANCE     NEGATIVO     │  ← Poppins Regular 10pt
│                                         │
│ [Contexto interpretativo]               │  ← Poppins Regular 14pt
│                                         │
│ SOURCE: NINJA SOCIAL LISTENING...       │
└─────────────────────────────────────────┘
  Fondo: Dust texture
```

### TIPO 7: CONNECTOR / TRANSITION (Conector)
**Slide de transición entre temas, introduce tensiones o nuevas secciones.**
```
┌─────────────────────────────────────────┐
│                                         │
│                                         │
│    [TEXTO TÍTULO]                       │  ← Instrument Serif, grande
│    [Subtexto opcional]                  │
│                                         │
│                                         │
└─────────────────────────────────────────┘
  Fondo: Color texture O Holographic gradient (NO dust texture)
  SIN upper bar. SIN watermark estándar.
```
**Usan 1 de las 3 texturas de conector** (Color textures o Gradients finales).

### TIPO 8: CODE CARD (Tarjeta de Código)
**Para presentar los 11 códigos del estudio.**
```
┌─────────────────────────────────────────┐
│ [========= UPPER BAR ===========]       │
│                                         │
│ >/ Código          >/ Código            │
│ Familia            Familia              │
│ e Identidad        Bienestar            │
│                                         │
│ [descripción]      [descripción]        │
│                                         │
│ >/ Código          >/ Código            │
│ Familia            Familia              │
│ Financiero         R. de Género         │
│                                         │
│ [descripción]      [descripción]        │
└─────────────────────────────────────────┘
  Fondo: Dust texture
  Layout: Grid 2x2, 2x3, o 3x2 según cantidad
```
**Nota:** El prefijo `>/ Código` es la firma visual del naming system. Siempre en Poppins Medium. El nombre del código en Instrument Serif.

### TIPO 9: TREND FORECAST
**Para presentar macro fuerzas y micro tendencias.**
```
┌─────────────────────────────────────────┐
│ [========= UPPER BAR ===========]       │
│                                         │
│ 3 MACRO FUERZAS    +55 MICROTRENDS     │
│                                         │
│ INVENTOLOGÍA       LOS HERNANDEZ       │
│ DE LA ADULTEZ      ARE PROMPTED        │
│                                         │
│ [descripción]      [descripción]       │
│                                         │
│                ALGORITMO               │
│                DEL HOGAR               │
│                [descripción]           │
└─────────────────────────────────────────┘
  Fondo: Dust texture
```

### TIPO 10: FRAMEWORK / METHODOLOGY
**Para presentar frameworks o metodologías.**
```
┌─────────────────────────────────────────┐
│ [========= UPPER BAR ===========]       │
│                                         │
│ DISEÑAMOS UN FRAMEWORK ÚNICO            │  ← Instrument Serif 36pt
│ PARA CONVERTIR LA DATA Y                │
│ INSIGHTS EN ACCIONABLES DE MARCA.       │
│                                         │
│ [Diagrama o flujo visual]               │
│                                         │
└─────────────────────────────────────────┘
  Fondo: Dust texture
```

### TIPO 11: PRICING / COMPARISON TABLE
**Para versiones Lite / Medium / Premium.**
```
  Layout: 3 columnas iguales con headers destacados
  Cada columna: Título + lista de features con bullets
  Fondo: Dust texture
```

### TIPO 12: CONTACT
**Slide final de contacto.**
```
  Layout: Centrado, limpio
  "Learn more? Talk to us"
  Datos de contacto + emojis
  Logo Ninja
  Fondo: Dust texture o gradiente suave
```

---

## FRAMEWORK DE DECISIÓN: CONTENIDO → TIPO DE SLIDE

Cuando el usuario provee texto, seguir esta lógica:

```
¿Es un número/dato hero?
  → SÍ: TIPO 3 (DATA HIGHLIGHT)
  → ¿Tiene más de 2 datos? → Grid de datos

¿Es una frase provocativa o tensión cultural?
  → SÍ: TIPO 4 (TENSION STATEMENT)

¿Es un gráfico con ejes/barras/líneas?
  → SÍ: TIPO 5 (CHART)
  → ¿Puedo hacerlo en python-pptx? → SI: proceder / NO: ofrecer alternativas

¿Son datos de social listening (menciones, alcance, sentimiento)?
  → SÍ: TIPO 6 (DIGITAL CONVERSATION)

¿Es una transición entre temas?
  → SÍ: TIPO 7 (CONNECTOR)

¿Es la descripción de un código del estudio?
  → SÍ: TIPO 8 (CODE CARD)

¿Son tendencias o forecasts?
  → SÍ: TIPO 9 (TREND FORECAST)

¿Es una explicación de metodología/framework?
  → SÍ: TIPO 10 (FRAMEWORK)

¿Es contenido general con título + párrafo?
  → SÍ: TIPO 2 (CONTENT DEVELOPMENT)
```

---

## IMPLEMENTACIÓN PYTHON-PPTX

### Setup Básico
```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu, Cm
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import os

# Dimensiones 16:9
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Paths de assets
ASSETS_BASE = "/Users/jeremyrodriguez/Downloads/Código Casa/Gráfica"
DUST_TEXTURES = [f"{ASSETS_BASE}/Dust texture/{f}" for f in os.listdir(f"{ASSETS_BASE}/Dust texture") if f.endswith('.png')]
UPPER_BAR = f"{ASSETS_BASE}/Upper bar.png"
NINJA_MASK_WHITE = f"{ASSETS_BASE}/Emojis + logos/mask white ninja.png"
INSTRUMENT_SERIF = f"{ASSETS_BASE}/Instrument_Serif/InstrumentSerif-Regular.ttf"

# Colores
BLACK_BG = RGBColor(0x0A, 0x0A, 0x0A)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GRAY_LIGHT = RGBColor(0xCC, 0xCC, 0xCC)
GRAY_MID = RGBColor(0x99, 0x99, 0x99)
GRAY_DARK = RGBColor(0x66, 0x66, 0x66)
```

### Función: Agregar Fondo Dust Texture
```python
def add_dust_background(slide, texture_index=0):
    """Agrega textura dust como fondo full-bleed."""
    texture_path = DUST_TEXTURES[texture_index % len(DUST_TEXTURES)]
    slide.shapes.add_picture(
        texture_path,
        left=0, top=0,
        width=SLIDE_WIDTH, height=SLIDE_HEIGHT
    )
```

### Función: Agregar Upper Bar
```python
def add_upper_bar(slide):
    """Agrega la barra rainbow holográfica en el top."""
    bar_height = Inches(0.25)  # Ajustar según aspecto real
    slide.shapes.add_picture(
        UPPER_BAR,
        left=0, top=0,
        width=SLIDE_WIDTH, height=bar_height
    )
```

### Función: Agregar Watermark
```python
def add_watermark(slide, section_name="BOOKLET"):
    """Agrega watermark de Código Casa."""
    txBox = slide.shapes.add_textbox(
        left=Inches(0.5), top=Inches(0.35),
        width=Inches(8), height=Inches(0.3)
    )
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = f"CÓDIGO CASA®  - {section_name} NINJA THINKING"
    p.font.size = Pt(9)
    p.font.name = "Poppins"
    p.font.color.rgb = GRAY_MID
```

### Función: Agregar Source Line
```python
def add_source(slide, source_text=None):
    """Agrega línea de fuente en el bottom."""
    if source_text is None:
        source_text = "Source: Código Casa: Estudio cuantitativo y cualitativo familias dominicanas 2024 | 500 personas | +70 horas de grupos focales"
    txBox = slide.shapes.add_textbox(
        left=Inches(0.5), top=Inches(6.9),
        width=Inches(12), height=Inches(0.4)
    )
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = source_text
    p.font.size = Pt(7)
    p.font.name = "Poppins"
    p.font.color.rgb = GRAY_MID
```

### Template: Slide Completo de Contenido
```python
def create_content_slide(prs, title, body_text, section="BOOKLET", source=None):
    """Crea un slide estándar de contenido."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    
    # Capas
    add_dust_background(slide)
    add_upper_bar(slide)
    add_watermark(slide, section)
    
    # Título (Instrument Serif)
    title_box = slide.shapes.add_textbox(
        left=Inches(0.8), top=Inches(1.2),
        width=Inches(11), height=Inches(1.5)
    )
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(36)
    p.font.name = "Instrument Serif"  # Must be installed
    p.font.color.rgb = WHITE
    
    # Body (Poppins)
    body_box = slide.shapes.add_textbox(
        left=Inches(0.8), top=Inches(3.0),
        width=Inches(11), height=Inches(3.5)
    )
    tf = body_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = body_text
    p.font.size = Pt(14)
    p.font.name = "Poppins"
    p.font.color.rgb = GRAY_LIGHT
    
    # Source
    if source:
        add_source(slide, source)
    
    return slide
```

### Template: Data Highlight
```python
def create_data_highlight(prs, headline, data_points, section="BOOKLET", source=None):
    """
    data_points = [
        {"number": "48%", "context": "Dice que sus padres participaron activamente"},
        {"number": "89%", "context": "Califica a sus figuras cuidadoras como muy influyentes"}
    ]
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    add_dust_background(slide)
    add_upper_bar(slide)
    add_watermark(slide, section)
    
    # Headline
    h_box = slide.shapes.add_textbox(
        left=Inches(0.8), top=Inches(1.0),
        width=Inches(11), height=Inches(1.5)
    )
    tf = h_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = headline.upper()
    p.font.size = Pt(28)
    p.font.name = "Instrument Serif"
    p.font.color.rgb = WHITE
    
    # Data points - distribute horizontally
    n = len(data_points)
    col_width = 11.0 / n
    
    for i, dp in enumerate(data_points):
        x = 0.8 + (i * col_width)
        
        # Number — SIEMPRE Instrument Serif Italic (NO Poppins Bold)
        num_box = slide.shapes.add_textbox(
            left=Inches(x), top=Inches(3.0),
            width=Inches(col_width - 0.3), height=Inches(1.38)  # 90pt × 0.039 × 0.394in/cm
        )
        tf = num_box.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.vertical_anchor = PP_ALIGN.TOP  # usar MSO_ANCHOR.TOP en implementación real
        p.text = dp["number"]
        p.font.size = Pt(90)  # 3col; usar 110pt para 2col
        p.font.name = "Instrument Serif"
        p.font.italic = True
        p.font.bold = False
        p.font.color.rgb = WHITE
        
        # Context
        ctx_box = slide.shapes.add_textbox(
            left=Inches(x), top=Inches(4.5),
            width=Inches(col_width - 0.3), height=Inches(1.5)
        )
        tf = ctx_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = dp["context"]
        p.font.size = Pt(14)
        p.font.name = "Poppins"
        p.font.color.rgb = GRAY_LIGHT
    
    if source:
        add_source(slide, source)
    
    return slide
```

---

## FLUJO DE TRABAJO

### Paso 1: Recibir Información
El usuario provee texto con la información de un capítulo/sección.

### Paso 2: Analizar y Clasificar
Para cada bloque de contenido, identificar:
- ¿Qué TIPO de slide necesita? (usar framework de decisión)
- ¿Cuántas slides requiere este contenido?
- ¿Hay gráficos? ¿Son replicables en python-pptx?

### Paso 3: Proponer Estructura
Antes de generar, presentar al usuario:
```
Capítulo X: [Nombre]
- Slide 1: TIPO 4 (Tensión) — "Frase tensión..."
- Slide 2: TIPO 3 (Data highlight) — 48% / 89%
- Slide 3: TIPO 5 (Chart) — Barras apiladas por edad
  ⚠️ NOTA: Este gráfico requiere [X]. Alternativas: [A, B, C]
- Slide 4: TIPO 6 (Digital) — 258 menciones, 1.3M alcance
```

### Paso 4: Generar
Solo después de aprobación, generar el .pptx.

### Paso 5: Verificar
- Abrir el archivo y confirmar que los assets se cargaron
- Verificar que las fuentes se aplican correctamente
- Confirmar que los gráficos son legibles

---

## LIMITACIONES CONOCIDAS Y ALTERNATIVAS

### Lo que python-pptx PUEDE hacer bien:
- Fondos con imágenes (dust textures, color textures)
- Textos con fuentes custom (si están instaladas en el sistema)
- Imágenes embebidas (logos, emojis, upper bar)
- Charts básicos (bar, line, pie, area, scatter)
- Tablas con estilos
- Posicionamiento preciso de elementos

### Lo que python-pptx NO puede hacer:
| Limitación | Alternativa |
|-----------|-------------|
| Gradientes de texto | Usar color sólido blanco (la textura da el color) |
| Blur/grain effects en texto | La textura de fondo provee el efecto |
| Charts complejos (treemap, sankey) | Generar como SVG/PNG aparte → embeber como imagen |
| Transparencia avanzada | Usar opacidad de texto vía alpha en color |
| Animaciones | No aplica — presentación estática |
| Masterslides reales | Simular con layers de imágenes |

### Cuando NO puedes replicar un gráfico:
1. **Opción A:** Generar el gráfico como imagen PNG/SVG usando el skill `codigo-casa-data-viz` y embeber
2. **Opción B:** Crear un placeholder slide con los datos en texto y marcar "[INSERTAR GRÁFICO]"
3. **Opción C:** Simplificar el gráfico a un tipo que python-pptx sí soporte
4. **SIEMPRE** informar al usuario antes de elegir

---

## CHECKLIST FINAL (POR SLIDE)

- [ ] Dust texture de fondo aplicada
- [ ] Upper bar en el top
- [ ] Watermark con sección correcta
- [ ] Títulos en Instrument Serif
- [ ] Body text en Poppins
- [ ] Escalas tipográficas respetadas
- [ ] Jerarquía visual clara (dato hero > contexto > source)
- [ ] Source line en el bottom
- [ ] Alineación consistente con slides anteriores
- [ ] Si hay gráfico: verificado que es replicable o alternativa propuesta

---

*Última actualización: 2026-04-16*
*Basado en análisis del PDF "Código Casa - Insights Booklet" (27 páginas) + inventario completo de assets gráficos*
