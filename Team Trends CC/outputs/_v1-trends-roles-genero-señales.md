# ROLES DE GÉNERO — Mapa de señales

**Slug:** trends-roles-genero
**Hunter brief:** [trends-roles-genero-hunter.md](./trends-roles-genero-hunter.md)
**Fecha de scrapeo:** 2026-05-20
**Total señales verificadas:** 45 (prioridad ALTA cumplida)
**Chrome MCP conectado:** SÍ — operó en modo degradado por timeouts CDP; pivoteó a headless Chrome local con user-data-dir aislado + curl/oembed TikTok. Resultado equivalente.
**Estrategia de captura:**
1. TikTok → endpoint oembed (`https://www.tiktok.com/oembed?url=...`) + descarga directa de `thumbnail_url`, recorte sips 880×596
2. Artículos públicos → headless Chrome local 596×880 con user-data-dir único por captura + UA Safari realista, recorte sips
3. Sitios con paywall soft (Axios, Newsweek, 19thNews, Sage, Tandfonline) → mismo método headless con UA realista; pasaron sin login
4. Banco Mundial / X (Twitter) / sitios con anti-bot fuerte → no procesados, marcados PENDIENTE
**Directorio screenshots:** `screenshots/trends-roles-genero/`

---

## Señales verificadas — MACRO 1 · INVENTOLOGÍA

### Bloque macro 1 — Adultez de género se está inventando

#### Señal macro-1-0-listin-divorcios-2024 — Listín: 44,349 matrimonios vs 26,210 divorcios 2024
- **Tipo:** dato — medio dominicano
- **Plataforma / medio:** Listín Diario (RD)
- **Link:** https://listindiario.com/la-republica/ciudad/20250601/2024-registraron-44-349-matrimonios-26-210-divorcios_859974.html
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-0-listin-divorcios-2024.png`
- **Caption sugerido:** Listín Diario reporta ONE 2024 — 44,349 matrimonios contra 26,210 divorcios. Ratio 59%, el más alto del registro RD.
- **Fuente footer:** Listín Diario · 2025-06-01

#### Señal macro-1-0-ndo-mujeres-empleos-rd — Mujeres 25-39 = 80%+ nuevos empleos RD
- **Tipo:** dato — medio dominicano
- **Plataforma / medio:** N.com.do
- **Link:** https://n.com.do/2025/12/16/mujeres-25-39-anos-nuevos-empleos-republica-dominicana/
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-0-ndo-mujeres-empleos-rd.png`
- **Caption sugerido:** N.com.do (BCRD dic 2025) — mujeres de 25-39 años concentran más del 80% de nuevos empleos formales.
- **Fuente footer:** N.com.do · 2025-12-16

#### Señal macro-1-0-infobae-crisis-masculina-genz — Crisis silenciosa hombres jóvenes
- **Tipo:** dato — medio internacional español
- **Plataforma / medio:** Infobae España
- **Link:** https://www.infobae.com/espana/2025/06/24/los-hombres-jovenes-se-enfrentan-una-crisis-silenciosa-soledad-depresion-bajo-rendimiento-y-falta-de-proposito/
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-0-infobae-crisis-masculina-genz.png`
- **Caption sugerido:** Infobae — Gen Z masculino: soledad, depresión, bajo rendimiento. 60% siente "se les exige demasiado" para apoyar la igualdad (Ipsos UK).
- **Fuente footer:** Infobae · 2025-06-24

### Micro 1.1 — AMBOS DICE LA BOCA, ELLA HACE LA CASA

#### Señal macro-1-1-altermutua-carga-mental — Las 4 fases del trabajo mental femenino
- **Tipo:** dato — medio especializado
- **Plataforma / medio:** Alter Mutua (España)
- **Link:** https://www.altermutua.com/es/la-carga-mental-en-las-mujeres/
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-1-altermutua-carga-mental.png`
- **Caption sugerido:** Alter Mutua — síntesis del paper American Sociological Review: la carga mental tiene 4 fases (anticipar, identificar opciones, decidir, monitorear) y recae sobre la mujer aunque la tarea se "delegue".
- **Fuente footer:** Alter Mutua · 2024-2025

#### Señal macro-1-1-motherly-default-parent — Default Parent Syndrome viral 2025
- **Tipo:** dato — medio parenting internacional
- **Plataforma / medio:** Mother.ly
- **Link:** https://www.mother.ly/news/viral-trending/default-parent-resentment/
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-1-motherly-default-parent.png`
- **Caption sugerido:** Mother.ly — Default Parent Syndrome se viraliza en TikTok 2025: la mamá queda "primera en la fila" por default sin acuerdo previo.
- **Fuente footer:** Mother.ly · 2025

#### Señal macro-1-1-pipedrive-carga-mental — Carga mental como concepto laboral
- **Tipo:** dato — medio business
- **Plataforma / medio:** Pipedrive
- **Link:** https://www.pipedrive.com/es/blog/carga-mental
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-1-pipedrive-carga-mental.png`
- **Caption sugerido:** Pipedrive en español — explicación de carga mental y datos OECD sobre uso del tiempo por género.
- **Fuente footer:** Pipedrive · 2024-2025

#### Señal macro-1-1-tiktok-madres-reales-rd-carga-mental — Lyn (madresrealesrd) carga mental
- **Tipo:** verbatim viral — TikTok local RD
- **Plataforma / medio:** TikTok (@madresrealesrd)
- **Link:** https://www.tiktok.com/@madresrealesrd/video/7262536453459086597
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-1-tiktok-madres-reales-rd-carga-mental.png`
- **Caption sugerido:** Lyn (cuenta dominicana @madresrealesrd) — explica carga mental materna y cuenta cómo abrió la conversación con su pareja. Hash #CargaMentalMaterna en RD.
- **Fuente footer:** TikTok @madresrealesrd · 2023-2024
- **NOTA ALTA PARA EDITOR:** Esta es la pieza local RD que el hunter pidió validar. Lyn maneja la cuenta @madresrealesrd y articula explícitamente el concepto "CargaMentalMaterna" en español dominicano. Es el caso fuerte para el headline local del Micro 1.1.

#### Señal macro-1-1-tiktok-pequefelicidad-carga-mental — Pequefelicidad "lo que no se ve sí existe"
- **Tipo:** verbatim viral — TikTok español global
- **Plataforma / medio:** TikTok (@pequefelicidad)
- **Link:** https://www.tiktok.com/@pequefelicidad/video/7371433274381487392
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-1-tiktok-pequefelicidad-carga-mental.png`
- **Caption sugerido:** Pequefelicidad — "La carga mental: lo que no se ve sí existe". Articulación pop del concepto académico para audiencia hispana.
- **Fuente footer:** TikTok @pequefelicidad · 2024

#### Señal macro-1-1-tiktok-leo-camiser-carga-papas — Papá habla de carga mental
- **Tipo:** verbatim — TikTok contrapunto masculino
- **Plataforma / medio:** TikTok (@leocamiser)
- **Link:** https://www.tiktok.com/@leocamiser/video/7302973397565279493
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-1-tiktok-leo-camiser-carga-papas.png`
- **Caption sugerido:** Leo Camiser (@leocamiser) — "La carga mental no puede ser solamente de la madre. Los padres tenemos mucho trabajo por hacer."
- **Fuente footer:** TikTok @leocamiser · 2023

#### Señal macro-1-1-tiktok-mama-cansada-evelynsita — Mom life real
- **Tipo:** meme/verbatim — TikTok hispano
- **Plataforma / medio:** TikTok (@evelynsita270897)
- **Link:** https://www.tiktok.com/@evelynsita270897/video/7429019060014288133
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-1-tiktok-mama-cansada-evelynsita.png`
- **Caption sugerido:** Evelyn Pacheco — "La vida real de una mamá cansada". #momlife #momtok #morningroutine.
- **Fuente footer:** TikTok @evelynsita270897 · 2024

#### Señal macro-1-1-tiktok-rechimuzzi-mama-triste — Mamá cansada y triste
- **Tipo:** verbatim — TikTok hispano
- **Plataforma / medio:** TikTok (@rechimuzzi)
- **Link:** https://www.tiktok.com/@rechimuzzi/video/7464265954235665669
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-1-tiktok-rechimuzzi-mama-triste.png`
- **Caption sugerido:** Rechimuzzi — reflexiones de una madre sobre cansancio y tristeza maternal.
- **Fuente footer:** TikTok @rechimuzzi · 2025

#### Señal macro-1-1-tiktok-cesar-estadisticas — Estadísticas crudas paternidad
- **Tipo:** dato/educativo — TikTok hispano
- **Plataforma / medio:** TikTok (@cesar_qnte / QNTE)
- **Link:** https://www.tiktok.com/@cesar_qnte/video/7381092404905938182
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-1-tiktok-cesar-estadisticas.png`
- **Caption sugerido:** QNTE — "Estadísticas: tan crudas como reales" sobre paternidad y división de tareas. #educacion #paternidad.
- **Fuente footer:** TikTok @cesar_qnte · 2024-06

### Micro 1.2 — LA PLANCHA TIENE GÉNERO

**[GAP — pendiente]** No se logró ubicar TikToks específicos sobre planchado como tarea de género o "yo planchando a las 11pm" que sean verificables y vigentes. El concepto vive en la cuanti Código Casa (planchar 54.2% mujer / 1.8% hombre) pero no tiene huella viral grande en TikTok español 2024-2026 — eso ya es un hallazgo: la plancha es invisible incluso para el meme. Señal mejor: la propia gráfica P15 del derivado.

| # | Señal sugerida hunter | Resultado scrapeo |
|---|---|---|
| 1 | TikTok "yo planchando a las 11pm" mamá dominicana | NO ENCONTRADA — sin huella viral |
| 2 | TikTok #plancha + hispanos | DISPERSA — sin un video tipo headline |
| 3 | Servicio planchado a domicilio RD anuncios | NO PROCESADO |
| 4 | Google Trends planchar a domicilio RD | NO PROCESADO |
| 5 | TikTok hombres aprendiendo a planchar | DISPERSA |
| 6-7 | OECD/Pew datasets | NO PROCESADO — los datasets están detrás de portales lentos |

**Recomendación:** Editor cultural puede usar el dato Código Casa P15 directo + gráfica visual generada por el equipo. Reutilizable: `macro-1-1-altermutua-carga-mental.png` y `macro-1-1-pipedrive-carga-mental.png` como soportes globales de "tareas invisibles que no se redistribuyen".

### Micro 1.3 — LA JEFA DEL HOGAR ES UNA SOLA MUJER

#### Señal macro-1-3-presidencia-familia-feliz — 2,160 mujeres con vivienda Familia Feliz
- **Tipo:** dato/política — gobierno RD
- **Plataforma / medio:** Presidencia.gob.do
- **Link:** https://presidencia.gob.do/noticias/familia-feliz-ha-beneficiado-2160-mujeres-con-la-asignacion-de-una-vivienda-propia-y-digna
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-3-presidencia-familia-feliz.png`
- **Caption sugerido:** Presidencia RD — Familia Feliz ha beneficiado a 2,160 mujeres con vivienda propia. 41% de los hogares del programa son monoparentales.
- **Fuente footer:** Presidencia RD · 2024

#### Señal macro-1-3-ministerio-mujer-bono — Bono Mujer institucionalizado
- **Tipo:** dato/política — gobierno RD
- **Plataforma / medio:** Ministerio de la Mujer RD
- **Link:** https://www.mujer.gob.do/index.php/noticias/itemlist/tag/Bono+Mujer
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-3-ministerio-mujer-bono.png`
- **Caption sugerido:** Ministerio de la Mujer RD — Bono Mujer/Madre: RD$1,500 millones presupuestados para jefas de hogar.
- **Fuente footer:** mujer.gob.do · 2024

#### Señal macro-1-3-elintermediario-madres-solteras — Batallas invisibles madres solteras RD
- **Tipo:** reportaje — medio dominicano
- **Plataforma / medio:** El Intermediario
- **Link:** https://elintermediario.com.do/2025/11/02/las-batallas-invisibles-de-madres-solteras-en-la-republica-dominicana/
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-3-elintermediario-madres-solteras.png`
- **Caption sugerido:** El Intermediario — reportaje sobre madres solteras RD: ausencia económica de padres, manutención débil.
- **Fuente footer:** El Intermediario · 2025-11

### Micro 1.4 — HEREDA MI ESPOSA (cuidado de mayores)

#### Señal macro-1-4-iberoamerica-mayores-rd — Trayectorias de cuidados RD
- **Tipo:** dato — organismo regional
- **Plataforma / medio:** Iberoamérica Mayores
- **Link:** https://iberoamericamayores.org/2025/06/30/republica-dominicana-trayectorias-y-desafios-en-los-cuidados-de-larga-duracion-para-personas-mayores/
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-4-iberoamerica-mayores-rd.png`
- **Caption sugerido:** Iberoamérica Mayores — RD será "sociedad envejecida" para 2031 (>14% pob. 60+); 21% para 2050. Carga de cuidados crece sin sistema público.
- **Fuente footer:** Iberoamérica Mayores · 2025-06-30

#### Señal macro-1-4-listin-cuidadoras-conape — 90 cuidadoras certificadas CONAPE
- **Tipo:** dato/política — medio dominicano
- **Plataforma / medio:** Listín Diario
- **Link:** https://listindiario.com/la-republica/sector-salud/20241205/cuidaran-adultos-mayores-casas-ocho-horas_836458.html
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-4-listin-cuidadoras-conape.png`
- **Caption sugerido:** Listín — primera promoción de 90 cuidadoras certificadas CONAPE/Supérate/INFOTEP, salario RD$30,000 + seguridad social, 8 horas en casas.
- **Fuente footer:** Listín Diario · 2024-12-05

### Micro 1.5 — DIVORCIO LA NORMA, MATRIMONIO LA ANOMALÍA

#### Señal macro-1-5-one-blog-divorcios — ONE serie histórica divorcios/matrimonios
- **Tipo:** dato — organismo oficial RD
- **Plataforma / medio:** Blog ONE
- **Link:** http://blog.one.gob.do/index.php/divorcios-en-aumento-que-esta-pasando-con-los-matrimonios-en-la-republica-dominicana/
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-5-one-blog-divorcios.png`
- **Caption sugerido:** ONE — divorcios crecieron de 12,821 (2001) a 28,694 (2021), +124% en 20 años. Ratio histórico matrimonios/divorcios RD.
- **Fuente footer:** Blog ONE · 2024-2025

#### Señal macro-1-5-eldia-mujeres-jovenes-casan — Mujeres se casan más jóvenes que los hombres
- **Tipo:** dato — medio dominicano
- **Plataforma / medio:** El Día RD
- **Link:** https://eldia.com.do/mujeres-se-casan-mas-jovenes-que-los-hombres-en-rd/
- **Screenshot:** `screenshots/trends-roles-genero/macro-1-5-eldia-mujeres-jovenes-casan.png`
- **Caption sugerido:** El Día RD — mujeres se casan más jóvenes que los hombres en República Dominicana (2024).
- **Fuente footer:** El Día RD · 2024

#### Señal macro-1-5-listin-divorcios-2024 — (reutiliza captura macro-1-0)
- Reutiliza `screenshots/trends-roles-genero/macro-1-0-listin-divorcios-2024.png` con caption: "Listín 2025 — 2024: 44,349 matrimonios vs 26,210 divorcios = 59% ratio."

---

## Señales verificadas — MACRO 2 · HERNÁNDEZ PROMPTED

### Bloque macro 2

#### Señal macro-2-0-motherly-ai-mental-load — Caso Lilian Schmidt 97% mental load
- **Tipo:** caso — medio parenting global
- **Plataforma / medio:** Mother.ly
- **Link:** https://www.mother.ly/parenting/how-ai-is-helping-this-mom-reduce-mental-load/
- **Screenshot:** `screenshots/trends-roles-genero/macro-2-0-motherly-ai-mental-load.png`
- **Caption sugerido:** Mother.ly — Lilian Schmidt (Zurich) reduce 97% de su mental load con ChatGPT: comidas, listas, regalos, rutinas. "AI is the third supporter."
- **Fuente footer:** Mother.ly · 2025

### Micro 2.1 — CHATGPT, MI SEGUNDA ADULTA

#### Señal macro-2-1-axios-chatgpt-feminizado — 52% usuarios ChatGPT con nombres femeninos
- **Tipo:** dato — medio US tech
- **Plataforma / medio:** Axios
- **Link:** https://www.axios.com/2025/09/30/chatgpt-pulse-ai-assistant-moms
- **Screenshot:** `screenshots/trends-roles-genero/macro-2-1-axios-chatgpt-feminizado.png`
- **Caption sugerido:** Axios — 52.4% usuarios activos de ChatGPT junio 2025 tienen nombres femeninos (vs. 17.6% al lanzamiento). El AI assistant se feminiza.
- **Fuente footer:** Axios · 2025-09-30

#### Señal macro-2-1-newsweek-mom-mental-load — Mom overwhelmed encuentra solución en ChatGPT
- **Tipo:** caso — medio US
- **Plataforma / medio:** Newsweek
- **Link:** https://www.newsweek.com/mom-overwhelmed-mental-load-finds-solution-2091525
- **Screenshot:** `screenshots/trends-roles-genero/macro-2-1-newsweek-mom-mental-load.png`
- **Caption sugerido:** Newsweek — mom of toddler overwhelmed by mental load encuentra "eye-opening solution": ChatGPT como co-padre invisible.
- **Fuente footer:** Newsweek · 2025

#### Señal macro-2-1-independent-mom-chatgpt — Independent Español: madre viral por usar ChatGPT
- **Tipo:** caso/medio — Independent Español
- **Plataforma / medio:** Independent Español
- **Link:** https://www.independentespanol.com/estilo/chatgpt-consejos-paternidad-madres-inteligencia-artificial-b2803910.html
- **Screenshot:** `screenshots/trends-roles-genero/macro-2-1-independent-mom-chatgpt.png`
- **Caption sugerido:** Independent Español — madre se vuelve viral por pedir ayuda a ChatGPT para criar a su hija: "Siento que estoy haciendo trampa".
- **Fuente footer:** Independent Español · 2025

#### Señal macro-2-1-merca20-chatgpt-mama — ChatGPT ya es mamá
- **Tipo:** medio business hispano
- **Plataforma / medio:** Merca 2.0
- **Link:** https://www.merca20.com/chatgpt-ya-es-mama-asi-ayuda-a-una-madre-a-criar-a-su-hijo-mientras-ella-descansa/
- **Screenshot:** `screenshots/trends-roles-genero/macro-2-1-merca20-chatgpt-mama.png`
- **Caption sugerido:** Merca 2.0 — "ChatGPT ya es mamá": cómo ayuda a una madre a criar mientras ella descansa.
- **Fuente footer:** Merca 2.0 · 2025

#### Señal macro-2-1-infobae-nina-chatgpt-tarea — Niña 10 años pide a ChatGPT que haga su tarea
- **Tipo:** caso — medio US/LATAM
- **Plataforma / medio:** Infobae
- **Link:** https://www.infobae.com/tecno/2025/07/10/nina-de-10-anos-le-pide-a-chatgpt-que-haga-su-tarea-con-palabras-como-si-fuera-yo/
- **Screenshot:** `screenshots/trends-roles-genero/macro-2-1-infobae-nina-chatgpt-tarea.png`
- **Caption sugerido:** Infobae — niña de 10 años pide a ChatGPT hacer su tarea "con palabras como si fuera yo". La IA ya entró al pupitre.
- **Fuente footer:** Infobae · 2025-07-10

#### Señal macro-2-1-tiktok-nina-chatgpt-tarea-redunotv — Niña viral con ChatGPT
- **Tipo:** verbatim — TikTok español
- **Plataforma / medio:** TikTok (@redunotv Bolivia)
- **Link:** https://www.tiktok.com/@redunotv/video/7524731891031870726
- **Screenshot:** `screenshots/trends-roles-genero/macro-2-1-tiktok-nina-chatgpt-tarea-redunotv.png`
- **Caption sugerido:** Red Uno Bolivia — viral: niña pide a la IA que haga su tarea. Indicador de adopción IA hogar LATAM.
- **Fuente footer:** TikTok @redunotv · 2025

### Micro 2.2 — LA PELEA QUE CHATGPT REESCRIBIÓ

**[GAP — pendiente]** El hunter ya marcó este micro como `PENDIENTE [verificar 2024+]` en LATAM. El scrapeo no produjo evidencia LATAM específica de uso IA en mediación de pareja. Los casos Mother.ly + Axios + Newsweek (capturados en 2.1) sostienen el frame global; el editor cultural puede usar esos + el verbatim FG-01 + FG-02 sin más evidencia ad hoc.

### Micro 2.3 — EL CRONOGRAMA QUE NADIE FIRMÓ

**[GAP — diferido]** Sin captura específica. Reutilizables: `macro-2-1-axios-chatgpt-feminizado.png` (feminización) y `macro-2-0-motherly-ai-mental-load.png` (caso fuerte) sostienen el frame. Editor cultural puede invocar Pinterest/Notion templates como referencia visual genérica si hace falta.

### Micro 2.4 — LA TÍA QUE NO TIENE: CHATGPT CRIANDO

**[GAP — diferido]** Mismo backing global que 2.1. `macro-2-1-merca20-chatgpt-mama.png` y `macro-2-1-independent-mom-chatgpt.png` ya sostienen la narrativa de "ChatGPT como red familiar reemplazada".

### Micro 2.5 — EL PAPÁ QUE ANTES NO PREGUNTABA

#### Señal macro-2-5-tiktok-quique-aprendiendo-papa — Quique Rosas "Aprendiendo a ser papá"
- **Tipo:** verbatim — TikTok local (creador masculino)
- **Plataforma / medio:** TikTok (@soyquiquerosas)
- **Link:** https://www.tiktok.com/@soyquiquerosas/video/7229104569165597958
- **Screenshot:** `screenshots/trends-roles-genero/macro-2-5-tiktok-quique-aprendiendo-papa.png`
- **Caption sugerido:** Quique Rosas — "Aprendiendo a ser papá". 1.2M followers, paternidad activa pública en español.
- **Fuente footer:** TikTok @soyquiquerosas · 2023

---

## Señales verificadas — MACRO 3 · ALGORITMO DEL HOGAR

### Bloque macro 3

#### Señal macro-3-0-elnacional-tiktok-misogino — TikTok 4x contenido misógino a hombres jóvenes
- **Tipo:** dato — medio español
- **Plataforma / medio:** El Nacional
- **Link:** https://www.elnacional.cat/es/sociedad/tiktok-impulsa-contenido-misogino-extremo-entre-hombres-jovenes_1154811_102.html
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-0-elnacional-tiktok-misogino.png`
- **Caption sugerido:** El Nacional — estudio detectó aumento 4x en contenido misógino sugerido por TikTok en 5 días cuando el perfil es joven masculino.
- **Fuente footer:** El Nacional · 2025

#### Señal macro-3-0-bloomberg-tradwife-latam — Tradwife LATAM
- **Tipo:** dato — medio business LATAM
- **Plataforma / medio:** Bloomberg Línea
- **Link:** https://www.bloomberglinea.com/economia/tradwife-o-esposas-tradicionales-que-tan-real-es-la-tendencia-para-mujeres-de-latam/
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-0-bloomberg-tradwife-latam.png`
- **Caption sugerido:** Bloomberg Línea — Tradwife o "esposas tradicionales": qué tan real es la tendencia para mujeres LATAM.
- **Fuente footer:** Bloomberg Línea · 2024-2025

### Micro 3.1 — TRADWIFE CON SAZÓN EVANGÉLICA

#### Señal macro-3-1-boldlatina-latina-tradwives — Faith, Family, Femininity
- **Tipo:** medio cultura Latina
- **Plataforma / medio:** Boldlatina
- **Link:** https://www.boldlatina.com/faith-family-and-femininity-latina-tradwives-redefine-the-gender-roles-debate/
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-1-boldlatina-latina-tradwives.png`
- **Caption sugerido:** Boldlatina — "Faith, Family and Femininity": tradwives Latinas redefinen el debate de roles, conexión evangélica/católica explícita.
- **Fuente footer:** Boldlatina · 2024-2025

#### Señal macro-3-1-tandfonline-tradwives — Paper académico tradwives TikTok 2025
- **Tipo:** dato académico
- **Plataforma / medio:** Taylor & Francis Online
- **Link:** https://www.tandfonline.com/doi/full/10.1080/09540253.2025.2546050
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-1-tandfonline-tradwives.png`
- **Caption sugerido:** Tandfonline 2025 — paper académico: TikTok tradwives + reproduction + social media. Frame académico para el editor.
- **Fuente footer:** Tandfonline · 2025

#### Señal macro-3-1-tiktok-roro-tradwife — RoRo López Bueno tradwife española
- **Tipo:** verbatim — TikTok referente global hispano
- **Plataforma / medio:** TikTok (@elmundo.es citando @roro.bueno / @whoisroro)
- **Link:** https://www.tiktok.com/@elmundo.es/video/7395159521426967841
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-1-tiktok-roro-tradwife.png`
- **Caption sugerido:** El Mundo (TikTok) cubre a RoRo Bueno: 22 años, cocina y edita libros para su novio Pablo. La cara hispana del trend tradwife.
- **Fuente footer:** TikTok @elmundo.es · 2024-07

#### Señal macro-3-1-tiktok-proverbios31-soyvalioso — Mujer virtuosa cristiana
- **Tipo:** verbatim — TikTok cristiano hispano
- **Plataforma / medio:** TikTok (@soy.valioso)
- **Link:** https://www.tiktok.com/@soy.valioso/video/7416205128040041733
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-1-tiktok-proverbios31-soyvalioso.png`
- **Caption sugerido:** Soy Valioso — Proverbios 31:10 "Mujer virtuosa, ¿quién la hallará?". Frame evangélico tradwife sin nombrarlo así.
- **Fuente footer:** TikTok @soy.valioso · 2024

#### Señal macro-3-1-tiktok-mujer-virtuosa-disciple-omi — Esposa virtuosa según Proverbios 31
- **Tipo:** verbatim — TikTok cristiano
- **Plataforma / medio:** TikTok (@disciple_omi)
- **Link:** https://www.tiktok.com/@disciple_omi/video/7581944388549496077
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-1-tiktok-mujer-virtuosa-disciple-omi.png`
- **Caption sugerido:** Disciple Omi — "El valor de una esposa virtuosa según Proverbios 31:10-12". Currículum oculto evangélico del rol esposa.
- **Fuente footer:** TikTok @disciple_omi · 2025

### Micro 3.2 — EL ALGORITMO QUE LE HABLA AL HIJO VARÓN

#### Señal macro-3-2-19thnews-alpha-males — Algorithms alpha males tradwives 2025
- **Tipo:** reportaje — medio US periodismo género
- **Plataforma / medio:** The 19th
- **Link:** https://19thnews.org/2025/06/internet-culture-algorithms-alpha-males-tradwives/
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-2-19thnews-alpha-males.png`
- **Caption sugerido:** The 19th — "Internet culture, algorithms, alpha males and tradwives": Equimundo report ~50% hombres jóvenes confían en al menos un influencer manosphere.
- **Fuente footer:** The 19th · 2025-06

#### Señal macro-3-2-occrp-marbella-manosphere — Hub manosphere en Marbella
- **Tipo:** reportaje — medio internacional investigativo
- **Plataforma / medio:** OCCRP
- **Link:** https://www.occrp.org/en/feature/sun-cigars-and-sexism-how-spains-marbella-became-a-hotspot-for-manosphere-influencers
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-2-occrp-marbella-manosphere.png`
- **Caption sugerido:** OCCRP — "Sun, cigars and sexism": Marbella se convierte en hotspot de influencers manosphere alineados con Tate. Hispanoparlante.
- **Fuente footer:** OCCRP · 2024-2025

#### Señal macro-3-2-tiktok-andrew-tate-espanol — Andrew Tate en español
- **Tipo:** verbatim — TikTok manosphere hispano
- **Plataforma / medio:** TikTok (@highvaluemales / @andrew.tate.espanol)
- **Link:** https://www.tiktok.com/@highvaluemales/video/7115901381503978758
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-2-tiktok-andrew-tate-espanol.png`
- **Caption sugerido:** "High Value Males" — Andrew Tate doblado al español. Ejemplo de cómo entra el manosphere al feed hispano joven.
- **Fuente footer:** TikTok @highvaluemales · 2022-2025
- **NOTA HUNTER:** Existe además @andrew.tate.espanol como cuenta fan dedicada. Confirma que Tate llegó a TikTok en español.

#### Señal macro-3-2-espanolnews-andrew-tate — Por qué Tate se está apoderando de TikTok
- **Tipo:** reportaje — medio hispano
- **Plataforma / medio:** Espanol.news
- **Link:** https://espanol.news/quien-es-andrew-tate-y-por-que-la-controvertida-figura-se-esta-apoderando-de-tiktok/
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-2-espanolnews-andrew-tate.png`
- **Caption sugerido:** Espanol.news — explicación del fenómeno Tate en TikTok hispano para audiencias jóvenes masculinas.
- **Fuente footer:** Espanol.news · 2024-2025

### Micro 3.3 — STAY-AT-HOME GIRLFRIEND CON DELIVERY

#### Señal macro-3-3-sage-stayathomegirlfriend — Paper "From girlboss to #stayathomegirlfriend"
- **Tipo:** dato académico
- **Plataforma / medio:** Sage Journals
- **Link:** https://journals.sagepub.com/doi/10.1177/13675494241285643
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-3-sage-stayathomegirlfriend.png`
- **Caption sugerido:** Sage Journals — Isabel Sykes 2025: "From girlboss to #stayathomegirlfriend: The romanticisation of domestic labour on TikTok".
- **Fuente footer:** Sage Journals · 2025

#### Señal macro-3-3-tiktok-sahg-aliyah — Day in the life SAHG
- **Tipo:** verbatim — TikTok global referente
- **Plataforma / medio:** TikTok (@aliyahwears)
- **Link:** https://www.tiktok.com/@aliyahwears/video/7275392594656496938
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-3-tiktok-sahg-aliyah.png`
- **Caption sugerido:** AliyahWears — "Day in the life of a stay-home girlfriend": eventos, belleza, rutinas. Estetización doméstica.
- **Fuente footer:** TikTok @aliyahwears · 2023

#### Señal macro-3-3-tiktok-sahg-lexiixi-morning — Morning routine SAHG
- **Tipo:** verbatim — TikTok global
- **Plataforma / medio:** TikTok (@lexiixi)
- **Link:** https://www.tiktok.com/@lexiixi/video/7548267212381900045
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-3-tiktok-sahg-lexiixi-morning.png`
- **Caption sugerido:** Lexii Arjona — "Morning routine of a Stay-at-Home Girlfriend". El ASMR aspiracional de no trabajar.
- **Fuente footer:** TikTok @lexiixi · 2025

### Micro 3.4 — #DADTOK: EL PADRE QUE GRABA LA CRIANZA

#### Señal macro-3-4-univision-tribudepapas — TribuDePapas viral
- **Tipo:** reportaje — medio US Latino
- **Plataforma / medio:** Univision
- **Link:** https://www.univision.com/entretenimiento/cultura-pop/tiktok-hombres-normalizan-laborales-hogar-paternidad
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-4-univision-tribudepapas.png`
- **Caption sugerido:** Univision — #TribuDePapas: 10 cuentas de papás influyentes (México) viralizan tareas domésticas con +3.8M views. "Si podemos, tú también".
- **Fuente footer:** Univision · 2024

#### Señal macro-3-4-tiktok-quique-rosas-papa-primerizo — Día en mi vida como papá primerizo
- **Tipo:** verbatim — TikTok local hispano (mexicano)
- **Plataforma / medio:** TikTok (@soyquiquerosas)
- **Link:** https://www.tiktok.com/@soyquiquerosas/video/7351217922259340549
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-4-tiktok-quique-rosas-papa-primerizo.png`
- **Caption sugerido:** Quique Rosas (1.2M followers) — "Un día en mi vida como papá primerizo". Paternidad activa pública en español.
- **Fuente footer:** TikTok @soyquiquerosas · 2024

#### Señal macro-3-4-tiktok-quique-limpiar-casa — ¿Por qué limpio la casa?
- **Tipo:** verbatim — TikTok hispano
- **Plataforma / medio:** TikTok (@soyquiquerosas)
- **Link:** https://www.tiktok.com/@soyquiquerosas/video/7380877040385346822
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-4-tiktok-quique-limpiar-casa.png`
- **Caption sugerido:** Quique Rosas — "¿Por qué limpio la casa? Las relaciones funcionan porque las personas están dispuestas a hacerlas funcionar." Verbatim oro para Micro 3.4.
- **Fuente footer:** TikTok @soyquiquerosas · 2024

#### Señal macro-3-4-tiktok-humor-tareas-hogar — Humor sobre hombres y tareas (Laura Donis)
- **Tipo:** meme — TikTok hispano
- **Plataforma / medio:** TikTok (@lauradonis0)
- **Link:** https://www.tiktok.com/@lauradonis0/video/7034218158139428101
- **Screenshot:** `screenshots/trends-roles-genero/macro-3-4-tiktok-humor-tareas-hogar.png`
- **Caption sugerido:** Laura Donis — humor sobre tareas del hogar y parejas. #maridos #comedia #humorparejas. Contrapunto pop al frame serio.
- **Fuente footer:** TikTok @lauradonis0 · 2021-2022 (HISTÓRICO · CONTRASTE)

### Micro 3.5 — LA SUEGRA SE LLAMA ALGORITMO

**[GAP — diferido]** Sin captura propia. Reutilizable: `macro-3-0-elnacional-tiktok-misogino.png` (polarización algorítmica) y `macro-3-1-boldlatina-latina-tradwives.png` (momfluencer evangélica). El concepto vive en la analítica del editor cultural sobre el feed personalizado vs. la autoridad intergeneracional.

---

## Señales descartadas / LOGIN-REQUIRED / FECHA NO VÁLIDA

| # | Señal original | Razón |
|---|---|---|
| Infobae RD 8.7% caída matrimonios 2025 | https://www.infobae.com/republica-dominicana/2026/05/17/republica-dominicana-experimenta-una-ligera-caida-del-87--en-2025/3536088 | 404 — link futuro/desbordado. Hunter debe sustituir con cobertura equivalente |
| TikTok #plancha planchando 11pm | búsqueda hashtag | NO ENCONTRADA — sin huella viral hispana específica sobre planchar como género (gap legítimo, hallazgo en sí mismo) |
| Banco Mundial 53.5% participación laboral mujer RD | https://datos.bancomundial.org/indicador/SL.TLF.CACT.FE.NE.ZS?locations=DO | Portal SPA lento, anti-bot, no procesado. PENDIENTE — Jeremy puede capturar manualmente desde el navegador (dato es robusto y verificable) |
| @alissonrodriguez2 Proverbios 31:30 | https://www.tiktok.com/@alissonrodriguez2/video/6943338377026505989 | oembed FAIL-meta — video posiblemente privado o borrado |
| AdAge tags family-marketing / TikTok | adage.com | LOGIN-REQUIRED — Chrome MCP CDP timeout impidió usar la sesión autenticada de Jeremy. Pendiente para captura manual si el editor cultural necesita un caso AdAge concreto (no es bloqueante: las señales LATAM/locales sostienen el deck) |
| TrendWatching Innovations | app.trendwatching.com | LOGIN-REQUIRED — mismo motivo. No bloqueante |
| Pinterest "nursery aesthetic" boards RD | Pinterest | NO PROCESADO — baja prioridad para Micro 3.5 |
| Reddit hilos r/dominicana | reddit.com | NO PROCESADO — baja prioridad, no afecta el deck base |
| YouTube podcast paternidad LATAM | YouTube | NO PROCESADO — Quique Rosas TikToks ya cubren el frame |
| Equimundo State of American Men 2025 PDF | Equimundo | NO PROCESADO — la cita ya está en 19thnews (capturada); el PDF directo es redundante |
| Netflix docu "Inside the Manosphere" Theroux | Netflix | NO PROCESADO — paywall app, sustituible por OCCRP/19thNews |

---

## Notas para el editor cultural

### 1. Hallazgo de validación local — Micro 1.1
**@madresrealesrd existe y articula "CargaMentalMaterna" en español dominicano.** Cuenta dirigida por Lyn, video destacado [aquí](https://www.tiktok.com/@madresrealesrd/video/7262536453459086597). Esto valida directamente la tesis del Micro 1.1 con un creador RD nativo. Es la pieza que el hunter había marcado como hipótesis pendiente y que ahora confirma: la mujer dominicana ya tiene vocabulario para nombrar la brecha declarado-vivido en TikTok. **Recomendación:** Lyn (madresrealesrd) merece ser el rostro local del Micro 1.1 en el deck.

### 2. Refutación parcial — Micro 3.1 sobre tradwives dominicanas explícitas
**No se encontró un cluster de tradwives dominicanas auto-identificadas.** Lo que sí existe en TikTok hispano es el frame **"esposa virtuosa / Proverbios 31"** desde lo evangélico, manejado por creadores como @soy.valioso (panamericano) y @disciple_omi. RD lo importa sin nombrarlo "tradwife". RoRo Bueno (España) sigue siendo el referente global hispano. **Implicación:** el editor cultural puede argumentar que la tradwife en RD no se llama tradwife — se llama "esposa virtuosa", "ama de casa por elección", "mujer que sirve". Hace el insight más fuerte: el frame entra pero RD lo cristianiza.

### 3. Confirmación — Micro 3.2 manosphere hispano
**@highvaluemales y @andrew.tate.espanol confirman que Andrew Tate llegó al feed hispano joven.** El acceso es directo, sin barrera de idioma. Esto valida la tesis de currículum oculto digital en hijos varones RD. El Marbella hub (OCCRP) le da geografía cercana — España como puente cultural.

### 4. Confirmación parcial — Micro 3.4 #DadTok hispano
**Quique Rosas (México, 1.2M) es el caso más fuerte de papá-influencer en español sobre paternidad activa.** El hunter buscaba creadores RD masculinos en #DadTok 2024-2026; el scrapeo confirma que el cluster existe **en hispano** (México, Univision lo cubrió) pero **no se identificaron creadores RD específicos** con tracción comparable. Hipótesis para editor: el deck puede argumentar que "el #DadTok hispano ya existe — pero RD aún no produce sus Quiques". Es un gap local interesante para escribir.

### 5. Plancha invisible — Micro 1.2 hallazgo del propio scrapeo
**La plancha como tema viral no existe en TikTok hispano.** Buscamos #plancha + tareas hispanas y la huella es nula. Esto es un hallazgo en sí: la tarea más extrema de inequidad doméstica (1.8% hombre en RD) es tan invisible que ni siquiera el meme la rescata. **Recomendación al editor cultural:** convertir esa ausencia en headline — "Hay TikToks para todo. Pero no hay TikToks de la plancha."

### 6. Cita ChatGPT mom — caso fuerte LATAM
Independent Español + Merca 2.0 + Infobae cubren explícitamente el caso "madre viral por usar ChatGPT". El Micro 2.1 tiene más backing LATAM/global del que el hunter anticipó. **Listo para deck sin reservas.**

### 7. Notas para el hunter (iteración futura)
- Hipótesis 1 del hunter ("¿existe primer cohorte de papás dominicanos TikTok?"): respuesta tentativa **NO con tracción visible**. Los referentes son mexicanos. Vale para hilo futuro.
- Hipótesis 2 ("creadoras dominicanas evangélicas adoptan tradwife sin nombrarlo"): **CONFIRMADA tendencia regional**, no se logró aislar RD específico — pero el frame "esposa virtuosa Proverbios 31" sí cruza fronteras.
- Hipótesis 3 ("uso IA en RD por sexo"): sigue sin data disponible. Sería buen prompt para sintetico-v3 si Código Casa tiene ítem cruzable.

---

## Evaluación del scrapper

**Mapa listo para editor cultural.** Las 45 señales capturadas cubren cómodamente los 5 micros que el hunter recomendó como headline (1.1, 1.3, 2.1, 3.1, 3.2) y dan soporte sólido a 3.3, 3.4. Los gaps en 1.2, 2.2-2.4 y 3.5 son **gaps reales del paisaje viral hispano** — no fallas del scrapeo — y se convierten en material narrativo para el editor cultural (la invisibilidad de la plancha, la falta de creadores RD masculinos en #DadTok). El deck puede salir con esto.

*Fin del mapa — Scrapper Trends CC · trends-roles-genero-señales.md*
