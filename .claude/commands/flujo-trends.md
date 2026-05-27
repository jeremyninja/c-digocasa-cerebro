---
description: Trend Forecast Código Casa de un capítulo — hunter + scrapper + editor cultural + montador (3 macros × 5 micros = 15 micros)
---

Ejecuta el flujo completo del Team Trends CC para el capítulo: $ARGUMENTS

El capítulo es uno de los 11 pilares canónicos Código Casa:
`familia-identidad` · `bienestar` · `finanzas` · `alimentacion` ·
`roles-genero` · `consumos` · `educacion` · `tecnologia` · `creencias` ·
`opiniones-politicas` · `mujer`.

Slug final: `trends-{capitulo}` (ej. `trends-roles-genero`).

---

## Paso 0 — Data estática obligatoria

Antes de cualquier paso, confirma que existe y es legible:
- `Team Trends CC/macrofuerzas-codigo-casa.md` (las 3 macros canónicas
  + reglas geo + freshness)

Si no existe, **detén el flujo** y avisa a Jeremy.

---

## Paso 1 — Hunter

Llama al agente `hunter-trends-cc` con el capítulo como input.

**Reglas innegociables del hunter (recuérdaselas en el prompt):**
- SIEMPRE leer primero `Team Trends CC/macrofuerzas-codigo-casa.md`
- 15 micros exactos = 5 por macro (Inventología + Hernández Prompted
  + Algoritmo del Hogar)
- 3 bloques macro contextualizados al capítulo (formato MED páginas
  1663-1694 / 1819-1849 / 1974-2003)
- Cobertura geográfica obligatoria: GLOBAL + LATAM + LOCAL (con tag
  `[GLOBAL]` / `[LATAM]` / `[LOCAL · DOMINICAN PROOF]` en cada dato)
- Freshness: solo data de 2024+ (excepto `[HISTÓRICO · CONTRASTE]`
  en bloque "The contrast")
- Cero invención. Si no encuentra stat, `PENDIENTE`
- Cero macros nuevas. Solo las 3 canónicas

**Output esperado:** `Team Trends CC/outputs/trends-{capitulo}-hunter.md`
con 3 bloques macro + 15 micros + tabla de cobertura geográfica.

## Checkpoint 1 — Validación del hunter

Si el hunter reporta:
- menos de 15 micros (3×5),
- micros sin Dominican Proof y sin marca `requiere validación local`,
- stats con freshness <2024 sin marca `[HISTÓRICO · CONTRASTE]`,
- cualquier micro fuera de las 3 macros canónicas,

**DETÉN el flujo** y reporta a Jeremy antes de pasar al scrapper.

---

## Paso 2 — Scrapper

Pasa el hunter brief al agente `scrapper-trends-cc`. Debe verificar
links y capturar screenshots `W149pt × H220pt` (596×880px @3x) con
naming `macro-{N}-{M}-{slug-señal}.png` en
`Team Trends CC/screenshots/trends-{capitulo}/`.

Total estimado de señales: 9 del bloque macro (3 macros × 3 pruebas)
+ 15 micros × 6–10 señales = 100+ candidatas. El scrapper prioriza
las 3 pruebas por macro y la "Prueba TikTok / Trend / Innovación" de
cada micro (3 por micro = 45 mínimo).

**Output esperado:** `Team Trends CC/outputs/trends-{capitulo}-señales.md`
+ screenshots verificados.

## Checkpoint 2 — Validación del scrapping

Si quedan señales no verificadas críticas (las 3 pruebas de algún
micro no se pudieron capturar), **DETÉN el flujo** y devuelve al
hunter para que ajuste el bundle antes de avanzar.

---

## Paso 3 — Editor cultural

Con el OK del scrapping, llama al agente `editor-cultural-cc`. Debe:
- Leer `macrofuerzas-codigo-casa.md` para anclar taglines canónicos
- Aplicar `voz-jeremy` + `humanizador-es` como skills obligatorios
- Redactar 3 bloques macro (formato MED) + 15 micros (formato MED
  con NOMBRE ≤190 chars, FENÓMENO, DATA Y SEÑALES con tag geo,
  HASHTAGS, THE CONTRAST, 3 PRUEBAS, 3 NEEDS)
- Mantener nombres canónicos de macros (no improvisar)

**Output esperado:** `Team Trends CC/outputs/trends-{capitulo}-editado.md`.

## Checkpoint 3 — Visto bueno antes de montar

Muestra a Jeremy el forecast editorial completo y pregunta explícito:
**"¿Procedo a montar el deck de 18 slides del Trend Forecast de
{capítulo}?"** No armes el .pptx hasta tener confirmación.

---

## Paso 4 — Montador

Con el OK, pasa todo al agente `montador-trends-cc`. Debe armar el
deck de **18 slides**:
- Slide 1–2: portada + index (opcionales)
- Slides 3, 9, 15: introducciones macro (3 columnas, layout
  simplificado)
- Slides 4–8, 10–14, 16–20: 15 micros canónicos (3 columnas DS Código
  Casa con fotos 149×220pt + hyperlinks + badge "Click me")
- Slide 21: cierre forecast (opcional)

Todas las cifras con tag geo, fuente inline en Poppins 6.5pt UPPERCASE,
hashtags en Instrument Serif tracking 0, headlines 50pt Instrument
Serif UPPERCASE.

**Output esperado:**
- `Team Trends CC/outputs/trends-{capitulo}-forecast.pptx`
- `Team Trends CC/outputs/trends-{capitulo}-forecast.pdf` (QA)
- `Team Trends CC/build_trends_{capitulo}.py` (script re-buildable)

---

No saltes pasos. No mezcles roles. El hunter no edita, el scrapper no
inventa señales, el editor no caza data nueva, el montador no escribe
copy. Si algún agente reporta falta de evidencia, devuelve al anterior
— no rellena.
