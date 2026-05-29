"""
build_trends_educacion.py — Capítulo 07 EDUCACIÓN

SOLO DATOS. Todo el layout vive en trends_deck_engine.py (el "CSS" central).
Para cambiar espaciado/tamaños/fuentes NO toques este archivo — edita el motor
y TODOS los capítulos se actualizan idénticos.
"""

from pathlib import Path
from trends_deck_engine import build_deck

BASE        = Path("/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC")
SCREENSHOTS = BASE / "screenshots" / "trends-educacion"
OUTPUT      = BASE / "outputs" / "trends-educacion-forecast.pptx"

# ─── Macros ─────────────────────────────────────────────────────────────────
M1_N = "MACRO 1"; M1_NAME = "INVENTOLOGÍA DE LA ADULTEZ"
M1_TAG = "Un mundo en crisis está reescribiendo qué significa ser adulto y formar familia."
M2_N = "MACRO 2"; M2_NAME = "LOS HERNÁNDEZ ARE PROMPTED"
M2_TAG = "El dominicano ya entró al mundo prompteado. Solo no lo nombra así."
M3_N = "MACRO 3"; M3_NAME = "ALGORITMO DEL HOGAR"
M3_TAG = "El feed se sentó en la mesa y nadie le ofreció silla."

DIVIDERS = [
    (1, M1_NAME, M1_TAG),
    (2, M2_NAME, M2_TAG),
    (3, M3_NAME, M3_TAG),
]

MICROS = [
    # ── Macro 1 ──────────────────────────────────────────────────────────────
    # 1.1 — El diploma dejó de ser el ticket
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="El diploma dejó de ser el ticket: 53% de empleadores ya contrata por skills demostrados.",
         fenomeno="En 2025, 53% de empleadores dejó de pedir título y contrató por habilidad demostrada. La paradoja: 85% dice contratar por skills, pero en los números reales apenas 1 de cada 700 contrataciones ocurre sin título. El ticket viejo perdió su monopolio simbólico.",
         hashtags="#skillsnotdegrees · #collegedropout · #selftaught · #careerchange · #notitulonecesario",
         triggers=[
             dict(stat="53%",   desc="De empleadores eliminó el requisito de título en 2025, +30% vs 2024.", source="TestGorilla · 2025"),
             dict(stat="85%",   desc="Dice contratar por skills — pero solo 1 de cada 700 contrataciones reales es sin título.", source="Harvard / Burning Glass · 2025"),
             dict(stat="1/700", desc="Contrataciones sin título en la realidad, vs el discurso skills-first dominante.", source="The Interview Guys · 2025"),
         ],
         signals=[
             dict(png="macro-1-1-tiktok-skillsnotdegrees.png",
                  caption="Página del hashtag #skillsnotdegrees en TikTok — grid del trend skills vs título.",
                  source="TikTok · 2025",
                  url="https://www.tiktok.com/tag/skillsnotdegrees"),
             dict(png="macro-1-1-interviewguys-skills-hiring-2025.png",
                  caption="State of Skills-Based Hiring 2025 — la paradoja 85% discurso vs 1/700 contrataciones sin título.",
                  source="The Interview Guys · 2025",
                  url="https://blog.theinterviewguys.com/the-state-of-skills-based-hiring/"),
             dict(png="macro-1-0-accelerec-skills-hiring.png",
                  caption="Hero artículo 'The 4-Year Degree Is Dead' — skills-based hiring como default 2025.",
                  source="Accelerec · 2025",
                  url="https://accelerec.com/the-4-year-degree-is-dead-why-skills-based-hiring-is-taking-over-in-2025/"),
         ]),

    # 1.2 — Ya nadie terminó de estudiar
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="Ya nadie terminó de estudiar: el adulto LATAM se re-skillea cada 2-3 años porque 39% de las habilidades cambia para 2030.",
         fenomeno="70% de profesionales dice que el upskilling es clave para su seguridad laboral, y 72% de los managers ya está en eso. El driver: 39% de las habilidades del trabajo van a cambiar para 2030. Quedarte quieto es quedarte atrás.",
         hashtags="#lifelonglearning · #reskilling · #upskilling · #aprenderparasiempre · #careergrowth",
         triggers=[
             dict(stat="70%",  desc="De profesionales dice que el upskilling es clave para su seguridad laboral.", source="edX Spring · 2025"),
             dict(stat="39%",  desc="De las habilidades laborales cambiarán para 2030 — el 'Great Skills Reset'.", source="WEF Future of Jobs · 2025"),
             dict(stat="129%", desc="Crecimiento interanual de inscripciones LATAM en ciberseguridad en Coursera.", source="Coursera Global Skills Report · 2025"),
         ],
         signals=[
             dict(png="macro-1-2-wef-future-of-jobs.png",
                  caption="WEF Future of Jobs 2025 — titular 'Great Skills Reset', 39% de skills cambian para 2030.",
                  source="WEF Future of Jobs · 2025",
                  url="https://www.weforum.org/stories/2025/01/future-of-jobs-report-2025-jobs-of-the-future-and-the-skills-you-need-to-get-them/"),
             dict(png="macro-1-2-coursera-global-skills-report.png",
                  caption="Coursera Global Skills Report 2025 — badge digital para profesionales en upskilling.",
                  source="Coursera Global Skills Report · 2025",
                  url="https://www.coursera.org/skills-reports/global"),
         ]),

    # 1.3 — Familias sacan a sus hijos del colegio por elección
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="Familias globales sacan a sus hijos del colegio por elección: el aula de 30 compite con microschools de 5-15 y currículos a la medida.",
         fenomeno="El homeschool creció 4.9% en 2024-25, casi 3x la tasa pre-pandemia, y 36% de estados de EEUU reportó máximos históricos. Aparecen microschools — hubs de 5 a 15 alumnos donde la familia diseña el currículo. Entre 1 y 2 millones de estudiantes ya asisten full-time.",
         hashtags="#homeschool · #microschool · #unschooling · #homeschoollife · #educacionalternativa",
         triggers=[
             dict(stat="4.9%",  desc="Crecimiento del homeschool en 2024-25, casi 3x la tasa pre-pandemia.", source="JHU Institute for Education Policy · 2025"),
             dict(stat="36%",   desc="De estados de EEUU reportó máximos históricos en homeschooling.", source="JHU Institute for Education Policy · 2025"),
             dict(stat="1-2M",  desc="Estudiantes en EEUU ya asisten a microschools full-time, promedio 22 alumnos.", source="RAND / National Microschooling Center · 2025"),
         ],
         signals=[
             dict(png="macro-1-3-jhu-homeschool-growth.png",
                  caption="JHU Homeschool Hub 2024-2025 — datos de crecimiento 4.9% con mapa de estados y máximos históricos.",
                  source="JHU Institute for Education Policy · 2025",
                  url="https://education.jhu.edu/edpolicy/policy-research-initiatives/homeschool-hub/homeschool-growth-2024-2025/"),
             dict(png="macro-1-3-cbsmiami-microschools.png",
                  caption="CBS Miami sobre microschools — hub de aprendizaje alternativo en Florida, familias eligiendo.",
                  source="CBS Miami · 2025",
                  url="https://www.cbsnews.com/miami/news/microschools-families-flexible-alternative/"),
             dict(png="macro-1-3-theschoolhouse-microschools.png",
                  caption="'Why Microschools Are Rising' — grupo pequeño de estudiantes en entorno alternativo.",
                  source="The Schoolhouse · 2025",
                  url="https://www.theschoolhouse.org/post/rising-microschools-education"),
         ]),

    # 1.4 — El siguiente paso obviootras ya no es obvio
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="El siguiente paso obvio tras el bachillerato dejó de ser obvio: gap year, bootcamp y emprendimiento adolescente sustituyen el ingreso inmediato.",
         fenomeno="Solo 18% de Gen Z global ve subir la escalera corporativa como algo inteligente. Y Big Tech lo validó: Google, IBM y Tesla quitaron el título para muchos roles. El recién graduado se da un año, hace un bootcamp, o monta un ingreso con skills digitales antes de comprometerse.",
         hashtags="#gapyear · #alternativestocollege · #teenentrepreneur · #nocollege · #emprendimientojoven",
         triggers=[
             dict(stat="18%",   desc="De Gen Z global ve subir la escalera corporativa como algo inteligente.", source="Fiverr · Oct 2025"),
             dict(stat="3",     desc="Big Tech — Google, IBM y Tesla — eliminaron el título universitario para muchos roles.", source="OneCodeSoft · 2025"),
             dict(stat="2025",  desc="#gapyear y 'alternatives to college' crecen como género propio de contenido en TikTok.", source="TikTok Discover · 2025"),
         ],
         signals=[
             dict(png="macro-1-4-tiktok-gapyear.png",
                  caption="Página del hashtag #gapyear en TikTok — grid de jóvenes mostrando su path alternativo.",
                  source="TikTok · 2025",
                  url="https://www.tiktok.com/tag/gapyear"),
             dict(png="macro-1-4-onecodesoft-bigtech-skills.png",
                  caption="'Degree vs. Skills: Big Tech's 2025 Micro-Credential Pivot' — Google, IBM, Tesla sin título.",
                  source="OneCodeSoft · 2025",
                  url="https://onecodesoft.com/blogs/degree-vs-skills-big-techs-2025-micro-credential-pivot"),
         ]),

    # 1.5 — La familia compensa lo que la escuela dejó de garantizar
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="La familia compensa lo que la escuela dejó de garantizar: 70% de niños no lee bien a los 10 y el mercado de tutoría AI ya vale US$3.55B.",
         fenomeno="La pandemia dejó un hueco que el sistema formal no recuperó. La pobreza de aprendizaje subió a ~70% en países de ingreso medio-bajo. NAEP reportó las mayores caídas en lectura y matemática en 35 años. ¿La respuesta de la familia? Pagar el refuerzo por fuera.",
         hashtags="#learningloss · #tutoring · #refuerzoescolar · #educationcrisis · #apoyoescolar",
         triggers=[
             dict(stat="~70%",    desc="Pobreza de aprendizaje post-pandemia en países de ingreso medio-bajo; LATAM perdió 225 días de clase.", source="Banco Mundial / UNESCO · 2024"),
             dict(stat="35 años", desc="NAEP reportó las mayores caídas en lectura y matemática de toda su historia evaluativa.", source="NAEP / UNA-USA · 2024"),
             dict(stat="US$3.55B", desc="Mercado de tutoría AI en 2025, proyectado a US$6.45B en 2030.", source="Future Market Insights · 2025"),
         ],
         signals=[
             dict(png="macro-1-5-worldbank-learning-poverty.png",
                  caption="World Bank Learning Poverty report — infografía sobre pobreza de aprendizaje global post-pandemia.",
                  source="World Bank · 2024",
                  url="https://www.worldbank.org/en/topic/education/publication/state-of-global-learning-poverty"),
             dict(png="macro-1-5-unausa-naep-scores.png",
                  caption="UNA-USA sobre las mayores caídas NAEP en lectura y matemática en 35 años.",
                  source="UNA-USA / NAEP · 2024",
                  url="https://unausa.org/gga-blog-post-1/"),
         ]),

    # ── Macro 2 ──────────────────────────────────────────────────────────────
    # 2.1 — El tutor 1-a-1 dejó de ser privilegio de élite
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="El tutor 1-a-1 dejó de ser privilegio de élite: Khanmigo pasó de 68k a 1.4M usuarios en un año.",
         fenomeno="Khanmigo pasó de 68k usuarios en 2023-24 a 1.4M a mediados de 2025 — y de 40k a 700k estudiantes K-12 en un ciclo. El mercado de tutores AI va de US$3.55B (2025) a US$6.45B (2030). El estudiante resuelve dudas a cualquier hora con un tutor que no se cansa ni cobra por sesión.",
         hashtags="#aitutor · #khanmigo · #studywithai · #tutoriaIA · #aprenderconIA",
         triggers=[
             dict(stat="1.4M",    desc="Usuarios de Khanmigo en mediados 2025, creciendo desde 68k en 2023-24.", source="Khan Academy / GlobalSociety · 2025"),
             dict(stat="700K",    desc="Estudiantes K-12 usando Khanmigo — de 40k a 700k en un ciclo escolar.", source="Khan Academy · 2025"),
             dict(stat="US$3.55B", desc="Mercado de tutores AI en 2025 proyectado a US$6.45B en 2030.", source="Future Market Insights · 2025"),
         ],
         signals=[
             dict(png="macro-2-1-khanmigo-hero-landing.png",
                  caption="Landing de Khanmigo — 'always-available teaching assistant' con interfaz del tutor AI.",
                  source="Khanmigo / Khan Academy · 2025",
                  url="https://khanmigo.ai/"),
             dict(png="macro-2-1-globalsociety-khanmigo-ai-tools.png",
                  caption="Khanmigo escala en distritos escolares — estudiante con herramientas AI de Khan Academy.",
                  source="Global Society · 2025",
                  url="https://www.globalsociety.earth/post/khan-academy-rolls-out-ai-powered-teaching-tools-as-school-districts-scale-up-adoption"),
             dict(png="macro-2-1-futuremarketinsights-ai-tutor.png",
                  caption="AI Tutoring Services Market — US$3.55B (2025) proyectado a US$6.45B (2030).",
                  source="Future Market Insights · 2025",
                  url="https://www.futuremarketinsights.com/reports/ai-tutoring-services-market"),
         ]),

    # 2.2 — Aprender se gamificó
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="Aprender se gamificó y compite con TikTok usando las mismas mecánicas: Duolingo sostiene 50.5M usuarios diarios con rachas, ligas y culpa del búho.",
         fenomeno="Duolingo superó 50.5M usuarios diarios en Q3 2025, +36% interanual. El churn bajó de 47% a 28% gracias a la gamificación. Revenue del trimestre: US$271.7M, +41%. La gente mantiene rachas no por disciplina — por el miedo a romperla.",
         hashtags="#duolingo · #duostreak · #languagelearning · #gamifiedlearning · #aprenderjugando",
         triggers=[
             dict(stat="50.5M", desc="Usuarios diarios de Duolingo en Q3 2025, +36% interanual.", source="Duolingo 8-K SEC · 2025"),
             dict(stat="28%",   desc="Churn de Duolingo — bajó de 47% a 28% gracias a la gamificación de rachas.", source="StriveCloud / Duolingo · 2025"),
             dict(stat="+41%",  desc="Revenue Q3 2025 de Duolingo: US$271.7M con 11.5M suscriptores pagos.", source="Duolingo SEC Filing FY2025"),
         ],
         signals=[
             dict(png="macro-2-2-duolingo-landing.png",
                  caption="Landing de Duolingo — búho Duo y propuesta gamificada de aprendizaje diario en 5 minutos.",
                  source="Duolingo · 2025",
                  url="https://www.duolingo.com/"),
             dict(png="macro-2-2-duolingo-streaks-gamification.png",
                  caption="Mecánica de rachas (streaks) de Duolingo — UI de objetivo diario y contador de racha.",
                  source="Duolingo · 2025",
                  url="https://www.strivecloud.io/blog/gamification-examples-boost-user-retention-duolingo"),
             dict(png="macro-2-2-strivecloud-duolingo-hero.png",
                  caption="Análisis de gamificación de Duolingo — retención de usuarios +36% interanual.",
                  source="StriveCloud · 2025",
                  url="https://www.strivecloud.io/blog/gamification-examples-boost-user-retention-duolingo"),
         ]),

    # 2.3 — La IA generativa automatizó la tarea
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="La IA generativa automatizó la tarea escolar: 84% de secundaria la usa, y la pregunta dejó de ser si copian.",
         fenomeno="84% de los estudiantes de secundaria usa IA generativa para schoolwork; 53% para ensayos. El uso en educación superior global saltó de 66% (2024) a 92% (2025). 44% de docentes detecta tarea sospechosa de IA cada semana, pero menos del 15% actúa.",
         hashtags="#chatgptforschool · #aihomework · #studyhack · #aidetector · #tareaconIA",
         triggers=[
             dict(stat="84%",  desc="De estudiantes de secundaria usa IA generativa para schoolwork; 89% para tareas.", source="Nerdynav · 2025"),
             dict(stat="92%",  desc="De estudiantes de educación superior usa IA en 2025, subiendo desde 66% en 2024.", source="Demandsage · 2026"),
             dict(stat="44%",  desc="De docentes detecta tarea sospechosa de IA semanalmente, pero <15% actúa.", source="EdWeek · 2025"),
         ],
         signals=[
             dict(png="macro-2-3-nerdynav-chatgpt-cheating-infographic.png",
                  caption="Infografía Nerdynav — 84% de secundaria usa IA para tareas, 89% para homework.",
                  source="Nerdynav · 2025",
                  url="https://nerdynav.com/chatgpt-cheating-statistics/"),
             dict(png="macro-2-3-nerdynav-student-usage-chart.png",
                  caption="Chart de uso de IA por tipo de tarea — ensayos, homework, investigación.",
                  source="Nerdynav · 2025",
                  url="https://nerdynav.com/chatgpt-cheating-statistics/"),
             dict(png="macro-2-3-edweek-ai-cheating.png",
                  caption="EdWeek — 44% de docentes detecta tarea IA semanalmente, <15% actúa por falta de prueba.",
                  source="Education Week · 2024",
                  url="https://www.edweek.org/technology/new-data-reveal-how-many-students-are-using-ai-to-cheat/2024/04"),
         ]),

    # 2.4 — El diploma de papel se mudó a la nube
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="El diploma de papel se mudó a la nube: 90% de empleadores prefiere candidato con microcredencial y los badges verificables son moneda de empleabilidad.",
         fenomeno="Más del 90% de empleadores prefiere candidato con microcredencial en el CV. Coursera lleva 15.4M+ inscripciones en certificados profesionales entry-level. El profesional exhibe el badge de Google o Coursera como prueba portátil y verificable.",
         hashtags="#microcredentials · #digitalbadges · #googlecertificate · #coursera · #credencialesdigitales",
         triggers=[
             dict(stat="+90%",   desc="De empleadores prefiere candidato con microcredencial en el CV.", source="Coursera / Fortune · 2025"),
             dict(stat="15.4M+", desc="Inscripciones en certificados profesionales entry-level de Coursera.", source="Coursera Global Skills Report · 2025"),
             dict(stat="2026",   desc="'Getting hired in 2026 is all about your microcredentials' — CEO Coursera a Gen Z.", source="Fortune · Dic 2025"),
         ],
         signals=[
             dict(png="macro-2-4-fortune-microcredentials.png",
                  caption="Fortune: 'Getting hired in 2026 is all about your microcredentials' — CEO Coursera.",
                  source="Fortune · Dec 2025",
                  url="https://fortune.com/2025/12/28/2026-microcredential-hiring-trend-coursera-greg-hart/"),
             dict(png="macro-2-4-coursera-google-cert.png",
                  caption="Google Career Certificates — badges digitales verificables para roles tech sin título universitario.",
                  source="Google / Coursera · 2025",
                  url="https://grow.google/certificates/"),
             dict(png="macro-2-4-edsurge-digital-credentials.png",
                  caption="EdSurge — credenciales digitales verificables que elevan el perfil sin esperar graduación.",
                  source="EdSurge · 2024",
                  url="https://www.edsurge.com/news/2024-11-22-how-digital-credentials-can-elevate-existing-programs"),
         ]),

    # 2.5 — El docente también usa IA
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="No solo el estudiante usa IA, el docente también: en RD 98% de la facultad universitaria conoce IA y el país lidera el uso de ChatGPT entre profesores.",
         fenomeno="El docente sobrecargado delega lo administrativo — planes de clase, rúbricas, exámenes — para enfocarse en enseñar. RD aparece con fuerza: 98% de docentes universitarios conoce IA, lidera uso de ChatGPT. Khanmigo se expandió de 45 a más de 380 distritos.",
         hashtags="#teacherai · #aiforteachers · #docenteIA · #smartclassroom · #edtechRD",
         triggers=[
             dict(stat="98%",  desc="De docentes universitarios RD conoce conceptos de IA; el país lidera uso de ChatGPT en facultad.", source="HMTV / INTEC-PUCMM-UASD · 2025"),
             dict(stat="380+", desc="Distritos escolares con Khanmigo, expandido desde 45 con herramientas docentes AI.", source="Khan Academy · 2025"),
             dict(stat="2025", desc="Paper dominicano 'Educación Superior en la Era de la IA: Entre la Innovación y la Ética'.", source="SciELO Dominican Republic · 2025"),
         ],
         signals=[
             dict(png="macro-2-5-hmtv-ai-profesor-rd-chrome.png",
                  caption="HMTV — 98% docentes universitarios RD conocen IA, país lidera uso de ChatGPT en facultad.",
                  source="HMTV / INTEC-PUCMM · 2025",
                  url="https://www.hmtv.com.do/index.php/noticias/noticias/42251-la-inteligencia-artificial-redefine-el-rol-del-profesor-universitario-en-republica-dominicana"),
             dict(png="macro-2-5-scielo-ai-educacion-rd.png",
                  caption="Paper SciELO DO — 'Educación Superior en la Era de la IA', adopción docente en RD.",
                  source="SciELO Dominican Republic · 2025",
                  url="https://scielo.do/scielo.php?script=sci_arttext&pid=S2636-21632025003900007&lang=pt"),
             dict(png="macro-2-0-demandsage-ai-education-stats.png",
                  caption="AI in Education Statistics 2026 — mercado US$5.88B → US$32.27B; 92% uso en ed. superior.",
                  source="Demandsage · 2026",
                  url="https://www.demandsage.com/ai-in-education-statistics/"),
         ]),

    # ── Macro 3 ──────────────────────────────────────────────────────────────
    # 3.1 — Estudiar se volvió contenido
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="Estudiar se volvió contenido: study with me lives y notas estéticas convierten el estudio solitario en espectáculo social.",
         fenomeno="Los 'study with me' lives y las notas estéticas convirtieron la sesión de estudio en una experiencia social-algorítmica. El educativo es la 2da categoría más vista en TikTok (16.1% de views). La disciplina ya no viene de adentro — viene de la mirada de extraños en el feed.",
         hashtags="#studytok · #studywithme · #studygram · #studymotivation · #estudiarconmigo",
         triggers=[
             dict(stat="16.1%", desc="Del total de views de TikTok corresponde a contenido educativo — 2da categoría más vista.", source="SmileTutor · 2025"),
             dict(stat="7.36%", desc="De engagement de las cuentas de educación superior en TikTok — sobre el promedio de plataforma.", source="SmileTutor · 2025"),
             dict(stat="2025",  desc="Revisión sistemática: métodos asistidos por TikTok elevan motivación, participación y desempeño.", source="CTO College · 2026"),
         ],
         signals=[
             dict(png="macro-3-0-tiktok-studytok-tag.png",
                  caption="Página del hashtag #studytok en TikTok — grid de top videos de estudio compartido y notas estéticas.",
                  source="TikTok · 2025",
                  url="https://www.tiktok.com/tag/studytok"),
             dict(png="macro-3-1-youtube-studywithme.png",
                  caption="Resultados YouTube 'study with me 2025' — grid de thumbnails del género de estudio compartido.",
                  source="YouTube · 2025",
                  url="https://www.youtube.com/results?search_query=study+with+me+2025"),
             dict(png="macro-3-1-southeastarrow-studytok.png",
                  caption="'The Rise of StudyTok: Motivational or a Distraction?' — debate sobre el estudio performativo.",
                  source="Southeast Arrow · 2025",
                  url="https://www.southeastarrow.com/lifestyle/the-rise-of-studytok-is-it-motivational-or-a-distraction-9240f298"),
         ]),

    # 3.2 — El feed reemplazó al buscador
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="El feed reemplazó al buscador como puerta del conocimiento: 53% de Gen Z consulta TikTok antes que Google.",
         fenomeno="53% de Gen Z consulta TikTok, Reddit o YouTube antes que Google. El estudiante busca la explicación de un tema escolar directo en el feed, en formato de 60 segundos con cara y voz. El criterio de qué es verdad ya no lo decide la fuente — lo decide el creador que te cae bien.",
         hashtags="#learnontiktok · #tiktoktaughtme · #edutok · #tiktokitdontgoogleit · #aprendintiktok",
         triggers=[
             dict(stat="53%",  desc="De Gen Z busca en TikTok, Reddit o YouTube antes que Google para informarse.", source="Resolve · 2026"),
             dict(stat="Gen Z", desc="Y Gen Alpha usan el video social como herramienta de búsqueda cotidiana, no Google.", source="Information Matters · 2026"),
             dict(stat="2025", desc="'Why Gen Z turns to YouTube and TikTok for learning' — el video como autoridad epistémica.", source="Uqualio · 2025"),
         ],
         signals=[
             dict(png="macro-3-2-informationmatters-genz-tiktok-search.png",
                  caption="'TikTok It, Don't Google It' — Gen Z con celular, 53% busca en TikTok antes que Google.",
                  source="Information Matters / Resolve · 2026",
                  url="https://informationmatters.org/2026/03/tiktok-it-dont-google-it-gen-z-gen-alpha-and-the-rise-of-social-video-as-an-everyday-search-tool/"),
             dict(png="macro-3-2-uqualio-genz-video-learning.png",
                  caption="Uqualio — Gen Z y el video como herramienta educativa; el feed como primera fuente.",
                  source="Uqualio · 2025",
                  url="https://uqualio.com/post/why-generation-z-turns-to-youtube-and-tiktok-for-learning-the-power-of-video-in-education"),
             dict(png="macro-3-0-smiletutor-studytok.png",
                  caption="SmileTutor sobre StudyTok — contenido educativo 16.1% de views totales de TikTok.",
                  source="SmileTutor · 2025",
                  url="https://smiletutor.sg/studytok-a-look-into-educational-tiktok-trends-their-impact-on-learning-and-how-students-can-use-them-effectively/"),
         ]),

    # 3.3 — El conocimiento se fragmentó al formato del feed
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="El conocimiento se fragmentó al formato del feed: el microlearning en píldoras de 60 segundos reemplaza la clase de 50 minutos.",
         fenomeno="El microlearning — conceptos en clips cortos — empezó a reemplazar la lectura larga y la clase entera. Las escuelas K-12 ya están adoptando el formato corto que el algoritmo impuso primero. Una revisión 2025 encontró que el microlearning asistido por TikTok mejora retención y engagement.",
         hashtags="#microlearning · #learnin60seconds · #edutok · #explained · #aprenderrapido",
         triggers=[
             dict(stat="K-12",  desc="Las escuelas adoptan el microlearning — el formato corto del algoritmo entra al aula formal.", source="NY State School Boards Assoc. · 2025"),
             dict(stat="↑",     desc="Revisión 2025: microlearning asistido por TikTok mejora retención y engagement escolar.", source="CTO College · 2026"),
             dict(stat="60s",   desc="Los formatos 'explained in 60 seconds' dominan EduTok y presionan al aula formal.", source="TikTok · 2025"),
         ],
         signals=[
             dict(png="macro-3-3-cto-microlearning.png",
                  caption="Microlearning y TikTok en el aula 2026 — formato corto mejora retención y engagement.",
                  source="CTO College · 2026",
                  url="https://correctionstocollegeca.org/tiktok-and-the-future-of-learning-microlearning-engagement-and-the-2026-classroom-revolution/"),
             dict(png="macro-3-3-nyssba-microlearning-k12.png",
                  caption="NYSSBA — microlearning entra a K-12: instituciones adoptan el formato corto del algoritmo.",
                  source="NYSSBA · 2025",
                  url="https://www.nyssba.org/news/2025/08/08/on-board-online-august-11-2025/bringing-microlearning-to-k-12-schools-offers-many-opportunities-challenges/"),
             dict(png="macro-3-3-linkedin-learning-ui.png",
                  caption="LinkedIn Learning — cursos bite-sized y microlearning para profesionales.",
                  source="LinkedIn Learning · 2025",
                  url="https://www.linkedin.com/learning/"),
         ]),

    # 3.4 — La orientación vocacional migró al feed
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="La orientación vocacional migró al feed: creadores muestran un día en mi trabajo y salarios reales, y eso moldea qué carrera elige un adolescente.",
         fenomeno="El orientador escolar tenía un test y un folleto. El feed tiene 'un día en mi vida como [profesión]' y salary reveals. 53% de Gen Z investiga en plataformas sociales antes de tomar decisiones, incluida la carrera. La vida real de una profesión pesa más que el brochure.",
         hashtags="#careertok · #dayinmylife · #salarytransparency · #careeradvice · #queestudiar",
         triggers=[
             dict(stat="53%",   desc="De Gen Z investiga en plataformas sociales antes de decisiones, incluida la carrera.", source="Resolve · 2026"),
             dict(stat="2026",  desc="#careertok y 'day in my life as a [profesión]' son formatos masivos de decisión vocacional.", source="TikTok Discover · 2025"),
             dict(stat="salary", desc="Salary transparency content — salary reveals en el feed moldean expectativas de ingreso.", source="ContentGrip · 2026"),
         ],
         signals=[
             dict(png="macro-3-4-tiktok-careertok.png",
                  caption="Hashtag #careertok en TikTok — grid de 'day in my life' y salary reveals que orientan vocaciones.",
                  source="TikTok · 2025",
                  url="https://www.tiktok.com/tag/careertok"),
             dict(png="macro-3-4-contentgrip-tiktok-genz.png",
                  caption="ContentGrip TikTok Trends Gen Z 2026 — career/salary transparency moldea decisiones vocacionales.",
                  source="ContentGrip · 2026",
                  url="https://www.contentgrip.com/tiktok-trends-gen-z-marketing-guide/"),
             dict(png="macro-3-4-youtube-careertok.png",
                  caption="YouTube 'day in my life career' — thumbnails del formato vocacional que reemplaza al orientador.",
                  source="YouTube · 2025",
                  url="https://www.youtube.com/results?search_query=day+in+my+life+career+tiktok+2025"),
         ]),

    # 3.5 — El feed materno dicta cómo se educa al niño
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="El feed materno dicta cómo se educa al niño: MomTok recomienda apps y currículos, desplazando a la maestra como autoridad pedagógica del hogar.",
         fenomeno="MomTok recomienda apps educativas, métodos de crianza-aprendizaje y 'guilt-free screen time', y la madre elige según lo que se vuelve viral. Canales como Ms. Rachel se convirtieron en autoridad de aprendizaje temprano vía el feed. La madre confía en otra madre del feed más que en el sistema.",
         hashtags="#momtok · #toddlerlearning · #guiltfreescreentime · #learningapps · #crianzaconpantalla",
         triggers=[
             dict(stat="MomTok", desc="Apps como Kiddopia, SplashLearn y Khan Academy Kids viralizadas por MomTok en el feed.", source="TikTok Discover · 2025"),
             dict(stat="2025-26", desc="TikTok reforzó Family Pairing en 2025-26 para el control parental de screen-time.", source="Boomerang · 2025"),
             dict(stat="Ms. Rachel", desc="Canal que se volvió autoridad de aprendizaje temprano vía recomendación del feed materno.", source="TikTok / YouTube · 2025"),
         ],
         signals=[
             dict(png="macro-3-5-boomerang-tiktok-parental.png",
                  caption="TikTok Family Pairing y controles parentales — la madre digital eligiendo qué ve su hijo.",
                  source="Boomerang · 2025",
                  url="https://useboomerang.com/article/tiktok-parental-control/"),
             dict(png="macro-3-5-youtube-msrachel.png",
                  caption="Ms. Rachel en YouTube — thumbnails de la creadora que se volvió autoridad pedagógica vía feed.",
                  source="YouTube / Ms. Rachel · 2025",
                  url="https://www.youtube.com/results?search_query=ms+rachel+toddler+learning+2025"),
             dict(png="macro-3-0-accio-edutok-stats.png",
                  caption="Accio — estadísticas de contenido educativo en TikTok 2025, métricas de EduTok.",
                  source="Accio · 2025",
                  url="https://www.accio.com/business/tiktok-educational-content-trends"),
         ]),
]

if __name__ == "__main__":
    build_deck(DIVIDERS, MICROS, SCREENSHOTS, OUTPUT)
