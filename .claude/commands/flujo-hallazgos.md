---
description: Flujo completo Código Casa para un pilar — caza, edita y monta deck MED
---

Ejecuta este flujo para el pilar: $ARGUMENTS

## Paso 1 — Cazador

Llama al agente `cazador-hallazgos-cc` para auditar la cobertura del pilar y construir/validar los hallazgos crudos del set.

**Reglas innegociables del cazador (recuérdaselas en el prompt):**
- NUNCA inventa hallazgos, cifras, verbatims ni contexto. Cero alucinación.
- Toda cifra DEBE provenir de las tabulaciones cuanti de Código Casa (base n=500, .md numerados, .txt de derivados). Si una cifra no está en la data, no entra al hallazgo.
- Todo verbatim DEBE provenir de las transcripciones de focus groups de Código Casa, citado con el FG correcto y contexto real.
- Cada stat se etiqueta con su pregunta del cuestionario y su base.
- Si una pregunta del cuestionario no tiene cobertura en los hallazgos, el cazador lo reporta explícito en la tabla de cobertura — no rellena con suposiciones.
- Si el rango 10–15 hallazgos no se alcanza con univariadas, usa cruces como herramienta interna (no van al output del bloque).

**Output esperado:** tabla de cobertura del cuestionario + bloques de hallazgo en formato del cazador (headline ≤190 chars, 1–3 stats etiquetados, 1–3 verbatims con FG).

## Checkpoint 1 — Validación de cifras

Si el cazador reporta:
- cifras que no cuadran con la base,
- preguntas del cuestionario sin cobertura,
- verbatims sin FG identificable, o
- menos de 10 hallazgos por pilar,

**DETÉN el flujo** y reporta a Jeremy antes de pasar al editor. No avances por inercia.

## Paso 2 — Editor

Pasa el output validado al agente `editor-hallazgos-cc` para que pula cada hallazgo: headline split plain/italic ≤190 chars, conclusión sin invención (no agrega nada que no esté en la data), verbatims revisados gramaticalmente con contexto claro, voz Código Casa sobria, sin marcas de IA.

**Output esperado:** bloques editoriales listos para deck.

## Checkpoint 2 — Visto bueno antes de montar

Antes de pasar al montador, muestra a Jeremy el set editorial final y pregunta explícito: **"¿Procedo a montar el deck con este set?"** No armes el .pptx hasta tener confirmación.

## Paso 3 — Montador

Con el OK de Jeremy, pasa los hallazgos editados al agente `montador-deck-cc` para que arme el .pptx siguiendo el knowledge pack Código Casa MED (5 tensiones × 8 slides = 40 slides por pilar, Instrument Serif + Poppins, kerning 0, headlines auto-size MAYÚSCULAS).

**Output esperado:** .pptx + PDF de QA + reporte de cambios.

---

No saltes pasos. No mezcles roles. El cazador no edita, el editor no inventa, el montador no caza.
