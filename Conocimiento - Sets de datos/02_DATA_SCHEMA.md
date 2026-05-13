# 02 · Data Schema — Qué Data Necesitas del .txt

El `.txt` que recibes del equipo de research tiene una estructura recurrente para cada tensión. Esta guía te dice exactamente qué extraer y dónde va en el deck.

## Estructura de cada bloque de tensión en el .txt

```
================================================================================
TENSIÓN X: TÍTULO LARGO DE LA TENSIÓN.
================================================================================

--------------------------------------------------------------------------------
HALLAZGO(S) ASIGNADOS
--------------------------------------------------------------------------------

HALLAZGO #XX

[Frase larga del hallazgo, 1-2 oraciones]

- XX.X% [descripción del stat 1]. (PXX)
- XX.X% [descripción del stat 2]. (PXX)
- XX.X% [descripción del stat 3]. (PXX)

CONSUMER VOICE:

"[Quote 1]"
-- [Tipología de grupo focal]

"[Quote 2]"
-- [Tipología]

[...]

--------------------------------------------------------------------------------
CRUCE TENSIÓN X — [NOMBRE DEL CRUCE]
Pregunta: PXX. [Pregunta exacta]
Base: 500 | Cruce: [Variable de cruce]
--------------------------------------------------------------------------------

IDEA DE VISUALIZACIÓN: [Descripción del gráfico ideal]

TABLA DE DATOS:
[tabla cruzada con totales y por segmento]

ANÁLISIS (190 chars):
[Texto de 190 caracteres con la lectura del cruce]

--------------------------------------------------------------------------------
CONVERSACIÓN DIGITAL: [TEMA]
--------------------------------------------------------------------------------

CONEXIÓN CON LA TENSIÓN: [Texto conector entre cuanti y digital]

[Stat principal de la conversación digital]

XXX MENCIONES
XX.XK ALCANCE

[Headline corto que sintetiza la conversación]

VOLUMEN DE CONVERSACIÓN "[TEMA]"

Análisis:

[Usuario] - [Plataforma]:
"[Quote 1]"

[Usuario] - [Plataforma]:
"[Quote 2]"

[Usuario] - [Plataforma]:
"[Quote 3]"

[Párrafo de cierre con interpretación de la conversación]

SOURCE: NINJA SOCIAL LISTENING IMPACT® — DATA RECOPILADA DESDE...

--------------------------------------------------------------------------------
VERDADES INCÓMODAS QUE NADIE TE QUIERE DECIR
--------------------------------------------------------------------------------

- [Verdad 1]
- [Verdad 2]
- [Verdad 3]

--------------------------------------------------------------------------------
MAPEO DE OPORTUNIDADES
--------------------------------------------------------------------------------

Verdad incómoda: [Verdad 1]
Oportunidad: [Oportunidad 1]
Detonador: [Pregunta detonadora 1]

[...x3]

--------------------------------------------------------------------------------
CASO REFERENCIA
--------------------------------------------------------------------------------

[Lección/lead-in del caso]

[Descripción del caso real]

--------------------------------------------------------------------------------
NUEVA NARRATIVA DE MARCA (Tensión X)
--------------------------------------------------------------------------------

[Tu marca] [Verbo de aspiración]
Pero sabe que [reconocimiento de la fricción]
Por eso [propuesta de valor diferenciada]

Postura/Rol de marca: [Postura]
Situación: [Situación que justifica la postura]
Verbo transformador: [Verbo en infinitivo]
Desde la tensión: [Reformulación de la tensión]
```

## Mapeo .txt → slide

### Para slide INTRO (slide 1, 9, 17, 25, 33)

**Necesitas:**
- Título completo de la tensión (de la línea `TENSIÓN X: ...`)
- Una frase corta para el subtítulo (de las "VERDADES INCÓMODAS")

**Ejemplo:**
- Título largo: "LA CASA PROPIA SIGUE SIENDO EL DESTINO. LO QUE NO SE VE ES EL CAMINO"
- Para el headline grande: "La casa propia sigue siendo el _destino_. Lo que no se ve es el _camino_." (las palabras clave en italic)
- Para el subtítulo: "El sueño no muere — se aplaza, de quincena en quincena."

**Cómo dividir el headline:**
- La parte regular = afirmación neutra
- La parte italic = la palabra/frase clave que hace girar el sentido

### Para slide HALLAZGO (slide 2, 10, 18, 26, 34)

**Necesitas:**
1. Una **headline split** que sintetice el hallazgo (lo escribe research o lo escribes tú interpretando el hallazgo)
2. **3 stats** con sus descripciones (de los bullets `- XX.X% [...]. (PXX)`)
3. Una **conclusión** italic (la primera oración del párrafo del hallazgo)
4. **Source** completo (todas las preguntas referenciadas + base)

**Reglas críticas:**
- **El headline va EN MAYÚSCULAS, centralizado al centro del slide, con tamaño AUTO según largo del texto** (el script `apply_design_fixes.py` lo elige automáticamente — de 30pt a 70pt según el largo). Esto reemplaza el 32pt sentence case del primer deck.
- Los **números grandes** se redondean a entero (47.8% → **48%**) por consistencia visual con el resto del deck
- Los **decimales SÍ se mantienen** dentro del texto descriptivo cuando son citas inline (calidad **45.8%**, salud **34.4%**)
- La **descripción de cada stat se split en 3 partes**: regular + **bold** (la palabra clave) + regular
- La **conclusión NO debe inventar contenido editorial extra** — usa SOLO lo que dice el .txt

**Ejemplo (Hallazgo #11 / T6):**

| Slot | Contenido |
|------|-----------|
| Headline plain (auto-size MAYÚSCULAS centrado) | "DICEN QUE LA PAZ VALE MÁS QUE EL DINERO, PERO ADMITEN QUE " |
| Headline italic (auto-size MAYÚSCULAS centrado) | "SIN DINERO NO HAY PAZ." |
| Stat 1 número | "48%" |
| Stat 1 part 1 | "nombra " |
| Stat 1 part 2 (bold) | "la economía" |
| Stat 1 part 3 | " como factor #1 de estrés, superando inseguridad, crianza y tiempo personal." |
| Stat 2 número | "46%" |
| Stat 2 part 1 | "señala como ideal de vivienda " |
| Stat 2 part 2 (bold) | `"tener una casa propia, no alquilada"` |
| Stat 2 part 3 | "." |
| Stat 3 número | "62%" |
| Stat 3 part 1 | "se siente " |
| Stat 3 part 2 (bold) | `"nada preparado"` |
| Stat 3 part 3 | " para la estabilidad financiera a largo plazo." |
| Conclusión | "La tranquilidad financiera emerge como el verdadero sueño dominicano, desplazando aspiraciones materiales." |
| Source | "Source: Código Casa — Estudio cuantitativo 2025 · P26, P54, P73 · Base 500." |

### Para slide CONSUMER VOICE (slide 3, 11, 19, 27, 35)

**Necesitas:**
- Un quote del bloque CONSUMER VOICE del hallazgo
- La tipología del FG que viene como atribución

**Cómo elegir el quote:**
- Que sea declarativo, sintético, en mayúsculas se ve bien si es corto
- Si los 3 quotes son largos, elige el más punchy o el que mejor sintetice
- NO mezclar 2 quotes diferentes
- NO inventar quotes — si no hay uno apropiado, díselo al equipo creativo

### Para slide CRUCE DE DATA (slide 4, 12, 20, 28, 36)

Este es el slide más complejo porque normalmente llega vacío y hay que construirlo desde la tabla cruzada del .txt.

**Necesitas (del bloque CRUCE TENSIÓN X):**
1. La **tabla de datos** completa
2. El **análisis de 190 chars**
3. La **idea de visualización** (te dice qué resaltar)

**Cómo extraer 3 stats narrativos de una tabla:**

La tabla suele tener formato:
```
                    | Total  |  E(<10K) | D(10-27K) | C(27-42K) | C(42-67K) | C+(67-82K)
Variable 1          | XX.X%  |  XX.X%  |   XX.X%  |   XX.X%  |   XX.X%  |   XX.X%
Variable 2          | XX.X%  |  XX.X%  |   XX.X%  |   XX.X%  |   XX.X%  |   XX.X%
```

**3 estrategias para elegir 3 stats narrativos:**

1. **Extremo + extremo + diferencial:** el segmento más alto, el más bajo, y la magnitud del gap
   - Ej: "44% del estrato E sufre violencia económica" / "20% es el promedio nacional" / "2.3x más violencia vive el estrato E"

2. **Top + segundo + sorpresa:** el dato dominante, el siguiente, y un dato contraintuitivo
   - Ej: "62% de los 55+ pone comer afuera primero" / "24% de 25-34 pone streaming primero" / "8.4% de los 55+ pone streaming primero"

3. **Cifra + cifra + ratio:** dos cifras directas + una relacional
   - Ej: "26% de los 55+ no tiene productos" / "6.2% de los 35-44 no tiene productos" / "26% de los 35-44 tiene préstamo personal"

**El headline del slide cruce** debe sintetizar la lectura del análisis 190 chars. **Va EN MAYÚSCULAS, centralizado al centro, con tamaño AUTO según largo del texto** (igual que el slide de Hallazgo). Sigue el patrón split (regular + italic en la parte clave del giro).

**La conclusión** se toma directamente del análisis 190 chars (puede acortarse, no extenderse).

**El source** debe especificar el cruce: `P77 · Cruce por NSE · Base 500.`

### Para slide CONVERSACIÓN DIGITAL (slide 5, 13, 21, 29, 37)

**Necesitas:**
1. **Headline** sintético del lado izquierdo (1-2 oraciones, parte regular + parte italic)
2. **Conector**: párrafo corto que une la cuanti con el comportamiento digital
3. **3 KPIs:** menciones (XXX), alcance (XX.XK o X.XM), métrica destacada (% del dataset, sentiment, etc.)
4. **3 quotes de social listening** con @usuario + plataforma + texto

**Reglas:**
- Los @usernames van en **blanco**, no en verde lima
- Las plataformas: `INSTAGRAM`, `TIKTOK`, `X / TWITTER` (uppercase)
- Los textos de quotes con comillas curvas (" ")
- El source: "Ninja Social Listening Impact® — Data 01 sept – 31 dic 2025." (italic en pie)

### Para slide MAPEO DE OPORTUNIDADES (slide 6, 14, 22, 30, 38)

**Copia directa del .txt.** Las 3 verdades, 3 oportunidades, 3 detonadores ya vienen redactados. Solo:
- Verifica que las 3 verdades coincidan con el bloque "VERDADES INCÓMODAS" del .txt
- Verifica que cada terna verdad-oportunidad-detonador esté pareada correctamente
- La cápsula verde arriba debe decir "Tensión 0X"

### Para slide KIT DE RESPUESTA DE MARCA (slide 7, 15, 23, 31, 39)

**Necesitas (del bloque NUEVA NARRATIVA DE MARCA):**
1. **Situación** (línea que dice "Situación: ...")
2. **Oportunidad clave** (deriva del verbo + postura)
3. **Postura/Rol** (línea que dice "Postura/Rol de marca: ...")
4. **Verbo transformador** (línea que dice "Verbo transformador: ...")
5. **Nueva Narrativa de Marca** (las 3 líneas: "Tu marca / Pero sabe / Por eso")

**Reglas:**
- "Tu marca" siempre va entre corchetes: `[Tu marca]`
- La narrativa se ensambla en **un solo párrafo fluido** con comas (no en 3 líneas separadas)
- Los 3 conectores `[Tu marca]`, `pero sabe que`, `por eso` van **en italic**, el resto en regular
- El bloque "Nueva Narrativa de Marca" tiene una **estética visual específica**: caja contenedora azul oscuro `#1A1A2E`, etiqueta vertical izquierda en uppercase blanco, texto narrativo en Instrument Serif al lado derecho. Ver `04_DECISIONES_DE_DISENO.md` sección 8 para el detalle visual exacto.

**Ejemplo correcto (Tensión 10):**

> *[Tu marca]* quiere que puedas tener planificación financiera, *pero sabe que* las excusas para gastar son más rápidas que la planificación, *por eso* simplifica tu forma de planificar para que no quepan las excusas.

**Estructura del texto:**
```
[Tu marca] quiere [VERBO + ASPIRACIÓN],
pero sabe que [RECONOCIMIENTO DE LA FRICCIÓN],
por eso [PROPUESTA DE VALOR DIFERENCIADA].
```

### Para slide CASO REFERENCIA (slide 8, 16, 24, 32, 40)

**Necesitas (del bloque CASO REFERENCIA):**
1. **Marca + país** (extracto del primer bloque del caso, ej: "Ticket Fairy 3.0 — Global")
2. **Headline en uppercase italic** que sintetice la lección
3. **Descripción del caso** (1-2 oraciones del .txt)
4. **Lección final** (cierre italic más pequeño)

**El placeholder de imagen queda como está** — el equipo creativo o la cuenta lo llenan después.

---

**Ver siguiente:** `03_WORKFLOW_OPERATIVO.md` — los pasos en orden para montar un deck.
