#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Trends Educacion — Forecast Deck (18 slides)
Layout: 3 dividers macro + 15 micros (5 por macro)
Canvas 13.333 x 7.5 in (1440x810 px @ 108dpi base)
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

BASE = "/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC"
SHOTS = os.path.join(BASE, "screenshots/trends-educacion")
OUT = os.path.join(BASE, "outputs/trends-educacion-forecast.pptx")

# Colors
BG = RGBColor(0x0D, 0x0D, 0x0D)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY_LABEL = RGBColor(0xA0, 0xA0, 0xA0)
GREY_MUTED = RGBColor(0x66, 0x66, 0x66)
ACCENT = RGBColor(0xFF, 0x2D, 0x2D)
TAB_BG = RGBColor(0xE8, 0xE8, 0xE8)
BLACK = RGBColor(0x00, 0x00, 0x00)
PLACEHOLDER_BG = RGBColor(0x22, 0x22, 0x22)

FONT_SERIF = "Instrument Serif"
FONT_SANS = "Poppins"

# ============================================================
# MACRO + MICRO DATA
# ============================================================

MACROS = [
    {
        "num": 1,
        "name": "INVENTOLOGÍA DE LA ADULTEZ",
        "short": "INVENTOLOGÍA",
        "tagline": "Un mundo en crisis está reescribiendo qué significa ser adulto y formar familia.",
    },
    {
        "num": 2,
        "name": "LOS HERNÁNDEZ ARE PROMPTED",
        "short": "HERNÁNDEZ PROMPTED",
        "tagline": "El dominicano ya entró al mundo prompteado. Solo no lo nombra así.",
    },
    {
        "num": 3,
        "name": "ALGORITMO DEL HOGAR",
        "short": "ALGORITMO DEL HOGAR",
        "tagline": "El feed se sentó en la mesa y nadie le ofreció silla.",
    },
]

MICROS = [
    # ----- MACRO 1 -----
    {
        "macro": 1,
        "headline": "EL DIPLOMA DEJÓ DE SER EL TICKET: 53% DE EMPLEADORES YA CONTRATA POR SKILLS DEMOSTRADOS, Y LA GENERACIÓN QUE ENTRA AL MERCADO LO SABE ANTES DE MATRICULARSE.",
        "body": "Por décadas el título universitario fue la prueba de que servías para el trabajo. Eso se aflojó. En 2025, 53% de empleadores dejó de pedir título y empezó a contratar por habilidad demostrada. Pero ojo — el discurso va más rápido que la práctica: 85% dice contratar por skills, y en los números reales apenas 1 de cada 700 contrataciones ocurre sin título. La paradoja es el trend: el ticket viejo perdió su monopolio simbólico aunque todavía pese en la mesa de decisión.",
        "hashtags": "#skillsnotdegrees · #collegedropout · #selftaught",
        "needs": "EMPLEABILIDAD · MIEDO · VALIDACIÓN",
        "triggers": [
            {"big": "53%", "desc": "Empleadores que eliminaron el requisito de título en 2025 — +30% vs año anterior.", "src": "TESTGORILLA · 2025"},
            {"big": "1/700", "desc": "Solo 1 de cada 700 contrataciones reales ocurre sin título — la paradoja del discurso.", "src": "HARVARD / BURNING GLASS · 2025"},
            {"big": "85%", "desc": "Dice contratar por skills, pero la práctica real desfasa al discurso corporativo.", "src": "THE INTERVIEW GUYS · 2025"},
        ],
        "signals": [
            {"img": "macro-1-1-tiktok-skillsnotdegrees.png", "cap": "Página del hashtag #skillsnotdegrees en TikTok — top videos del trend skills vs título.", "src": "TIKTOK · 2025", "url": "https://www.tiktok.com/tag/skillsnotdegrees"},
            {"img": "macro-1-1-interviewguys-skills-hiring-2025.png", "cap": "State of Skills-Based Hiring 2025 — gráfico con la paradoja 85% discurso vs 1/700 contrataciones.", "src": "THE INTERVIEW GUYS · 2025", "url": "https://blog.theinterviewguys.com/the-state-of-skills-based-hiring/"},
            {"img": "macro-1-0-accelerec-skills-hiring.png", "cap": "\"The 4-Year Degree Is Dead\" — editorial sobre el skills-based hiring como nuevo default.", "src": "ACCELEREC · 2025", "url": "https://accelerec.com/the-4-year-degree-is-dead-why-skills-based-hiring-is-taking-over-in-2025/"},
        ],
    },
    {
        "macro": 1,
        "headline": "YA NADIE TERMINÓ DE ESTUDIAR: EL ADULTO LATAM SE RE-SKILLEA CADA 2-3 AÑOS PORQUE 39% DE LAS HABILIDADES LABORALES CAMBIA PARA 2030.",
        "body": "Antes te graduabas y cerrabas el capítulo de estudiar. Ese capítulo no cierra ya. 70% de profesionales dice que el upskilling es clave para su seguridad laboral, y 72% de los managers ya está en eso. No buscan otro título — buscan cursos cortos, certificados, skills sueltos que apilan mientras trabajan. El driver es claro: 39% de las habilidades del trabajo van a cambiar para 2030. El WEF lo llama el \"Great Skills Reset\". Quedarte quieto es quedarte atrás.",
        "hashtags": "#lifelonglearning · #reskilling · #upskilling",
        "needs": "VIGENCIA · MIEDO · AUTONOMÍA",
        "triggers": [
            {"big": "70%", "desc": "Dice que el upskilling es clave para su seguridad laboral; 72% de managers ya lo hace.", "src": "EDX SPRING · 2025"},
            {"big": "39%", "desc": "De las habilidades laborales cambiarán para 2030 — el \"Great Skills Reset\" del WEF.", "src": "WEF FUTURE OF JOBS · 2025"},
            {"big": "129%", "desc": "Crecimiento interanual de inscripciones LATAM en ciberseguridad en Coursera.", "src": "COURSERA GLOBAL SKILLS · 2025"},
        ],
        "signals": [
            {"img": "macro-1-2-coursera-global-skills-report.png", "cap": "Coursera Global Skills Report 2025 — badge del upskilling LATAM en números.", "src": "COURSERA · 2025", "url": "https://www.coursera.org/skills-reports/global"},
            {"img": "macro-1-2-wef-future-of-jobs.png", "cap": "WEF Future of Jobs 2025 — \"Great Skills Reset\" y gráfico de habilidades del futuro.", "src": "WEF · 2025", "url": "https://www.weforum.org/stories/2025/01/future-of-jobs-report-2025-jobs-of-the-future-and-the-skills-you-need-to-get-them/"},
            {"img": "macro-1-2-coursera-global-skills-report.png", "cap": "Coursera como plataforma donde el adulto LATAM re-skilea en semanas, no en años.", "src": "COURSERA · 2025", "url": "https://www.coursera.org/skills-reports/global"},
        ],
    },
    {
        "macro": 1,
        "headline": "FAMILIAS GLOBALES SACAN A SUS HIJOS DEL COLEGIO POR ELECCIÓN, NO POR CRISIS: EL AULA DE 30 COMPITE CON MICROSCHOOLS DE 5-15 Y CURRÍCULOS A LA MEDIDA.",
        "body": "El homeschool dejó de ser cosa de nicho. Creció 4.9% en 2024-25, casi 3x la tasa pre-pandemia, y 36% de los estados de EEUU reportó máximos históricos. En paralelo aparecen las microschools — hubs de 5 a 15 alumnos, promedio 22, donde la familia diseña el currículo. Entre 1 y 2 millones de estudiantes ya asisten full-time. La motivación no es la fuga de un sistema en llamas. Es el control: la familia quiere armar la educación, no delegarla.",
        "hashtags": "#homeschool · #microschool · #unschooling",
        "needs": "CONTROL · PERTENENCIA · RESENTIMIENTO",
        "triggers": [
            {"big": "4.9%", "desc": "Crecimiento del homeschool en 2024-25 — casi 3x la tasa pre-pandemia.", "src": "JHU INSTITUTE FOR EDUCATION POLICY · 2025"},
            {"big": "1-2M", "desc": "Estudiantes en EEUU que ya asisten a microschools full-time, promedio 22 alumnos.", "src": "RAND / NATIONAL MICROSCHOOLING CENTER · 2025"},
            {"big": "36%", "desc": "De los estados de EEUU reportó máximos históricos de homeschool en 2024-25.", "src": "JHU INSTITUTE FOR EDUCATION POLICY · 2025"},
        ],
        "signals": [
            {"img": "macro-1-3-cbsmiami-microschools.png", "cap": "CBS Miami sobre microschools — hub de aprendizaje alternativo en Florida.", "src": "CBS MIAMI · 2025", "url": "https://www.cbsnews.com/miami/news/microschools-families-flexible-alternative/"},
            {"img": "macro-1-3-jhu-homeschool-growth.png", "cap": "JHU Homeschool Hub 2024-25 — datos de crecimiento 4.9% con mapa de estados.", "src": "JHU INSTITUTE FOR EDUCATION POLICY · 2025", "url": "https://education.jhu.edu/edpolicy/policy-research-initiatives/homeschool-hub/homeschool-growth-2024-2025/"},
            {"img": "macro-1-3-theschoolhouse-microschools.png", "cap": "\"Why Microschools Are Rising\" — visual del grupo pequeño como modelo educativo.", "src": "THE SCHOOLHOUSE · 2025", "url": "https://www.theschoolhouse.org/post/rising-microschools-education"},
        ],
    },
    {
        "macro": 1,
        "headline": "EL \"SIGUIENTE PASO OBVIO\" TRAS EL BACHILLERATO DEJÓ DE SER OBVIO: GAP YEAR, BOOTCAMP Y EMPRENDIMIENTO ADOLESCENTE SUSTITUYEN EL INGRESO INMEDIATO A LA UNIVERSIDAD.",
        "body": "Terminabas el bachillerato y entrabas a la universidad. Punto. Eso ya no es el default. Solo 18% de Gen Z global ve subir la escalera corporativa como algo inteligente — el camino lineal perdió prestigio. Y Big Tech lo validó: Google, IBM y Tesla quitaron el título para muchos roles. Entonces el recién graduado se da un año, hace un bootcamp, o monta un ingreso con skills digitales antes de comprometerse a una carrera cara. No es vagancia. Es calcular el costo antes de firmar.",
        "hashtags": "#gapyear · #alternativestocollege · #nocollege",
        "needs": "AUTONOMÍA · EMPLEABILIDAD · MIEDO",
        "triggers": [
            {"big": "18%", "desc": "De Gen Z global ve subir la escalera corporativa como inteligente — el path lineal perdió.", "src": "FIVERR · OCT 2025"},
            {"big": "3", "desc": "Big Tech que eliminó el título para muchos roles: Google, IBM y Tesla.", "src": "ONECODESOFT · 2025"},
            {"big": "#gapyear", "desc": "Y \"alternatives to college\" crecen como género propio de contenido en TikTok.", "src": "TIKTOK DISCOVER · 2025"},
        ],
        "signals": [
            {"img": "macro-1-4-tiktok-gapyear.png", "cap": "Grid #gapyear en TikTok — jóvenes mostrando el path alternativo y el año sabático.", "src": "TIKTOK · 2025", "url": "https://www.tiktok.com/tag/gapyear"},
            {"img": "macro-1-4-onecodesoft-bigtech-skills.png", "cap": "\"Degree vs. Skills: Big Tech's 2025 Micro-Credential Pivot\" — Google, IBM y Tesla lideran.", "src": "ONECODESOFT · 2025", "url": "https://onecodesoft.com/blogs/degree-vs-skills-big-techs-2025-micro-credential-pivot"},
            {"img": "macro-1-4-onecodesoft-bigtech-skills.png", "cap": "El micro-credential pivot corporativo como validación del path sin diploma.", "src": "ONECODESOFT · 2025", "url": "https://onecodesoft.com/blogs/degree-vs-skills-big-techs-2025-micro-credential-pivot"},
        ],
    },
    {
        "macro": 1,
        "headline": "LA FAMILIA COMPENSA LO QUE LA ESCUELA DEJÓ DE GARANTIZAR: 70% DE NIÑOS EN PAÍSES DE INGRESO MEDIO-BAJO NO LEE BIEN A LOS 10, Y EL MERCADO DE TUTORÍA AI YA VALE US$3.55B.",
        "body": "La pandemia dejó un hueco que el sistema formal no recuperó. La pobreza de aprendizaje subió a cerca de 70% en países de ingreso medio-bajo, y LATAM perdió en promedio 225 días de clase presencial. NAEP reportó las mayores caídas en lectura y matemática en 35 años. ¿La respuesta de la familia? Pagar el refuerzo por fuera. El mercado de tutoría AI llegó a US$3.55B en 2025. La casa empezó a suplir lo que el aula dejó de asegurar.",
        "hashtags": "#learningloss · #tutoring · #refuerzoescolar",
        "needs": "SUPLIR · CULPA · MIEDO",
        "triggers": [
            {"big": "70%", "desc": "Pobreza de aprendizaje post-pandemia; LATAM perdió 225 días presenciales en promedio.", "src": "BANCO MUNDIAL / UNESCO · 2024"},
            {"big": "US$3.55B", "desc": "Mercado de tutoría AI en 2025 — la casa suple lo que el aula dejó de asegurar.", "src": "FUTURE MARKET INSIGHTS · 2025"},
            {"big": "35 años", "desc": "Las mayores caídas en lectura y matemática que el NAEP ha reportado en su historia.", "src": "NAEP / UNA-USA · 2024"},
        ],
        "signals": [
            {"img": "macro-1-5-worldbank-learning-poverty.png", "cap": "World Bank Learning Poverty — infografía de pobreza de aprendizaje global post-pandemia.", "src": "WORLD BANK · 2024", "url": "https://www.worldbank.org/en/topic/education/publication/state-of-global-learning-poverty"},
            {"img": "macro-1-5-unausa-naep-scores.png", "cap": "UNA-USA / NAEP — las mayores caídas en lectura y matemáticas en 35 años.", "src": "UNA-USA / NAEP · 2024", "url": "https://unausa.org/gga-blog-post-1/"},
            {"img": "macro-1-5-worldbank-learning-poverty.png", "cap": "La brecha de aprendizaje también es una brecha de bolsillo — refuerzo pagado vs hueco abierto.", "src": "WORLD BANK · 2024", "url": "https://www.worldbank.org/en/topic/education/publication/state-of-global-learning-poverty"},
        ],
    },
    # ----- MACRO 2 -----
    {
        "macro": 2,
        "headline": "EL TUTOR 1-A-1 DEJÓ DE SER PRIVILEGIO DE ÉLITE: KHANMIGO PASÓ DE 68K A 1.4M USUARIOS Y LA FAMILIA ACCEDE A TUTORÍA CON IA POR UNA FRACCIÓN DEL COSTO DEL PROFESOR PARTICULAR.",
        "body": "La tutoría privada siempre fue cosa de quien podía pagarla. Eso se está moviendo. Khanmigo pasó de 68k usuarios en 2023-24 a 1.4M a mediados de 2025 — y de 40k a 700k estudiantes K-12 en un ciclo. El mercado de tutores AI va de US$3.55B (2025) a US$6.45B (2030). El comportamiento observable: el estudiante resuelve dudas a cualquier hora, con un tutor que no se cansa ni cobra por sesión. El acceso a la tutoría 1-a-1 se está abaratando rápido.",
        "hashtags": "#aitutor · #khanmigo · #studywithai",
        "needs": "EQUIDAD · SUPLIR · RESENTIMIENTO",
        "triggers": [
            {"big": "1.4M", "desc": "Usuarios de Khanmigo a mediados de 2025 — creció desde 68k en 2023-24.", "src": "KHAN ACADEMY / GLOBALSOCIETY · 2025"},
            {"big": "US$6.45B", "desc": "Proyección mercado de tutores AI para 2030 — desde US$3.55B en 2025.", "src": "FUTURE MARKET INSIGHTS · 2025"},
            {"big": "700K", "desc": "Estudiantes K-12 en Khanmigo en un solo ciclo — desde 40k al inicio.", "src": "KHAN ACADEMY · 2025"},
        ],
        "signals": [
            {"img": "macro-3-0-tiktok-studytok-tag.png", "cap": "\"AI helped me pass\" — testimonios de estudio con IA en StudyTok.", "src": "TIKTOK · 2025", "url": "https://www.tiktok.com/tag/studytok"},
            {"img": "macro-2-1-globalsociety-khanmigo-ai-tools.png", "cap": "Khanmigo escala en distritos escolares — estudiante con herramientas AI de Khan Academy.", "src": "GLOBAL SOCIETY · 2025", "url": "https://www.globalsociety.earth/post/khan-academy-rolls-out-ai-powered-teaching-tools-as-school-districts-scale-up-adoption"},
            {"img": "macro-2-1-khanmigo-hero-landing.png", "cap": "Khanmigo — \"always-available teaching assistant\", UI del tutor AI 24/7.", "src": "KHANMIGO / KHAN ACADEMY · 2025", "url": "https://khanmigo.ai/"},
        ],
    },
    {
        "macro": 2,
        "headline": "APRENDER SE GAMIFICÓ Y COMPITE CON TIKTOK USANDO LAS MISMAS MECÁNICAS: DUOLINGO SOSTIENE 50.5M USUARIOS DIARIOS CON RACHAS, LIGAS Y LA CULPA DEL BÚHO.",
        "body": "El estudio nunca tuvo dopamina. Duolingo se la puso. Superó 50.5M usuarios diarios en Q3 2025 [+36% interanual], y el churn bajó de 47% a 28% gracias a la gamificación. Rachas, ligas, notificaciones — las mismas mecánicas de enganche que usa TikTok, aplicadas a aprender un idioma. Revenue Q3 2025: US$271.7M, +41%, con 11.5M suscriptores pagos. La gente mantiene rachas de cientos de días no por disciplina — por el miedo a romper la racha. El búho Duo ya es un meme propio.",
        "hashtags": "#duolingo · #duostreak · #gamifiedlearning",
        "needs": "HÁBITO · CULPA · PERTENENCIA",
        "triggers": [
            {"big": "50.5M", "desc": "Usuarios diarios Duolingo Q3 2025 (+36%); churn bajó de 47% a 28%.", "src": "DUOLINGO 8-K SEC · 2025"},
            {"big": "+41%", "desc": "Revenue Q3 2025: US$271.7M; 11.5M suscriptores pagos.", "src": "DUOLINGO SEC FILING FY2025"},
            {"big": "#duolingo", "desc": "El búho Duo y la \"Duolingo guilt\" — género viral con cientos de millones de views.", "src": "TIKTOK · 2025"},
        ],
        "signals": [
            {"img": "macro-2-2-duolingo-landing.png", "cap": "Landing de Duolingo — el búho Duo y la propuesta gamificada de 5 min al día.", "src": "DUOLINGO · 2025", "url": "https://www.duolingo.com/"},
            {"img": "macro-2-2-duolingo-streaks-gamification.png", "cap": "Mecánica de rachas de Duolingo — UI de objetivo diario y contador de racha visible.", "src": "DUOLINGO · 2025", "url": "https://www.strivecloud.io/blog/gamification-examples-boost-user-retention-duolingo"},
            {"img": "macro-2-2-strivecloud-duolingo-hero.png", "cap": "Análisis de la gamificación de Duolingo — retención de usuarios +36% interanual.", "src": "STRIVECLOUD · 2025", "url": "https://www.strivecloud.io/blog/gamification-examples-boost-user-retention-duolingo"},
        ],
    },
    {
        "macro": 2,
        "headline": "LA IA GENERATIVA AUTOMATIZÓ LA TAREA ESCOLAR: 84% DE SECUNDARIA LA USA, 53% PARA ENSAYOS, Y LA PREGUNTA DEJÓ DE SER SI COPIAN — ES SI EL APRENDIZAJE SOBREVIVE.",
        "body": "La tarea escolar se automatizó. 84% de los estudiantes de secundaria usa IA generativa para schoolwork, 89% para tareas, 53% para ensayos. El uso en educación superior global saltó de 66% (2024) a 92% (2025). Y el sistema no sabe qué hacer: 44% de los docentes detecta tarea sospechosa de IA cada semana, pero menos del 15% actúa por falta de prueba. El comportamiento visible: el estudiante genera el ensayo con ChatGPT y luego lo \"humaniza\" para esquivar los detectores.",
        "hashtags": "#chatgptforschool · #aihomework · #studyhack",
        "needs": "EFICIENCIA · VACÍO · CULPA",
        "triggers": [
            {"big": "84%", "desc": "Estudiantes de secundaria que usan IA generativa para schoolwork; 89% para tareas.", "src": "NERDYNAV · 2025"},
            {"big": "92%", "desc": "Uso de IA en educación superior global en 2025 — desde 66% en 2024.", "src": "DEMANDSAGE · 2026"},
            {"big": "44%", "desc": "Docentes que detectan tarea sospechosa de IA semanalmente; <15% actúa.", "src": "EDWEEK · 2025"},
        ],
        "signals": [
            {"img": "macro-2-3-nerdynav-chatgpt-cheating-infographic.png", "cap": "Nerdynav: 84% usa IA para tareas, 89% homework, 53% ensayos — infografía de uso.", "src": "NERDYNAV · 2025", "url": "https://nerdynav.com/chatgpt-cheating-statistics/"},
            {"img": "macro-2-3-edweek-ai-cheating.png", "cap": "EdWeek: 44% detecta tarea sospechosa semanalmente, <15% actúa por falta de prueba.", "src": "EDUCATION WEEK · 2024", "url": "https://www.edweek.org/technology/new-data-reveal-how-many-students-are-using-ai-to-cheat/2024/04"},
            {"img": "macro-2-3-nerdynav-student-usage-chart.png", "cap": "Chart de uso de IA por tipo de tarea — essays, homework, research.", "src": "NERDYNAV · 2025", "url": "https://nerdynav.com/chatgpt-cheating-statistics/"},
        ],
    },
    {
        "macro": 2,
        "headline": "EL DIPLOMA DE PAPEL SE MUDÓ A LA NUBE: 90% DE EMPLEADORES PREFIERE CANDIDATO CON MICROCREDENCIAL, Y LOS BADGES VERIFICABLES SE VOLVIERON MONEDA DE EMPLEABILIDAD.",
        "body": "El título tardaba 4 años y vivía en una pared. La microcredencial tarda semanas y vive en LinkedIn. Más del 90% de empleadores prefiere a un candidato con microcredencial en el CV. Coursera lleva 15.4M+ inscripciones en certificados profesionales entry-level. El comportamiento observable: el profesional exhibe el badge de Google o Coursera en su perfil como prueba portátil y verificable de que sabe hacer algo — sin esperar a graduarse de nada.",
        "hashtags": "#microcredentials · #digitalbadges · #googlecertificate",
        "needs": "VALIDACIÓN · EMPLEABILIDAD · MIEDO",
        "triggers": [
            {"big": "90%+", "desc": "De empleadores prefiere candidato con microcredencial en el CV.", "src": "COURSERA / FORTUNE · 2025"},
            {"big": "15.4M+", "desc": "Inscripciones en certificados profesionales entry-level de Coursera.", "src": "COURSERA GLOBAL SKILLS · 2025"},
            {"big": "4 sem", "desc": "Lo que tarda un badge verificable vs 4 años de carrera — portátil en LinkedIn.", "src": "EDSURGE · 2024"},
        ],
        "signals": [
            {"img": "macro-2-4-fortune-microcredentials.png", "cap": "Fortune: \"Getting hired in 2026 is all about your microcredentials\" — CEO Coursera.", "src": "FORTUNE · DEC 2025", "url": "https://fortune.com/2025/12/28/2026-microcredential-hiring-trend-coursera-greg-hart/"},
            {"img": "macro-2-4-edsurge-digital-credentials.png", "cap": "EdSurge sobre credenciales digitales verificables — foto conceptual de badges en laptop.", "src": "EDSURGE · 2024", "url": "https://www.edsurge.com/news/2024-11-22-how-digital-credentials-can-elevate-existing-programs"},
            {"img": "macro-2-4-coursera-google-cert.png", "cap": "Google Career Certificates — badges digitales verificables para roles tech sin título.", "src": "GOOGLE / COURSERA · 2025", "url": "https://grow.google/certificates/"},
        ],
    },
    {
        "macro": 2,
        "headline": "NO SOLO EL ESTUDIANTE USA IA, EL DOCENTE TAMBIÉN: EN RD 98% DE LA FACULTAD UNIVERSITARIA CONOCE IA Y EL PAÍS LIDERA EL USO DE CHATGPT ENTRE PROFESORES ENCUESTADOS.",
        "body": "La IA en el aula no es solo el alumno copiando. El docente sobrecargado delega lo administrativo — planes de clase, rúbricas, exámenes, retroalimentación — para enfocarse en enseñar. Y aquí RD aparece con fuerza: 98% de los docentes universitarios dominicanos conoce conceptos de IA, y el país lidera el uso de ChatGPT entre la facultad encuestada [INTEC-PUCMM-UASD]. Khanmigo, del lado de las herramientas docentes, se expandió de 45 a más de 380 distritos. El profesor también está prompteado.",
        "hashtags": "#teacherai · #docenteIA · #edtechRD",
        "needs": "CAPACIDAD · VIGENCIA · INVISIBILIDAD",
        "triggers": [
            {"big": "98%", "desc": "Docentes universitarios RD que conocen IA — el país lidera uso ChatGPT en facultad.", "src": "HMTV / INTEC-PUCMM-UASD · 2025"},
            {"big": "380+", "desc": "Distritos escolares con Khanmigo — expandido desde 45 con herramientas docentes AI.", "src": "KHAN ACADEMY · 2025"},
            {"big": "#1 RD", "desc": "Lidera el uso de ChatGPT entre la facultad universitaria encuestada en LATAM.", "src": "SCIELO DOMINICAN REPUBLIC · 2025"},
        ],
        "signals": [
            {"img": "macro-2-5-hmtv-ai-profesor-rd-chrome.png", "cap": "HMTV: 98% docentes RD conocen IA — país lidera uso ChatGPT en facultad universitaria.", "src": "HMTV / INTEC-PUCMM · 2025", "url": "https://www.hmtv.com.do/index.php/noticias/noticias/42251-la-inteligencia-artificial-redefine-el-rol-del-profesor-universitario-en-republica-dominicana"},
            {"img": "macro-2-5-scielo-ai-educacion-rd.png", "cap": "Paper SciELO DO \"Educación Superior en la Era de la IA\" — adopción docente en RD.", "src": "SCIELO DOMINICAN REPUBLIC · 2025", "url": "https://scielo.do/scielo.php?script=sci_arttext&pid=S2636-21632025003900007&lang=pt"},
            {"img": "macro-2-1-khanmigo-hero-landing.png", "cap": "Khanmigo expandido a 380+ distritos — herramientas AI para el docente, no solo el alumno.", "src": "KHANMIGO / KHAN ACADEMY · 2025", "url": "https://khanmigo.ai/"},
        ],
    },
    # ----- MACRO 3 -----
    {
        "macro": 3,
        "headline": "ESTUDIAR SE VOLVIÓ CONTENIDO: \"STUDY WITH ME\" LIVES Y NOTAS ESTÉTICAS CONVIERTEN EL ESTUDIO SOLITARIO EN ESPECTÁCULO SOCIAL, CON ACCOUNTABILITY DE EXTRAÑOS EN EL FEED.",
        "body": "Estudiar era algo que hacías solo en tu cuarto. Ahora se transmite. Los \"study with me\" lives y las notas estéticas convirtieron la sesión de estudio en una experiencia social-algorítmica. El educativo es la 2da categoría más vista en TikTok [16.1% de views]. El comportamiento visible: el estudiante prende un live de su sesión, o estudia \"junto\" a un video de alguien más, y la disciplina ya no viene de adentro — viene de la mirada de extraños en el feed.",
        "hashtags": "#studytok · #studywithme · #studymotivation",
        "needs": "PERTENENCIA · SOLEDAD · VALIDACIÓN",
        "triggers": [
            {"big": "16.1%", "desc": "El contenido educativo es la 2da categoría más vista en TikTok.", "src": "SMILETUTOR · 2025"},
            {"big": "7.36%", "desc": "Engagement de las cuentas de educación superior en TikTok — top del platform.", "src": "TIKTOK / SMILETUTOR · 2025"},
            {"big": "#studytok", "desc": "\"Shut up and study\" lives crecen como subcultura de estudio en comunidad.", "src": "SMILETUTOR / TIKTOK · 2025"},
        ],
        "signals": [
            {"img": "macro-3-0-tiktok-studytok-tag.png", "cap": "Grid #studytok en TikTok — estudio compartido y notas estéticas como subcultura.", "src": "TIKTOK · 2025", "url": "https://www.tiktok.com/tag/studytok"},
            {"img": "macro-3-1-youtube-studywithme.png", "cap": "Resultados YouTube \"study with me 2025\" — genre del estudio compartido en video.", "src": "YOUTUBE · 2025", "url": "https://www.youtube.com/results?search_query=study+with+me+2025"},
            {"img": "macro-3-1-southeastarrow-studytok.png", "cap": "\"The Rise of StudyTok: Motivational or Distraction?\" — el debate del estudio performativo.", "src": "SOUTHEAST ARROW · 2025", "url": "https://www.southeastarrow.com/lifestyle/the-rise-of-studytok-is-it-motivational-or-a-distraction-9240f298"},
        ],
    },
    {
        "macro": 3,
        "headline": "EL FEED REEMPLAZÓ AL BUSCADOR COMO PUERTA DEL CONOCIMIENTO: 53% DE GEN Z CONSULTA TIKTOK ANTES QUE GOOGLE, Y QUÉ ES \"VERDAD\" LO CURAN CREADORES, NO FUENTES.",
        "body": "\"Búscalo en Google\" se volvió \"búscalo en TikTok\". 53% de Gen Z consulta TikTok, Reddit o YouTube antes que Google para informarse. El comportamiento observable: el estudiante busca la explicación de un tema escolar directo en el feed, en formato de 60 segundos con cara y voz, en vez de leer un artículo. El criterio de qué es verdad ya no lo decide la fuente — lo decide el creador que te cae bien.",
        "hashtags": "#learnontiktok · #tiktoktaughtme · #edutok",
        "needs": "INMEDIATEZ · PERTENENCIA · VACÍO",
        "triggers": [
            {"big": "53%", "desc": "De Gen Z busca en TikTok/Reddit/YouTube antes que Google para informarse.", "src": "RESOLVE · 2026"},
            {"big": "60 seg", "desc": "La unidad de conocimiento que reemplazó al artículo — formato que ganó contra Google.", "src": "INFORMATION MATTERS · 2026"},
            {"big": "Gen Z", "desc": "Y Gen Alpha usan el video social como herramienta de búsqueda cotidiana.", "src": "INFORMATION MATTERS · 2026"},
        ],
        "signals": [
            {"img": "macro-3-2-informationmatters-genz-tiktok-search.png", "cap": "\"TikTok It, Don't Google It\" — 53% de Gen Z busca en social antes que Google.", "src": "INFORMATION MATTERS / RESOLVE · 2026", "url": "https://informationmatters.org/2026/03/tiktok-it-dont-google-it-gen-z-gen-alpha-and-the-rise-of-social-video-as-an-everyday-search-tool/"},
            {"img": "macro-3-2-uqualio-genz-video-learning.png", "cap": "Gen Z y el video como herramienta educativa — jóvenes con celular aprendiendo.", "src": "UQUALIO · 2025", "url": "https://uqualio.com/post/why-generation-z-turns-to-youtube-and-tiktok-for-learning-the-power-of-video-in-education"},
            {"img": "macro-3-2-informationmatters-genz-tiktok-search.png", "cap": "La autoridad del conocimiento se desplazó del que sabe al que comunica bien.", "src": "INFORMATION MATTERS · 2026", "url": "https://informationmatters.org/2026/03/tiktok-it-dont-google-it-gen-z-gen-alpha-and-the-rise-of-social-video-as-an-everyday-search-tool/"},
        ],
    },
    {
        "macro": 3,
        "headline": "EL CONOCIMIENTO SE FRAGMENTÓ AL FORMATO DEL FEED: EL MICROLEARNING EN PÍLDORAS DE 60 SEGUNDOS REEMPLAZA LA CLASE DE 50 MINUTOS, Y LA ESCUELA K-12 YA ESTÁ ADOPTÁNDOLO.",
        "body": "La clase de 50 minutos perdió contra el tramo de atención que el feed entrenó. El microlearning — conceptos en clips cortos — empezó a reemplazar la lectura larga y la clase entera. Lo curioso es que dejó de ser solo cosa de redes: las escuelas K-12 ya están adoptando el formato corto que el algoritmo impuso primero. Una revisión 2025 encontró que el microlearning asistido por TikTok mejora retención y engagement. El estudiante aprende en píldoras porque su atención fue calibrada por el feed.",
        "hashtags": "#microlearning · #learnin60seconds · #aprenderrapido",
        "needs": "ATENCIÓN · INMEDIATEZ · VACÍO",
        "triggers": [
            {"big": "50 min", "desc": "La clase de 50 min pierde vs el clip de 60 seg — la atención fue calibrada por el feed.", "src": "NYSSBA · 2025"},
            {"big": "K-12", "desc": "Ya está adoptando el formato corto que el algoritmo impuso primero.", "src": "NYSSBA · 2025"},
            {"big": "↑ retención", "desc": "Revisión 2025: microlearning asistido por TikTok mejora retención y engagement.", "src": "CTO COLLEGE · 2026"},
        ],
        "signals": [
            {"img": "macro-3-3-cto-microlearning.png", "cap": "\"TikTok and the Future of Learning\" — microlearning mejora retención en el aula 2026.", "src": "CTO COLLEGE · 2026", "url": "https://correctionstocollegeca.org/tiktok-and-the-future-of-learning-microlearning-engagement-and-the-2026-classroom-revolution/"},
            {"img": "macro-3-3-nyssba-microlearning-k12.png", "cap": "NYSSBA: microlearning entra a K-12 — escuelas adoptando el formato del algoritmo.", "src": "NYSSBA · 2025", "url": "https://www.nyssba.org/news/2025/08/08/on-board-online-august-11-2025/bringing-microlearning-to-k-12-schools-offers-many-opportunities-challenges/"},
            {"img": "macro-3-3-linkedin-learning-ui.png", "cap": "LinkedIn Learning — cursos bite-sized, el formato corto para el profesional en movimiento.", "src": "LINKEDIN LEARNING · 2025", "url": "https://www.linkedin.com/learning/"},
        ],
    },
    {
        "macro": 3,
        "headline": "LA ORIENTACIÓN VOCACIONAL MIGRÓ AL FEED: CREADORES MUESTRAN \"UN DÍA EN MI TRABAJO\" Y SALARIOS REALES, Y ESO MOLDEA QUÉ CARRERA ELIGE UN ADOLESCENTE MÁS QUE CUALQUIER ORIENTADOR.",
        "body": "El orientador escolar tenía un test y un folleto. El feed tiene \"un día en mi vida como [profesión]\" y salary reveals. El comportamiento observable: el adolescente descarta o elige una carrera basándose en lo que ve a un creador hacer y ganar, no en lo que le dice un consejero. 53% de Gen Z investiga en plataformas sociales antes de tomar decisiones, incluida la carrera. La vida real de una profesión — sin filtro institucional — pesa más que el brochure.",
        "hashtags": "#careertok · #dayinmylife · #salarytransparency",
        "needs": "PROYECCIÓN · MIEDO · AUTONOMÍA",
        "triggers": [
            {"big": "#careertok", "desc": "\"Day in my life as [profesión]\" — formato masivo que influye la decisión vocacional.", "src": "TIKTOK DISCOVER · 2025"},
            {"big": "53%", "desc": "De Gen Z investiga en plataformas sociales antes de decisiones, incluida la carrera.", "src": "RESOLVE · 2026"},
            {"big": "salary", "desc": "Salary transparency content en TikTok moldea expectativas antes del primer trabajo.", "src": "CONTENTGRIP · 2026"},
        ],
        "signals": [
            {"img": "macro-3-4-tiktok-careertok.png", "cap": "Página #careertok en TikTok — grid de \"day in my life\" y salary reveals vocacionales.", "src": "TIKTOK · 2025", "url": "https://www.tiktok.com/tag/careertok"},
            {"img": "macro-3-4-youtube-careertok.png", "cap": "YouTube \"day in my life career\" — thumbnails del formato que reemplaza al orientador.", "src": "YOUTUBE · 2025", "url": "https://www.youtube.com/results?search_query=day+in+my+life+career+tiktok+2025"},
            {"img": "macro-3-4-contentgrip-tiktok-genz.png", "cap": "ContentGrip: career/salary transparency content en el trend report Gen Z 2026.", "src": "CONTENTGRIP · 2026", "url": "https://www.contentgrip.com/tiktok-trends-gen-z-marketing-guide/"},
        ],
    },
    {
        "macro": 3,
        "headline": "EL FEED MATERNO DICTA CÓMO SE EDUCA AL NIÑO: MOMTOK RECOMIENDA APPS, CURRÍCULOS Y \"GUILT-FREE SCREEN TIME\", Y DESPLAZÓ A LA MAESTRA COMO AUTORIDAD PEDAGÓGICA DEL HOGAR.",
        "body": "La maestra solía ser la autoridad sobre cómo aprende el niño. Ahora compite con otra madre en el feed. MomTok recomienda apps educativas, métodos de crianza-aprendizaje y \"guilt-free screen time\", y la madre elige según lo que se vuelve viral. Apps como Kiddopia, SplashLearn y Khan Academy Kids se mueven por esa recomendación. Canales como Ms. Rachel se convirtieron en autoridad de aprendizaje temprano vía el feed. El comportamiento visible: la madre confía en otra madre del feed más que en el sistema.",
        "hashtags": "#momtok · #toddlerlearning · #guiltfreescreentime",
        "needs": "VALIDACIÓN · CULPA · SOLEDAD",
        "triggers": [
            {"big": "#momtok", "desc": "Apps como Kiddopia, SplashLearn y Khan Academy Kids viralizadas por MomTok.", "src": "TIKTOK DISCOVER · 2025"},
            {"big": "Ms. Rachel", "desc": "Se convirtió en autoridad de aprendizaje temprano vía recomendación del feed materno.", "src": "TIKTOK / YOUTUBE · 2025"},
            {"big": "Family Pairing", "desc": "TikTok reforzó el control parental de screen-time en 2025-26 ante la demanda maternal.", "src": "BOOMERANG · 2025"},
        ],
        "signals": [
            {"img": "macro-3-5-boomerang-tiktok-parental.png", "cap": "TikTok Family Pairing — la madre digital eligiendo qué ve su hijo en el feed.", "src": "BOOMERANG · 2025", "url": "https://useboomerang.com/article/tiktok-parental-control/"},
            {"img": "macro-3-5-youtube-msrachel.png", "cap": "Ms. Rachel en YouTube — la creadora que se volvió autoridad pedagógica vía feed.", "src": "YOUTUBE / MS. RACHEL · 2025", "url": "https://www.youtube.com/results?search_query=ms+rachel+toddler+learning+2025"},
            {"img": "macro-3-5-boomerang-tiktok-parental.png", "cap": "La autoridad pedagógica del hogar migró de la maestra a la creadora del feed.", "src": "BOOMERANG · 2025", "url": "https://useboomerang.com/article/tiktok-parental-control/"},
        ],
    },
]

assert len(MICROS) == 15, f"Expected 15 micros, got {len(MICROS)}"

# ============================================================
# HELPERS
# ============================================================

def add_bg(slide, prs):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.line.fill.background()
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG
    return bg

def set_run(run, text, font=FONT_SANS, size=10, bold=False, italic=False, color=WHITE):
    run.text = text
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color

def add_textbox(slide, x, y, w, h, text, font=FONT_SANS, size=10, bold=False, italic=False,
                color=WHITE, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=1.0,
                word_wrap=True):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = word_wrap
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    r = p.add_run()
    set_run(r, text, font, size, bold, italic, color)
    return tb

def add_line(slide, x1, y1, x2, y2, color_hex="FFFFFF", alpha_pct=6, weight_emu=9525):
    line = slide.shapes.add_connector(1, x1, y1, x2, y2)
    line.line.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    line.line.width = Emu(weight_emu)
    ln = line.line._get_or_add_ln()
    solidFill = ln.find(qn('a:solidFill'))
    if solidFill is None:
        solidFill = etree.SubElement(ln, qn('a:solidFill'))
    for child in list(solidFill):
        solidFill.remove(child)
    srgb = etree.SubElement(solidFill, qn('a:srgbClr'))
    srgb.set('val', color_hex)
    alpha = etree.SubElement(srgb, qn('a:alpha'))
    alpha.set('val', str(int(alpha_pct * 1000)))
    return line

def add_hyperlink_rect(slide, x, y, w, h, url):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    sh.fill.background()
    sh.line.fill.background()
    sh.click_action.hyperlink.address = url
    return sh

def add_badge_click_me(slide, x, y):
    bw = Pt(46)
    bh = Pt(14)
    b = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, bw, bh)
    b.fill.solid()
    b.fill.fore_color.rgb = ACCENT
    b.line.fill.background()
    tf = b.text_frame
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    set_run(r, "CLICK ME", font=FONT_SANS, size=7, bold=True, color=WHITE)
    return b

# ============================================================
# DIVIDER SLIDE
# ============================================================

def build_divider(prs, macro):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, prs)

    sw, sh = prs.slide_width, prs.slide_height
    cx = sw // 2

    # Etiqueta MACRO N — Poppins Bold 14pt #A0A0A0 UPPERCASE
    lbl_w = Inches(4)
    lbl_h = Inches(0.4)
    lbl_y = sh // 2 - Inches(1.8)
    add_textbox(slide, cx - lbl_w // 2, lbl_y, lbl_w, lbl_h,
                f"MACRO {macro['num']}",
                font=FONT_SANS, size=14, bold=True, color=GREY_LABEL,
                align=PP_ALIGN.CENTER)

    # Nombre macro — Instrument Serif Regular 100pt UPPERCASE white centered
    name_y = lbl_y + lbl_h + Pt(24)
    name_h = Inches(2.5)
    name_w = Inches(12.5)
    tb = slide.shapes.add_textbox(cx - name_w // 2, name_y, name_w, name_h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.line_spacing = 0.95
    r = p.add_run()
    set_run(r, macro['name'].upper(), font=FONT_SERIF, size=100, color=WHITE)

    # Tagline — Instrument Serif Italic 24pt #A0A0A0 centrada con comillas
    tag_y = name_y + name_h + Pt(16)
    tag_w = Inches(11)
    add_textbox(slide, cx - tag_w // 2, tag_y, tag_w, Inches(0.6),
                f"“{macro['tagline']}”",
                font=FONT_SERIF, size=24, italic=True, color=GREY_LABEL,
                align=PP_ALIGN.CENTER)

# ============================================================
# MICRO SLIDE
# ============================================================

def build_micro(prs, micro):
    macro = MACROS[micro['macro'] - 1]
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, prs)

    sw, sh = prs.slide_width, prs.slide_height
    # Grid
    margin_x = Inches(0.4)
    top_y = Inches(0.35)
    gutter = Inches(0.2)
    col_w = (sw - 2 * margin_x - 2 * gutter) // 3
    col_left_x = margin_x
    col_center_x = col_left_x + col_w + gutter
    col_right_x = col_center_x + col_w + gutter

    # ---- TABS arriba col-left ----
    tab_y = top_y
    tab_h = Inches(0.22)
    tab1_w = Inches(0.85)
    tab2_w = Inches(2.2)
    # tab1 MACRO N
    t1 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, col_left_x, tab_y, tab1_w, tab_h)
    t1.fill.solid(); t1.fill.fore_color.rgb = TAB_BG
    t1.line.color.rgb = TAB_BG
    t1.line.width = Emu(3175)
    tf = t1.text_frame
    tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05); tf.margin_top = 0; tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); set_run(r, f"MACRO {macro['num']}", font=FONT_SANS, size=8, bold=True, color=BLACK)
    # tab2 short name
    t2 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, col_left_x + tab1_w, tab_y, tab2_w, tab_h)
    t2.fill.background()
    t2.line.color.rgb = RGBColor(0x60, 0x60, 0x60)
    t2.line.width = Emu(3175)
    tf = t2.text_frame
    tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05); tf.margin_top = 0; tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); set_run(r, macro['short'], font=FONT_SANS, size=8, color=GREY_LABEL)

    # ---- Column labels ----
    labels_y = tab_y + tab_h + Inches(0.25)
    labels_h = Inches(0.25)
    add_textbox(slide, col_left_x, labels_y, col_w, labels_h,
                "DEFINICIÓN", font=FONT_SANS, size=8, bold=True, color=GREY_LABEL)
    add_textbox(slide, col_center_x, labels_y, col_w, labels_h,
                "TRIGGERS", font=FONT_SANS, size=8, bold=True, color=GREY_LABEL)
    add_textbox(slide, col_right_x, labels_y, col_w, labels_h,
                "SEÑALES", font=FONT_SANS, size=8, bold=True, color=GREY_LABEL)

    # Horizontal line under labels
    line_y = labels_y + labels_h + Inches(0.04)
    add_line(slide, margin_x, line_y, sw - margin_x, line_y, alpha_pct=6, weight_emu=9525)

    # Vertical lines between columns
    content_top = line_y + Inches(0.15)
    content_bottom = sh - Inches(0.3)
    add_line(slide, col_center_x - gutter // 2, content_top, col_center_x - gutter // 2, content_bottom, alpha_pct=6, weight_emu=9525)
    add_line(slide, col_right_x - gutter // 2, content_top, col_right_x - gutter // 2, content_bottom, alpha_pct=6, weight_emu=9525)

    # ===== COL LEFT — Headline + Body + Hashtags + Needs =====
    cur_y = content_top
    headline = micro['headline']
    hl = len(headline)
    if hl <= 80:
        hl_size = 50
    elif hl <= 120:
        hl_size = 42
    elif hl <= 160:
        hl_size = 30
    elif hl <= 200:
        hl_size = 22
    else:
        hl_size = 18
    hl_h = Inches(2.2)
    tb = slide.shapes.add_textbox(col_left_x, cur_y, col_w - Inches(0.1), hl_h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.line_spacing = 0.95
    r = p.add_run()
    set_run(r, headline.upper(), font=FONT_SERIF, size=hl_size, color=WHITE)
    cur_y += hl_h + Inches(0.1)

    # EL FENÓMENO label
    add_textbox(slide, col_left_x, cur_y, col_w, Inches(0.18),
                "EL FENÓMENO", font=FONT_SANS, size=7, bold=True, color=GREY_LABEL)
    cur_y += Inches(0.2)
    # Body — Poppins Regular 10pt white line-spacing 1.0
    body_h = Inches(1.5)
    tb = slide.shapes.add_textbox(col_left_x, cur_y, col_w - Inches(0.1), body_h)
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.line_spacing = 1.0
    r = p.add_run()
    set_run(r, micro['body'], font=FONT_SANS, size=10, color=WHITE)
    cur_y += body_h + Inches(0.05)

    # HASHTAGS label + content — Instrument Serif Regular 23pt
    add_textbox(slide, col_left_x, cur_y, col_w, Inches(0.18),
                "HASHTAGS", font=FONT_SANS, size=7, bold=True, color=GREY_LABEL)
    cur_y += Inches(0.2)
    tb = slide.shapes.add_textbox(col_left_x, cur_y, col_w - Inches(0.1), Inches(0.7))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.line_spacing = 1.1
    r = p.add_run()
    set_run(r, micro['hashtags'], font=FONT_SERIF, size=23, color=WHITE)
    cur_y += Inches(0.75)

    # 3 NEEDS label + content — Instrument Serif Regular 14pt
    add_textbox(slide, col_left_x, cur_y, col_w, Inches(0.18),
                "3 NEEDS", font=FONT_SANS, size=7, bold=True, color=GREY_LABEL)
    cur_y += Inches(0.2)
    tb = slide.shapes.add_textbox(col_left_x, cur_y, col_w - Inches(0.1), Inches(0.5))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.line_spacing = 1.05
    r = p.add_run()
    set_run(r, micro['needs'], font=FONT_SERIF, size=14, color=WHITE)

    # ===== COL CENTER — TRIGGERS (3 vertical stats + desc box 170x35pt) =====
    trig_top = content_top
    block_h = (content_bottom - trig_top) / 3
    big_w = Inches(1.5)
    desc_box_w = Pt(170)
    desc_box_h = Pt(35)
    src_h = Inches(0.18)

    for i, trig in enumerate(micro['triggers']):
        bx = col_center_x
        by = int(trig_top + i * block_h)
        # Big stat
        big = trig['big']
        big_len = len(big)
        if big_len <= 3:
            big_size = 72
        elif big_len <= 5:
            big_size = 54
        elif big_len <= 7:
            big_size = 42
        elif big_len <= 10:
            big_size = 32
        else:
            big_size = 24
        tb = slide.shapes.add_textbox(bx, by, big_w, Inches(1.2))
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.line_spacing = 1.0
        r = p.add_run()
        set_run(r, big, font=FONT_SERIF, size=big_size, color=WHITE)
        # Source under big
        add_textbox(slide, bx, by + Inches(1.25), big_w, src_h,
                    trig['src'], font=FONT_SANS, size=7, color=GREY_MUTED)
        # Desc box to the right — W170pt x H35pt Poppins 10pt white
        dbx = bx + big_w + Inches(0.05)
        dby = by + Inches(0.15)
        tb = slide.shapes.add_textbox(dbx, dby, desc_box_w, desc_box_h)
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.line_spacing = 1.0
        r = p.add_run()
        set_run(r, trig['desc'], font=FONT_SANS, size=10, color=WHITE)

    # ===== COL RIGHT — SEÑALES (3 fotos 149x220pt + caja caption 170x35pt) =====
    sig_top = content_top
    photo_w = Pt(149)
    photo_h = Pt(220)
    cap_box_w = Pt(170)
    cap_box_h = Pt(35)
    block_h_r = (content_bottom - sig_top) / 3

    for i, sig in enumerate(micro['signals']):
        bx = col_right_x
        by = int(sig_top + i * block_h_r)
        img_path = os.path.join(SHOTS, sig['img'])
        if os.path.exists(img_path):
            try:
                slide.shapes.add_picture(img_path, bx, by, width=photo_w, height=photo_h)
            except Exception as e:
                print(f"  WARNING: could not add image {sig['img']}: {e}")
                ph = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, bx, by, photo_w, photo_h)
                ph.fill.solid(); ph.fill.fore_color.rgb = PLACEHOLDER_BG
                ph.line.color.rgb = WHITE; ph.line.width = Emu(3175)
                tf = ph.text_frame; tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
                tf.vertical_anchor = MSO_ANCHOR.MIDDLE
                p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
                r = p.add_run()
                set_run(r, "CAPTURA MANUAL\nJEREMY", font=FONT_SANS, size=8, bold=True, color=GREY_MUTED)
        else:
            print(f"  WARNING: image not found: {img_path}")
            ph = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, bx, by, photo_w, photo_h)
            ph.fill.solid(); ph.fill.fore_color.rgb = PLACEHOLDER_BG
            ph.line.color.rgb = WHITE; ph.line.width = Emu(3175)
            tf = ph.text_frame; tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
            r = p.add_run()
            set_run(r, "CAPTURA MANUAL\nJEREMY", font=FONT_SANS, size=8, bold=True, color=GREY_MUTED)

        # Badge "Click me" upper right of photo
        bd_x = bx + photo_w - Pt(38)
        bd_y = by - Pt(6)
        add_badge_click_me(slide, bd_x, bd_y)

        # Hyperlink invisible overlay over photo
        add_hyperlink_rect(slide, bx, by, photo_w, photo_h, sig['url'])

        # Caption box to the right — W170pt x H35pt Poppins 10pt white
        cap_x = bx + photo_w + Inches(0.08)
        cap_y = by + Inches(0.15)
        tb = slide.shapes.add_textbox(cap_x, cap_y, cap_box_w, cap_box_h)
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.line_spacing = 1.0
        r = p.add_run()
        set_run(r, sig['cap'], font=FONT_SANS, size=10, color=WHITE)
        # Source under caption
        add_textbox(slide, cap_x, cap_y + cap_box_h + Inches(0.02), cap_box_w, src_h,
                    sig['src'], font=FONT_SANS, size=7, color=GREY_MUTED)

# ============================================================
# MAIN
# ============================================================

def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    micros_by_macro = {1: [], 2: [], 3: []}
    for m in MICROS:
        micros_by_macro[m['macro']].append(m)

    for macro in MACROS:
        build_divider(prs, macro)
        for micro in micros_by_macro[macro['num']]:
            build_micro(prs, micro)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    prs.save(OUT)
    print(f"Saved: {OUT}")
    print(f"Total slides: {len(prs.slides)}")

if __name__ == "__main__":
    main()
