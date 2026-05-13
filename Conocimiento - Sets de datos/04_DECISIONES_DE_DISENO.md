# 04 · Decisiones de Diseño — Reglas no Negociables

Estas son las reglas visuales que se establecieron en la primera ronda del deck Finanzas. Aplican a todos los decks Código Casa MED.

## 1. Tipografía y kerning

### Tipografías
- **Headlines slides Hallazgo y Cruce de Data:** Instrument Serif, **MAYÚSCULAS**, centrado al centro del slide. Tamaño objetivo: **90pt** (ver nota crítica abajo sobre realidad operativa)
- **Headlines del resto del deck (split plain/italic):** Instrument Serif, 32pt
- **Stats grandes (números):** Instrument Serif italic, 96pt
- **Descripciones de stat:** Poppins regular, 11pt (con bold en parte 2)
- **Cuerpo / conclusión italic:** Poppins italic, 12pt
- **Source pie de página:** Poppins italic, 9pt
- **Headers de slide tipo MAPEO/KIT:** Poppins, uppercase
- **Quotes Consumer Voice:** Instrument Serif, mayúsculas

### Regla crítica de titulares de Hallazgo y Cruce

Los headlines de los slides **Hallazgo (2, 10, 18, 26, 34)** y **Cruce de Data (4, 12, 20, 28, 36)** siguen estas reglas:

- **MAYÚSCULAS** siempre
- **Centralizado** vertical y horizontalmente
- **Italic selectivo** en la frase clave del giro de sentido (patrón split plain + italic)
- **Tamaño AUTO** según el largo del headline (el script lo aplica solo)

### Tabla de tamaños (auto-aplicada por el script)

El script `apply_design_fixes.py` mide el largo del headline en caracteres y elige el tamaño que cabe limpio sin invadir el espacio de los stats:

| Largo del headline | Tamaño auto | # de líneas típicas |
|--------------------|-------------|---------------------|
| <30 caracteres     | **70pt**    | 1 línea             |
| 30-44 caracteres   | **55pt**    | 2 líneas            |
| 45-65 caracteres   | **42pt**    | 2-3 líneas          |
| 66-85 caracteres   | **36pt**    | 3 líneas            |
| >85 caracteres     | **30pt**    | 3-4 líneas          |

**Por qué no 90pt fijo:** 90pt sólo cabe limpio en headlines de menos de 30 caracteres. Los headlines de Código Casa MED suelen ser de 50-80 caracteres (porque combinan declaración + giro), así que un tamaño fijo de 90pt rompe el layout y se solapa con los stats. La auto-escala mantiene el headline grande pero respeta el espacio.

**Si quieres forzar un tamaño específico:** edita la función `_pick_headline_size` en el script y cambia los valores. Por ejemplo, para todo a 60pt fijo:
```python
def _pick_headline_size(headline_text):
    return "6000", "1737000", "60pt"
```

**Cómo escribir headlines que permitan 70-90pt:** mantenlos cortos. Un headline de 25-30 caracteres tipo "EL DINERO _MANDA_." califica para 70pt. Para 90pt necesitarías algo de 15-20 caracteres tipo "_SIN DINERO_ NO HAY PAZ."

### Dimensiones técnicas

- Posición de la caja del headline: `x=914400` (1" desde izquierda), `y=914400` (1" desde top)
- Ancho: `cx=10362895` (~10.7", se extiende a casi todo el ancho del slide)
- Altura máxima disponible antes de invadir los stats: `1737000 EMU` (~1.4")
- La caja se ajusta automáticamente entre `1280160` y `1737000` EMU según el tamaño elegido

**Ejemplo correcto (formato visual):**

```
       DICEN QUE LA PAZ VALE MÁS QUE EL DINERO,
              PERO ADMITEN QUE
                                      ▲
                       SIN DINERO NO HAY PAZ.
                       ▲ italic
```

**Versión anterior (32pt sentence case — ya no se usa):**

> "Dicen que la paz vale más que el dinero, pero admiten que _sin dinero no hay paz._"

**Versión nueva (auto-size MAYÚSCULAS centrado):**

> "DICEN QUE LA PAZ VALE MÁS QUE EL DINERO, PERO ADMITEN QUE _SIN DINERO NO HAY PAZ._"

### Kerning
**Todo el deck en `spc="0"`.** No se permiten valores positivos de spacing entre letras (los 100, 200, 300, 400, 600, 700 que vienen por defecto del creativo se eliminan).

El script `apply_design_fixes.py` lo hace automáticamente.

## 2. Paleta de colores

| Color | Hex | Uso |
|-------|-----|-----|
| Negro | `#000000` | Fondo de todos los slides |
| Blanco | `#FFFFFF` | Texto principal, cifras, todos los verbatims |
| Gris carbón | `#2E2E2E` | Cajas de quotes en Conversación Digital, líneas separadoras entre stats |
| Gris medio | `#4D4D4D` | Bordes de placeholders punteados |
| Verde lima | `#B8FF4D` | **SOLO** la cápsula "Tensión 0X" en slides Mapeo y Kit de Marca |
| Azul oscuro | `#1A1A2E` | Fondo de la columna izquierda en slides Caso Referencia |

### Reglas críticas de color

**El verde lima (`#B8FF4D`) NUNCA se usa para texto.**
- Sí: cápsula "Tensión 0X" arriba de Mapeo y Kit de Marca (es un fondo de bloque)
- No: @usernames de verbatims (van en blanco)
- No: títulos
- No: botones o highlights

**Esto fue un error en la primera ronda.** Los @usernames venían en verde lima por defecto y hubo que pasarlos todos a blanco.

## 3. Layout — slides Hallazgo y Cruce de Data

Ambos comparten el mismo layout (por eso uno sirve de plantilla para construir el otro):

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│         [HEADLINE PLAIN] [HEADLINE ITALIC]                   │
│         Instrument Serif 32pt · centrado                     │
│                                                              │
│                                                              │
│       [STAT1]   │   [STAT2]   │   [STAT3]                    │
│         96pt    │     96pt    │     96pt                     │
│                                                              │
│   [desc1]       │   [desc2]    │   [desc3]                   │
│   3 partes      │   3 partes   │   3 partes                  │
│   (reg+bold+reg)│              │                              │
│                                                              │
│                                                              │
│              [Conclusión italic centrada]                    │
│                                                              │
│                                                              │
│  Source: ... pie de página italic 9pt                       │
└─────────────────────────────────────────────────────────────┘
```

**Líneas separadoras:** entre los 3 stats hay líneas verticales finas en `#2E2E2E`. Se mantienen al construir cruces.

## 4. Reglas para cifras grandes

### Redondeo de números

| Regla | Ejemplo | Por qué |
|-------|---------|---------|
| Porcentajes a entero | 47.8% → **48%** | Consistencia visual entre los 3 stats |
| Decimales se mantienen si son significativos | 4.4%, 6.6%, 8.4% | Estos no redondean bien (4% pierde información) |
| Múltiplos como ratios | 2.3x, 4x | Forma legítima de representar una diferencia |
| K/M para volúmenes grandes | 1.25K, 2.88M, 7.4M | Las cifras absolutas no caben |

### Caracteres que NO caben en el slot de stats

El slot visual del stat grande está pensado para **3-4 caracteres** (96pt). Si pones más:
- "26.1%" se desborda → pasa a "26%"
- "14-19%" se desborda → usa "14%" y mete el rango en la descripción
- "RD$50,000" no cabe — busca otra forma de expresarlo

### Citas decimales SÍ caben en descripciones

Cuando es un dato comparativo dentro del párrafo descriptivo, el decimal se mantiene:
- "calidad **45.8%**" — sí
- "salud **34.4%**" — sí
- "el **95.6% restante**" — sí

## 5. Reglas para texto

### Descripciones de stat (3 partes)

Cada descripción se split en 3 partes para crear ritmo visual:

```
[regular] [BOLD: palabra clave] [regular]
```

Ejemplo:
- Part 1 regular: "del estrato "
- Part 2 BOLD: "E (<RD$10K)"
- Part 3 regular: " sufre violencia económica en su entorno familiar."

**La parte BOLD siempre es:**
- Una variable demográfica destacada (`55+`, `E (<RD$10K)`, `C+ (RD$67-82K)`)
- Una palabra concepto destacada (`la economía`, `efectivo en casa`, `seguros`)
- Una cita textual (`"tener una casa propia, no alquilada"`, `"nada preparado"`)

### Headlines split (plain + italic)

El patrón es: parte declarativa neutra + parte italic con el giro de sentido.

Ejemplos del deck Finanzas:
- "Dicen que la paz vale más que el dinero, pero admiten que _sin dinero no hay paz._"
- "La comida fuera de casa es _el último placer_ que se negocia."
- "El alquiler comprime a _ambos extremos por razones opuestas._"

**La parte italic NO es decoración** — es donde la oración hace girar el sentido. Si una headline no tiene un giro, no debe tener italic.

### Comillas

- **Comillas curvas (" ")** para quotes: tanto en Consumer Voice como en cuotes inline dentro de descripciones
- **Comillas rectas (" ")** SOLO si el .txt original las usa así
- En XML van como `&quot;` o como caracteres Unicode `"` y `"`

## 6. Reglas para verbatims (Conversación Digital)

### Cajas de verbatim
- Fondo: `#2E2E2E` (gris carbón)
- Padding generoso (cerca de 30pt arriba/abajo)
- Bordes redondeados (~12px)

### Estructura interna
```
@usuario                              PLATAFORMA
                                      (alineado derecha)

"Texto del quote con comillas curvas
y wrapping natural."
```

### Color
- @usuario: **blanco**
- Plataforma: **blanco**, uppercase, tracking ligeramente abierto
- Texto del quote: **blanco**

**No usar verde lima en ningún elemento del verbatim.**

## 7. Reglas para Mapeo de Oportunidades

### Cápsula "Tensión 0X"
- Fondo: verde lima `#B8FF4D`
- Texto: negro
- Esquinas completamente redondeadas (pill shape)

### Tabla 3×3
- Headers en uppercase: VERDAD INCÓMODA · OPORTUNIDAD · DETONADOR
- Cada celda tiene padding generoso
- Flechas (→) entre columnas
- Texto centrado

## 8. Reglas para Kit de Respuesta de Marca

### Cápsulas 01/02/03
- Numeradas con tipografía grande
- Subtítulo en uppercase: OPORTUNIDAD CLAVE · POSTURA · ROL · VERBO TRANSFORMACIÓN
- Cuerpo del texto en regular blanco

### Bloque "NUEVA NARRATIVA DE MARCA" — estética actualizada

El bloque tiene una estética específica que se debe replicar consistentemente:

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   ┌──────────┐    [Tu marca] quiere [verbo de aspiración], pero sabe   │
│   │  NUEVA   │    que [reconocimiento de la fricción], por eso          │
│   │ NARRATIVA│    [propuesta de valor diferenciada].                    │
│   │ DE MARCA │                                                          │
│   └──────────┘                                                          │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘
```

**Especificaciones visuales:**

- **Caja contenedora:** rectángulo con fondo `#1A1A2E` (azul oscuro), bordes ligeramente redondeados (~8-12px), borde sutil tipo `#2E2E2E` 1px
- **Etiqueta izquierda "NUEVA NARRATIVA DE MARCA":**
  - Tipografía: Poppins, **uppercase**, **bold**, ~10pt
  - Color: blanco
  - Tracking ligeramente abierto
  - Multilínea (3 líneas: "NUEVA / NARRATIVA / DE MARCA")
  - Centrado vertical y horizontal en su slot
  - Ocupa ~25% del ancho de la caja
- **Texto de la narrativa (lado derecho):**
  - Tipografía: Instrument Serif, ~18pt, regular
  - Color: blanco
  - Alineación: izquierda
  - Padding: generoso (la caja respira)
  - Multilínea con wrapping natural
- **Italics dentro del texto:**
  - `[Tu marca]` — italic, entre corchetes
  - `pero sabe que` — italic
  - `por eso` — italic
  - El resto del texto en regular
- **Flecha indicadora arriba (opcional):**
  - Aparece sobre el bloque una flecha ↓ blanca pequeña
  - Conecta visualmente con los bloques de arriba (Situación → Oportunidad/Postura/Verbo → Nueva Narrativa)

**Estructura del texto (3 partes con conectores en italic):**

```
[Tu marca] quiere [VERBO + ASPIRACIÓN],
pero sabe que [RECONOCIMIENTO DE LA FRICCIÓN],
por eso [PROPUESTA DE VALOR DIFERENCIADA].
```

**Ejemplo correcto (de Tensión 10):**

> *[Tu marca]* quiere que puedas tener planificación financiera, *pero sabe que* las excusas para gastar son más rápidas que la planificación, *por eso* simplifica tu forma de planificar para que no quepan las excusas.

**Reglas:**
- Las 3 frases se ensamblan en **un solo párrafo fluido**, separadas por comas (no por líneas o bullets)
- Los **3 conectores italic** (`[Tu marca]`, `pero sabe que`, `por eso`) son **fijos** — no se cambian
- El texto entre conectores es lo que cambia por tensión
- La caja debe verse "respirable" — texto generosamente espaciado, no apretado

## 9. Sources

### Slides cuanti (Hallazgo y Cruce)
Format estándar:
> `Source: Código Casa — Estudio cuantitativo 2025 · P[X], P[Y] · Base 500.`

### Slides Conversación Digital
Format estándar:
> `Ninja Social Listening Impact® — Data 01 sept – 31 dic 2025.`

### Slides Mapeo, Kit, Caso
Format estándar:
> `Source: Ninja Thinking 2026`

## 10. Lo que NO se debe hacer

- **No inventar datos** que no estén en el .txt. Cero excepciones.
- **No cambiar la estructura de 8 slides por tensión.** Si el creativo agrega un slide intermedio, hay que evaluar si rompe el flujo del deck.
- **No usar verde para texto.** Solo para la cápsula tipo pill.
- **No mezclar tipografías.** Solo Instrument Serif + Poppins. Punto.
- **No dejar placeholders.** Si llegaron, hay que llenarlos. Si no se puede llenar, hay que escalar al equipo.
- **No combinar 2 quotes en 1.** Si el quote del .txt es muy largo, se elige el más fuerte; no se hace un mash-up.
- **No traducir literalmente del análisis 190 chars al deck.** Se editorializa para fluir, pero sin agregar interpretación nueva.

---

**Ver siguiente:** `05_EJEMPLO_TRABAJADO_T6.md` — un ejemplo completo end-to-end.
