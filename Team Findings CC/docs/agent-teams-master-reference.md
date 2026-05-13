---
title: Agent Teams — Master Reference Guide
source: https://code.claude.com/docs/en/agent-teams
last_updated: 2026-05-04
status: experimental (Claude Code v2.1.32+)
purpose: Reference para que Claude diseñe, lance y opere equipos de agentes de forma efectiva.
---

# Agent Teams — Master Reference Guide

> Este documento es la referencia operativa para construir, lanzar y coordinar agent teams en Claude Code. Está pensado para ser leído por Claude antes de orquestar un equipo.

---

## 1. Concepto en una frase

Un **agent team** es un conjunto de sesiones independientes de Claude Code coordinadas por una sesión "lead". Cada teammate corre en su propio context window, comparte una task list, y puede mensajearse directamente con los demás (no solo con el lead).

> Requiere Claude Code v2.1.32 o superior. Verificar con `claude --version`.

---

## 2. Cuándo usar (y cuándo NO)

### Usar agent teams cuando:
- **Investigación o review en paralelo**: múltiples ángulos sobre el mismo problema, con teammates que se desafían mutuamente.
- **Features o módulos nuevos**: cada teammate posee piezas separadas que no se pisan.
- **Debugging con hipótesis competidoras**: cada teammate prueba una teoría distinta en paralelo.
- **Coordinación cross-layer**: cambios que tocan frontend, backend y tests, cada uno con dueño distinto.

### NO usar agent teams cuando:
- El trabajo es **secuencial** (un paso depende del anterior).
- Múltiples teammates necesitarían **editar el mismo archivo**.
- Hay muchas dependencias entre piezas.
- Es una tarea rutinaria que una sesión sola maneja.
- El costo de tokens no se justifica (ver §13).

---

## 3. Subagents vs Agent Teams (decision matrix)

| Eje              | Subagents                                       | Agent Teams                                          |
| :--------------- | :---------------------------------------------- | :--------------------------------------------------- |
| Context          | Propio; resultado vuelve al caller              | Propio; totalmente independiente                     |
| Comunicación     | Solo reportan al main agent                     | Teammates se mensajean entre sí directamente         |
| Coordinación     | Main agent maneja todo                          | Task list compartida con auto-coordinación           |
| Mejor para       | Tareas focalizadas donde solo importa el output | Trabajo complejo que requiere debate y colaboración  |
| Costo de tokens  | Bajo (resultado se resume)                      | Alto (cada teammate es una instancia Claude entera)  |
| Cuándo elegir    | Quick wins, una pregunta puntual                | Cuando los workers necesitan hablarse entre ellos    |

**Regla rápida**: ¿los workers necesitan compartir hallazgos y desafiarse? → team. ¿Solo necesitas N respuestas en paralelo? → subagents.

---

## 4. Cómo habilitar agent teams

Está deshabilitado por default. Activar con env var `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

**Vía settings.json** (recomendado para persistencia):

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Ubicaciones válidas (en orden de scope):
- `~/.claude/settings.json` (user, todos los proyectos)
- `<proyecto>/.claude/settings.json` (project)
- Variable de entorno del shell

> Nota: en este workspace ya está activado en [Team Findings CC/.claude/settings.json](../.claude/settings.json).

---

## 5. Arquitectura

| Componente   | Rol                                                                                  |
| :----------- | :----------------------------------------------------------------------------------- |
| Team lead    | Sesión principal que crea el team, spawnea teammates y coordina trabajo              |
| Teammates    | Instancias separadas de Claude Code; cada una trabaja sobre tareas asignadas         |
| Task list    | Lista compartida de work items que los teammates reclaman y completan                |
| Mailbox      | Sistema de mensajería entre agentes                                                  |

**Storage local**:
- Team config: `~/.claude/teams/{team-name}/config.json`
- Task list: `~/.claude/tasks/{team-name}/`

> ⚠️ **No editar a mano** el team config ni pre-autorearlo. Claude lo regenera con cada update de estado y sobreescribe cambios manuales. No existe equivalente project-level: un `.claude/teams/teams.json` en el repo es ignorado.

El team config tiene un array `members` con name, agent ID y agent type de cada teammate. Los teammates pueden leer este archivo para descubrir a sus compañeros.

---

## 6. Display modes

Dos modos:

| Modo         | Funcionamiento                                                | Requisitos                                 |
| :----------- | :------------------------------------------------------------ | :----------------------------------------- |
| In-process   | Todos los teammates dentro del terminal del lead              | Cualquier terminal                         |
| Split panes  | Cada teammate en su propio pane                                | tmux **o** iTerm2 con `it2` CLI            |

**Default**: `"auto"` — usa split panes si ya estás en tmux, in-process si no.
**Forzar split panes**: `"tmux"` (auto-detecta tmux vs iTerm2).
**Forzar in-process**: setear en `~/.claude/settings.json`:

```json
{ "teammateMode": "in-process" }
```

Por sesión (override): `claude --teammate-mode in-process`.

### Navegación in-process
- `Shift+Down`: ciclar entre teammates (después del último vuelve al lead).
- `Enter`: ver la sesión del teammate seleccionado.
- `Escape`: interrumpir el turno actual del teammate.
- `Ctrl+T`: toggle de la task list.

### Limitaciones de display
- VS Code integrated terminal: NO soporta split panes.
- Windows Terminal: NO soporta split panes.
- Ghostty: NO soporta split panes.
- tmux funciona mejor en macOS. En iTerm2, el entrypoint sugerido es `tmux -CC`.

---

## 7. Iniciar un team

Pídelo en lenguaje natural. Claude crea el team, spawnea teammates y coordina:

```text
I'm designing a CLI tool that helps developers track TODO comments across
their codebase. Create an agent team to explore this from different angles:
one teammate on UX, one on technical architecture, one playing devil's advocate.
```

Claude decide la cantidad de teammates, o puedes especificar:

```text
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

### Dos formas de iniciar
- **Tú lo pides**: das una task que se beneficia de paralelismo y pides el team explícitamente.
- **Claude lo propone**: si Claude detecta que la task se beneficia, sugiere crear un team. Tú confirmas.

En ambos casos: **Claude no crea team sin aprobación explícita**.

---

## 8. Spawnear con subagent definitions

Puedes referenciar un [subagent](https://code.claude.com/docs/en/sub-agents) por nombre desde cualquier scope (project, user, plugin, CLI):

```text
Spawn a teammate using the security-reviewer agent type to audit the auth module.
```

**Lo que hereda el teammate del subagent definition**:
- `tools` allowlist
- `model`
- El body del definition se **agrega** al system prompt (no lo reemplaza)

**Lo que NO hereda** (importante):
- `skills` y `mcpServers` del frontmatter del subagent **no se aplican** cuando corre como teammate.
- El teammate carga skills y MCP servers del project + user settings, igual que una sesión regular.

**Siempre disponibles para el teammate** (incluso con `tools` restringido):
- `SendMessage` (mensajería entre agentes)
- Task management tools

---

## 9. Plan approval (gate de calidad)

Para tareas complejas o riesgosas, requiere que el teammate planee antes de ejecutar:

```text
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

**Flujo**:
1. Teammate trabaja en plan mode (read-only).
2. Termina el plan → envía request al lead.
3. Lead aprueba o rechaza con feedback.
4. Si rechazado: teammate revisa y resubmite (sigue en plan mode).
5. Si aprobado: teammate sale de plan mode y empieza implementación.

**El lead decide autónomamente**. Para influir su criterio, dale guidelines en el prompt:
- "Only approve plans that include test coverage"
- "Reject plans that modify the database schema"
- "Reject plans that touch shared utility files"

---

## 10. Comunicación

### Cómo se comparte info entre agentes
- **Delivery automático**: los mensajes se entregan sin polling.
- **Idle notifications**: cuando un teammate termina y se detiene, notifica al lead automáticamente.
- **Task list compartida**: todos ven status de tareas y pueden reclamar trabajo disponible.
- **Direct messaging**: mensaje a un teammate específico por nombre. Para alcanzar a todos, un mensaje por destinatario.

### Naming
El lead asigna nombres al spawn. Para tener nombres predecibles que puedas referenciar después, **dile al lead cómo llamar a cada uno** en el prompt de spawn:

```text
Spawn three teammates: name them "ux", "arch", and "devils-advocate".
```

### Talk to teammates directly
Cada teammate es una sesión Claude Code completa.
- **In-process**: `Shift+Down` para ciclar, escribir y Enter para enviar.
- **Split panes**: click en el pane para interactuar directo.

---

## 11. Tasks: states, claiming, dependencies

### Estados
- `pending`
- `in progress`
- `completed`

### Dependencias
Una tarea pending con dependencias no resueltas no puede ser reclamada hasta que las dependencias estén completed. El sistema desbloquea automáticamente cuando se completan.

### Asignación
- **Lead asigna**: "give task X to teammate Y".
- **Self-claim**: tras terminar una task, el teammate reclama la siguiente disponible y no bloqueada.

**File locking** previene race conditions cuando múltiples teammates intentan reclamar la misma task simultáneamente.

### Sizing de tasks (heurística)
- Demasiado chicas → coordination overhead > beneficio.
- Demasiado grandes → teammates trabajan mucho sin check-in, riesgo de esfuerzo desperdiciado.
- Justo: unidades self-contained con deliverable claro (una función, un test file, un review).
- **5-6 tasks por teammate** es el rango productivo sin context-switching excesivo.
- Si tienes 15 tasks independientes: 3 teammates es buen punto de partida.

---

## 12. Hooks como quality gates

Tres hooks específicos para teams:

| Hook              | Cuándo dispara                          | Effect del exit code 2                            |
| :---------------- | :-------------------------------------- | :------------------------------------------------ |
| `TeammateIdle`    | Teammate va a entrar en idle            | Envía feedback y mantiene al teammate trabajando  |
| `TaskCreated`     | Una task está siendo creada             | Previene la creación y envía feedback             |
| `TaskCompleted`   | Una task está siendo marcada completa   | Previene la completion y envía feedback           |

**Casos de uso típicos**:
- Forzar tests antes de cerrar tareas.
- Bloquear creación de tareas que toquen archivos sensibles.
- Mantener teammates trabajando hasta cumplir un criterio (ej: cobertura mínima).

---

## 13. Token costs

**Realidad**: agent teams usan significativamente más tokens que una sesión sola. Cada teammate tiene su propio context window y consumo escala linealmente con el número de teammates activos.

**Vale la pena**:
- Research, review, work en features nuevas.

**No vale la pena**:
- Tareas rutinarias.
- Trabajo secuencial.
- Cuando una sola sesión puede con todo.

**Reglas operativas**:
- Empezar con **3-5 teammates** para la mayoría de workflows.
- Escalar solo cuando el trabajo se beneficia genuinamente del paralelismo.
- 3 teammates focalizados > 5 dispersos.

---

## 14. Lifecycle: spawn, run, shutdown, cleanup

### Permisos
- Teammates inician con los permission settings del lead.
- Si el lead corre con `--dangerously-skip-permissions`, todos los teammates también.
- Después del spawn puedes cambiar el modo de cada teammate, pero NO puedes setear modos per-teammate al momento del spawn.

### Context que carga el teammate al spawn
- `CLAUDE.md` (de su working directory)
- MCP servers (de project + user settings)
- Skills (de project + user settings)
- El spawn prompt del lead

**NO hereda** la conversación del lead. Hay que darle todo lo necesario en el spawn prompt.

### Shutdown de un teammate
```text
Ask the researcher teammate to shut down
```
El lead manda shutdown request. El teammate aprueba y sale, o rechaza con explicación.

### Cleanup del team
```text
Clean up the team
```
Limpia los recursos compartidos. **Falla si hay teammates activos** — primero hay que apagarlos.

> ⚠️ **Siempre el lead hace cleanup**. Los teammates no deben ejecutar cleanup porque su contexto de team puede no resolverse correctamente, dejando recursos en estado inconsistente.

---

## 15. Best practices

### Dale suficiente contexto en el spawn prompt
Los teammates cargan project context automáticamente, pero NO heredan la conversación del lead. Incluye detalles task-specific:

```text
Spawn a security reviewer teammate with the prompt: "Review the authentication module
at src/auth/ for security vulnerabilities. Focus on token handling, session
management, and input validation. The app uses JWT tokens stored in
httpOnly cookies. Report any issues with severity ratings."
```

### Empieza con research/review
Si eres nuevo a teams: PR reviews, research de librerías, debugging. Boundaries claros, no requieren escribir código, muestran el valor sin los retos de coordinación de implementación paralela.

### Evita conflictos de archivos
Dos teammates editando el mismo archivo → overwrites. Particiona el trabajo por archivos.

### Espera a que terminen
A veces el lead empieza a implementar tareas él mismo en vez de esperar. Si pasa:
```text
Wait for your teammates to complete their tasks before proceeding
```

### Monitor y steer
- Chequea progreso periódicamente.
- Redirige approaches que no funcionan.
- Sintetiza findings a medida que llegan.
- Dejar correr unattended demasiado tiempo aumenta riesgo de esfuerzo desperdiciado.

### Pre-aprueba permisos comunes
Las permission requests de teammates burbujean al lead. Configura tus [permissions](https://code.claude.com/docs/en/permissions) antes de spawnear para reducir interrupciones.

---

## 16. Patrones de uso (prompts probados)

### Patrón A — Parallel code review

```text
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```

**Por qué funciona**: cada reviewer aplica un filtro distinto sobre el mismo PR. El lead sintetiza.

### Patrón B — Hipótesis competidoras (debate científico)

```text
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.
```

**Por qué funciona**: la estructura adversarial pelea contra anchoring bias. La teoría que sobrevive al debate tiene más probabilidad de ser la causa real.

### Patrón C — Exploración multi-perspectiva

```text
I'm designing X. Create an agent team to explore from different angles:
one on UX, one on technical architecture, one playing devil's advocate.
```

**Por qué funciona**: roles independientes que pueden explorar el problema sin esperarse.

### Patrón D — Refactor cross-module

```text
Create a team with 4 teammates to refactor these modules in parallel.
Each teammate owns a different module — no shared file edits.
Use Sonnet for each teammate. Require plan approval before any changes.
```

**Por qué funciona**: ownership claro por módulo + plan approval evita cambios destructivos.

### Patrón E — Research con findings doc compartido

```text
Spawn 3 research teammates to investigate <topic>. Each takes a different
angle. They write findings to docs/research/<their-name>.md. After they
finish, synthesize into docs/research/SUMMARY.md.
```

**Por qué funciona**: outputs estructurados, sin overwrites, síntesis explícita al final.

---

## 17. Troubleshooting

| Síntoma                                       | Diagnóstico / Acción                                                                                  |
| :-------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| Teammates "no aparecen"                       | In-process: pueden estar corriendo invisibles. `Shift+Down` para ciclar.                             |
| Task no era suficientemente compleja          | Claude decide spawnear o no. Pide team explícitamente o haz la task más rica.                         |
| Split panes no funcionan                      | `which tmux` para verificar. Para iTerm2: instalar `it2` CLI y habilitar Python API en preferences.   |
| Demasiados permission prompts                 | Pre-aprueba operaciones comunes en permission settings antes de spawnear.                             |
| Teammates se detienen ante errores            | Revisa output con `Shift+Down`. Da instrucciones directas o spawnea un reemplazo.                     |
| Lead apaga el team antes de tiempo            | Dile "keep going" o "wait for teammates to finish before proceeding".                                 |
| Tmux session huérfana después del cleanup     | `tmux ls` y `tmux kill-session -t <name>`.                                                            |

---

## 18. Limitaciones (estado experimental)

- **Sin session resumption con teammates in-process**: `/resume` y `/rewind` no restauran teammates in-process. El lead puede intentar mensajear a teammates que ya no existen → spawnea nuevos.
- **Task status puede atrasarse**: a veces un teammate no marca task como completed, bloqueando dependientes. Verificar manualmente y actualizar.
- **Shutdown lento**: teammates terminan su request o tool call actual antes de salir.
- **Un team por sesión**: el lead solo maneja un team a la vez. Cleanup antes de empezar otro.
- **Sin nested teams**: teammates no pueden spawnear sus propios teams. Solo el lead.
- **Lead es fijo**: la sesión que crea el team es lead de por vida. No se promueve un teammate a lead.
- **Permisos al spawn**: todos los teammates inician con el mode del lead. Cambias después, no al spawn.
- **CLAUDE.md sí funciona normalmente**: teammates leen `CLAUDE.md` de su working directory.

---

## 19. Cheatsheet operativo

### Comandos rápidos
```text
# Crear team
"Create an agent team to <task>. Spawn N teammates: <roles>."

# Especificar modelo
"Use Sonnet for each teammate."

# Plan approval
"Require plan approval before they make any changes."

# Usar subagent definition
"Spawn a teammate using the <subagent-name> agent type to <task>."

# Mantener al lead esperando
"Wait for your teammates to complete their tasks before proceeding."

# Apagar un teammate
"Ask the <name> teammate to shut down."

# Cleanup
"Clean up the team."
```

### Decision tree rápido
```
¿La task se beneficia de paralelismo?
├─ NO → sesión sola
└─ SÍ →
   ¿Workers necesitan hablarse entre sí?
   ├─ NO → subagents
   └─ SÍ →
      ¿Pueden trabajar sobre archivos distintos?
      ├─ NO → repensar particionamiento o sesión sola
      └─ SÍ → agent team (3-5 teammates, 5-6 tasks c/u)
```

### Checklist pre-spawn
- [ ] Task es paralelizable (no secuencial, no same-file).
- [ ] `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` está seteado.
- [ ] Versión Claude Code ≥ v2.1.32.
- [ ] Permisos comunes pre-aprobados.
- [ ] Display mode adecuado (in-process default está bien).
- [ ] Spawn prompts incluyen contexto task-specific (no asumas que heredan conversación).
- [ ] Naming explícito si planeas referenciar teammates después.
- [ ] Plan approval activado para cambios riesgosos.
- [ ] Hooks configurados si necesitas quality gates.

### Checklist post-completion
- [ ] Verificar que todas las tasks están en `completed`.
- [ ] Sintetizar findings (si era research/review).
- [ ] Apagar teammates.
- [ ] Cleanup del team con el lead.
- [ ] Verificar que no hay tmux sessions huérfanas.

---

## 20. Referencias externas

- Doc oficial: https://code.claude.com/docs/en/agent-teams
- Subagents (alternativa más liviana): https://code.claude.com/docs/en/sub-agents
- Hooks: https://code.claude.com/docs/en/hooks
- Settings: https://code.claude.com/docs/en/settings
- Permissions: https://code.claude.com/docs/en/permissions
- Worktrees (paralelismo manual): https://code.claude.com/docs/en/worktrees
- Token costs: https://code.claude.com/docs/en/costs#agent-team-token-costs
- Comparison subagent vs team: https://code.claude.com/docs/en/features-overview#compare-similar-features
