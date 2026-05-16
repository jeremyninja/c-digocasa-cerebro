# Memoria de sesión — Protocolo de Verdades Ocultas + cierre Código Casa

**Fecha:** 2026-05-15
**Sesión:** Jornada larga con automatización de hallazgos por pilar (cloud routines) + diseño del Protocolo de Lectura en Tensión.
**Para qué sirve este documento:** memoria operativa para Team Hallazgo Código Casa. Recoge el framework, los aprendizajes y los verbatims-oro de la sesión. Punto de referencia para futuras tandas de hallazgos por pilar.

---

## 1. Lo que se montó en infraestructura

### Repo cerebro
- `c-digocasa-cerebro` (GitHub privado, jeremyninja/c-digocasa-cerebro)
- Contiene Data System + Agentes Hallazgos + .claude/ (agents + skills) + Data System Mujer Finanzas
- Push back funciona vía PAT fine-grained (Contents Read+Write, scope al solo repo, 30d expiración)

### Cloud routines (Anthropic remote agents)
- Una routine por pilar, schedule cron escalonado 4h entre disparos para respetar rate limits 5h
- Workflow: cazador → editor → montador → commit + push automático
- Persist_session: false (cada session se evapora al terminar — los outputs DEBEN pushear o se pierden)
- Configurado: PAT en `git remote set-url` antes de cualquier operación de push

### Pilares procesados a la fecha
- Bienestar (sesión interactiva previa, referencia de calidad)
- Mujer v2 (CC + Finance Women, exclusión Banreservas) → v3 (25 hallazgos)
- Sistema de Creencias (15 hallazgos + crítica de cuali sobre vulnerabilidad)
- Opiniones Políticas (14 hallazgos + reframes anti-AI)
- En cola: Alimentación, Roles de Género, Tecnología, Consumos, Educación

### Versiones de specs de diseño
- **v5:** stats 10×3cm (378×113pt), descripción 13pt, headline 50pt fijo
- **v6:** Consumer Voice verbatim 50pt (era 60pt), cards cuali 15×6cm (567×227pt, era 549×221pt)

---

## 2. EL FRAMEWORK CENTRAL — Protocolo de Lectura en Tensión

> *El cuanti dice qué pasa. El cuali dice cómo se llama. La verdad escondida vive en el espacio entre los dos.*

Cinco cruces operativos que el editor debe correr ANTES de cerrar cada hallazgo:

### Cruce 1 — Contradicción interna del cuanti
Buscar dos cifras del mismo set que se contradicen lógicamente. Si A% se declara X pero solo B% actúa X (B << A), ahí hay grieta cultural.
- *Ej:* 30.2% "muy practicante religioso" + 2.2% "dejó productos por fe" → rito sin sacrificio.
- *Ej:* 74% planifica + 50% no ahorra → la administradora ejemplar no falla por planificación, le falla el ingreso.

### Cruce 2 — Brecha semántica cuanti × cuali
Tomar la categoría más fuerte del cuanti (ej. "violencia económica") y buscarla literal en los FG. Si aparece poco y la conducta sí aparece con otro nombre, hay sub-reporte semántico.
- *Ej:* cuanti dice "violencia económica 20%", cuali dice "él es el proveedor", "aguantar".
- *Ej:* cuanti dice "orgullo financiero 5.5%", cuali dice "salir adelante", "mudarme sola".
- *Ej:* cuanti dice "política", cuali dice "politiquería" — categorías distintas.

### Cruce 3 — Sospecha del "ninguno / nunca / no"
Cuando una respuesta negativa >50%, tratarla como sospechosa por defecto. Buscar en cuali si la conducta sí aparece con otro encuadre.
- *Ej:* 75% "mi hijo no sufrió bullying" + cuali "generación de cristal" → minimización.
- *Ej:* 56% "no sufrí violencia" + cuali "aguante", "respuesta al amor" → vocabulario heredado.
- *Ej:* 48.5% "no hace nada por su salud" + cuali "cogerlo al paso", "estudiar para drenar" → autocuidado existente sin permiso de nombrarse.

### Cruce 4 — Efecto sin causa
Buscar si la gente pide un efecto deseado sin pedir la causa estructural. Cuando hay desproporción (60% pide A, <15% pide condición B necesaria), eso revela ideal sin disposición de pago.
- *Ej:* 63% "padres más presentes" vs 13% "flexibilidad laboral".
- *Ej:* 54.6% pide "escuelas eduquen finanzas" vs 8.8% "yo misma".

### Cruce 5 — Transmisión intergeneracional
El cuanti pregunta a la víctima/protagonista actual. El cuali revela cómo se está formando la próxima generación. Buscar verbatims donde el adulto narre dos cosas a la vez: lo que aprendió de su mamá/papá Y lo que su hijo/a está aprendiendo de él/ella.
- *Ej:* "Mi mamá me decía hay que aguantar" + "Mi hija entiende que si me golpea es respuesta al amor" → 3 generaciones de violencia naturalizada.
- *Ej:* "Mi mamá me mandaba a vender conconetes" → educación financiera por línea femenina.

### Reporte interno del protocolo

Al final de cada hallazgo, el editor reporta:
```
PROTOCOLO LECTURA EN TENSIÓN aplicado:
- Cruce 1 (contradicción interna): [hallazgo o N/A]
- Cruce 2 (brecha semántica): [palabras buscadas + frecuencia en FG, hallazgo o N/A]
- Cruce 3 (sospecha del "ninguno"): [hallazgo o N/A]
- Cruce 4 (efecto sin causa): [hallazgo o N/A]
- Cruce 5 (transmisión intergeneracional): [verbatims encontrados o N/A]
- Conclusión: hallazgo profundizado / hallazgo plano confirmado / falta data
```

---

## 3. Macrotensión del estudio Código Casa

Después de profundizar 3 pilares (Mujer, Creencias, Opiniones Políticas), emerge un patrón consistente que puede ser la macrotensión del estudio completo:

> **El dominicano declara los ideales en el lenguaje del cuestionario y vive los procesos en otro vocabulario.** Pide efectos sin tocar causas. Hereda categorías que le ahorran nombrar lo que vive. Lo declarado mide el techo del reconocimiento — lo vivido vive un piso más abajo, en otras palabras.

Manifestaciones:
- **Violencia:** declara "no fui víctima" (56%), vive "aguante", "amor", "orden del hogar".
- **Bullying:** declara "mi hijo no" (75%), vive "generación de cristal", "sensibilidad excesiva".
- **Política:** declara "no me interesa" (58%), vive rechazo a "politiquería" + ciudadanía cotidiana activa.
- **Vulnerabilidad:** rankea a las mujeres #1 vulnerables, 91% de mujeres dice "no fui víctima de discriminación".
- **Padres presentes:** declara que se necesita "presencia" (63%), no pide flexibilidad laboral que la haría posible (13%).
- **Religión:** declara "muy practicante" (30.2%), no abandona consumo por fe (2.2%).
- **Mujer y dinero:** declara "orgullo" 5.5%, expresa orgullo de "haberme mudado sola", "no deberle a nadie".

---

## 4. Verbatims-oro encontrados en esta sesión (para futuras tandas)

### Pilar Mujer — transmisión generacional + estructura
> «Mi mamá me enseñó desde pequeña cómo yo tenía que manejarme y guardar mi dinero, pero me enseñó que primero tengo que ganarme. Me mandaba a vender conconetes para la calle, y yo era chiquita.» — *Familia Masivo Emprendedoras (FW)*

> «Aunque mis hijos se lleven el 100%, uno siempre se queda como más rezagado y se deja para último. La comida saludable de ellos no la hago necesariamente para mí.» — *Familia Mixta*

> «Me siento orgullosa de haberme mudado sola. Lo fuerte que yo he sido, lo lejos que yo he llegado.» — *Familia Masivo Jóvenes (FW)*

> «Me entré a la cooperativa de la empresa para que no me extraigan el dinero. Es la única forma que ese dinero no entre a mi cuenta y salga.» — *Familia Preferente Jefas de Hogar (FW)*

### Pilar Sistema de Creencias — generación de cristal + transmisión violencia
> «La generación de cristal son los más sensibles, que cualquier cosita tú le haces, que te voy a acusar, que me voy a hacer sensible, que me voy a suicidar.» — *Familia Biparental Hijos Pequeños*

> «Yo la crié como en una burbuja de cristal.» — *Familia Monoparental*

> «Mi mamá siempre le aguantó muchas cosas a mi padrastro por mantener la familia unida. Yo me crié con esos dos conceptos: hay que aguantar.» — *Familia Monoparental*

### Pilar Opiniones Políticas — politiquería + clase media resentida + crítica estructural
> «A la gente no le gusta hablar de política. La gente entiende que la política es la campaña política, la politiquería o el partidismo. Eso no es política. Hasta tú salir a beberte una cerveza es político.» — *Familia Sin Hijos*

> «Ya el concepto de la política antes había mucha política de buena intención. Hoy en día hay un vacío. Estamos en: vamos a una política, oye este apoyo, por el parque tú me das lo mío. Ya esa es la mentalidad. Ya todo está jodido, total.» — *Familia Mixta*

> «Hasta que el Estado no indique que sus servidores públicos hagan uso de las escuelas públicas, esto no va a cambiar. En el momento que un funcionario tenga que mandar a sus hijos a una escuela pública, eso cambia.» — *Familia Biparental con Hijos Pequeños*

> «Mi esposo dijo que no iba a votar. Le dije, ¿por qué? — Porque tú eres un ladrón. ¿Y me vota para que lo saques? — No. Estos son peores.» — *Familia Biparental con Hijos Pequeños*

> «La clase trabajadora, yo lo veo en el sentido de que beneficios tú le das beneficio a lo pobre a costilla mía. Pero cuando yo estoy en la misma situación sin trabajo, tú no me das beneficio. Yo desde que entró la pandemia duré cuatro meses sin empleo, a mí nadie me dio bono. Y yo dije: nosotros vivimos matando, no calificamos para nada. La clase trabajadora es la que mantiene a los pobres y también le mantiene las empresas a los ricos.» — *Familia Sin Hijos*

---

## 5. Aprendizajes operativos de la sesión (para no repetir errores)

### Sobre las routines cloud
- **El PAT debe estar en la routine ANTES del primer disparo.** Si se agrega después, hay que re-disparar y se pierden los outputs del disparo previo (persist_session=false).
- **El cazador remoto reutiliza scripts previos del repo sin re-leer specs.** Cuando se hace v5 → v6, hay que patchear el build_*.py o el agente generará dimensiones viejas. Documentado en aprendizajes-montador-cc.md sección de LECCIÓN OPERATIVA CRÍTICA.

### Sobre la voz editorial
- **"No es X, es Y" es la marca de IA más persistente del corpus.** El editor debe leer 7.bis y 7.ter cada vez. Patrones a eliminar: "imaginario", "chip", "narrativa" repetidos; "tener nombre de X"; "X no se enteró"; "la realidad cambió, X no"; "el verdadero X".
- **"Sobre-explicación" es el segundo patrón AI:** "Esto demuestra que…", "Lo que está en juego es…". Si el dato y el verbatim ya cuentan la historia, la lección moral sobra.

### Sobre el cazador
- **Los hallazgos solos univariados son piso, no techo.** El cazador entrega bien las cifras y los verbatims, pero la VERDAD OCULTA emerge al cruzar dos preguntas distintas o al confrontar cuanti × cuali. Ese trabajo lo hace el editor con el Protocolo de 5 Cruces.
- **Las preguntas abiertas sin codificar son mina sin explotar.** Q56 (creencias sobre familias del mismo sexo), Q60 (formas de cambio), etc. tienen cientos de verbatims que el derivado no procesa. Vale la pena codificarlas temáticamente.

### Sobre el deck
- **v6 dimensions:** stats 378×113pt fijo (10×3cm), descripción 13pt, headline 50pt fijo (no auto-size), CV verbatim 50pt Instrument Serif, cards cuali 567×227pt (15×6cm), side by side, padding 30/25pt para cuali (NO 80/60 que era del CV legacy).
- **SOURCE al pie solo en Mujer.** Otros pilares no llevan source (regla v5).
- **Slide cuali side by side** para hallazgos solo-cuali con 2-3 verbatims. Stack vertical NO.

---

## 6. Próximos pasos para Team Hallazgo

### Inmediato (esta semana)
- [ ] QA visual de Mujer v3, Sistema de Creencias, Opiniones Políticas en Keynote
- [ ] Aplicar reframes con Protocolo de 5 Cruces a Opiniones Políticas (6 slides + 1 nuevo cuali)
- [ ] Revisar outputs de Alimentación, Roles de Género, Tecnología, Consumos, Educación cuando lleguen las routines

### Pendiente de orquestación
- [ ] Codificación temática de preguntas abiertas (Q56 Creencias, P61 Política, M45b Mujer) — abre 3-4 hallazgos cuali nuevos por pilar.
- [ ] Re-tabular Q62 Creencias y P64 Política desde xlsx — preguntas con data colapsada en derivado.
- [ ] Identidad y Finanzas: pendientes de procesar (los últimos 2 pilares para cerrar el estudio).

### Knowledge base
- [ ] El framework de 5 Cruces ya está en `aprendizajes-editor-cc.md` sección 0. Es la primera cosa que lee el editor en cada pilar.
- [ ] La macrotensión "vocabulario declarado vs vocabulario vivido" debería volverse el hallazgo macro del estudio completo en el deck consolidado.

---

## 7. Reglas de cita rápida (para no abrir aprendizajes-editor cada vez)

**Atribución:** solo tipología familiar — "Familia Monoparental", "Familia Sin Hijos", "Familia Mixta", "Familia Extendida", "Familia Biparental con Hijos Pequeños", "Familia Biparental con Hijos Adultos", "Familia Homoparental". Para FW: "Familia Masivo Jóvenes", "Familia Masivo Jefas de Hogar", "Familia Masivo Líderes", "Familia Masivo Emprendedoras", "Familia Preferente [perfil]".

**Comillas:** españolas «...» en todos los verbatims publicables.

**Source format:** `Source: Código Casa — Estudio cuantitativo + cualitativo 2025 · Q##/P## · Base 500.` (NO Banreservas en source del FW — usar "Estudio Mujer y Finanzas" en su lugar).

**Headline:** ≤190 chars, split plain/italic, MAYÚSCULAS, Instrument Serif 50pt.

**Stats:** 3 elementos típicos. Cifra grande Instrument Serif 180pt italic, descripción Poppins 13pt en caja 10×3cm.

---

*Fin de la memoria. Mantener este documento actualizado conforme se procesen los pilares restantes (Identidad, Finanzas) y se profundicen los actuales con el Protocolo de Lectura en Tensión.*
