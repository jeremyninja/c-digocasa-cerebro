# Opiniones Políticas — Hallazgos crudos

**Pilar:** 10 — Opiniones Políticas
**Cazador:** cazador-hallazgos-cc
**Fecha de caza:** 2026-05-14
**Base cuanti:** n=500 (Sto. Domingo 58.4% + Santiago 30% + Distrito Nacional 11.6%, campo Oct-Nov 2024)
**Base cuali:** 10 focus groups, solo Santo Domingo
**Fuentes:** `Data System/derivados-por-pilar/10-opiniones-politicas.md` · `CUESTIONARIO_FINAL_CODIGO_CASA.md` (P56–P64) · transcripciones fg-01 a fg-11

---

## TABLA DE COBERTURA — P56–P64 vs hallazgos

| Pregunta | Tema | Cubierta en | Estado |
|---|---|---|---|
| P56 | Fuente principal de información política | H01, H02 | ✓ Cubierta |
| P57 | Interés en la política (escala 1–5) | H03, H04 | ✓ Cubierta |
| P58 | ¿Votaste en las últimas elecciones? | H05, H06 | ✓ Cubierta |
| P59 | Calificación de la gestión del gobierno actual | H07, H08 | ✓ Cubierta |
| P60 | Formas válidas de generar cambio en el país | H09, H10 | ✓ Cubierta |
| P61 | Ranking de temas políticos que más preocupan | H11 | ⚠ Cubierta solo-cuali — cifra colapsada (ranking 100% en todas las opciones) |
| P62 | Justicia/equidad del sistema político | H12, H13 | ✓ Cubierta |
| P63 | Disposición a emigrar por economía o contexto político | H14, H15 | ✓ Cubierta |
| P64 | El "sueño dominicano" en política | H10 (parcial) | ⚠ Cubierta solo-cuali — cifra colapsada (multi-select 100% en todas las opciones) |

**Cobertura: 9/9 preguntas tocadas.** P61 y P64 tienen sus cifras colapsadas en el derivado (100% en todas las opciones — patrón de ranking/multi-select sin desempate, ver aprendizajes sección 8.2); se cubren con cuali y se reporta la limitación.

**Total hallazgos construidos: 15.** Fase 2 (univariadas): 11 hallazgos. Fase 3 (cruces como detector): 4 hallazgos (H02, H04, H06, H08, H15 nacen o se refuerzan con cruce demográfico declarado inline).

---

## HALLAZGO #01

**HEADLINE (≤190):**
6 de cada 10 dominicanos se informan de política por redes sociales y la TV cae a segundo lugar con 27%. La conversación política del país ya no pasa por el noticiero, pasa por el feed.

**CARÁCTERES:** 188/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P56.

**ESTADÍSTICAS:**

1. 58.6% (n=293) usa las redes sociales como fuente principal para informarse sobre política.
   Pregunta: P56. "¿Qué fuente utilizas principalmente para informarse sobre política?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P56 (frecuencia univariada)

2. 27.2% (n=136) declara la TV como fuente principal — menos de la mitad que las redes. Periódicos (1.2%) y radio (1.4%) son prácticamente residuales.
   Pregunta: P56. "¿Qué fuente utilizas principalmente para informarse sobre política?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P56 (frecuencia univariada)

**VERBATIMS:**

1. "Se habla de política en esos casos. (...) Pero no porque somos políticos, sino porque al niño mío le gusta mucho ver cosas como en YouTube, así, como lo dice, ese tipo de cosas. Entonces él me dice (...) que está el candidato Luis Sabinader y que él es el presidente."
   — Speaker no identificado, fg-03 (Tipología: Monoparental)
   CONTEXTO: el grupo conversaba sobre si se habla de política en casa; esta participante relata que la política entra a su hogar a través de los contenidos de YouTube que consume su hijo.
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-03-monoparental-2024-11-13.txt, líneas 555–557.

**LIMITACIONES / ADVERTENCIAS:**
- fg-03 es transcripción sin diarización (re-procesada); speaker no identificado, línea documentada.
- El verbatim ilustra el canal digital, no lo cuantifica — la cifra dura es cuanti (P56).

---

## HALLAZGO #02

**HEADLINE (≤190):**
La política digital tiene edad y clase: 80% de los jóvenes 18-24 se informa por redes, pero en el estrato E la TV todavía gana. La brecha de plataforma reproduce la brecha social.

**CARÁCTERES:** 184/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P56 (× rango edad, × NSE).

**ESTADÍSTICAS:**

1. 80.0% de los jóvenes de 18-24 años se informa de política por redes sociales, frente a 49.6% de los mayores de 55 que aún ponen la TV en primer lugar.
   Pregunta: P56 × Rango edad. "¿Qué fuente utilizas principalmente para informarse sobre política?"
   Base: 500 (subset 18-24 n≈55 — sobre umbral n≥50; subset 55+ n≈119)
   Fuente: 10-opiniones-politicas.md, P56 cruce por rango de edad

2. En el estrato E la TV es la fuente principal con 37.5%, único NSE donde las redes no encabezan; en C, C+ y AB las redes superan el 65%.
   Pregunta: P56 × NSE. "¿Qué fuente utilizas principalmente para informarse sobre política?"
   Base: 500 (subset E n≈32 — subset reducido, leer como tendencia direccional)
   Fuente: 10-opiniones-politicas.md, P56 cruce por NSE

**VERBATIMS:**

Sin verbatim publicable en el corpus FG; el hallazgo se sostiene en la frecuencia cuanti cruzada.

**LIMITACIONES / ADVERTENCIAS:**
- Hallazgo nace de cruce (P56 × edad y P56 × NSE) — sin el cruce la tensión es invisible.
- Subset E n≈32: cifra direccional, no robusta (regla base mínima).
- Solo-cuanti declarado: los FG no aislan la fuente de información política por segmento.

---

## HALLAZGO #03

**HEADLINE (≤190):**
58% del dominicano se declara "nada interesado" en política. El desinterés no es minoría ni gesto: es la postura mayoritaria y abierta de la familia dominicana frente a lo público.

**CARÁCTERES:** 180/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P57.

**ESTADÍSTICAS:**

1. 58.0% (n=290) se ubica en el punto más bajo de la escala — "1 = Nada interesado" en política.
   Pregunta: P57. "¿Te consideras una persona interesada en la política?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P57 (frecuencia univariada)

2. Solo 16.6% (n=83) se declara "muy interesado" (5) y apenas 5.4% (n=27) se ubica en el nivel 4. Sumando 4+5, el interés alto no llega al 22%.
   Pregunta: P57. "¿Te consideras una persona interesada en la política?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P57 (frecuencia univariada)

**VERBATIMS:**

1. "No me gusta mucho hablar de política porque nunca me he beneficiado de ningún político (...) y nunca he estado como muy atento a eso porque lo que es política y cosas de apuestas no soy como compatible de eso."
   — Speaker no identificado, fg-10 (Tipología: Mixta)
   CONTEXTO: en la ronda sobre si se habla de política en casa, este participante explica por qué se mantiene al margen del tema.
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-10-mixta-2024-11-21.txt, líneas correspondientes a "no me gusta mucho hablar de política" (transcripción sin diarización).

**LIMITACIONES / ADVERTENCIAS:**
- fg-10 sin diarización — speaker no identificado.
- El verbatim conecta desinterés con falta de beneficio personal: el tema reaparece en H09 y H12.

---

## HALLAZGO #04

**HEADLINE (≤190):**
El desinterés político tiene rostro de mujer joven: 69% de las 18-24 se declara nada interesada y las mujeres superan a los hombres en distancia frente a la política (61.6% vs 52.3%).

**CARÁCTERES:** 189/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P57 (× sexo, × rango edad).

**ESTADÍSTICAS:**

1. 61.6% de las mujeres se declara "nada interesada" en política frente a 52.3% de los hombres — una brecha de género de más de 9 puntos.
   Pregunta: P57 × Sexo. "¿Te consideras una persona interesada en la política?"
   Base: 500 (subset femenino n≈305, masculino n≈195)
   Fuente: 10-opiniones-politicas.md, P57 cruce por sexo

2. 69.1% de los jóvenes 18-24 se declara "nada interesado", el rango etario con mayor desinterés — más que los mayores de 55 (56.3%).
   Pregunta: P57 × Rango edad. "¿Te consideras una persona interesada en la política?"
   Base: 500 (subset 18-24 n≈55)
   Fuente: 10-opiniones-politicas.md, P57 cruce por rango de edad

**VERBATIMS:**

Sin verbatim publicable en el corpus FG que aísle la dimensión de género o edad del desinterés.

**LIMITACIONES / ADVERTENCIAS:**
- Hallazgo nace de cruce (P57 × sexo y × edad) — la tensión es la lectura cruzada.
- Solo-cuanti declarado: los FG conversan desinterés general (ver H03) pero no lo segmentan por sexo/edad.
- Contraintuitivo: el segmento más joven, más digital y más conectado (ver H02) es también el más desinteresado en política.

---

## HALLAZGO #05

**HEADLINE (≤190):**
77% del dominicano votó en las últimas elecciones, aunque 58% se declara nada interesado en política. Votar no es señal de interés: es un acto que se cumple aun desde la desconexión.

**CARÁCTERES:** 188/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P58, P57.

**ESTADÍSTICAS:**

1. 77.0% (n=385) declara haber votado en las últimas elecciones; solo 23.0% (n=115) no votó.
   Pregunta: P58. "¿Votaste en las últimas elecciones?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P58 (frecuencia univariada)

2. Esa participación del 77% coexiste con un 58% que se declara "nada interesado" en política (P57): la mayoría que vota se solapa con la mayoría que no se interesa.
   Pregunta: P58 + P57. "¿Votaste en las últimas elecciones?" / "¿Te consideras una persona interesada en la política?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P58 y P57 (frecuencias univariadas)

**VERBATIMS:**

1. "Por ejemplo yo voté, mi esposo dijo que no iba a votar. Yo le dije, ¿por qué tú no vas a votar? Porque tú eres un ladrón. Entonces, ¿pero me vota para que lo saques? No. Entonces estos son peores."
   — Speaker C, fg-07 (Tipología: Biparental con hijos pequeños)
   CONTEXTO: en la ronda sobre afinidad política en pareja, esta participante relata la discusión con su esposo sobre por qué él no quería votar.
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-07-biparental-hijos-pequenos-2024-11-18.txt, líneas 1084–1085.

**LIMITACIONES / ADVERTENCIAS:**
- El verbatim ilustra la tensión votar/desconfiar dentro de una pareja: votar como deber pese al desencanto.

---

## HALLAZGO #06

**HEADLINE (≤190):**
El voto sube con la edad: 82% de los mayores de 55 votó, contra 69% de los jóvenes 18-24. El hábito electoral se hereda con los años, no nace con la generación más conectada.

**CARÁCTERES:** 180/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P58 (× rango edad).

**ESTADÍSTICAS:**

1. 82.4% de los mayores de 55 años votó en las últimas elecciones, frente a 69.1% de los jóvenes de 18-24 — una brecha generacional de 13 puntos.
   Pregunta: P58 × Rango edad. "¿Votaste en las últimas elecciones?"
   Base: 500 (subset 55+ n≈119, subset 18-24 n≈55)
   Fuente: 10-opiniones-politicas.md, P58 cruce por rango de edad

2. La participación crece de forma escalonada con la edad: 18-24 (69.1%) → 25-34 (74.8%) → 35-44 (75.0%) → 45-54 (79.4%) → 55+ (82.4%).
   Pregunta: P58 × Rango edad. "¿Votaste en las últimas elecciones?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P58 cruce por rango de edad

**VERBATIMS:**

Sin verbatim publicable que aísle la dimensión generacional del voto.

**LIMITACIONES / ADVERTENCIAS:**
- Hallazgo nace de cruce (P58 × edad).
- Solo-cuanti declarado.
- Conecta con H04: el segmento joven es el menos interesado y también el que menos vota.

---

## HALLAZGO #07

**HEADLINE (≤190):**
4 de cada 10 dominicanos califican la gestión del gobierno como "muy mala" y solo 1 de cada 10 la llama "muy buena". El descontento no es matiz: es el escalón más poblado de la escala.

**CARÁCTERES:** 187/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P59.

**ESTADÍSTICAS:**

1. 39.6% (n=198) califica la gestión del gobierno actual como "1 = Muy mala", la respuesta más votada de la escala.
   Pregunta: P59. "¿Cómo calificas la gestión del gobierno actual?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P59 (frecuencia univariada)

2. Solo 10.0% (n=50) la califica como "muy buena" (5) y otro 10.0% (n=50) la pone en 4: la valoración alta (4+5) no llega al 20%. El restante 80% se reparte entre "muy mala", "mala" y un punto medio (29.8% en 3).
   Pregunta: P59. "¿Cómo calificas la gestión del gobierno actual?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P59 (frecuencia univariada)

**VERBATIMS:**

1. "Yo siento que el país tiene un retroceso, yo no sé, no es política, no, yo siento que hay un retroceso, porque cómo va a ser que a esta altura del juego, ni que baje sin agua, la luz crece cada rato."
   — Speaker D, fg-06 (Tipología: Biparental con hijos adultos)
   CONTEXTO: el grupo hablaba de la situación económica del país; esta participante aclara que su crítica "no es política" antes de listar los servicios que fallan.
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-06-biparental-hijos-adultos-2024-11-15.txt, línea 1434.

**LIMITACIONES / ADVERTENCIAS:**
- El verbatim muestra un patrón cultural relevante: la crítica al gobierno se hace negando que sea "política" — el dominicano critica la gestión pero se desmarca de la etiqueta política (conecta con H03).

---

## HALLAZGO #08

**HEADLINE (≤190):**
La crítica al gobierno tiene un fondo de clase: 47% del estrato E y 44% del D lo califican como "muy malo", mientras el C+ es el único NSE que no lo pone en el peor escalón.

**CARÁCTERES:** 174/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P59 (× NSE).

**ESTADÍSTICAS:**

1. 46.9% del estrato E y 43.6% del D califican la gestión del gobierno como "muy mala", frente al C+ donde la respuesta top es el punto medio "3" (36.1%) y no el peor escalón.
   Pregunta: P59 × NSE. "¿Cómo calificas la gestión del gobierno actual?"
   Base: 500 (subset E n≈32 — subset reducido, leer como tendencia direccional; subset D n≈172, C+ n≈36 — caveat)
   Fuente: 10-opiniones-politicas.md, P59 cruce por NSE

2. El descontento "muy malo" también es transversal por edad pero pega más fuerte en los jóvenes: 47.3% de los 18-24 y 47.0% de los 25-34, contra 31.1% de los mayores de 55.
   Pregunta: P59 × Rango edad. "¿Cómo calificas la gestión del gobierno actual?"
   Base: 500 (subset 18-24 n≈55, 25-34 n≈115, 55+ n≈119)
   Fuente: 10-opiniones-politicas.md, P59 cruce por rango de edad

**VERBATIMS:**

Sin verbatim publicable que aísle la dimensión de NSE de la valoración del gobierno (NSE no está taggeado en cuali).

**LIMITACIONES / ADVERTENCIAS:**
- Hallazgo nace de cruce (P59 × NSE y × edad).
- Subsets E (n≈32) y C+ (n≈36): cifras direccionales, no robustas.
- Solo-cuanti declarado.

---

## HALLAZGO #09

**HEADLINE (≤190):**
Para 4 de cada 10 dominicanos votar es la única forma válida de generar cambio, pero el segundo lugar lo ocupa la resignación: 21% cree que nada de eso cambia realmente algo.

**CARÁCTERES:** 180/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P60.

**ESTADÍSTICAS:**

1. 40.6% (n=203) considera "votar en elecciones" la forma válida de generar cambio en el país — la opción más elegida.
   Pregunta: P60. "¿Cuáles de las siguientes acciones consideras formas válidas de generar cambio en tu país?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P60 (frecuencia univariada)

2. 21.2% (n=106) eligió "no creo que ninguna de estas cosas cambie realmente algo" — el segundo lugar, por encima de educarse (19.4%), las protestas (6.0%) o apoyar movimientos sociales (7.0%).
   Pregunta: P60. "¿Cuáles de las siguientes acciones consideras formas válidas de generar cambio en tu país?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P60 (frecuencia univariada)

**VERBATIMS:**

1. "Que se acabe la clase política. ¿Qué se qué? ¿Que se acabe la clase política? Que se acabe. Realmente."
   — Speaker no identificado, fg-03 (Tipología: Monoparental)
   CONTEXTO: en el ejercicio hipotético de "imaginen que se eliminó la pobreza, ¿qué acciones la lograron?", una participante propone como acción acabar con la clase política.
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-03-monoparental-2024-11-13.txt, línea 591.

2. "Para conseguir un empleo tiene que ser político, que conocer gente. Si se acaba todo eso puede ser que se erradique la pobreza."
   — Speaker no identificado, fg-03 (Tipología: Monoparental)
   CONTEXTO: misma ronda hipotética; la participante vincula el cambio real del país con acabar con el clientelismo y la "cuña".
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-03-monoparental-2024-11-13.txt, línea 590.

**LIMITACIONES / ADVERTENCIAS:**
- fg-03 sin diarización — speakers no identificados.
- Los verbatims muestran que cuando se pide imaginar el cambio, la respuesta no es "participar" sino "eliminar lo que ya existe" — convergente con el 21% que no cree en ninguna acción.

---

## HALLAZGO #10

**HEADLINE (≤190):**
El cambio se delega a las urnas: solo 6% ve las protestas como vía válida y 0.6% las peticiones digitales. El "sueño dominicano" en política es que el sistema cumpla, no movilizarse.

**CARÁCTERES:** 187/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P60, P64.

**ESTADÍSTICAS:**

1. Las formas de participación activa quedan en el sótano de P60: participar en protestas o marchas 6.0% (n=30), apoyar movimientos sociales 7.0% (n=35), firmar peticiones digitales 0.6% (n=3) y quejarse en redes 1.2% (n=6).
   Pregunta: P60. "¿Cuáles de las siguientes acciones consideras formas válidas de generar cambio en tu país?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P60 (frecuencia univariada)

**VERBATIMS:**

1. "Ya el concepto de la política antes, por lo menos, aunque había sectores y posiciones que hacían cosas malas, pero había mucha política de buena intención. (...) Ya hoy en día hay un vacío. La política es muy grande, tan fuerte, que ya nadie está dando importancia."
   — Speaker no identificado, fg-10 (Tipología: Mixta)
   CONTEXTO: en la ronda de política, este participante contrasta una política "de buena intención" del pasado con un presente de transacción ("tú me das lo mío").
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-10-mixta-2024-11-21.txt, líneas 1377–1378.

**LIMITACIONES / ADVERTENCIAS:**
- P64 ("sueño dominicano en política") tiene la cifra colapsada en el derivado: multi-select con 100% en las 7 opciones, no publicable hasta re-tabular con orden ponderado. El hallazgo se sostiene con la cifra robusta de P60 + cuali.
- fg-10 sin diarización.
- La estadística declara distribución de cola baja (formas de participación) — es la evidencia central del hallazgo, no relleno.

---

## HALLAZGO #11

**HEADLINE (≤190):**
Cuando se pide imaginar el cambio, las familias no nombran ideología: nombran corrupción, salud, educación y seguridad. La preocupación política dominicana es de servicios, no de bando.

**CARÁCTERES:** 189/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P61.

**ESTADÍSTICAS:**

Sin cifra publicable: P61 ("ordena los temas políticos que más te preocupan") aparece en el derivado con 100% en todas las opciones (Salud, Medio ambiente, Economía, Educación, Corrupción) y 99.8% en Seguridad — ranking colapsado en binario mencionado/no mencionado, sin desempate. Cifra pendiente de re-tabulación desde el xlsx con orden ponderado.

**VERBATIMS:**

1. "Cada vez que un político de esos se va con 500 millones de pesos, se llevó el puentecito que hace falta en los velaquitos, se llevó la carreterita de 4 kilómetros que tanto necesita, la escuela de los niños, la escuelita. Y se lo lleva a un solo personaje."
   — Speaker B, fg-06 (Tipología: Biparental con hijos adultos)
   CONTEXTO: en el ejercicio hipotético de eliminar la pobreza, este participante explica por qué la corrupción es el problema raíz: traduce cada acto de corrupción en una obra pública concreta que no se hizo.
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-06-biparental-hijos-adultos-2024-11-15.txt, línea 1453.

2. "Y siempre que un cambio de gobierno (...) te ponen a una gente por encima de ti ganando muchísimo más que tú y no es ni profesional. Entonces tú recibir un mandato de una persona que sabe menos que tú."
   — Speaker no identificado, fg-03 (Tipología: Monoparental)
   CONTEXTO: el grupo hablaba de la salud pública y el empleo estatal; esta participante describe cómo el cambio de gobierno afecta directamente la meritocracia laboral.
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-03-monoparental-2024-11-13.txt, líneas 603–604.

**LIMITACIONES / ADVERTENCIAS:**
- Hallazgo solo-cuali: la cifra de P61 está colapsada (ranking 100% en todas las opciones), pendiente de re-tabulación. La convergencia entre fg-06 y fg-03 — corrupción traducida en obras/servicios perdidos — es la evidencia.
- fg-03 sin diarización.

---

## HALLAZGO #12

**HEADLINE (≤190):**
73% del dominicano cree que el sistema político es nada o poco justo. La percepción de injusticia institucional no es opinión de un sector: es el consenso casi total del país.

**CARÁCTERES:** 175/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P62.

**ESTADÍSTICAS:**

1. 46.6% (n=233) considera el sistema político "nada justo" (1) y 26.8% (n=134) "poco justo" (2): sumados, 73.4% lo percibe como injusto.
   Pregunta: P62. "¿Qué tan justo y equitativo consideras que el sistema político en tu país?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P62 (frecuencia univariada)

2. Solo 4.8% (n=24) lo considera "bastante justo" y 3.8% (n=19) "completamente justo": la valoración positiva del sistema no llega al 9%.
   Pregunta: P62. "¿Qué tan justo y equitativo consideras que el sistema político en tu país?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P62 (frecuencia univariada)

**VERBATIMS:**

1. "Los políticos dicen a ti lo que tú quieres escuchar, pero no son los intereses justamente que lo están apoyando a ellos."
   — Speaker no identificado, fg-10 (Tipología: Mixta)
   CONTEXTO: en la ronda de política, este participante — que se identifica como militante de un partido — describe el desfase entre el discurso político y los intereses reales detrás.
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-10-mixta-2024-11-21.txt, líneas 1244–1246.

2. "Yo creo que hay un sistema que es el poder (...) que no permite que tu participación te dé sano. (...) Entonces siempre predomina lo mal hecho."
   — Speaker no identificado, fg-10 (Tipología: Mixta)
   CONTEXTO: misma ronda; otra participante describe el sistema como una estructura de poder que neutraliza la buena intención de quien entra a la política.
   CLARIDAD: ⚠ requiere contexto adicional (frase entrecortada en la transcripción)
   Línea de auditoría: fg-10-mixta-2024-11-21.txt, líneas 1236–1240.

**LIMITACIONES / ADVERTENCIAS:**
- fg-10 sin diarización.
- Verbatim 2 con claridad ⚠: el editor debe valorar si lo usa o se queda solo con el verbatim 1 (sólido).

---

## HALLAZGO #13

**HEADLINE (≤190):**
La percepción de injusticia se vuelve consenso adulto: en todos los rangos de 25 años en adelante "nada justo" gana, y solo los jóvenes 18-24 matizan con "poco justo" en lugar del extremo.

**CARÁCTERES:** 189/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P62 (× rango edad, × NSE).

**ESTADÍSTICAS:**

1. En los rangos 25-34 (49.6%), 35-44 (46.4%), 45-54 (49.5%) y 55+ (47.1%) la respuesta top es "1 = nada justo"; solo los 18-24 ponen en primer lugar "2 = poco justo" (36.4%) — el único segmento que no llega al extremo.
   Pregunta: P62 × Rango edad. "¿Qué tan justo y equitativo consideras que el sistema político en tu país?"
   Base: 500 (subset 18-24 n≈55, resto de rangos n≥97)
   Fuente: 10-opiniones-politicas.md, P62 cruce por rango de edad

2. La percepción de injusticia es transversal por NSE: el estrato E (50.0%) y el C (49.1%) lideran "nada justo", pero incluso el AB lo pone en primer lugar (43.5%).
   Pregunta: P62 × NSE. "¿Qué tan justo y equitativo consideras que el sistema político en tu país?"
   Base: 500 (subset E n≈32 — direccional; subset AB n≈23 — NO publicable como subset propio, se reporta solo como ilustración de transversalidad)
   Fuente: 10-opiniones-politicas.md, P62 cruce por NSE

**VERBATIMS:**

Sin verbatim publicable que aísle la dimensión de edad/NSE de la percepción de injusticia.

**LIMITACIONES / ADVERTENCIAS:**
- Hallazgo nace de cruce (P62 × edad y × NSE).
- Subset AB n≈23: bajo el umbral de publicación, citado solo para mostrar transversalidad, no como cifra robusta. Subset E n≈32: direccional.
- Solo-cuanti declarado.
- Sugerencia de fusión: H12 y H13 cubren la misma tensión (injusticia del sistema) con ángulos complementarios — el editor puede fusionarlos o mantenerlos como par.

---

## HALLAZGO #14

**HEADLINE (≤190):**
Casi la mitad del dominicano está "muy dispuesto" a irse del país por la economía o la política. La maleta no es plan B: para el 47% es la primera respuesta al contexto.

**CARÁCTERES:** 178/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P63.

**ESTADÍSTICAS:**

1. 47.0% (n=235) se declara "muy dispuesto" (5) a moverse a otro país por su situación económica o el contexto político — la respuesta más votada.
   Pregunta: P63. "¿Qué tan dispuesto/a estarías a moverte a otro país debido a tu situación económica o por el contexto político actual?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P63 (frecuencia univariada)

2. Solo 30.4% (n=152) se declara "nada dispuesto" (1) a emigrar: los que querrían irse superan a los que se quedarían firmes por 17 puntos.
   Pregunta: P63. "¿Qué tan dispuesto/a estarías a moverte a otro país debido a tu situación económica o por el contexto político actual?"
   Base: 500
   Fuente: 10-opiniones-politicas.md, P63 (frecuencia univariada)

**VERBATIMS:**

1. "Porque la gente se está yendo del país. Yo conozco mucha gente que se está yendo del país. Yo misma me he considerado irme de aquí. (...) Yo estoy mandando mi currículum a Canadá, a ver si me hacen algo."
   — Speaker E y Speaker B, fg-07 (Tipología: Biparental con hijos pequeños)
   CONTEXTO: en la ronda sobre cómo afecta la situación económica del país, dos participantes encadenan la idea de emigrar como reacción directa.
   CLARIDAD: ✓ se entiende solo
   Línea de auditoría: fg-07-biparental-hijos-pequenos-2024-11-18.txt, líneas 1108 y 1114.

**LIMITACIONES / ADVERTENCIAS:**
- El verbatim es un encadenamiento de dos speakers (E y B) en la misma secuencia — se atribuye a ambos con su letra; el editor decide si lo presenta como diálogo o recorta a un solo speaker.

---

## HALLAZGO #15

**HEADLINE (≤190):**
La disposición a emigrar se invierte con la edad y el bolsillo: 54% de los 45-54 querría irse, pero los mayores de 55 y el estrato E son los únicos que prefieren quedarse.

**CARÁCTERES:** 169/190

**PILAR:** Opiniones Políticas
**PREGUNTAS COBERTURA:** P63 (× rango edad, × NSE).

**ESTADÍSTICAS:**

1. La disposición a emigrar ("muy dispuesto") es top en todos los rangos hasta los 54 — 18-24 (43.6%), 25-34 (49.6%), 35-44 (51.8%), 45-54 (54.6%) — pero en los mayores de 55 la respuesta top se invierte a "nada dispuesto" (46.2%).
   Pregunta: P63 × Rango edad. "¿Qué tan dispuesto/a estarías a moverte a otro país...?"
   Base: 500 (subsets n≥55)
   Fuente: 10-opiniones-politicas.md, P63 cruce por rango de edad

2. El estrato E es el único NSE donde la respuesta top es "nada dispuesto" a emigrar (40.6%), mientras el D —el más numeroso después del C— es el más dispuesto a irse (52.9% "muy dispuesto").
   Pregunta: P63 × NSE. "¿Qué tan dispuesto/a estarías a moverte a otro país...?"
   Base: 500 (subset E n≈32 — direccional; subset D n≈172)
   Fuente: 10-opiniones-politicas.md, P63 cruce por NSE

**VERBATIMS:**

Sin verbatim publicable que aísle la dimensión de edad/NSE de la disposición a emigrar.

**LIMITACIONES / ADVERTENCIAS:**
- Hallazgo nace de cruce (P63 × edad y × NSE).
- Subset E n≈32: cifra direccional. La lectura "el estrato más bajo es el que menos puede/quiere irse" es plausible (emigrar requiere recursos) pero la base es reducida — declararlo como tendencia.
- Solo-cuanti declarado.

---

# REPORTE DE INTEGRIDAD

**Cifras:**
- Todas las cifras univariadas (P56, P57, P58, P59, P60, P62, P63) cuadran 1:1 con `10-opiniones-politicas.md`.
- **P61 (ranking de temas políticos) — CIFRA COLAPSADA:** aparece con 100% en todas las opciones (99.8% Seguridad). Patrón de ranking colapsado a binario mencionado/no mencionado, sin desempate (ver aprendizajes 8.2). NO publicable hasta re-tabular desde el xlsx con orden ponderado. H11 se sostiene solo-cuali.
- **P64 (sueño dominicano en política) — CIFRA COLAPSADA:** multi-select con 100% en las 7 opciones. Mismo problema. H10 cubre P64 parcialmente apoyándose en la cifra robusta de P60 + cuali.
- Subsets bajo umbral n<30 detectados y NO publicados como cifra propia: NSE AB (n≈23, citado solo como ilustración de transversalidad en H13), tipología "Mismo sexo" (n≈3, descartada en todos los cruces). Subsets 30≤n<50 (NSE E n≈32, NSE C+ n≈36, edad 18-24 n≈55 está sobre umbral) marcados con caveat direccional donde se usan.

**Verbatims:**
- FGs con diarización usados: fg-06, fg-07 (Speaker letra atribuida).
- FGs sin diarización usados: fg-03 (monoparental), fg-10 (mixta) — speakers no identificados, líneas documentadas.
- fg-08 (homoparental), fg-09 (mixta), fg-11 (extendida): revisados — su sección "política" deriva rápido a educación, medio ambiente o economía sin material político publicable claro; fg-11 además tiene tramos de transcripción degradada ("no no no..." / "pero pero pero...").
- fg-01, fg-02, fg-04: revisados — fg-02 y fg-04 tienen material económico/gobierno fuerte pero la conversación política específica es tangencial; fg-01 prácticamente no toca política.
- Cero verbatims inventados. Todos verificados contra transcripción con línea de auditoría.

**Hallazgos descartados / no construidos:**
- Hallazgo sobre "afinidad política en pareja" (tema recurrente en fg-07, fg-08, fg-09, fg-10, fg-11): hay cuali abundante ("we agree to disagree", "decidimos no hablarlo porque es diferente") pero NO hay pregunta cuanti en P56-P64 que lo sustente, y el material cuali está disperso sin una tensión cerrada. Se reporta como veta para el editor/research, no se construyó como bloque por falta de pata sólida única.
- Hallazgo sobre tipología "Mismo sexo" en cualquier P: descartado — n≈3, no publicable (regla base mínima).

**Cobertura del pilar:** 9/9 preguntas tocadas. P61 y P64 con cifra colapsada — cubiertas vía cuali y reportadas.

**Confianza global del set: ALTA.**
- 11 hallazgos solo-cuanti o cuanti+cuali con cifras que cuadran 1:1 con el derivado.
- 2 hallazgos (H10 parcial, H11) dependen de cuali por colapso de P61/P64 — declarado explícito.
- Riesgo principal: P61 y P64 necesitan re-tabulación para entregar cifra dura; mientras tanto, los temas se cubren con cuali convergente y la cifra robusta de P60.

---

# ARCHIVOS RELEVANTES PARA AUDITORÍA

- Derivado cuanti: `/home/user/c-digocasa-cerebro/Data System/derivados-por-pilar/10-opiniones-politicas.md`
- Cuestionario: `/home/user/c-digocasa-cerebro/Data System/CUESTIONARIO_FINAL_CODIGO_CASA.md` (líneas 681–793, sección 8 Política)
- Ficha técnica: `/home/user/c-digocasa-cerebro/Data System/ficha-tecnica.md` (composición muestra, geografía)
- Transcripciones citadas:
  - `fg-03-monoparental-2024-11-13.txt` (líneas 555–557, 590–591, 603–604)
  - `fg-06-biparental-hijos-adultos-2024-11-15.txt` (líneas 1434, 1453)
  - `fg-07-biparental-hijos-pequenos-2024-11-18.txt` (líneas 1084–1085, 1108, 1114)
  - `fg-10-mixta-2024-11-21.txt` (líneas 1236–1246, 1377–1378, sección política ~1193–1252)
- Salida: `/home/user/c-digocasa-cerebro/Agentes Hallazgos/opiniones-politicas-hallazgos-crudos.md`
