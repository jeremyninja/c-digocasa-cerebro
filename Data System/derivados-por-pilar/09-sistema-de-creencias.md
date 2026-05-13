---
study: codigo_casa
pilar: Sistema de Creencias
pilar_position: 09
source_questionnaire: Cuestionario Cuantitativo Código Casa 2026
source_data: BBDD madre · TABULACIONES_CRUCES_CODIGO_CASA.xlsx
n: 500
generated: 2026-05-04
total_preguntas: 15
numeracion: Q55–Q69 (cuestionario final tabulado, 11 pilares canónicos)
---

# 09. Sistema de Creencias

> Derivado del estudio Código Casa (n=500, Sto. Domingo + Santiago + DN, campo Oct-Nov 2024).
>
> **15 preguntas con tabulación verificada en la BBDD madre.**
>
> Este pilar consolida tres bloques:
> 1. **Religión y espiritualidad** (Q57–Q59) — reclasificadas desde *Salud y Bienestar* del cuestionario 2026.
> 2. **Derechos y familias del mismo sexo** (Q55–Q56) — reclasificadas desde *Familia e Identidad*.
> 3. **Justicia, inclusión, vulnerabilidad y tercera edad** (Q60–Q69) — bloque original del 2026.
>
> Cada pregunta incluye texto del cuestionario 2026, tipo, frecuencia univariada y, cuando aplica, cruces top por NSE, sexo, rango de edad y tipología de hogar.
>
> **Advertencia metodológica:** el campo `texto_pregunta` en la BBDD madre presenta desfases con el cuestionario aplicado a partir de la hoja P36 (texto pegado secuencialmente sin verificar contra los datos reales). Las preguntas mostradas abajo se identificaron por las **opciones efectivamente tabuladas**, no por el texto declarado. Cuando hay discrepancia, se muestra una advertencia.

---


## Derechos y familias del mismo sexo

## Q55 · BBDD `P18` · 2026 `Q020`

**¿Qué tan de acuerdo estás con que una pareja del mismo sexo pueda acceder a los siguientes derechos como cualquier otra familia?**

_Tipo (cuestionario): Pregunta Cerrada · Subsample: General · Tipo (BBDD): Grid/Batería-Likert_

**Distribución por ítem (n=500 base por ítem)**

**Ítem:** Obtener un préstamo mancomunado en un banco

| % | n | Respuesta |
|---:|---:|---|
| 37.8% | 189 | 1 En desacuerdo |
| 30.4% | 152 | 5 Muy de acuerdo |
| 14.8% | 74 | 4 Algo de acuerdo |
| 9.2% | 46 | 3 Neutro (ni en desacuerdo, ni de acuerdo) |
| 7.8% | 39 | 2 Poco de acuerdo |

**Ítem:** Comprar una propiedad juntos

| % | n | Respuesta |
|---:|---:|---|
| 39.8% | 199 | 5 Muy de acuerdo |
| 33.0% | 165 | 1 En desacuerdo |
| 12.2% | 61 | 4 Algo de acuerdo |
| 8.0% | 40 | 3 Neutro (ni en desacuerdo, ni de acuerdo) |
| 7.0% | 35 | 2 Poco de acuerdo |

**Ítem:** Adoptar legalmente un hijo o hija

| % | n | Respuesta |
|---:|---:|---|
| 61.8% | 309 | 1 En desacuerdo |
| 20.6% | 103 | 5 Muy de acuerdo |
| 6.6% | 33 | 2 Poco de acuerdo |
| 6.4% | 32 | 3 Neutro (ni en desacuerdo, ni de acuerdo) |
| 4.6% | 23 | 4 Algo de acuerdo |

**Ítem:** Acceder a servicios de salud familiar como beneficiarios mut

| % | n | Respuesta |
|---:|---:|---|
| 47.8% | 239 | 5 Muy de acuerdo |
| 26.2% | 131 | 1 En desacuerdo |
| 10.0% | 50 | 4 Algo de acuerdo |
| 8.4% | 42 | 2 Poco de acuerdo |
| 7.6% | 38 | 3 Neutro (ni en desacuerdo, ni de acuerdo) |

**Ítem:** Ser reconocidos legalmente como padres o madres de un mismo

| % | n | Respuesta |
|---:|---:|---|
| 60.4% | 302 | 1 En desacuerdo |
| 21.2% | 106 | 5 Muy de acuerdo |
| 6.6% | 33 | 2 Poco de acuerdo |
| 6.4% | 32 | 4 Algo de acuerdo |
| 5.4% | 27 | 3 Neutro (ni en desacuerdo, ni de acuerdo) |

**Nota:** los cruces demográficos para una matriz Likert deben analizarse ítem por ítem. La BBDD madre los contiene en la misma hoja `P18` (columnas C5+ por bloque). Para uso programático ver el script de tabulación.


---

## Q56 · BBDD `P19` · 2026 `Q021`

**¿Qué piensas sobre las familias compuestas por una pareja del mismo sexo? (Entender si hay alguna duda, preocupación o aceptación para estas familias)**

_Tipo (cuestionario): Pregunta abierta · Subsample: General · Tipo (BBDD): Simple_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P19. Para ti, ¿qué es una buena alimentación?"_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Pregunta abierta — 454 verbatims sin codificar en la BBDD madre.**

La hoja `P19` contiene la respuesta literal de cada participante (n=500), no una frecuencia agrupada por categorías. Para análisis cualitativo se recomienda codificar manualmente o usar las transcripciones de focus groups (no aplica el matiz cuali aquí — ver capítulo Identidad).


---

## Religión y espiritualidad

## Q57 · BBDD `P29` · 2026 `Q033`

**En momentos de dificultad o incertidumbre, ¿qué tan frecuentemente recurres a la religión o espiritualidad como una forma de alivio o refugio?**

_Tipo (cuestionario): Abierta · Subsample: General · Tipo (BBDD): Likert_

**Frecuencia (base n=500)**

| % | n | Categoría |
|---:|---:|---|
| 64.0% | 320 | 5 = Siempre |
| 23.6% | 118 | 3 = A veces |
| 6.6% | 33 | 1 = Nunca |
| 3.4% | 17 | 4 |
| 1.4% | 7 | 2 |
| 1.0% | 5 | No recurro a la religión o espiritualidad (NO LEER) |

#### Cruce por NSE (top respuesta)

| NSE | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| AB | 5 = Siempre | 11 | 47.8% |
| C+ | 5 = Siempre | 19 | 52.8% |
| C | 5 = Siempre | 134 | 61.5% |
| D | 5 = Siempre | 125 | 72.7% |
| E | 5 = Siempre | 19 | 59.4% |
| NS/NR | 5 = Siempre | 12 | 63.2% |

#### Cruce por Sexo (top respuesta)

| Sexo | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Femenino | 5 = Siempre | 216 | 70.8% |
| Masculino | 5 = Siempre | 104 | 53.3% |

#### Cruce por Rango de edad (top respuesta)

| Rango de edad | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| 18-24 | 5 = Siempre | 30 | 54.5% |
| 25-34 | 5 = Siempre | 74 | 63.8% |
| 35-44 | 5 = Siempre | 71 | 63.4% |
| 45-54 | 5 = Siempre | 68 | 69.4% |
| 55 o más | 5 = Siempre | 77 | 64.7% |

#### Cruce por Tipología de hogar (top respuesta)

| Tipología de hogar | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Biparental hijos <18 | 5 = Siempre | 119 | 62.6% |
| Monoparental | 5 = Siempre | 77 | 63.1% |
| Extendido | 5 = Siempre | 34 | 54.0% |
| Sin hijos con mascotas | 5 = Siempre | 21 | 58.3% |
| Con hijos sin mascotas | 5 = Siempre | 22 | 78.6% |
| Mismo sexo | 5 = Siempre | 2 | 66.7% |
| Otro | 5 = Siempre | 45 | 77.6% |


---

## Q58 · BBDD `P30` · 2026 `Q034`

**¿Cuál es tu relación actual con la religión o la espiritualidad?**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Simple_

**Frecuencia (base n=500)**

| % | n | Categoría |
|---:|---:|---|
| 30.8% | 154 | Creyente ocasional |
| 30.2% | 151 | Muy practicante y activa/o |
| 28.8% | 144 | Espiritual pero no practicante |
| 6.8% | 34 | No me identifico con ninguna religión ni práctica espiritual |
| 2.2% | 11 | Mi religión modifica mi forma de vida (no consumo alcochol, no celebro cumpleaños...) |
| 1.2% | 6 | No creyente |

#### Cruce por NSE (top respuesta)

| NSE | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| AB | Muy practicante y activa/o | 8 | 34.8% |
| C+ | Espiritual pero no practicante | 14 | 38.9% |
| C | Creyente ocasional | 67 | 30.7% |
| D | Muy practicante y activa/o | 61 | 35.5% |
| E | Creyente ocasional | 12 | 37.5% |
| NS/NR | Muy practicante y activa/o | 7 | 36.8% |

#### Cruce por Sexo (top respuesta)

| Sexo | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Femenino | Muy practicante y activa/o | 97 | 31.8% |
| Masculino | Creyente ocasional | 62 | 31.8% |

#### Cruce por Rango de edad (top respuesta)

| Rango de edad | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| 18-24 | Creyente ocasional | 25 | 45.5% |
| 25-34 | Creyente ocasional | 34 | 29.3% |
| 35-44 | Creyente ocasional | 42 | 37.5% |
| 45-54 | Muy practicante y activa/o | 33 | 33.7% |
| 55 o más | Muy practicante y activa/o | 56 | 47.1% |

#### Cruce por Tipología de hogar (top respuesta)

| Tipología de hogar | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Biparental hijos <18 | Espiritual pero no practicante | 63 | 33.2% |
| Monoparental | Muy practicante y activa/o | 41 | 33.6% |
| Extendido | Creyente ocasional | 21 | 33.3% |
| Sin hijos con mascotas | Muy practicante y activa/o | 13 | 36.1% |
| Con hijos sin mascotas | Muy practicante y activa/o | 8 | 28.6% |
| Mismo sexo | Creyente ocasional | 2 | 66.7% |
| Otro | Muy practicante y activa/o | 27 | 46.6% |


---

## Q59 · BBDD `P31` · 2026 `Q036`

**¿Cuáles de los siguientes productos o servicios has dejado de consumir por razones religiosas?**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Multirespuesta (MR)_

**Frecuencia agregada — multirespuesta (n efectivo = 11)**

> ⚠️ n efectivo bajo. Solo 11 respondientes mencionaron al menos una opción; el resto declaró ninguna o no respondió. Los % se calculan sobre quienes respondieron.

| % | n | Categoría |
|---:|---:|---|
| 36.4% | 4 | Alcohol |
| 36.4% | 4 | Juegos de azar (loterías, apuestas) |
| 36.4% | 4 | Tabaco o vapes |
| 36.4% | 4 | Contenido sexual (series, libros, redes sociales) |
| 36.4% | 4 | Prácticas espirituales ajenas a mi fe |
| 27.3% | 3 | Otro (Especifique): ___________ |
| 27.3% | 3 | Música o espectáculos considerados inapropiados |
| 27.3% | 3 | Marcas o empresas con posturas contrarias a mi fe |
| 9.1% | 1 | Comidas o bebidas específicas (por ejemplo, cerdo, mariscos, etc.) |


---

## Discriminación, inclusión y diversidad

## Q60 · BBDD `P70` · 2026 `Q068`

**¿Has sido víctima de discriminación en los últimos 3 años? (Por raza, color de piel, etnia, nacionalidad, orientación sexual, religión, etc)**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Multirespuesta (MR)_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P70. ¿Cuál es el principal problema de tu entorno/vecindario?"_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Frecuencia agregada — multirespuesta (n efectivo = 500)**

| % | n | Categoría |
|---:|---:|---|
| 91.2% | 456 | No he sido víctima de discriminación |
| 3.2% | 16 | Otra (especificar): ___________ |
| 2.8% | 14 | Comentarios ofensivos o burlas relacionadas con el color de piel. |
| 1.8% | 9 | Comentarios ofensivos o burlas relacionadas con el cabello. |
| 0.8% | 4 | (Discriminación en espacios religiosos o comunitarios |
| 0.6% | 3 | Exclusión social o laboral por nivel socioeconómico |
| 0.6% | 3 | Violencia verbal o física por alguna de estas razones |
| 0.6% | 3 | Discriminación en el trabajo o al buscar empleo |
| 0.2% | 1 | Exclusión social o laboral por edad. |
| 0.2% | 1 | Exclusión social o laboral por origen étnico o nacionalidad. |
| 0.2% | 1 | (Trato desigual en espacios públicos o instituciones (escuelas, hospitales, oficinas) |

#### Cruce por NSE (top respuesta)

| NSE | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| AB | No he sido víctima de discriminación | 21 | 91.3% |
| C+ | No he sido víctima de discriminación | 35 | 97.2% |
| C | No he sido víctima de discriminación | 195 | 89.4% |
| D | No he sido víctima de discriminación | 163 | 94.8% |
| E | No he sido víctima de discriminación | 27 | 84.4% |
| NS/NR | No he sido víctima de discriminación | 15 | 78.9% |

#### Cruce por Sexo (top respuesta)

| Sexo | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Femenino | No he sido víctima de discriminación | 278 | 91.1% |
| Masculino | No he sido víctima de discriminación | 178 | 91.3% |

#### Cruce por Rango de edad (top respuesta)

| Rango de edad | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| 18-24 | No he sido víctima de discriminación | 52 | 94.5% |
| 25-34 | No he sido víctima de discriminación | 101 | 87.1% |
| 35-44 | No he sido víctima de discriminación | 104 | 92.9% |
| 45-54 | No he sido víctima de discriminación | 91 | 92.9% |
| 55 o más | No he sido víctima de discriminación | 108 | 90.8% |

#### Cruce por Tipología de hogar (top respuesta)

| Tipología de hogar | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Biparental hijos <18 | No he sido víctima de discriminación | 178 | 93.7% |
| Monoparental | No he sido víctima de discriminación | 102 | 83.6% |
| Extendido | No he sido víctima de discriminación | 59 | 93.7% |
| Sin hijos con mascotas | No he sido víctima de discriminación | 31 | 86.1% |
| Con hijos sin mascotas | No he sido víctima de discriminación | 27 | 96.4% |
| Mismo sexo | No he sido víctima de discriminación | 3 | 100.0% |
| Otro | No he sido víctima de discriminación | 56 | 96.6% |


---

## Q61 · BBDD `P71` · 2026 `Q070`

**¿Cómo calificas la inclusión de personas con discapacidad en su comunidad?**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Simple_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P71. ¿Cuánto gastas mensualmente en vivienda (alquiler o hipoteca)?"_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Frecuencia (base n=500)**

| % | n | Categoría |
|---:|---:|---|
| 54.2% | 271 | 1 = Muy baja |
| 19.0% | 95 | 5 = Muy alta |
| 12.4% | 62 | 3 |
| 7.4% | 37 | 2 |
| 7.0% | 35 | 4 |

#### Cruce por NSE (top respuesta)

| NSE | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| AB | 1 = Muy baja | 6 | 26.1% |
| C+ | 1 = Muy baja | 16 | 44.4% |
| C | 1 = Muy baja | 115 | 52.8% |
| D | 1 = Muy baja | 108 | 62.8% |
| E | 1 = Muy baja | 16 | 50.0% |
| NS/NR | 1 = Muy baja | 10 | 52.6% |

#### Cruce por Sexo (top respuesta)

| Sexo | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Femenino | 1 = Muy baja | 167 | 54.8% |
| Masculino | 1 = Muy baja | 104 | 53.3% |

#### Cruce por Rango de edad (top respuesta)

| Rango de edad | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| 18-24 | 1 = Muy baja | 23 | 41.8% |
| 25-34 | 1 = Muy baja | 52 | 44.8% |
| 35-44 | 1 = Muy baja | 59 | 52.7% |
| 45-54 | 1 = Muy baja | 61 | 62.2% |
| 55 o más | 1 = Muy baja | 76 | 63.9% |

#### Cruce por Tipología de hogar (top respuesta)

| Tipología de hogar | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Biparental hijos <18 | 1 = Muy baja | 97 | 51.1% |
| Monoparental | 1 = Muy baja | 67 | 54.9% |
| Extendido | 1 = Muy baja | 30 | 47.6% |
| Sin hijos con mascotas | 1 = Muy baja | 20 | 55.6% |
| Con hijos sin mascotas | 1 = Muy baja | 12 | 42.9% |
| Mismo sexo | 1 = Muy baja | 2 | 66.7% |
| Otro | 1 = Muy baja | 43 | 74.1% |


---

## Q62 · BBDD `P72` · 2026 `Q071`

**Ordena los grupos más vulnerables en tu país, el primero siendo el más vulnerable:**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Multirespuesta (MR)_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P72. Para préstamo hipotecario: ¿qué institución te genera más confianza?"_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Pregunta de ranking.** Cada participante ordenó todas las opciones, por lo que la frecuencia univariada plana muestra todos los items al 100%. La hoja `P72` no incluye descomposición por posición de ranking.

**Items rankeados:**

- Comunidades rurales
- Migrantes
- Población LGBTQ+
- Personas con discapacidad
- Razas de minoría
- Mujeres
- Envejecientes
- Clases sociales más necesitadas
- Niños/as


---

## Q63 · BBDD `P73` · 2026 `Q073`

**¿Crees que tu comunidad está preparada para incluir a personas neurodivergentes y/o con discapacidad (limitaciones físicas) en la vida cotidiana (trabajo, escuela, actividades sociales, transporte, etc.)?**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Simple_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P73. Para un préstamo personal de mejoras del hogar, ¿qué prefieres?"_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Frecuencia (base n=500)**

| % | n | Categoría |
|---:|---:|---|
| 61.8% | 309 | 1 = Nada preparada |
| 13.4% | 67 | 3 |
| 12.0% | 60 | 5 = Muy preparada |
| 7.4% | 37 | 2 |
| 5.4% | 27 | 4 |

#### Cruce por NSE (top respuesta)

| NSE | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| AB | 1 = Nada preparada | 9 | 39.1% |
| C+ | 1 = Nada preparada | 19 | 52.8% |
| C | 1 = Nada preparada | 129 | 59.2% |
| D | 1 = Nada preparada | 123 | 71.5% |
| E | 1 = Nada preparada | 17 | 53.1% |
| NS/NR | 1 = Nada preparada | 12 | 63.2% |

#### Cruce por Sexo (top respuesta)

| Sexo | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Femenino | 1 = Nada preparada | 190 | 62.3% |
| Masculino | 1 = Nada preparada | 119 | 61.0% |

#### Cruce por Rango de edad (top respuesta)

| Rango de edad | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| 18-24 | 1 = Nada preparada | 30 | 54.5% |
| 25-34 | 1 = Nada preparada | 69 | 59.5% |
| 35-44 | 1 = Nada preparada | 66 | 58.9% |
| 45-54 | 1 = Nada preparada | 60 | 61.2% |
| 55 o más | 1 = Nada preparada | 84 | 70.6% |

#### Cruce por Tipología de hogar (top respuesta)

| Tipología de hogar | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Biparental hijos <18 | 1 = Nada preparada | 115 | 60.5% |
| Monoparental | 1 = Nada preparada | 74 | 60.7% |
| Extendido | 1 = Nada preparada | 36 | 57.1% |
| Sin hijos con mascotas | 1 = Nada preparada | 21 | 58.3% |
| Con hijos sin mascotas | 1 = Nada preparada | 19 | 67.9% |
| Mismo sexo | 5 = Muy preparada | 1 | 33.3% |
| Otro | 1 = Nada preparada | 44 | 75.9% |


---

## Q64 · BBDD `P74` · 2026 `Q074`

**¿Qué tan cómodo/a te sientes hablando de orientación sexual o identidad de género dentro de tu familia?**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Likert_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P74. ¿Cómo califica el acceso a servicios básicos en su hogar?"_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Frecuencia (base n=500)**

| % | n | Categoría |
|---:|---:|---|
| 36.8% | 184 | 5 = Muy comodo/a |
| 34.8% | 174 | 1 = Nada cómodo/a |
| 12.2% | 61 | 3 |
| 11.6% | 58 | 4 |
| 4.6% | 23 | 2 |

#### Cruce por NSE (top respuesta)

| NSE | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| AB | 5 = Muy comodo/a | 7 | 30.4% |
| C+ | 5 = Muy comodo/a | 14 | 38.9% |
| C | 5 = Muy comodo/a | 86 | 39.4% |
| D | 1 = Nada cómodo/a | 76 | 44.2% |
| E | 1 = Nada cómodo/a | 13 | 40.6% |
| NS/NR | 1 = Nada cómodo/a | 9 | 47.4% |

#### Cruce por Sexo (top respuesta)

| Sexo | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Femenino | 5 = Muy comodo/a | 123 | 40.3% |
| Masculino | 1 = Nada cómodo/a | 77 | 39.5% |

#### Cruce por Rango de edad (top respuesta)

| Rango de edad | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| 18-24 | 1 = Nada cómodo/a | 22 | 40.0% |
| 25-34 | 5 = Muy comodo/a | 42 | 36.2% |
| 35-44 | 5 = Muy comodo/a | 50 | 44.6% |
| 45-54 | 5 = Muy comodo/a | 38 | 38.8% |
| 55 o más | 1 = Nada cómodo/a | 49 | 41.2% |

#### Cruce por Tipología de hogar (top respuesta)

| Tipología de hogar | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Biparental hijos <18 | 5 = Muy comodo/a | 76 | 40.0% |
| Monoparental | 1 = Nada cómodo/a | 47 | 38.5% |
| Extendido | 1 = Nada cómodo/a | 25 | 39.7% |
| Sin hijos con mascotas | 1 = Nada cómodo/a | 15 | 41.7% |
| Con hijos sin mascotas | 1 = Nada cómodo/a | 12 | 42.9% |
| Mismo sexo | 5 = Muy comodo/a | 1 | 33.3% |
| Otro | 1 = Nada cómodo/a | 22 | 37.9% |


---

## Acoso, cambio social y violencia

## Q65 · BBDD `P75` · 2026 `Q075`

**¿Alguno de tus hijos ha vivido una experiencia de acoso o bullying (escolar o digital)?**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Simple_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P75. ¿Con qué frecuencia realiza mejoras o mantenimiento en su vivienda?"_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Frecuencia (base n=500)**

| % | n | Categoría |
|---:|---:|---|
| 75.0% | 375 | No |
| 12.8% | 64 | No tengo hijos |
| 11.6% | 58 | Sí |
| 0.6% | 3 | Prefiero no responder |


---

## Q66 · BBDD `P76` · 2026 `Q076`

**¿Cuál de los siguientes cambios sociales consideras más urgente para lograr mayor equidad en la vida familiar y laboral?**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Simple_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P76. ¿Consideras que tu hogar es lo suficientemente amplio para su familia?"_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Frecuencia (base n=500)**

| % | n | Categoría |
|---:|---:|---|
| 62.6% | 313 | Que los padres estén más presentes en la crianza y las tareas del hogar. |
| 20.0% | 100 | Ambas primeras opciones por igual. |
| 12.8% | 64 | Que exista mayor flexibilidad laboral para ambos padres, no solo para las madres. |
| 2.8% | 14 | Que la maternidad no implique una pausa o retroceso profesional para las mujeres. |
| 1.8% | 9 | Ninguna de las anteriores. |

#### Cruce por NSE (top respuesta)

| NSE | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| AB | Ambas primeras opciones por igual. | 10 | 43.5% |
| C+ | Que los padres estén más presentes en la crianza y las tarea… | 24 | 66.7% |
| C | Que los padres estén más presentes en la crianza y las tarea… | 137 | 62.8% |
| D | Que los padres estén más presentes en la crianza y las tarea… | 105 | 61.0% |
| E | Que los padres estén más presentes en la crianza y las tarea… | 24 | 75.0% |
| NS/NR | Que los padres estén más presentes en la crianza y las tarea… | 15 | 78.9% |

#### Cruce por Sexo (top respuesta)

| Sexo | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Femenino | Que los padres estén más presentes en la crianza y las tarea… | 198 | 64.9% |
| Masculino | Que los padres estén más presentes en la crianza y las tarea… | 115 | 59.0% |

#### Cruce por Rango de edad (top respuesta)

| Rango de edad | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| 18-24 | Que los padres estén más presentes en la crianza y las tarea… | 33 | 60.0% |
| 25-34 | Que los padres estén más presentes en la crianza y las tarea… | 68 | 58.6% |
| 35-44 | Que los padres estén más presentes en la crianza y las tarea… | 65 | 58.0% |
| 45-54 | Que los padres estén más presentes en la crianza y las tarea… | 70 | 71.4% |
| 55 o más | Que los padres estén más presentes en la crianza y las tarea… | 77 | 64.7% |

#### Cruce por Tipología de hogar (top respuesta)

| Tipología de hogar | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Biparental hijos <18 | Que los padres estén más presentes en la crianza y las tarea… | 124 | 65.3% |
| Monoparental | Que los padres estén más presentes en la crianza y las tarea… | 81 | 66.4% |
| Extendido | Que los padres estén más presentes en la crianza y las tarea… | 35 | 55.6% |
| Sin hijos con mascotas | Que los padres estén más presentes en la crianza y las tarea… | 24 | 66.7% |
| Con hijos sin mascotas | Que los padres estén más presentes en la crianza y las tarea… | 13 | 46.4% |
| Mismo sexo | Que los padres estén más presentes en la crianza y las tarea… | 2 | 66.7% |
| Otro | Que los padres estén más presentes en la crianza y las tarea… | 34 | 58.6% |


---

## Q67 · BBDD `P77` · 2026 `Q078`

**¿Cuál de los siguientes tipos de violencia has experimentado con mayor frecuencia en los últimos 3 años?**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Multirespuesta (MR)_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P77. Ordena los factores más importantes al elegir una vivienda."_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Frecuencia agregada — multirespuesta (n efectivo = 500)**

| % | n | Categoría |
|---:|---:|---|
| 56.4% | 282 | No he sufrido ningún tipo de violencia |
| 20.2% | 101 | Violencia económica (restricción del acceso al dinero, control financiero) |
| 17.4% | 87 | Violencia emocional o psicológica (manipulación, insultos, amenazas, control) |
| 7.6% | 38 | Violencia física (agresiones, golpes, empujones) |
| 2.0% | 10 | Otra (especificar): ___________ |
| 0.8% | 4 | Prefiero no responder |

#### Cruce por NSE (top respuesta)

| NSE | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| AB | No he sufrido ningún tipo de violencia | 13 | 56.5% |
| C+ | No he sufrido ningún tipo de violencia | 20 | 55.6% |
| C | No he sufrido ningún tipo de violencia | 127 | 58.3% |
| D | No he sufrido ningún tipo de violencia | 97 | 56.4% |
| E | No he sufrido ningún tipo de violencia | 14 | 43.8% |
| NS/NR | No he sufrido ningún tipo de violencia | 11 | 57.9% |

#### Cruce por Sexo (top respuesta)

| Sexo | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Femenino | No he sufrido ningún tipo de violencia | 165 | 54.1% |
| Masculino | No he sufrido ningún tipo de violencia | 117 | 60.0% |

#### Cruce por Rango de edad (top respuesta)

| Rango de edad | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| 18-24 | No he sufrido ningún tipo de violencia | 29 | 52.7% |
| 25-34 | No he sufrido ningún tipo de violencia | 58 | 50.0% |
| 35-44 | No he sufrido ningún tipo de violencia | 63 | 56.2% |
| 45-54 | No he sufrido ningún tipo de violencia | 59 | 60.2% |
| 55 o más | No he sufrido ningún tipo de violencia | 73 | 61.3% |

#### Cruce por Tipología de hogar (top respuesta)

| Tipología de hogar | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Biparental hijos <18 | No he sufrido ningún tipo de violencia | 103 | 54.2% |
| Monoparental | No he sufrido ningún tipo de violencia | 65 | 53.3% |
| Extendido | No he sufrido ningún tipo de violencia | 33 | 52.4% |
| Sin hijos con mascotas | No he sufrido ningún tipo de violencia | 23 | 63.9% |
| Con hijos sin mascotas | No he sufrido ningún tipo de violencia | 18 | 64.3% |
| Mismo sexo | Violencia económica (restricción del acceso al dinero, contr… | 2 | 66.7% |
| Otro | No he sufrido ningún tipo de violencia | 40 | 69.0% |


---

## Tercera edad

## Q68 · BBDD `P78` · 2026 `Q080`

**¿Quién se encarga principalmente del cuidado de esa persona mayor en tu familia?**

_Tipo (cuestionario): Cerrada
Condición: si respondió sí a la pregunta anterior · Subsample: General · Tipo (BBDD): Likert_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P78. ¿Qué tan satisfecho está con la calidad de vida en su hogar actual? (1=Nada / 5=Muy satisfecho)"_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Frecuencia (base n=500)**

| % | n | Categoría |
|---:|---:|---|
| 72.8% | 364 | No vive conmigo ninguna persona mayor en mi hogar |
| 12.8% | 64 | Yo mismo/a |
| 5.4% | 27 | Otro miembro de la familia (hijo/a, nieto/a, hermano/a, etc.) |
| 3.4% | 17 | No requiere cuidados especiales |
| 2.0% | 10 | Compartimos la responsabilidad entre varios |
| 1.6% | 8 | Otro (especificar): ___________ |
| 1.4% | 7 | Su pareja o cónyuge |
| 0.6% | 3 | Un cuidador o personal contratado |

#### Cruce por NSE (top respuesta)

| NSE | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| AB | No vive conmigo ninguna persona mayor en mi hogar | 19 | 82.6% |
| C+ | No vive conmigo ninguna persona mayor en mi hogar | 25 | 69.4% |
| C | No vive conmigo ninguna persona mayor en mi hogar | 169 | 77.5% |
| D | No vive conmigo ninguna persona mayor en mi hogar | 122 | 70.9% |
| E | No vive conmigo ninguna persona mayor en mi hogar | 19 | 59.4% |
| NS/NR | No vive conmigo ninguna persona mayor en mi hogar | 10 | 52.6% |

#### Cruce por Sexo (top respuesta)

| Sexo | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Femenino | No vive conmigo ninguna persona mayor en mi hogar | 238 | 78.0% |
| Masculino | No vive conmigo ninguna persona mayor en mi hogar | 126 | 64.6% |

#### Cruce por Rango de edad (top respuesta)

| Rango de edad | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| 18-24 | No vive conmigo ninguna persona mayor en mi hogar | 41 | 74.5% |
| 25-34 | No vive conmigo ninguna persona mayor en mi hogar | 96 | 82.8% |
| 35-44 | No vive conmigo ninguna persona mayor en mi hogar | 92 | 82.1% |
| 45-54 | No vive conmigo ninguna persona mayor en mi hogar | 79 | 80.6% |
| 55 o más | No vive conmigo ninguna persona mayor en mi hogar | 56 | 47.1% |

#### Cruce por Tipología de hogar (top respuesta)

| Tipología de hogar | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Biparental hijos <18 | No vive conmigo ninguna persona mayor en mi hogar | 155 | 81.6% |
| Monoparental | No vive conmigo ninguna persona mayor en mi hogar | 90 | 73.8% |
| Extendido | No vive conmigo ninguna persona mayor en mi hogar | 35 | 55.6% |
| Sin hijos con mascotas | No vive conmigo ninguna persona mayor en mi hogar | 28 | 77.8% |
| Con hijos sin mascotas | No vive conmigo ninguna persona mayor en mi hogar | 18 | 64.3% |
| Mismo sexo | No vive conmigo ninguna persona mayor en mi hogar | 2 | 66.7% |
| Otro | No vive conmigo ninguna persona mayor en mi hogar | 36 | 62.1% |


---

## Q69 · BBDD `P79` · 2026 `Q082`

**¿Qué sientes que hace falta para que las personas de la tercera edad vivan con mayor dignidad y bienestar?**

_Tipo (cuestionario): Cerrada · Subsample: General · Tipo (BBDD): Multirespuesta (MR)_

> ⚠️ El campo `texto_pregunta` en la BBDD declara: _"P79. ¿Qué fuente utilizas principalmente para informarte sobre política?"_ — pero las opciones tabuladas corresponden a la pregunta del cuestionario 2026 mostrada arriba. Inconsistencia documentada en el reporte de tabulación.

**Frecuencia agregada — multirespuesta (n efectivo = 500)**

| % | n | Categoría |
|---:|---:|---|
| 73.8% | 369 | Pensiones o apoyos económicos suficientes |
| 53.4% | 267 | Acceso gratuito o asequible a servicios de salud |
| 32.4% | 162 | Respeto y reconocimiento en el entorno familiar y comunitario |
| 32.2% | 161 | Prevención del abandono, la soledad y el maltrato |
| 30.0% | 150 | Viviendas adaptadas o seguras para personas mayores |
| 26.8% | 134 | Programas de integración social y recreativa |
| 24.0% | 120 | Apoyo y capacitación para cuidadores familiares |
| 20.2% | 101 | Accesibilidad en espacios públicos y transporte |
| 1.0% | 5 | Otro (especificar): ___________ |

#### Cruce por NSE (top respuesta)

| NSE | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| AB | Pensiones o apoyos económicos suficientes | 18 | 78.3% |
| C+ | Pensiones o apoyos económicos suficientes | 30 | 83.3% |
| C | Pensiones o apoyos económicos suficientes | 154 | 70.6% |
| D | Pensiones o apoyos económicos suficientes | 134 | 77.9% |
| E | Pensiones o apoyos económicos suficientes | 25 | 78.1% |
| NS/NR | Pensiones o apoyos económicos suficientes | 8 | 42.1% |

#### Cruce por Sexo (top respuesta)

| Sexo | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Femenino | Pensiones o apoyos económicos suficientes | 225 | 73.8% |
| Masculino | Pensiones o apoyos económicos suficientes | 144 | 73.8% |

#### Cruce por Rango de edad (top respuesta)

| Rango de edad | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| 18-24 | Pensiones o apoyos económicos suficientes | 36 | 65.5% |
| 25-34 | Pensiones o apoyos económicos suficientes | 82 | 70.7% |
| 35-44 | Pensiones o apoyos económicos suficientes | 82 | 73.2% |
| 45-54 | Pensiones o apoyos económicos suficientes | 75 | 76.5% |
| 55 o más | Pensiones o apoyos económicos suficientes | 94 | 79.0% |

#### Cruce por Tipología de hogar (top respuesta)

| Tipología de hogar | Top respuesta | n | % en grupo |
|---|---|---:|---:|
| Biparental hijos <18 | Pensiones o apoyos económicos suficientes | 141 | 74.2% |
| Monoparental | Pensiones o apoyos económicos suficientes | 92 | 75.4% |
| Extendido | Pensiones o apoyos económicos suficientes | 42 | 66.7% |
| Sin hijos con mascotas | Pensiones o apoyos económicos suficientes | 27 | 75.0% |
| Con hijos sin mascotas | Pensiones o apoyos económicos suficientes | 21 | 75.0% |
| Mismo sexo | Acceso gratuito o asequible a servicios de salud | 3 | 100.0% |
| Otro | Pensiones o apoyos económicos suficientes | 44 | 75.9% |


---


## Apéndice — Preguntas del cuestionario 2026 NO aplicadas en este pilar

El cuestionario 2026 declara 26 preguntas bajo *Sistema de Creencias*. De ellas, **11 no fueron aplicadas en el campo** y por tanto no aparecen en la BBDD madre:

- Bloque *Justicia e Inclusión*: Q065 (acceso a oportunidades), Q066 (institución más confiable), Q067 (justicia equitativa por NSE), Q069 (rol del gobierno en inclusión), Q072 (causas más relevantes).
- Bloque *Tercera Edad*: Q077 (calidad de vida tercera edad), Q079 (preocupación adultos mayores), Q081 (rol del Estado).
- Otras: Q077–Q083 fragmentos sobre violencia/acoso/cambio social no aplicados.

Adicionalmente, la pregunta abierta Q021 sobre familias del mismo sexo se conserva en la hoja `P19` como **454 verbatims sin codificar** — requiere análisis cualitativo manual o codificación temática para extraer patrones.

## Limitaciones

1. **Religión:** la BBDD captura prácticas y frecuencia, no denominación. No se preguntó si el participante es católico, evangélico, etc.
2. **LGBT:** las preguntas Q55–Q56 miden actitud hacia familias y derechos de parejas del mismo sexo, no autoidentificación.
3. **Tipología "Mismo sexo":** representa solo el 0.6% de la muestra (3 hogares). Cruces sobre esta categoría tienen base mínima — interpretar con cautela.
4. **Discriminación (Q60):** 91.2% declara no haber sido víctima en los últimos 3 años. Las menciones positivas son muy bajas en n absoluto; los % de la frecuencia se mantienen sobre n=500.
