# 01 · Estructura del Deck

Cada deck Código Casa MED de un pilar contiene **5 tensiones**. Cada tensión usa **8 slides** con tipos fijos. Total: **40 slides** (5 × 8).

## Mapa de slides por tensión

Para una tensión cualquiera (uso T6 como ejemplo aquí), los 8 slides son:

| # | Tipo | Contenido | Source en el .txt |
|---|------|-----------|---------------------|
| 1 | **Intro** | Headline grande de la tensión + subtítulo | Línea de la tabla de contenido + verdad incómoda |
| 2 | **Hallazgo** | Headline + 3 stats cuanti + conclusión + source | Bloque "HALLAZGO #XX" |
| 3 | **Consumer Voice** | 1 quote grande + atribución | Sección CONSUMER VOICE del hallazgo |
| 4 | **Cruce de Data** | Headline + 3 stats cuanti + conclusión + source | Bloque "CRUCE TENSIÓN X" |
| 5 | **Conversación Digital** | Stat headline + 3 KPIs + 3 quotes de social listening + source | Bloque "CONVERSACIÓN DIGITAL" |
| 6 | **Mapeo de Oportunidades** | Tabla 3×3: Verdad incómoda → Oportunidad → Detonador | Bloque "MAPEO DE OPORTUNIDADES" |
| 7 | **Kit de Respuesta de Marca** | Situación + 3 cápsulas (Oportunidad/Postura/Verbo) + Nueva Narrativa | Bloque "NUEVA NARRATIVA DE MARCA" |
| 8 | **Caso Referencia** | Marca + país + headline + descripción del caso + lección | Bloque "CASO REFERENCIA" |

## Numeración real en el .pptx (40 slides)

| Tensión | Intro | Hallazgo | Consumer Voice | Cruce | Conv. Digital | Mapeo | Kit Marca | Caso |
|---------|-------|----------|----------------|-------|---------------|-------|-----------|------|
| T1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| T2 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| T3 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
| T4 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 |
| T5 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |

Si tu deck es T6-T10, la numeración es la misma (1-40), porque cada deck es independiente.

## Por qué importa esta estructura

1. **Cada slide tiene un rol único.** El Hallazgo es la afirmación; el Cruce es la profundidad; la Conversación Digital es la voz pública; el Caso es la inspiración global. No se mezclan.

2. **El equipo creativo monta el deck con placeholders.** Los slides 4 (cruce) suelen llegar como cajas con texto "Aquí va el cruce: X por NSE" porque el research aún no había procesado el dato. **Tu trabajo es llenar esos placeholders con la data real del .txt.**

3. **Los slides de Hallazgo y Cruce comparten plantilla visual** (3 stats grandes + descripciones + conclusión). Esto es estratégico: permite usar uno como template del otro cuando hay que construir el cruce desde cero. Ver `scripts/build_cruce_slides.py`.

4. **Los slides 6 (Mapeo) y 7 (Kit de Marca) son los más densos.** El .txt los trae casi listos para copiar. Si ahí hay diferencias, es casi siempre por reescritura editorial del creativo, no por error de research.

## Tipos de slide y qué cuidar

### Intro (slide 1, 9, 17, 25, 33)
- Header arriba: solo dice **"TENSIÓN 0X"** (sin "· FINANZAS" ni nombre del pilar)
- Headline grande con cita del título de tensión
- Subtítulo italic más abajo

### Hallazgo (slide 2, 10, 18, 26, 34)
- **Headline split en MAYÚSCULAS, centralizado al centro del slide, tamaño AUTO según largo del texto** (de 30pt a 70pt — el script lo aplica solo). Parte regular + parte italic con la frase clave.
- 3 números grandes (porcentajes, cifras absolutas o múltiplos)
- Bajo cada número: descripción de 3 partes (regular + bold + regular)
- Conclusión italic centrada
- Source en pie de página con número de pregunta y base

### Consumer Voice (slide 3, 11, 19, 27, 35)
- "CONSUMER VOICE" como kicker arriba
- Quote en mayúsculas, comillas curvas, italic
- Atribución: "— Tipología de FG"

### Cruce de Data (slide 4, 12, 20, 28, 36)
- **Mismo layout que Hallazgo** (3 stats + conclusión)
- **Headline split en MAYÚSCULAS, centralizado al centro del slide, tamaño AUTO según largo** (igual que Hallazgo)
- Pero la data viene de un cruce específico (NSE, edad, sexo, tipología)
- El source debe especificar el cruce: "P77 · Cruce por NSE · Base 500"

### Conversación Digital (slide 5, 13, 21, 29, 37)
- Lado izquierdo: headline + párrafo conector + 3 KPIs (menciones, alcance, métrica destacada)
- Lado derecho: 3 cajas con quotes de redes sociales (@usuario + plataforma + texto)
- Los @usernames van en **blanco** (no en verde lima — es un cambio de la primera ronda)

### Mapeo de Oportunidades (slide 6, 14, 22, 30, 38)
- Cápsula verde lima arriba: "Tensión 0X"
- Título: "MAPEO DE OPORTUNIDADES"
- Tabla 3 columnas × 3 filas: Verdad Incómoda → Oportunidad → Detonador
- 3 verdades, 3 oportunidades, 3 detonadores. Una flecha entre cada paso.

### Kit de Respuesta de Marca (slide 7, 15, 23, 31, 39)
- Cápsula verde lima arriba: "Tensión 0X"
- Título: "KIT DE RESPUESTA DE MARCA"
- "De un hallazgo a una narrativa."
- Situación → 3 columnas (01 Oportunidad Clave / 02 Postura · Rol / 03 Verbo Transformación) → **Bloque "Nueva Narrativa de Marca"** (caja contenedora azul oscuro `#1A1A2E` con etiqueta vertical izquierda en uppercase + texto narrativo en Instrument Serif a la derecha — ver `04_DECISIONES_DE_DISENO.md` sección 8 para el detalle visual)

### Caso Referencia (slide 8, 16, 24, 32, 40)
- Marca + país (kicker)
- Espacio para imagen
- Headline en uppercase italic
- Descripción del caso
- Lección como subtítulo italic

---

**Ver siguiente:** `02_DATA_SCHEMA.md` — qué data específica necesitas extraer del `.txt` para cada slide.
