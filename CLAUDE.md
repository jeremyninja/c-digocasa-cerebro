# Código Casa — Cerebro del proyecto

Estudio NINJA Thinking sobre familias dominicanas. Cuanti n=500 (Sto. Domingo + Santiago + DN, campo Oct-Nov 2024) + 11 focus groups + cuestionario tabulado en 11 pilares canónicos.

## Estructura del proyecto

- `Data System/` — **fuente única de verdad cuanti**
  - `CUESTIONARIO_FINAL_CODIGO_CASA.md` — cuestionario completo
  - `ficha-tecnica.md` — metodología
  - `01-system-prompt.txt` — voz Código Casa
  - `derivados-por-pilar/01..11-*.md` — derivados cuanti por pilar (univariadas + cruces NSE/sexo/edad/tipología)
  - `derivados-por-pilar/transcripciones-codigo-casa/` — 11 FG transcripts en .txt
  - `BBDD madre/` — base cruda

- `Agentes Hallazgos/` — **outputs del flujo de hallazgos**
  - `cazador-hallazgos-cc.md`, `editor-hallazgos-cc.md`, `montador-deck-cc.md`, `flujo-hallazgos.md` — definiciones source (también copiadas en `.claude/`)
  - `aprendizajes-cazador-cc.md`, `aprendizajes-editor-cc.md`, `aprendizajes-montador-cc.md` — lessons learned acumuladas, LEERLAS antes de cazar/editar/montar
  - `bienestar-*.md` y `bienestar-*.pptx` — ejemplo completo de pilar procesado (referencia de calidad)
  - `mujer-hallazgos-crudos.md`, `mujer-hallazgos-editados.md` — Pilar Mujer ya procesado hasta editor (falta montar deck)
  - `COMO-MONTAR-UN-PILAR.md` — instructivo paso a paso

- `workspace/` — scripts auxiliares y BBDD operativa
- `capitulos/`, `Team Findings CC/`, `Conocimiento - Sets de datos/`, `Logo/` — material de soporte

## Pilares canónicos

| # | Pilar | Archivo derivado | Subsample |
|---|---|---|---|
| 01 | Identidad | `01-identidad.md` | General n=500 |
| 02 | Bienestar | `02-bienestar.md` | General n=500 |
| 03 | Finanzas | `03-finanzas.md` | General n=500 |
| 04 | Alimentación | `04-alimentacion.md` | General n=500 |
| 05 | Roles de Género | `05-roles-de-genero.md` | General n=500 |
| 06 | Consumos | `06-consumos.md` | General n=500 |
| 07 | Educación | `07-educacion.md` | General n=500 |
| 08 | Tecnología | `08-tecnologia.md` | General n=500 |
| 09 | Sistema de Creencias | `09-sistema-de-creencias.md` | General n=500 |
| 10 | Opiniones Políticas | `10-opiniones-politicas.md` | General n=500 |
| 11 | Mujer | `11-mujer.md` | Mujeres n≈305 |

## Flujo de hallazgos por pilar

1. **Cazador** (`cazador-hallazgos-cc`) — construye 10-15 hallazgos validados desde el derivado + FGs. Output: `{pilar}-hallazgos-crudos.md`.
2. **Editor** (`editor-hallazgos-cc`) — pule voz, headlines ≤190 chars, verbatims revisados. Output: `{pilar}-hallazgos-editados.md`.
3. **Montador** (`montador-deck-cc`) — arma deck MED 40 slides (5 tensiones × 8 slides) Instrument Serif + Poppins. Output: `{pilar}-deck-flat.pptx` + PDF QA.

Slash command: `/flujo-hallazgos {nombre del pilar}` ejecuta los 3 pasos secuencial.

## Reglas innegociables

- **Cero alucinación.** Toda cifra viene de los `.md` derivados o la BBDD madre. Todo verbatim viene de los FG transcripts con cita del grupo.
- **Cobertura del cuestionario obligatoria.** El cazador genera tabla de cobertura para cada pregunta del pilar.
- **Cruces son herramienta interna.** No van al output del bloque.
- **Output en `Agentes Hallazgos/`.** Nunca en otra carpeta.
