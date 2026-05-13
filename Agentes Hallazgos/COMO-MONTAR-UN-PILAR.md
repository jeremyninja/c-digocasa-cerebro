# Cómo montar un pilar de Código Casa — manual de uso

**Para:** Jeremy.
**Setup actual:** 3 agentes (cazador, editor, montador) + 1 slash command (`/flujo-hallazgos`) + 3 archivos de aprendizajes + knowledge pack del montador.

---

## Vía rápida — slash command

Cuando quieras correr el flujo completo de un pilar:

```
/flujo-hallazgos <nombre del pilar>
```

Ejemplos:

```
/flujo-hallazgos bienestar
/flujo-hallazgos finanzas
/flujo-hallazgos identidad
```

El comando ejecuta los 3 agentes en orden con dos checkpoints:

1. **Cazador** caza 10–15 hallazgos del pilar (en prueba de humo, 5).
   - Lee `aprendizajes-cazador-cc.md`, las rutas exactas, y aplica las 7 no-negociables.
   - Entrega tabla de cobertura + bloques de hallazgo + reporte de integridad.

2. **Checkpoint 1.** Si las cifras no cuadran, hay preguntas sin cobertura, verbatims sin FG identificable, o menos del rango pedido — **el flujo se detiene** y te reporta antes de pasar al editor.

3. **Editor** pule a voz Jeremy / Código Casa.
   - Lee `aprendizajes-editor-cc.md` (voz destilada de tus 3 capítulos publicados).
   - Invoca `escritura-es` y `humanizador-es` en orden estricto.
   - Entrega bloques editoriales con headlines split, conclusiones sin invención, verbatims limpios.

4. **Checkpoint 2.** Antes de montar deck, te muestra el set editorial y te pregunta explícito *"¿Procedo a montar?"*. **No arma .pptx sin tu OK.**

5. **Montador** arma el `.pptx` MED (5 tensiones × 8 slides = 40 slides, o el formato que pidas).
   - Lee `aprendizajes-montador-cc.md` y el knowledge pack en `Conocimiento - Sets de datos/`.
   - Aplica reglas no negociables: Instrument Serif + Poppins, kerning 0, headlines MAYÚSCULAS auto-tamaño, paleta y sources estándar.
   - Entrega `.pptx` + PDF de QA + reporte de cambios.

---

## Modo prueba de humo

Si solo quieres validar el flujo con un set chico, agrega al final:

```
/flujo-hallazgos bienestar — prueba de humo, solo 5 hallazgos
```

El cazador cosechará 5 en lugar de 10–15. Aun así aplica todas las reglas anti-invención.

Para el montador, tienes 3 formatos de prueba de humo:
- **A)** 5 hallazgos = 5 slides flat (uno por hallazgo) — más rápido, valida voz visual.
- **B)** Una tensión completa (8 slides) con un hallazgo como caso testigo — valida estructura MED entera.
- **C)** 5 slides headline + 5 slides verbatim (10 slides) — valida look & feel sin compromiso estructural.

Le dices al montador cuál formato quieres y se ajusta.

---

## Vía manual — invocar agentes uno por uno

Si quieres correr solo una parte del flujo, usa lenguaje natural:

| Lo que quieres | Frase típica |
|---|---|
| Solo cazar hallazgos | *"vamos con el pilar de bienestar"* o *"caza hallazgos del pilar X"* |
| Auditar un pilar ya cazado | *"audita el pilar Y"* o *"valida la cobertura del cuestionario para Z"* |
| Solo pulir un set ya cazado | *"pule estos hallazgos"* o *"déjalos en voz Código Casa"* |
| Solo montar deck con set editado | *"monta el deck de X"* o *"arma el .pptx de la tensión Y"* |
| Aplicar fixes de diseño a un .pptx | *"aplica fixes de diseño al deck"* o *"QA visual del deck"* |

Cada agente sabe cuál es su scope y no se mete con el del otro.

---

## Qué necesitas tener antes de correr un pilar

Para que el cazador no se trabe:

1. **`.md` derivado del pilar** existe en `Data System/derivados-por-pilar/0X-pilar.md`.
2. **Cuestionario canónico** en `Data System/CUESTIONARIO_FINAL_CODIGO_CASA.md`.
3. **Transcripciones de FG** en `Data System/derivados-por-pilar/transcripciones-codigo-casa/`.

Para que el montador no se trabe:

4. **Knowledge pack** en `Conocimiento - Sets de datos/` (los 7 archivos `.md` + scripts + deck de referencia).
5. **`.txt` MED del pilar** con cruces tabulados (si vas a montar 40 slides). Si solo quieres 5 slides flat por hallazgo, no hace falta.

---

## Qué hacer cuando algo falla

### Caso 1 — el cazador reporta P## con 100% en todas las opciones
**Causa:** ranking colapsado en el `.md` derivado (mismo problema que tuvimos con P28 en Bienestar).

**Acción:** decide si:
- Avanzas con caveat ("evidencia cualitativa convergente, cifra cuanti pendiente"), o
- Pausas para regenerar el `.md` desde el xlsx con orden ponderado.

### Caso 2 — el derivado mezcla pilares
**Causa:** herencia de mapeo previo a la reclasificación canónica (ej. `02-bienestar.md` lista preguntas de Identidad y Creencias).

**Acción:** el cazador lo reporta en la tabla de cobertura. Para audit completo, decide si los derivados se realinean al cuestionario canónico antes de seguir, o si trabajas con el derivado tal cual y documentas la mezcla.

### Caso 3 — el montador dice que el knowledge pack no está disponible
**Causa:** la ruta del pack cambió o no se montó la carpeta en sesión.

**Acción:** verifica que la carpeta `Conocimiento - Sets de datos/` esté en `Documents/Cerebro/Código Casa/`. El montador lee de ahí. Si no, paras.

### Caso 4 — un agente custom no aparece como invocable
**Causa:** Claude Code carga la lista de agentes al arranque; si los agregaste durante la sesión actual, no se ven hasta reiniciar.

**Acción:** cierra Claude Code (`Cmd+Q`) y vuelve a abrirlo. La sesión nueva carga los agentes desde `~/.claude/agents/` (que son symlinks al master en `Cerebro/Código Casa/Agentes Hallazgos/`).

---

## Mantenimiento

### Editar un agente o un aprendizaje
Edita el archivo maestro en:

`/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Agentes Hallazgos/`

Los symlinks en `~/.claude/agents/` y `~/.claude/commands/` se actualizan automático. **Una sola fuente de verdad.**

### Agregar un aprendizaje nuevo
Si descubres un patrón de tu voz, una regla del montador, o un caso particular del cazador, agrégalo al archivo de aprendizajes correspondiente:

- `aprendizajes-cazador-cc.md`
- `aprendizajes-editor-cc.md`
- `aprendizajes-montador-cc.md`

Los agentes lo leen al arranque.

### Reentrenar después de un nuevo capítulo publicado
Cuando publiques un capítulo nuevo (ej. Roles de Género, Tecnología), pídeme:

> *"reentrena al editor con el capítulo nuevo de [pilar]"*

Voy, lo leo, extraigo patrones nuevos, actualizo `aprendizajes-editor-cc.md` y la voz queda calibrada.

---

## Estado del setup (mayo 2026)

| Recurso | Ubicación maestra | Activación |
|---|---|---|
| Agente cazador | `Agentes Hallazgos/cazador-hallazgos-cc.md` | Symlink en `~/.claude/agents/` |
| Agente editor | `Agentes Hallazgos/editor-hallazgos-cc.md` | Symlink en `~/.claude/agents/` |
| Agente montador | `Agentes Hallazgos/montador-deck-cc.md` | Symlink en `~/.claude/agents/` |
| Slash command flujo | `Agentes Hallazgos/flujo-hallazgos.md` | Symlink en `~/.claude/commands/` |
| Aprendizajes cazador | `Agentes Hallazgos/aprendizajes-cazador-cc.md` | Lo lee el cazador al arrancar |
| Aprendizajes editor | `Agentes Hallazgos/aprendizajes-editor-cc.md` | Lo lee el editor al arrancar |
| Aprendizajes montador | `Agentes Hallazgos/aprendizajes-montador-cc.md` | Lo lee el montador al arrancar |
| Knowledge pack montador | `Conocimiento - Sets de datos/` | Lo lee el montador al arrancar |
| Manual de uso | `Agentes Hallazgos/COMO-MONTAR-UN-PILAR.md` | Este archivo |

---

## TL;DR

```
/flujo-hallazgos bienestar
```

El sistema hace el resto, te detiene en los 2 checkpoints, y te entrega `.pptx` + PDF + reporte.
