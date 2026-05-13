# 05 · Ejemplo Trabajado — Tensión 6 de Finanzas

Este es un walk-through completo de cómo se llevó la Tensión 6 ("La casa propia sigue siendo el destino...") desde el `.txt` al deck final, slide por slide.

Sirve como referencia concreta cuando estás trabajando un nuevo pilar y dudas de cómo aplicar las reglas.

## El input — qué llegó del research

### Bloque del .txt para Tensión 6

```
================================================================================
TENSIÓN 6: LA CASA PROPIA SIGUE SIENDO EL DESTINO. LO QUE NO SE VE ES EL CAMINO
================================================================================

HALLAZGO #11

Dicen que la paz vale más que el dinero, pero admiten que sin dinero no hay paz.
La tranquilidad financiera emerge como el verdadero sueño dominicano,
desplazando aspiraciones materiales.

- 47.8% nombra la economía como factor #1 de estrés, superando inseguridad,
  crianza y tiempo personal. (P26)
- 46.4% señala como ideal de vivienda 'tener una casa propia, no alquilada'. (P54)
- 61.8% se siente 'nada preparada' para la estabilidad financiera a largo plazo. (P73)

CONSUMER VOICE:

"Mi sueño es tener siempre tranquilidad a nivel financiero."
-- Grupo Biparental Hijos Adultos

[...]

CRUCE TENSIÓN 6 — Violencia económica por NSE
Pregunta: P77. ¿Has sufrido algún tipo de violencia en tu entorno familiar?
Base: 500 | Cruce: NSE (ingresos del hogar)

TABLA DE DATOS:
                                | Total  |  E(<10K) | D(10-27K) | C(27-42K) | C(42-67K) | C+(67-82K)
Base                            |  500   |    32    |    172    |    144    |     74    |     21
No he sufrido violencia         | 56.4%  |  43.8%   |   56.4%   |   53.5%   |   67.6%   |   47.6%
Violencia económica             | 20.2%  |  43.8%   |   18.0%   |   18.8%   |   18.9%   |   23.8%

ANÁLISIS (190 chars):
43.8% del estrato E sufre violencia económica — el doble del promedio. Donde no hay
casa propia ni ingreso estable, el dinero se convierte en mecanismo de control.
La pobreza agrava el abuso.

CONVERSACIÓN DIGITAL: FINANZAS + VIVIENDA

[...]

921 MENCIONES
7.4M ALCANCE

[3 quotes de redes sobre vivienda y hipotecas]

VERDADES INCÓMODAS QUE NADIE TE QUIERE DECIR

- El sistema hipotecario dominicano está diseñado para quien ya sabe cómo funciona.
- El sueño de la casa propia no es una aspiración -- es una aspiración cultural arraigada.
- El sueño de la casa compite con el arroz y los huevos.

[Mapeo, Caso, Narrativa de marca...]
```

### El estado del .pptx al recibirlo

Slides 1-8 corresponden a Tensión 6. Estado al inicio:

| Slide | Tipo | Estado |
|-------|------|--------|
| 1 | Intro | Decía "TENSIÓN 06 · FINANZAS" — había que limpiar |
| 2 | Hallazgo | Tenía datos, pero la headline tenía punto en vez de coma; la cita no tenía la frase completa entre comillas; tenía oraciones editoriales extra en la conclusión |
| 3 | Consumer Voice | OK |
| 4 | Cruce | Placeholder vacío con "Aquí va el cruce: violencia económica por NSE" |
| 5 | Conv. Digital | Verbatims en verde lima — había que pasar a blanco |
| 6 | Mapeo | OK |
| 7 | Kit Marca | OK |
| 8 | Caso | OK |

## Slide por slide — qué se hizo

### Slide 1 — Intro

**Antes:**
```
Header: "TENSIÓN 06 · FINANZAS"
Headline: "La casa propia sigue siendo el destino. Lo que no se ve es el camino."
Subtítulo: "El sueño no muere — se aplaza, de quincena en quincena."
```

**Después:**
```
Header: "TENSIÓN 06"
Headline: idem
Subtítulo: idem
```

**Cambio:** quité "· FINANZAS" del header. Lo demás quedó igual.

### Slide 2 — Hallazgo (el que más cambios tuvo)

**Antes (problemas marcados):**
```
Headline: "Dicen que la paz vale más que el dinero. Pero admiten que sin dinero no hay paz."
                                                    ⚠ punto debería ser coma

Stat 1: 48% — "nombra la economía como factor #1 de estrés..."  ✓ OK

Stat 2: 46% — 'señala como ideal de vivienda "tener una casa propia", no alquilada.'
                                              ⚠ comilla cierra antes de tiempo

Stat 3: 62% — "se siente 'nada preparado' para la estabilidad..."  ✓ OK

Conclusión:
"La tranquilidad financiera emerge como el verdadero sueño dominicano,
desplazando aspiraciones materiales. La casa propia no se rinde como
                                       ⚠ esta segunda oración no está en el .txt
meta — se posterga como camino."
```

**Después (con regla nueva: MAYÚSCULAS centrado, tamaño auto-detectado):**
```
Headline (auto-size MAYÚSCULAS centrado al centro del slide):
"DICEN QUE LA PAZ VALE MÁS QUE EL DINERO, PERO ADMITEN QUE SIN DINERO NO HAY PAZ."
                                                  ▲ "SIN DINERO NO HAY PAZ." va en italic
                                                  ✓ coma corregida + UPPERCASE + auto-size
                                                  (80 chars → 36pt automáticamente)

Stat 2 corregido: 'señala como ideal de vivienda "tener una casa propia, no alquilada".'
                                                 ✓ frase completa entre comillas

Conclusión: "La tranquilidad financiera emerge como el verdadero sueño dominicano,
            desplazando aspiraciones materiales."
            ✓ solo lo que el .txt sustenta
```

**Importante:** Si tu deck primera ronda tenía el headline en 32pt sentence case (como el deck Finanzas T1-T10 original), **el script lo actualiza automáticamente al formato nuevo: MAYÚSCULAS, centrado, con tamaño calculado según largo**. Aplica a los 5 slides de Hallazgo Y los 5 de Cruce de Data sin que tengas que hacer nada manual.

**Lección clave:** los 3 bullets del .txt tienen **47.8%, 46.4%, 61.8%**. En el slide se redondearon a **48%, 46%, 62%** porque el slot visual no soporta decimales en el número grande. Pero las descripciones inline mantienen su precisión.

### Slide 3 — Consumer Voice

No se tocó. El quote elegido por el creativo es válido (está literalmente en el bloque CONSUMER VOICE del .txt).

### Slide 4 — Cruce de Data (este se construyó desde cero)

**Antes:**
```
[caja punteada vacía]
"PLACEHOLDER"
"Aquí va el cruce: violencia económica por NSE."
Source: Código Casa — P77 · Cruce por NSE · Base 500.
```

**Proceso de construcción:**

1. **Leí la tabla cruzada del .txt:**
   - Total: 20.2% sufre violencia económica
   - Estrato E: 43.8%
   - Otros estratos: 18-23.8%

2. **Leí el análisis 190 chars:**
   - "43.8% del estrato E sufre violencia económica — el doble del promedio. Donde no hay casa propia ni ingreso estable, el dinero se convierte en mecanismo de control."

3. **Decidí los 3 stats narrativos** (estrategia: extremo + extremo + diferencial):
   - Stat 1: el extremo más alto → 44% del estrato E
   - Stat 2: el promedio → 20% promedio nacional
   - Stat 3: la magnitud del gap → 2.3x más

4. **Escribí el headline split:**
   - Plain: "El estrato más bajo sufre violencia económica al "
   - Italic: "doble del promedio."

5. **Escribí las 3 descripciones (3 partes cada una):**
   - Stat 1: "del estrato " + **E (<RD$10K)** + " sufre violencia económica en su entorno familiar."
   - Stat 2: "es el " + **promedio nacional** + " de violencia económica en familias dominicanas."
   - Stat 3: "más violencia vive el " + **estrato E** + " que el promedio. La pobreza agrava el abuso."

6. **Adapté la conclusión** del análisis 190 chars:
   - "Donde no hay casa propia ni ingreso estable, el dinero se convierte en mecanismo de control. La pobreza agrava el abuso."

7. **Source:** mantuve el que ya estaba (correcto): `Source: Código Casa — Estudio cuantitativo 2025 · P77 · Cruce por NSE · Base 500.`

**Resultado:**
```
Headline (auto-size MAYÚSCULAS centrado al centro del slide):
"EL ESTRATO MÁS BAJO SUFRE VIOLENCIA ECONÓMICA AL DOBLE DEL PROMEDIO."
                                                ▲ "DOBLE DEL PROMEDIO." va en italic
                                                (68 chars → 36pt automáticamente)

Stats:       44%        |        20%        |       2.3x
             ─────────────────────────────────────────
             del estrato         es el                más violencia vive
             E (<RD$10K)         promedio nacional    el estrato E
             sufre violencia     de violencia         que el promedio.
             económica en su     económica en         La pobreza agrava
             entorno familiar.   familias dominicanas. el abuso.

Conclusión:  "Donde no hay casa propia ni ingreso estable, el dinero se
              convierte en mecanismo de control. La pobreza agrava el abuso."

Source:      Código Casa — Estudio cuantitativo 2025 · P77 · Cruce por NSE · Base 500.
```

### Slide 5 — Conversación Digital

**Antes:** los @usernames en verde lima (`#B8FF4D`).

**Después:** los @usernames en blanco.

Resto del slide quedó igual. Los 3 quotes (@EnocStubbs, @Pashhy, @U28760Nu) y los KPIs (921 menciones, 7.4M alcance) coinciden con el .txt.

### Slide 6 — Mapeo de Oportunidades

No se tocó. Las 3 ternas (verdad/oportunidad/detonador) coinciden con el .txt.

### Slide 7 — Kit de Respuesta de Marca

No se tocó. Postura ("Ser el banco de las realidades, no solo de los sueños"), verbo (Mapear), narrativa — todo coincide con el .txt.

### Slide 8 — Caso Referencia

No se tocó. El caso Ticket Fairy 3.0 está descrito tal cual en el .txt.

## Resumen — qué cambió para T6

De los 8 slides:
- **3 slides cambiaron significativamente:** 1 (limpieza de header), 2 (texto del hallazgo), 4 (construcción completa del cruce)
- **1 slide cambió cosméticamente:** 5 (color de @usernames)
- **4 slides no se tocaron:** 3, 6, 7, 8

**Tiempo invertido:** ~30 minutos (incluyendo construir el cruce desde cero)

## Lección general

> El bloque del .txt tiene **toda la información necesaria** para llenar los 8 slides correctamente. Cuando el deck del creativo y el .txt difieren, **la regla es: gana el .txt.**

> Las únicas excepciones son redondeo visual de números (47.8% → 48%) y editorialización menor para fluir narrativamente — pero **nunca se agrega información ni se cambian datos**.

---

**Ver siguiente:** `06_ERRORES_COMUNES.md` — lo que NO hay que hacer.
