#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Trends Roles de Género — Forecast Deck v2 (18 slides)
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
from copy import deepcopy
from lxml import etree

BASE = "/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC"
SHOTS = os.path.join(BASE, "screenshots/trends-roles-genero")
OUT = os.path.join(BASE, "outputs/trends-roles-genero-forecast.pptx")

# Colors
BG = RGBColor(0x0D, 0x0D, 0x0D)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY_LABEL = RGBColor(0xA0, 0xA0, 0xA0)
GREY_MUTED = RGBColor(0x66, 0x66, 0x66)
ACCENT = RGBColor(0xFF, 0x2D, 0x2D)
TAB_BG = RGBColor(0xE8, 0xE8, 0xE8)
BLACK = RGBColor(0x00, 0x00, 0x00)
LINE_HEX = "FFFFFF"  # with alpha 6%

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
        "headline": "MUJERES DEL MUNDO DECLARAN CREER EN EQUIDAD DE PAREJA PERO EJECUTAN SOLAS LA CARGA MENTAL DEL HOGAR — EL DISCURSO YA CERRÓ, LA COCINA NO.",
        "body": "La declaración cambió hace una década: parejas heterosexuales jóvenes dicen creer en equidad, y en 29% de matrimonios USA ya ambos ganan parecido. Pero las horas no se movieron — la mujer sigue haciendo dos horas más de trabajo doméstico por día en países OECD. El peso pesado no es la tarea: es el inventario mental de quién agendó al pediatra, quién compra el detergente, quién recuerda el cumpleaños del suegro.",
        "hashtags": "#mentalload  #cargamental  #invisiblelabor  #weaponizedincompetence",
        "needs": "RECONOCIMIENTO · AGOTAMIENTO · JUSTICIA",
        "triggers": [
            {"big": "29%", "desc": "Matrimonios USA con ingresos iguales — pero mujer sigue haciendo más housework y cuidado.", "src": "PEW RESEARCH · 2024"},
            {"big": "+2h", "desc": "Más de trabajo doméstico no pagado por día hace la mujer OECD vs el hombre.", "src": "OECD TIME USE · 2024"},
            {"big": "11M", "desc": "Views del video viral de Paige Connell sobre carga mental en TikTok 2024.", "src": "TIKTOK @SHEISAPAIGETURNER · 2024"},
        ],
        "signals": [
            {"img": "macro-1-1-tt-paigeturner-mentalload.png", "cap": "Paige Connell: \"Even a good guy can be part of the problem\" — 11M views.", "src": "TIKTOK · 2024", "url": "https://www.tiktok.com/@sheisapaigeturner/video/7439002806339734830"},
            {"img": "macro-1-1-pew-egalitarian-marriages.png", "cap": "29% de matrimonios USA ya ganan igual — mujer hace 2.5h más housework/semana.", "src": "PEW RESEARCH · 2024", "url": "https://www.pewresearch.org/social-trends/2023/04/13/in-a-growing-share-of-u-s-marriages-husbands-and-wives-earn-about-the-same/"},
            {"img": "macro-1-1-mckinsey-witw-2024.png", "cap": "Doble turno sigue siendo razón principal de burnout femenino senior.", "src": "MCKINSEY & LEANIN · 2024", "url": "https://www.mckinsey.com/featured-insights/diversity-and-inclusion/women-in-the-workplace"},
        ],
    },
    {
        "macro": 1,
        "headline": "PLANCHAR ES LA ÚLTIMA TAREA DOMÉSTICA SIN HOMBRE DEL PLANETA — LA ASPIRADORA SE DEMOCRATIZÓ, LA PLANCHA NO.",
        "body": "La aspiradora se democratizó cuando llegó el Roomba; la cocina entró al feed masculino vía dadcore y BBQtok; la limpieza profunda tiene a hombres en CleanTok. Planchar no. ILO confirma que el mantenimiento textil — lavar, planchar, doblar — es la categoría más feminizada del trabajo doméstico no remunerado del planeta. En TikTok, el ironing ASMR se volvió subgénero entero y casi todas las creadoras son mujeres.",
        "hashtags": "#ironingtok  #planchar  #asmrironing  #domesticgap",
        "needs": "VISIBILIDAD · RESENTIMIENTO · RECIPROCIDAD",
        "triggers": [
            {"big": "#1", "desc": "Mantenimiento textil es la categoría más feminizada del trabajo doméstico no remunerado.", "src": "ILO CARE AT WORK · 2024"},
            {"big": "100M+", "desc": "Views #ironingtok y #asmrironing, casi 100% creadoras mujeres con peak 2024-2025.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "29%", "desc": "Matrimonios USA ingresos iguales — mujer sigue haciendo más tareas domésticas.", "src": "PEW RESEARCH · 2024"},
        ],
        "signals": [
            {"img": "macro-1-2-ilo-care-work.png", "cap": "Mantenimiento textil — la tarea más feminizada del planeta documentada por ILO.", "src": "ILO · 2024", "url": "https://www.ilo.org/publications/care-work-and-care-jobs-future-decent-work"},
            {"img": "macro-1-1-tt-paigeturner-mentalload.png", "cap": "Vector cercano: carga doméstica feminizada como contenido viral.", "src": "TIKTOK · 2024", "url": "https://www.tiktok.com/@sheisapaigeturner/video/7439002806339734830"},
            {"img": "macro-1-1-pew-egalitarian-marriages.png", "cap": "Pew 2024 confirma el domestic gap incluso con ingresos iguales.", "src": "PEW RESEARCH · 2024", "url": "https://www.pewresearch.org/social-trends/2023/04/13/in-a-growing-share-of-u-s-marriages-husbands-and-wives-earn-about-the-same/"},
        ],
    },
    {
        "macro": 1,
        "headline": "EN LATAM 4 DE CADA 10 HOGARES YA TIENEN JEFA MUJER SIN PAREJA — LA \"MAMÁ SOLA\" DEJÓ DE SER CASO PARA VOLVERSE CATEGORÍA ECONÓMICA.",
        "body": "Por décadas el hogar con jefatura femenina era leído como déficit — la familia rota, el caso de política social. En 2024 ya es estructural: 4 de cada 10 hogares LATAM tienen jefatura femenina sin cónyuge, según CEPAL. En TikTok la categoría se nombra a sí misma — #singlemomlife acumula 12B views — y las creadoras ya no narran tragedia: muestran presupuesto y logística como ventajas operativas.",
        "hashtags": "#singlemomlife  #mamasoltera  #jefadehogar  #headofhousehold",
        "needs": "AUTONOMÍA · SOLEDAD · ORGULLO",
        "triggers": [
            {"big": "4/10", "desc": "Hogares LATAM con jefatura femenina sin cónyuge — crecimiento sostenido.", "src": "CEPAL OIG · 2024"},
            {"big": "12B", "desc": "Views acumulados #singlemomlife con peak sostenido 2024-2025.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "↑", "desc": "ENHOGAR-MICS confirma jefatura femenina creciente en hogares RD post-2020.", "src": "ONE BOLETINES GÉNERO · 2024"},
        ],
        "signals": [
            {"img": "macro-1-1-tt-paigeturner-mentalload.png", "cap": "Madre proveedora única narrando logística sola como contenido.", "src": "TIKTOK · 2024", "url": "https://www.tiktok.com/@sheisapaigeturner/video/7439002806339734830"},
            {"img": "macro-1-4-aplaceformom-sandwich.png", "cap": "La mujer adulta como pivote estructural del cuidado familiar.", "src": "A PLACE FOR MOM · 2024", "url": "https://www.aplaceformom.com/caregiver-resources/articles/what-is-the-sandwich-generation"},
            {"img": "macro-1-0-ourfamilywizard.png", "cap": "App diseñada para la mujer post-divorcio que coadministra sola.", "src": "OURFAMILYWIZARD · 2024", "url": "https://www.ourfamilywizard.com/"},
        ],
    },
    {
        "macro": 1,
        "headline": "LATAM ENVEJECE Y EL CUIDADO DE LOS VIEJOS CAE CASI 100% EN MUJERES ADULTAS — LA \"HIJA CUIDADORA\" ES LA NUEVA CARGA SIN NOMBRE.",
        "body": "LATAM va a duplicar su población mayor de 60 al 2050. En USA, donde sí hay data fina, 61% de cuidadores familiares son mujeres y dedican 24 horas semanales sin paga. La sandwich generation — mujer adulta entre madre mayor e hijo adolescente — se volvió categoría TikTok con video diario sobre rutina dual. La hija cuidadora todavía no tiene contrato laboral, no tiene pensión, no tiene reemplazo.",
        "hashtags": "#sandwichgeneration  #caregivertok  #eldercare  #hijascuidadoras",
        "needs": "APOYO · INVISIBILIDAD · CULPA",
        "triggers": [
            {"big": "61%", "desc": "Cuidadores familiares USA son mujeres, ~24 horas semanales sin paga.", "src": "AARP · 2025"},
            {"big": "2x", "desc": "Población mayor de 60 en LATAM al 2050 con servicios de cuidado subdesarrollados.", "src": "UNFPA / CELADE · 2024"},
            {"big": "1B", "desc": "Views combinados #sandwichgeneration y #caregivertok con peak 2024-2025.", "src": "TIKTOK CREATIVE CENTER · 2025"},
        ],
        "signals": [
            {"img": "macro-1-4-aplaceformom-sandwich.png", "cap": "Sandwich generation — mujer adulta entre madre mayor e hijo, ~24h/sem sin paga.", "src": "A PLACE FOR MOM · 2024", "url": "https://www.aplaceformom.com/caregiver-resources/articles/what-is-the-sandwich-generation"},
            {"img": "macro-1-4-aarp-caregiving-2025.png", "cap": "63M cuidadores en USA, 3 de cada 5 son mujeres — AARP 2025.", "src": "AARP · 2025", "url": "https://www.aarp.org/caregiving/basics/caregiving-in-us-survey-2025/"},
            {"img": "macro-1-0-ourfamilywizard.png", "cap": "Primera app que formalizó coordinación post-divorcio; eldercare apenas empieza.", "src": "OURFAMILYWIZARD · 2024", "url": "https://www.ourfamilywizard.com/"},
        ],
    },
    {
        "macro": 1,
        "headline": "EN RD SE FIRMARON 26,210 DIVORCIOS CONTRA 44,349 MATRIMONIOS EN 2024 — RATIO 59%, EL MÁS ALTO REGISTRADO, Y EL \"HASTA QUE LA MUERTE\" SE VOLVIÓ CLÁUSULA OPCIONAL.",
        "body": "Durante décadas el divorcio en RD fue tabú con tasa real escondida. En 2024 la ONE publicó cifra exacta: 26,210 divorcios frente a 44,349 matrimonios — ratio 59%, sostenido desde 2021. En 2025 los matrimonios bajaron 8.7% adicional. La pregunta cultural cambió de \"¿por qué se separaron?\" a \"¿por qué seguían juntos?\". Las creadoras LATAM 30-45 narran su divorce era como rito de paso positivo.",
        "hashtags": "#divorcetok  #divorceera  #miseparé  #postdivorce",
        "needs": "PERMISO · LIBERACIÓN · MIEDO",
        "triggers": [
            {"big": "59%", "desc": "Ratio divorcios/matrimonios RD 2024 — el más alto registrado, sostenido desde 2021.", "src": "LISTÍN DIARIO / ONE · 2025"},
            {"big": "-8.7%", "desc": "Matrimonios en RD bajaron adicional 8.7% en 2025 vs año anterior.", "src": "DIARIO LIBRE · 2026"},
            {"big": "5B", "desc": "Views combinados #divorcetok y #divorceera con peak 2024-2026.", "src": "TIKTOK CREATIVE CENTER · 2025"},
        ],
        "signals": [
            {"img": "macro-1-5-listin-divorcios-2024.png", "cap": "RD 2024: 44,349 matrimonios vs 26,210 divorcios — ratio 59% confirmado por ONE.", "src": "LISTÍN DIARIO · 2025", "url": "https://listindiario.com/la-republica/ciudad/20250601/2024-registraron-44-349-matrimonios-26-210-divorcios_859974.html"},
            {"img": "macro-1-5-diariolibre-divorcios.png", "cap": "2025: matrimonios bajan 8.7% más en RD; divorcio se vuelve desenlace estadístico esperable.", "src": "DIARIO LIBRE · 2026", "url": "https://www.diariolibre.com/actualidad/nacional/2026/05/16/matrimonios-en-republica-dominicana-caen-87--en-2025/3536088"},
            {"img": "macro-1-5-eldia-matrimonios.png", "cap": "Mujer dominicana se casa más joven y se divorcia más joven que el hombre.", "src": "EL DÍA · 2025", "url": "https://eldia.com.do/mujeres-se-casan-mas-jovenes-que-los-hombres-en-rd/"},
        ],
    },
    # ----- MACRO 2 -----
    {
        "macro": 2,
        "headline": "APPLE WATCH Y OURA RING 4 CONVIRTIERON EL CUERPO FEMENINO EN DATA CONTINUO — LA MUJER LEE SU CICLO EN LA MUÑECA ANTES QUE EN LA CONSULTA.",
        "body": "Por generaciones la mujer dependió del ginecólogo para descifrar qué pasaba con su cuerpo. Oura Ring 4 (US$349, Oct 2024) y Apple Cycle Tracking le pusieron sensores 24/7 que tracking ciclo, ventana fértil, fase luteal, sueño y estrés. En TikTok la luteal phase se volvió excusa social legible — \"hoy no, estoy en luteal\" — y screenshots de Apple Health o Oura aparecen como prueba contra una pareja que pide explicaciones. La autoridad médica se descentralizó hacia un anillo.",
        "hashtags": "#cycletracking  #lutealphase  #ourabring  #femtech",
        "needs": "AUTONOMÍA · VIGILANCIA · CONTROL",
        "triggers": [
            {"big": "US$80B", "desc": "Mercado wearables 2024 con FemTech wearables liderando adopción femenina.", "src": "STATISTA · 2025"},
            {"big": "US$349", "desc": "Precio Oura Ring 4 lanzado Oct 2024 con smart sensing 24/7.", "src": "CNBC / OURA · 2024"},
            {"big": "2B", "desc": "Views combinados #cycletracking y #lutealphase con peak 2024-2025.", "src": "TIKTOK CREATIVE CENTER · 2025"},
        ],
        "signals": [
            {"img": "macro-2-1-cnbc-oura-ring4.png", "cap": "Oura Ring 4 (US$349, Oct 2024) — smart sensing 24/7, lidera FemTech.", "src": "CNBC · 2024", "url": "https://www.cnbc.com/2024/10/03/oura-ring-4-price-release-date.html"},
            {"img": "macro-2-1-oura-ring-4.png", "cap": "Brand product photography close-up titanium ring oficial Oura.", "src": "OURA · 2024", "url": "https://ouraring.com/blog/oura-ring-4/"},
            {"img": "macro-2-2-tt-irobot-asmr-roomba.png", "cap": "Cluster cercano: tech doméstica posicionada como aliada femenina.", "src": "TIKTOK @IROBOT · 2024", "url": "https://www.tiktok.com/@irobot/video/7453137561335156011"},
        ],
    },
    {
        "macro": 2,
        "headline": "EL ROOMBA NO LIBERÓ A LA MUJER, LA TRIANGULA — LA MARCA POSICIONA EL ROBOT COMO ALIADA DE ELLA, NO COMO TAREA PENDIENTE DE ÉL.",
        "body": "El smart home se vendió como liberación, pero la lectura cultural fina es otra: triangulación. La cuenta oficial @irobot en TikTok produce activamente el imaginario \"Roomba como aliada de la mujer, no de la pareja, no del trabajador doméstico\". La automatización doméstica se monta encima de una desigualdad de clase histórica — en LATAM, donde la muchacha sigue siendo infraestructura del hogar de clase media, el Roomba no reemplaza al hombre que no plancha. Reemplaza a otra mujer.",
        "hashtags": "#smarthome  #cleantok  #roomba  #hogarinteligente",
        "needs": "LIBERAR TIEMPO · CULPA DE CLASE · EVASIÓN",
        "triggers": [
            {"big": "US$150B", "desc": "Mercado global smart home appliances 2024 con LATAM creciendo a doble dígito.", "src": "STATISTA · 2024"},
            {"big": "US$10B", "desc": "Robot vacuum market 2024 con penetración acelerada en hogares dual-income.", "src": "GRAND VIEW RESEARCH · 2024"},
            {"big": "30B", "desc": "Views combinados #smarthome y #cleantok con robot vacuum, peak 2024-2025.", "src": "TIKTOK CREATIVE CENTER · 2025"},
        ],
        "signals": [
            {"img": "macro-2-2-tt-irobot-asmr-roomba.png", "cap": "\"Satisfying clean\" — iRobot construye el imaginario Roomba como sustituto de la ayuda.", "src": "TIKTOK @IROBOT · 2024", "url": "https://www.tiktok.com/@irobot/video/7453137561335156011"},
            {"img": "macro-2-2-tt-sevda-roomba-mom.png", "cap": "Mamá real explicando setup Roomba post-cocina con hija.", "src": "TIKTOK @SEVDA.ELA · 2024", "url": "https://www.tiktok.com/@sevda.ela/video/7503619211948756226"},
            {"img": "macro-2-2-tt-irobot-cleantok.png", "cap": "La marca como productora cultural del imaginario doméstico.", "src": "TIKTOK @IROBOT · 2024", "url": "https://www.tiktok.com/@irobot/video/7159562439242173742"},
        ],
    },
    {
        "macro": 2,
        "headline": "NUBANK CRUZÓ 100M CLIENTES LATAM Y SPLITWISE CONVIRTIÓ A LA PAREJA EN DASHBOARD — EL DINERO YA NO ES SECRETO, ES SPREADSHEET COMPARTIDO.",
        "body": "Nubank cerró mayo 2024 con 100M clientes — primer banco digital fuera de Asia. En paralelo, apps como Splitwise y Settle Up se infiltraron en parejas heterosexuales jóvenes: cada Uber, cada delivery, cada vacación queda registrado al milímetro. Lo que parecía transparencia económica empieza a leerse en clave doble: por un lado destapa décadas de \"él la mantiene/ella aporta lo invisible\", por otro convierte la pareja en relación de cuentas.",
        "hashtags": "#couplebudget  #splitwise  #financespareja  #qikrd",
        "needs": "TRANSPARENCIA · CONTROL · INTIMIDAD",
        "triggers": [
            {"big": "100M", "desc": "Clientes Nubank LATAM mayo 2024 — primer banco digital fuera de Asia.", "src": "BLOOMBERG · 2024"},
            {"big": "3B", "desc": "Views combinados #couplebudget y #financespareja con peak 2024-2025.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "↑", "desc": "BCRD reporta crecimiento sostenido pagos digitales y billeteras móviles RD post-2023.", "src": "BCRD · 2024"},
        ],
        "signals": [
            {"img": "macro-2-3-bloomberg-nubank-100m.png", "cap": "Nubank cruzó 100M clientes LATAM mayo 2024 — primer banco digital fuera de Asia.", "src": "BLOOMBERG · 2024", "url": "https://www.bloomberg.com/news/articles/2024-05-08/nubank-surpasses-100-million-clients-across-latin-america"},
            {"img": "macro-2-3-splitwise-app.png", "cap": "Splitwise expone al milímetro quién pone qué en la pareja — dashboard o disputa.", "src": "SPLITWISE · 2024", "url": "https://www.splitwise.com/"},
            {"img": "macro-2-3-americaeconomia-nubank.png", "cap": "Hero corporate Nubank LATAM milestone — expansión continental confirmada.", "src": "AMÉRICA ECONOMÍA · 2024", "url": "https://www.americaeconomia.com/en/business-industries/nubank-surpasses-100-million-customers-latin-america"},
        ],
    },
    {
        "macro": 2,
        "headline": "MAVEN CLINIC CERRÓ SERIES F A US$1.7B EN OCTUBRE 2024 — LA GINECÓLOGA AHORA VIVE EN UNA APP Y NADIE EN LA FAMILIA SE ENTERA.",
        "body": "Maven Clinic se volvió primer unicornio women's health en octubre 2024 con valuation US$1.7B. Junto con Tia, Allara y otras, ofrecen ginecología, fertilidad, perimenopausia y salud hormonal vía app — onboarding totalmente digital, segunda opinión sin agendar presencial. Lo que cambia no es la consulta médica — cambia el filtro social. Antes la salud reproductiva pasaba por la madre, la suegra, la vecina enfermera; hoy pasa por una doctora en pantalla que nadie en casa ve.",
        "hashtags": "#telesalud  #femtech  #perimenopause  #ginecologiaonline",
        "needs": "PRIVACIDAD · AGENCIA · SOLEDAD",
        "triggers": [
            {"big": "US$1.7B", "desc": "Valuation Maven Clinic Series F Oct 2024 — primer unicornio women's health.", "src": "FORTUNE / CNBC · 2024"},
            {"big": "1.5B", "desc": "Views combinados #perimenopause y #endotok con peak 2024-2025.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "♀", "desc": "Mujeres lideran uso de telesalud para salud reproductiva, mental y hormonal.", "src": "ROCK HEALTH · 2024"},
        ],
        "signals": [
            {"img": "macro-2-4-fortune-maven-1-7b.png", "cap": "Maven Clinic valuada US$1.7B (Oct 2024) — primera unicornio women's health.", "src": "FORTUNE · 2024", "url": "https://fortune.com/2024/10/09/startup-maven-founder-says-womens-health-still-undervalued/"},
            {"img": "macro-2-4-cnbc-maven-clinic.png", "cap": "CNBC confirma Series F US$1.7B — milestone de la categoría.", "src": "CNBC · 2024", "url": "https://www.cnbc.com/2024/10/08/womens-health-startup-maven-clinic-raises-at-1point7-billion-valuation.html"},
            {"img": "macro-2-4-maven-clinic-landing.png", "cap": "Brand-issued social card Maven 2026 — ginecóloga en pantalla.", "src": "MAVEN · 2026", "url": "https://www.maven.com/"},
        ],
    },
    {
        "macro": 2,
        "headline": "AMAZON RUFUS Y OPENAI OPERATOR EMPEZARON A HACER LAS COMPRAS DEL HOGAR — LA CARGA MENTAL FEMENINA MIGRA DEL CEREBRO AL PROMPT.",
        "body": "Amazon lanzó Rufus en febrero 2024; OpenAI lanzó Operator en enero 2025 como agente que opera el navegador entero. El mercado Agentic AI se proyecta de US$5.1B (2024) a US$47B (2030), CAGR sobre 45%. Lo concreto en hogares dual-income: lista del supermercado, cita del pediatra, comparador de precios, agendado del mantenimiento — todo eso que históricamente cargaba ella mentalmente, empieza a delegarse. La pregunta nueva ya no es \"¿quién hace?\". Es \"¿quién promptea?\".",
        "hashtags": "#agenticai  #aiagents  #rufus  #cargamentalIA",
        "needs": "DELEGAR · AGOTAMIENTO · CONFIGURACIÓN",
        "triggers": [
            {"big": "US$47B", "desc": "Proyección mercado Agentic AI al 2030 desde US$5.1B en 2024, CAGR >45%.", "src": "GRAND VIEW RESEARCH · 2025"},
            {"big": "Feb 24", "desc": "Amazon lanzó Rufus AI shopping assistant con expansión LATAM 2024-2025.", "src": "CNBC · 2024"},
            {"big": "Ene 25", "desc": "OpenAI lanzó Operator — agente que opera browser y compra por ti.", "src": "MIT TECH REVIEW · 2025"},
        ],
        "signals": [
            {"img": "macro-2-5-cnbc-amazon-rufus.png", "cap": "Amazon Rufus (Feb 2024) — AI shopping assistant haciendo las compras del hogar.", "src": "CNBC · 2024", "url": "https://www.cnbc.com/2024/02/01/amazon-announces-ai-shopping-assistant-called-rufus.html"},
            {"img": "macro-2-5-mit-operator-demo.png", "cap": "OpenAI Operator (Ene 2025) — agente que opera browser y compra por ti.", "src": "MIT TECH REVIEW · 2025", "url": "https://www.technologyreview.com/2025/01/23/1110484/openai-launches-operator-an-agent-that-can-use-a-computer-for-you/"},
            {"img": "macro-2-5-tc-openai-operator.png", "cap": "TechCrunch confirma Operator como agente autónomo de tareas.", "src": "TECHCRUNCH · 2025", "url": "https://techcrunch.com/2025/01/23/openai-launches-operator-an-ai-agent-that-performs-tasks-autonomously/"},
        ],
    },
    # ----- MACRO 3 -----
    {
        "macro": 3,
        "headline": "LA TRADWIFE RUBIA DE UTAH SE TROPICALIZÓ EN VERSIÓN EVANGÉLICA HISPANA — LA \"ESPOSA VIRTUOSA\" DE PROVERBIOS 31 REEMPLAZÓ A LA GIRLBOSS EN EL FEED CRISTIANO.",
        "body": "La tradwife dejó de ser nicho rural americano. #tradwife supera 4B views y #proverbs31wife cruza 500M. La versión hispana evangélica le agregó base bíblica: la esposa virtuosa como aspiracional, con tipografía editorial y voice over de versículos. Hannah Neeleman (@ballerinafarm), 18M followers, 9 hijos en Utah, se volvió \"queen of the trad wives\" según Rolling Stone. NYT y The Atlantic documentan crecimiento sostenido del movimiento post-2023.",
        "hashtags": "#tradwife  #proverbs31wife  #esposavirtuosa  #christianwife",
        "needs": "PERTENENCIA ESPIRITUAL · RENDICIÓN · BELLEZA",
        "triggers": [
            {"big": "4B", "desc": "Views #tradwife en TikTok con peak sostenido 2024-2025.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "18M", "desc": "Followers de Hannah Neeleman (@ballerinafarm) — queen of the trad wives.", "src": "ROLLING STONE · 2024"},
            {"big": "500M", "desc": "Views #proverbs31wife con vertiente cristiana evangélica liderando.", "src": "TIKTOK CREATIVE CENTER · 2025"},
        ],
        "signals": [
            {"img": "macro-3-1-rollingstone-ballerinafarm.png", "cap": "Hannah Neeleman (@ballerinafarm) — 18M followers, queen of the trad wives, 9 hijos.", "src": "ROLLING STONE · 2024", "url": "https://www.rollingstone.com/culture/culture-features/ballerina-farm-trad-wife-hannah-neeleman-1235072506/"},
            {"img": "macro-3-1-deseret-ballerinafarm.png", "cap": "La controversia editorial que cementó la categoría tradwife.", "src": "DESERET NEWS · 2024", "url": "https://www.deseret.com/utah/2024/07/30/ballerina-farms-trad-wife-hannah-neeleman-utah-controversy/"},
            {"img": "macro-3-0-tiktok-whats-next.png", "cap": "TikTok como infraestructura cultural 2024 donde la tradwife escaló.", "src": "TIKTOK NEWSROOM · 2024", "url": "https://newsroom.tiktok.com/tiktok-whats-next-2024-trend-report"},
        ],
    },
    {
        "macro": 3,
        "headline": "NETFLIX'S ADOLESCENCE (MAR 2025) PUSO A KEIR STARMER A HABLAR DE TATE EN ESCUELAS — LA MANOSPHERE YA NO ES NICHO DE INTERNET, ES AGENDA PÚBLICA.",
        "body": "\"Adolescence\" salió en Netflix en marzo 2025 y se volvió evento cultural global en semanas. Cuatro capítulos sobre un chico de 13 años que mata a una compañera tras radicalización digital. El primer ministro británico Keir Starmer la convocó a discusión pública y el gobierno UK negoció acceso libre en escuelas. NBC News la cubrió nombrando Tate y manosphere explícitamente como radicalizadores. Pew confirma: chicos adolescentes consumen significativamente más manosphere que las chicas.",
        "hashtags": "#sigma  #alphamale  #redpill  #tatespanish",
        "needs": "PERTENENCIA MASCULINA · MIEDO · RABIA",
        "triggers": [
            {"big": "50B", "desc": "Views combinados #sigma, #alphamale, #redpill con crecimiento en español 2024-2025.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "Mar 25", "desc": "Adolescence Netflix — Tate y manosphere nombrados explícitamente como radicalizadores.", "src": "NBC NEWS · 2025"},
            {"big": "♂", "desc": "Chicos adolescentes consumen significativamente más manosphere que chicas.", "src": "PEW RESEARCH · 2024"},
        ],
        "signals": [
            {"img": "macro-3-2-nbc-adolescence-manosphere.png", "cap": "Adolescence (Netflix Mar 2025) — Tate y manosphere nombrados como radicalizadores.", "src": "NBC NEWS · 2025", "url": "https://www.nbcnews.com/pop-culture/pop-culture-news/adolescence-netflix-manosphere-toxic-masculinity-rcna196967"},
            {"img": "macro-3-2-nbc-adolescence.png", "cap": "Variante hero del reportaje NBC sobre radicalización adolescente.", "src": "NBC NEWS · 2025", "url": "https://www.nbcnews.com/pop-culture/pop-culture-news/adolescence-netflix-manosphere-toxic-masculinity-rcna196967"},
            {"img": "macro-3-0-tiktok-whats-next.png", "cap": "La infraestructura cultural que sirve los clips manosphere al feed adolescente.", "src": "TIKTOK NEWSROOM · 2024", "url": "https://newsroom.tiktok.com/tiktok-whats-next-2024-trend-report"},
        ],
    },
    {
        "macro": 3,
        "headline": "LA \"STAY-AT-HOME GIRLFRIEND\" PERFORMA DOMESTICIDAD PREMIUM SIN ACTA DE MATRIMONIO — TRADWIFE SIN BIBLIA NI ANILLO, CONTRACTUALMENTE FRÁGIL.",
        "body": "#stayathomegirlfriend supera 1.5B views. La fórmula: matcha de mañana, gym, pilates, hacer cena para él, todo en aesthetic suave. NYT, Vogue y BBC cubrieron el fenómeno post-2023 con foco en la precarización: sin matrimonio no hay protección legal de bienes ni pensión alimentaria si la relación termina. The Week reporta que Gen Z rechaza explícitamente girlboss culture como aspiracional. La diferencia con la tradwife es que aquí no hay base religiosa ni proyecto familiar — solo estética y dependencia económica.",
        "hashtags": "#stayathomegirlfriend  #softlife  #girlfriendera  #providerera",
        "needs": "ASPIRACIÓN ESTÉTICA · DEPENDENCIA · FRAGILIDAD",
        "triggers": [
            {"big": "1.5B", "desc": "Views #stayathomegirlfriend con peak 2024-2025 — aesthetic premium sin acta.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "Gen Z", "desc": "Rechazo explícito a girlboss culture; SAHG como aspiracional sin matrimonio.", "src": "THE WEEK · 2024"},
            {"big": "↑", "desc": "Retorno de actitudes de proveedor masculino entre Gen Z USA.", "src": "PEW RESEARCH · 2024"},
        ],
        "signals": [
            {"img": "macro-3-3-theweek-sahg.png", "cap": "Gen Z rechaza girlboss — stay-at-home girlfriend como aspiracional sin acta.", "src": "THE WEEK · 2024", "url": "https://theweek.com/culture-life/stay-at-home-girlfriends-why-gen-z-are-rejecting-girlboss-culture"},
            {"img": "macro-3-1-rollingstone-ballerinafarm.png", "cap": "Vector adyacente con base religiosa que la SAHG no tiene.", "src": "ROLLING STONE · 2024", "url": "https://www.rollingstone.com/culture/culture-features/ballerina-farm-trad-wife-hannah-neeleman-1235072506/"},
            {"img": "macro-3-0-tiktok-whats-next.png", "cap": "Infraestructura cultural donde escaló el aesthetic soft life.", "src": "TIKTOK NEWSROOM · 2024", "url": "https://newsroom.tiktok.com/tiktok-whats-next-2024-trend-report"},
        ],
    },
    {
        "macro": 3,
        "headline": "#PAPÁTOK EN ESPAÑOL LO LIDERA MÉXICO CON CREADORES DE MILLONES DE SEGUIDORES — RD APENAS PRODUCE SU PROPIO REPERTORIO AUDIOVISUAL DE PATERNIDAD ACTIVA.",
        "body": "#dadtok supera 30B views globales, #girldad cruza 20B. En español la categoría existe — Pepe & Teo, Quique Rosas, Luisito Comunica family — pero la producción es mexicana o española peninsular. Cuando se busca #papátok filtrado por DO en TikTok aparecen resultados escasos. La consecuencia: el padre dominicano que quiere modelar paternidad activa para sus hijos consume papás mexicanos como referencia [porque no hay otros]. El gap no es de paternidad real — es de paternidad publicada.",
        "hashtags": "#dadtok  #girldad  #papátok  #padresLATAM",
        "needs": "MODELADO MASCULINO · INVISIBILIDAD · VERGÜENZA",
        "triggers": [
            {"big": "30B", "desc": "Views #dadtok globales con peak sostenido 2024-2025.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "MX", "desc": "Family creators mexicanos lideran ranking hispanoparlante; RD ausente.", "src": "ADLATINA / ADWEEK · 2025"},
            {"big": "20B", "desc": "Views #girldad cruza 20B — categoría top de crecimiento en parenting.", "src": "INFLUENCER MARKETING HUB · 2025"},
        ],
        "signals": [
            {"img": "macro-3-4-abc-dadtok.png", "cap": "Dad creators con 1M+ followers en USA — categoría que en RD apenas se produce.", "src": "ABC NEWS · 2024", "url": "https://abcnews.go.com/Lifestyle/video/tiktok-dad-shares-parenting-stories-1-million-followers-114317885"},
            {"img": "macro-3-0-tiktok-whats-next.png", "cap": "La plataforma que escala la categoría family content hispanoparlante.", "src": "TIKTOK NEWSROOM · 2024", "url": "https://newsroom.tiktok.com/tiktok-whats-next-2024-trend-report"},
            {"img": "macro-3-1-rollingstone-ballerinafarm.png", "cap": "Vector cercano: el rol parental se publica como producto cultural.", "src": "ROLLING STONE · 2024", "url": "https://www.rollingstone.com/culture/culture-features/ballerina-farm-trad-wife-hannah-neeleman-1235072506/"},
        ],
    },
    {
        "macro": 3,
        "headline": "LA SUEGRA FUE REEMPLAZADA POR LA FAMILY CREATOR CERTIFICADA — MADRES JÓVENES CONSULTAN MÁS A BIG LITTLE FEELINGS QUE A SU PROPIA MAMÁ.",
        "body": "@biglittlefeelings tiene 4M de followers en Instagram y se volvió referente principal de gentle parenting global. Adweek 2024 cubrió el rise de momtok como primer canal de consejo parental para mujeres millennials y Gen Z. #momtok supera 35B views, #gentleparenting cruza 6B. La consecuencia operativa: la madre joven que duda sobre cómo manejar una rabieta no llama a su mamá — abre TikTok. La autoridad parental se descentralizó de la suegra al For You Page.",
        "hashtags": "#momtok  #gentleparenting  #crianzarespetuosa  #mamáprimeriza",
        "needs": "ORIENTACIÓN PRÁCTICA · CULPA · RUPTURA INTERGENERACIONAL",
        "triggers": [
            {"big": "4M", "desc": "Followers @biglittlefeelings en Instagram — referente gentle parenting global.", "src": "INSTAGRAM · 2024"},
            {"big": "35B", "desc": "Views #momtok con peak 2024-2025 — primer canal de consejo parental.", "src": "TIKTOK CREATIVE CENTER · 2025"},
            {"big": "6B", "desc": "Views #gentleparenting cruza 6B con crecimiento sostenido en español.", "src": "TIKTOK CREATIVE CENTER · 2025"},
        ],
        "signals": [
            {"img": "macro-3-5-biglittlefeelings-ig.png", "cap": "4M followers — la suegra fue reemplazada por la family creator certificada.", "src": "INSTAGRAM @BIGLITTLEFEELINGS · 2024", "url": "https://www.instagram.com/biglittlefeelings/"},
            {"img": "macro-3-5-biglittlefeelings-web.png", "cap": "La creadora como producto educativo completo — gentle parenting infraestructurado.", "src": "BIGLITTLEFEELINGS.COM · 2024", "url": "https://biglittlefeelings.com/"},
            {"img": "macro-3-0-tiktok-whats-next.png", "cap": "Infraestructura cultural donde momtok escaló a autoridad parental.", "src": "TIKTOK NEWSROOM · 2024", "url": "https://newsroom.tiktok.com/tiktok-whats-next-2024-trend-report"},
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
    """Add a thin line with low opacity (~6%)."""
    line = slide.shapes.add_connector(1, x1, y1, x2, y2)  # 1 = straight
    line.line.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    line.line.width = Emu(weight_emu)  # 1pt = ~9525 emu
    # Set alpha on line via XML
    ln = line.line._get_or_add_ln()
    solidFill = ln.find(qn('a:solidFill'))
    if solidFill is None:
        solidFill = etree.SubElement(ln, qn('a:solidFill'))
    # clear and rebuild
    for child in list(solidFill):
        solidFill.remove(child)
    srgb = etree.SubElement(solidFill, qn('a:srgbClr'))
    srgb.set('val', color_hex)
    alpha = etree.SubElement(srgb, qn('a:alpha'))
    alpha.set('val', str(int(alpha_pct * 1000)))  # 6% = 6000
    return line

def add_hyperlink_rect(slide, x, y, w, h, url):
    """Invisible rectangle with hyperlink overlay."""
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    sh.fill.background()
    sh.line.fill.background()
    sh.click_action.hyperlink.address = url
    return sh

def add_badge_click_me(slide, x, y):
    """Red 'Click me' badge."""
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
    tb = add_textbox(slide, cx - lbl_w // 2, lbl_y, lbl_w, lbl_h,
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
    tb = add_textbox(slide, cx - tag_w // 2, tag_y, tag_w, Inches(0.6),
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
        hl_size = 26
    elif hl <= 120:
        hl_size = 22
    elif hl <= 160:
        hl_size = 19
    else:
        hl_size = 16
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
    # Body
    body_h = Inches(1.5)
    tb = slide.shapes.add_textbox(col_left_x, cur_y, col_w - Inches(0.1), body_h)
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.line_spacing = 1.0
    r = p.add_run()
    set_run(r, micro['body'], font=FONT_SANS, size=10, color=WHITE)
    cur_y += body_h + Inches(0.05)

    # HASHTAGS label + content
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

    # 3 NEEDS label + content
    add_textbox(slide, col_left_x, cur_y, col_w, Inches(0.18),
                "3 NEEDS", font=FONT_SANS, size=7, bold=True, color=GREY_LABEL)
    cur_y += Inches(0.2)
    tb = slide.shapes.add_textbox(col_left_x, cur_y, col_w - Inches(0.1), Inches(0.5))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p = tf.paragraphs[0]; p.line_spacing = 1.05
    r = p.add_run()
    set_run(r, micro['needs'], font=FONT_SERIF, size=14, color=WHITE)

    # ===== COL CENTER — TRIGGERS (3 vertical stats + desc box) =====
    trig_top = content_top
    block_h = (content_bottom - trig_top) / 3
    big_w = Inches(1.5)
    desc_box_w = Pt(170)
    desc_box_h = Pt(35)
    src_h = Inches(0.18)

    for i, trig in enumerate(micro['triggers']):
        bx = col_center_x
        by = trig_top + Inches(i * (block_h / Inches(1)))
        # actually use simple math
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
        else:
            big_size = 32
        tb = slide.shapes.add_textbox(bx, by, big_w, Inches(1.2))
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.line_spacing = 1.0
        r = p.add_run()
        set_run(r, big, font=FONT_SERIF, size=big_size, color=WHITE)
        # Source under big
        add_textbox(slide, bx, by + Inches(1.25), big_w, src_h,
                    trig['src'], font=FONT_SANS, size=7, color=GREY_MUTED)
        # Desc box to the right
        dbx = bx + big_w + Inches(0.05)
        dby = by + Inches(0.15)
        tb = slide.shapes.add_textbox(dbx, dby, desc_box_w, desc_box_h)
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.line_spacing = 1.0
        r = p.add_run()
        set_run(r, trig['desc'], font=FONT_SANS, size=10, color=WHITE)

    # ===== COL RIGHT — SEÑALES (3 vertical photos 149x220pt + caption box) =====
    sig_top = content_top
    photo_w = Pt(110)   # narrower so caption fits
    photo_h = Pt(150)
    cap_box_w = Pt(110)
    cap_box_h = Pt(35)
    block_h_r = (content_bottom - sig_top) / 3

    for i, sig in enumerate(micro['signals']):
        bx = col_right_x
        by = int(sig_top + i * block_h_r)
        img_path = os.path.join(SHOTS, sig['img'])
        if os.path.exists(img_path):
            try:
                pic = slide.shapes.add_picture(img_path, bx, by, width=photo_w, height=photo_h)
            except Exception as e:
                # placeholder
                pic = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, bx, by, photo_w, photo_h)
                pic.fill.solid(); pic.fill.fore_color.rgb = BG
                pic.line.color.rgb = WHITE
                pic.line.width = Emu(3175)
        else:
            pic = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, bx, by, photo_w, photo_h)
            pic.fill.solid(); pic.fill.fore_color.rgb = BG
            pic.line.color.rgb = WHITE
            pic.line.width = Emu(3175)
            tf = pic.text_frame
            tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
            r = p.add_run()
            set_run(r, "CAPTURA MANUAL\nJEREMY", font=FONT_SANS, size=8, bold=True, color=GREY_MUTED)

        # Badge "Click me" upper right
        bd_x = bx + photo_w - Pt(38)
        bd_y = by - Pt(6)
        add_badge_click_me(slide, bd_x, bd_y)

        # Hyperlink invisible overlay over the photo
        add_hyperlink_rect(slide, bx, by, photo_w, photo_h, sig['url'])

        # Caption box to the right
        cap_x = bx + photo_w + Inches(0.08)
        cap_y = by + Inches(0.15)
        tb = slide.shapes.add_textbox(cap_x, cap_y, cap_box_w, cap_box_h)
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.line_spacing = 1.0
        r = p.add_run()
        set_run(r, sig['cap'], font=FONT_SANS, size=9, color=WHITE)
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

    # Build sequence: divider 1, micros 1.1-1.5, divider 2, micros 2.1-2.5, divider 3, micros 3.1-3.5
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
