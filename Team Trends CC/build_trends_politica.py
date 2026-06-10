"""
build_trends_politica.py — Capítulo 10 OPINIONES POLÍTICAS

SOLO DATOS. Todo el layout vive en trends_deck_engine.py (el "CSS" central).
Para cambiar espaciado/tamaños/fuentes NO toques este archivo — edita el motor
y TODOS los capítulos se actualizan idénticos.

Inputs leídos:
  - Team Trends CC/outputs/trends-politica-editado.md
  - Team Trends CC/outputs/trends-politica-senales.md
  - Team Trends CC/screenshots/trends-politica/*.png  (38 PNGs verificados)
"""

from pathlib import Path
from trends_deck_engine import build_deck

BASE        = Path("/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC")
SCREENSHOTS = BASE / "screenshots" / "trends-politica"
OUTPUT      = BASE / "outputs" / "trends-politica-forecast.pptx"

# ─── Macros canónicas (nombres y taglines del editado.md) ───────────────────
M1_N    = "MACRO 1"; M1_NAME = "INVENTOLOGÍA DE LA ADULTEZ"
M1_TAG  = "Un mundo en crisis está reescribiendo qué significa ser adulto y formar familia."

M2_N    = "MACRO 2"; M2_NAME = "LOS HERNÁNDEZ ARE PROMPTED"
M2_TAG  = "El dominicano ya entró al mundo prompteado. Solo no lo nombra así."

M3_N    = "MACRO 3"; M3_NAME = "ALGORITMO DEL HOGAR"
M3_TAG  = "El feed se sentó en la mesa y nadie le ofreció silla."

DIVIDERS = [
    (1, M1_NAME, M1_TAG),
    (2, M2_NAME, M2_TAG),
    (3, M3_NAME, M3_TAG),
]

MICROS = [
    # ── Macro 1 · INVENTOLOGÍA DE LA ADULTEZ ────────────────────────────────
    # 1.1 — VOTO SÍ, FE NO
    dict(
        macro_n=M1_N, macro_name=M1_NAME,
        headline="Vota porque toca, no porque crea: el sufragio sobrevive como ritual mientras la fe en que cambie algo se erosiona en toda LATAM.",
        fenomeno="Antes votar y creer venían juntos. Hoy se separan. En LATAM convive una tasa de voto declarado alta con desconfianza profunda: solo 45% de los jóvenes está satisfecho con la democracia. El acto se mantiene como hábito cívico — la esperanza no. Aparece el lenguaje del «menos malo» que convierte el voto en cálculo de daño.",
        hashtags="#elmenosmalo · #votoútil · #desencanto",
        triggers=[
            dict(stat="45%",
                 desc="De jóvenes LATAM satisfecho con la democracia; casi 40% desconfía de su gobierno.",
                 source="Latinobarómetro · 2024"),
            dict(stat="77%",
                 desc="Votó en la última elección dominicana y 46.6% considera el sistema nada justo — vota y no cree.",
                 source="Código Casa · 2025"),
            dict(stat="2024",
                 desc="LATAM pasa «del desencanto de la política a la redefinición de la democracia» según U. Navarra.",
                 source="Global Affairs U. Navarra · 2024"),
        ],
        signals=[
            dict(png="macro-1-1-unav-desencanto-latam.png",
                 caption="Artículo académico sobre redefinición de democracia en LATAM — del desencanto a nuevas formas de participación.",
                 source="Global Affairs U. Navarra · 2024",
                 url="https://en.unav.edu/web/global-affairs/latinoam%C3%A9rica-del-desencanto-de-la-pol%C3%ADtica-a-la-redefinici%C3%B3n-de-la-democracia"),
            dict(png="macro-1-1-tiktok-votoutil-hashtag.png",
                 caption="Página hashtag #votoútil en TikTok — grid de videos sobre voto estratégico «el menos malo».",
                 source="TikTok · 2026",
                 url="https://www.tiktok.com/tag/votoútil"),
        ],
    ),
    # 1.2 — LA SALIDA EN VEZ DE LA VOZ
    dict(
        macro_n=M1_N, macro_name=M1_NAME,
        headline="La salida en vez de la voz: ante un sistema que se siente injusto, la respuesta de muchos jóvenes no es protesta, es pasaporte.",
        fenomeno="La teoría cívica clásica decía: si algo te molesta, alza la voz. Una generación está cambiando la voz por la salida. Emigrar funciona como voto con los pies. Los vlogs de «me voy del país» ordenan el futuro como proyecto migratorio antes que como proyecto cívico.",
        hashtags="#salirdelpaís · #diáspora · #dominicanosporelmundo",
        triggers=[
            dict(stat="66.1%",
                 desc="De jóvenes dominicanos 18-21 ha considerado vivir fuera del país (61% de los 22-25).",
                 source="Diario Libre · 2024"),
            dict(stat="2.87M",
                 desc="Dominicanos residían fuera al cierre de 2024; 37.2% de la diáspora tiene menos de 25 años.",
                 source="Prensa Latina · 2025"),
            dict(stat="47%",
                 desc="Se declara muy dispuesto a emigrar en el espejo Código Casa — la salida planificada.",
                 source="Código Casa · 2025"),
        ],
        signals=[
            dict(png="macro-1-2-tiktok-salirdelpais-hashtag.png",
                 caption="Página hashtag #salirdelpaís en TikTok — grid de vlogs de emigración, el futuro como aeropuerto.",
                 source="TikTok · 2026",
                 url="https://www.tiktok.com/tag/salirdelpais"),
            dict(png="macro-1-2-diariolibre-migracion-dominicana.png",
                 caption="Artículo Diario Libre: 66.1% de jóvenes 18-21 ha considerado vivir fuera del país.",
                 source="Diario Libre · 2024",
                 url="https://www.diariolibre.com/opinion/mas-firmas/2024/09/16/migracion-los-dominicanos-tambien-emigran/2851533"),
            dict(png="macro-1-2-prensalatina-emigracion-rd.png",
                 caption="Prensa Latina: 2.87M dominicanos en la diáspora al cierre de 2024; 37.2% menores de 25.",
                 source="Prensa Latina · 2025",
                 url="https://www.prensa-latina.cu/2025/07/17/mas-de-27-mil-dominicanos-emigraron-en-2024-revela-investigacion/"),
        ],
    ),
    # 1.3 — EL SUEÑO ES INSTITUCIONAL, NO PARTIDISTA
    dict(
        macro_n=M1_N, macro_name=M1_NAME,
        headline="El sueño dejó de ser un líder y pasó a ser una regla que se cumpla: la lealtad de bandera cede ante el deseo de instituciones que funcionen.",
        fenomeno="El ideal cívico migra de la persona a la regla. La confianza en instituciones formales cae mientras sube la confianza en pares y líderes comunitarios. El lenguaje cambia de «es de los míos» a «que cumpla lo que prometió». Se premia y castiga gestión por resultado, no por color.",
        hashtags="#queseaolacumplan · #instituciones · #resultados",
        triggers=[
            dict(stat="↓",
                 desc="Confianza en instituciones formales en LATAM/Caribe cae mientras sube en pares e influencers.",
                 source="Security Journal Americas · 2026"),
            dict(stat="46.6%",
                 desc="Considera el sistema nada justo en RD — no pide un caudillo, pide que la regla deje de tener excepciones.",
                 source="Código Casa · 2025"),
            dict(stat="2024",
                 desc="«Redefinición de la democracia»: el ciudadano exige resultados, no identidad partidista.",
                 source="Global Affairs U. Navarra · 2024"),
        ],
        signals=[
            dict(png="macro-1-3-securityjournal-trust-gap.png",
                 caption="Reporte Security Journal Americas 2026: brecha de confianza institucional en el Caribe y LATAM.",
                 source="Security Journal Americas · 2026",
                 url="https://securityjournalamericas.com/caribbean-latin-american-security-2026/"),
        ],
    ),
    # 1.4 — CIUDADANÍA DE CAUSA, NO DE CARNET
    dict(
        macro_n=M1_N, macro_name=M1_NAME,
        headline="Ciudadanía de causa, no de carnet: el 70% de la Gen Z global apoya algo, pero lo hace por tema puntual y online, no por militancia ni membresía.",
        fenomeno="La adultez cívica nueva no se afilia: se activa. Antes pertenecer era firmar una membresía estable. Ahora el compromiso es por tema — clima, género, justicia — y por temporada. El mismo estudio detecta activismo, fatiga y división conviviendo en la misma persona. Se apoya sin atarse.",
        hashtags="#causa · #cambiosocial · #sinpartido",
        triggers=[
            dict(stat="70%",
                 desc="De Gen Z global involucrado en una causa social o política; un tercio son activistas regulares.",
                 source="ShoutOut UK · 2025"),
            dict(stat="58%",
                 desc="Se declara nada interesado en política en RD — pero «política» ahí significa el aparato partidario, no la causa.",
                 source="Código Casa · 2025"),
            dict(stat="2024",
                 desc="Gen Z muestra activismo + fatiga + división simultáneos en torno a la elección (Montclair 2024).",
                 source="Montclair State University · 2024"),
        ],
        signals=[
            dict(png="macro-1-4-shoutoutuk-genz-activism.png",
                 caption="Hero del artículo ShoutOut UK: 70% de Gen Z involucrado en causas sociales, mayormente online.",
                 source="ShoutOut UK · 2025",
                 url="https://www.shoutoutuk.org/2025/09/19/gen-z-and-the-rise-of-performative-activism/"),
        ],
    ),
    # 1.5 — EL DESINTERÉS NO ES IGNORANCIA, ES BLINDAJE
    dict(
        macro_n=M1_N, macro_name=M1_NAME,
        headline="Decir «no me interesa la política» dejó de ser ignorancia: para el joven LATAM es blindaje emocional, autocuidado contra un sistema que solo le da frustración.",
        fenomeno="Lo que parecía apatía es, cada vez más, una postura activa. El joven LATAM ve el sistema como distante, burocrático e inefectivo para resolver lo cotidiano y se aparta a propósito. La «fatiga» aparece como uno de los cuatro ejes de la relación Gen Z con la política. Mutear noticias se vuelve contenido de bienestar.",
        hashtags="#newsdetox · #apolítico · #desconectar",
        triggers=[
            dict(stat="58%",
                 desc="Nada interesado en política en el espejo Código Casa — leído con el patrón global, es protección.",
                 source="Código Casa · 2025"),
            dict(stat="Fatiga",
                 desc="«Fatiga» como uno de los cuatro ejes de la relación Gen Z con la política 2024 (Montclair).",
                 source="Montclair State University · 2024"),
            dict(stat="2024",
                 desc="Nuevas generaciones ven la política como distante, burocrática e inefectiva para lo cotidiano.",
                 source="Latinobarómetro · 2024"),
        ],
        signals=[
            dict(png="macro-1-5-tiktok-newsdetox-hashtag.png",
                 caption="Página hashtag #newsdetox en TikTok — detox de noticias como contenido de bienestar y protección emocional.",
                 source="TikTok · 2026",
                 url="https://www.tiktok.com/tag/newsdetox"),
            dict(png="macro-1-5-montclair-genz-fatigue.png",
                 caption="Cover del estudio Montclair 2024: negatividad, activismo, división y fatiga Gen Z en redes.",
                 source="Montclair State University · 2024",
                 url="https://www.montclair.edu/college-of-communication-and-media/2024/12/05/negativity-activism-division-and-fatigue-gen-z-social-media-and-the-2024-election/"),
        ],
    ),

    # ── Macro 2 · LOS HERNÁNDEZ ARE PROMPTED ────────────────────────────────
    # 2.1 — EL DEEPFAKE QUE HABLA COMO TU PRESIDENTE
    dict(
        macro_n=M2_N, macro_name=M2_NAME,
        headline="El deepfake que habla como tu presidente: la IA ya falsifica voz y cara de figuras públicas, y en RD 2024 un audio presidencial falso circuló por bots.",
        fenomeno="La voz y la cara de figuras públicas se volvieron material falsificable. En la campaña RD 2024 circuló un audio deepfake presidencial sobre un tema sensible, difundido por cientos de bots IA vía una interfaz falsa de WhatsApp. La consecuencia es un reflejo nuevo: el votante duda de lo que oye antes de reenviarlo.",
        hashtags="#deepfake · #esIA · #verifica",
        triggers=[
            dict(stat="+350%",
                 desc="Hasta +550% proyectado en campañas de desinformación con IA en Sudamérica y el Caribe a 2026.",
                 source="GlobeNewswire · 2025"),
            dict(stat="2024",
                 desc="Audio deepfake presidencial sobre migración difundido por cientos de bots IA vía WhatsApp falso en RD.",
                 source="N Digital · 2024"),
            dict(stat="«¿Es IA?»",
                 desc="Auge de videos «esto es un deepfake» desmontando contenido político falso en feeds jóvenes.",
                 source="TikTok · 2026"),
        ],
        signals=[
            dict(png="macro-2-1-ndigital-deepfake-rd.png",
                 caption="Hero image N Digital: deepfake de audio presidencial en elecciones RD 2024 — el único visual local documentado.",
                 source="N Digital · 2024",
                 url="https://n.com.do/2024/05/14/el-deep-fake-irrumpe-en-las-elecciones-de-rd/"),
            dict(png="macro-2-1-ndigital-deepfake-article.png",
                 caption="Artículo N Digital: deepfake presidencial difundido por cientos de bots IA vía WhatsApp falso.",
                 source="N Digital · 2024",
                 url="https://n.com.do/2024/05/14/el-deep-fake-irrumpe-en-las-elecciones-de-rd/"),
            dict(png="macro-2-1-globenewswire-disinfo-550pct.png",
                 caption="Assessment GlobeNewswire: +350-550% proyectado en desinformación IA para Sudamérica y el Caribe a 2026.",
                 source="GlobeNewswire · 2025",
                 url="https://www.globenewswire.com/news-release/2025/10/10/3164963/0/en/AI-Disinformation-amp-Security-Threats-South-America-amp-Caribbean-2026-Assessment-Reveals-a-350-550-Projected-Increase-in-AI-Disinformation-Campaigns.html"),
        ],
    ),
    # 2.2 — LE PREGUNTÉ AL CHATBOT SI ERA VERDAD (Y MINTIÓ)
    dict(
        macro_n=M2_N, macro_name=M2_NAME,
        headline="Le preguntó al chatbot si era verdad y le mintió: el ciudadano usa Grok o ChatGPT para verificar noticias, pero los estudios muestran que repiten el bulo.",
        fenomeno="El árbitro de la verdad cambió de cara. AFP documentó que Grok, ChatGPT y Gemini repiten desinformación cuando se usan como fact-checkers, sobre todo en breaking news. El comportamiento observable es citar la respuesta del bot como prueba: «lo dijo Grok». La herramienta de verificación se convierte en fuente de error con cara de autoridad.",
        hashtags="#preguntéalachat · #grok · #verifica",
        triggers=[
            dict(stat="Grok",
                 desc="Usuarios citan a Grok como evidencia de que un clip era real cuando era generado por IA.",
                 source="AFP / TechXplore · 2025"),
            dict(stat="LATAM",
                 desc="WhatsApp emerge como mercado clave de chatbots IA en LATAM — terreno de verificación y desinformación.",
                 source="Aurora Inbox · 2025"),
            dict(stat="2025",
                 desc="«Hey chatbot, is this true?» — AFP documenta chatbots repitiendo desinformación en breaking news.",
                 source="TechXplore / AFP · 2025"),
        ],
        signals=[
            dict(png="macro-2-2-techxplore-chatbot-factcheck.png",
                 caption="Hero TechXplore/AFP: Grok, ChatGPT y Gemini repiten desinformación al usarse como fact-checkers.",
                 source="TechXplore / AFP · 2025",
                 url="https://techxplore.com/news/2025-06-hey-chatbot-true-ai-factchecks.html"),
            dict(png="macro-2-2-tiktok-fakenews-hashtag.png",
                 caption="Página hashtag #fakenews en TikTok — videos de verificación y denuncia de contenido falso.",
                 source="TikTok · 2026",
                 url="https://www.tiktok.com/tag/fakenews"),
            dict(png="macro-2-3-aurora-whatsapp-chatbot-latam.png",
                 caption="Aurora Inbox: futuro de chatbots en WhatsApp LATAM — terreno de verificación y desinformación.",
                 source="Aurora Inbox · 2025",
                 url="https://www.aurorainbox.com/en/2025/05/15/future-chatbots-whatsapp-trends-ai-automation/"),
        ],
    ),
    # 2.3 — LA VERIFICACIÓN ENTRA AL WHATSAPP DE LA FAMILIA
    dict(
        macro_n=M2_N, macro_name=M2_NAME,
        headline="La verificación entra al WhatsApp de la familia: frente a la cadena del tío surge la civic tech que chequea el bulo en la misma app donde circula.",
        fenomeno="Antes el bulo familiar no tenía contrapeso conversacional — circulaba y se quedaba. Ahora la civic tech entra al chat: chatbots y servicios de fact-checking que verifican por la misma app donde llega el audio sospechoso. AFP opera fact-checking en 26 idiomas dentro del programa de Meta. El gesto nuevo: reenviar el audio al bot antes de creerlo.",
        hashtags="#factchecking · #verificado · #cadenadewhatsapp",
        triggers=[
            dict(stat="26",
                 desc="Idiomas en que AFP opera fact-checking dentro del programa de Meta, incluyendo LATAM.",
                 source="AFP / TechXplore · 2025"),
            dict(stat="2024",
                 desc="UNESCO corrió taller de alfabetización mediática en Santo Domingo frente a la desinformación.",
                 source="UNESCO · 2024"),
            dict(stat="LATAM",
                 desc="WhatsApp consolidado como canal de chatbots IA de verificación en LATAM.",
                 source="Aurora Inbox · 2025"),
        ],
        signals=[
            dict(png="macro-2-3-tiktok-factchecking-hashtag.png",
                 caption="Página hashtag #factchecking en TikTok — tutoriales de verificación y civic tech.",
                 source="TikTok · 2026",
                 url="https://www.tiktok.com/tag/factchecking"),
            dict(png="macro-2-3-unesco-alfabetizacion-rd.png",
                 caption="UNESCO: taller de alfabetización mediática en Santo Domingo para combatir desinformación.",
                 source="UNESCO · 2024",
                 url="https://www.unesco.org/en/articles/unesco-promotes-media-and-information-literacy-means-counteract-disinformation-dominican-republic"),
            dict(png="macro-2-3-aurora-whatsapp-chatbot-latam.png",
                 caption="Chatbots de verificación en WhatsApp LATAM — la civic tech llega al chat antes que el reenvío del tío.",
                 source="Aurora Inbox · 2025",
                 url="https://www.aurorainbox.com/en/2025/05/15/future-chatbots-whatsapp-trends-ai-automation/"),
        ],
    ),
    # 2.4 — BOTS, NO MILITANTES
    dict(
        macro_n=M2_N, macro_name=M2_NAME,
        headline="Bots, no militantes: la «base» que ves apoyando online puede ser sintética; cientos de cuentas IA amplifican a una escala que ningún humano alcanza.",
        fenomeno="La movilización política se automatiza. Antes la base de apoyo eran personas que podías contar. Ahora cientos de bots IA amplifican narrativas a una escala que ningún militante humano alcanza — el deepfake presidencial RD 2024 se difundió justo así. Cuando algo se vuelve tendencia muy rápido, la pregunta es si los comentarios son gente o cuentas.",
        hashtags="#bots · #cuentasfalsas · #manipulación",
        triggers=[
            dict(stat="100s",
                 desc="De bots basados en IA difundieron el deepfake presidencial RD 2024 vía WhatsApp falso.",
                 source="N Digital · 2024"),
            dict(stat="+550%",
                 desc="Operaciones de desinformación IA apuntan a procesos electorales en la región a 2026.",
                 source="GlobeNewswire · 2025"),
            dict(stat="«¿Bot?»",
                 desc="«Cómo detectar un bot o cuenta falsa» como contenido de educación digital con alto alcance.",
                 source="TikTok · 2026"),
        ],
        signals=[
            dict(png="macro-2-1-tiktok-deepfake-hashtag.png",
                 caption="Página hashtag #deepfake en TikTok — videos de desmontaje y alerta ciudadana contra cuentas falsas.",
                 source="TikTok · 2026",
                 url="https://www.tiktok.com/tag/deepfake"),
            dict(png="macro-2-1-ndigital-deepfake-article.png",
                 caption="Artículo N Digital: cientos de bots IA detrás de la difusión del audio falso en elecciones RD 2024.",
                 source="N Digital · 2024",
                 url="https://n.com.do/2024/05/14/el-deep-fake-irrumpe-en-las-elecciones-de-rd/"),
            dict(png="macro-2-4-globenewswire-ai-disinfo.png",
                 caption="Assessment GlobeNewswire: operaciones de desinformación IA dirigidas a procesos electorales en la región.",
                 source="GlobeNewswire · 2025",
                 url="https://www.globenewswire.com/news-release/2025/10/10/3164963/0/en/AI-Disinformation-amp-Security-Threats-South-America-amp-Caribbean-2026-Assessment-Reveals-a-350-550-Projected-Increase-in-AI-Disinformation-Campaigns.html"),
        ],
    ),
    # 2.5 — EL ALGORITMO COMO ASESOR DE CAMPAÑA
    dict(
        macro_n=M2_N, macro_name=M2_NAME,
        headline="El algoritmo como asesor de campaña: KamalaHQ hizo 1.5B de vistas en TikTok. La política ya opera como cuenta de creador — remix, clip y engagement.",
        fenomeno="La campaña dejó de hablar como institución y empezó a hablar como creador. En 2024 KamalaHQ acumuló 1.5B de vistas con 5M de seguidores; la de Trump, 1B con 12M. El 48% de los usuarios de TikTok 18-29 usa la plataforma para seguir política. Y el feed tiene sesgo: el contenido tóxico atrae más engagement. La persuasión se mudó al scroll.",
        hashtags="#campañatiktok · #clips · #remix",
        triggers=[
            dict(stat="1.5B",
                 desc="Vistas de KamalaHQ en TikTok 2024 (5M seguidores); Trump 1B vistas (12M). Campaña como creador.",
                 source="eMarketer · 2024"),
            dict(stat="48%",
                 desc="De usuarios TikTok 18-29 usa la plataforma para seguir la política — la persuasión se mudó al scroll.",
                 source="Pew Research · 2024"),
            dict(stat="51,680",
                 desc="Videos políticos analizados en 2024: el contenido tóxico y partidista atrae consistentemente más engagement.",
                 source="HKS Misinformation Review · 2024"),
        ],
        signals=[
            dict(png="macro-2-5-emarketer-tiktok-election.png",
                 caption="eMarketer: KamalaHQ 1.5B vistas / Trump 1B vistas en TikTok 2024 — campaña política como cuenta de creador.",
                 source="eMarketer · 2024",
                 url="https://www.emarketer.com/content/tiktok-becomes-key-battleground-gen-z-voters-2024-election"),
            dict(png="macro-2-5-pew-tiktok-news.png",
                 caption="Pew: 48% de usuarios TikTok 18-29 usa la plataforma para seguir política.",
                 source="Pew Research · 2025",
                 url="https://www.pewresearch.org/short-reads/2025/01/17/a-closer-look-at-americans-experiences-with-news-on-tiktok/"),
            dict(png="macro-2-5-hks-toxic-tiktok-article.png",
                 caption="HKS Misinformation Review: 51,680 videos políticos 2024 — el contenido tóxico atrae más engagement.",
                 source="HKS Misinformation Review · 2024",
                 url="https://misinforeview.hks.harvard.edu/article/toxic-politics-and-tiktok-engagement-in-the-2024-u-s-election/"),
        ],
    ),

    # ── Macro 3 · ALGORITMO DEL HOGAR ───────────────────────────────────────
    # 3.1 — EL NOTICIERO ERES TÚ, NO EL CANAL
    dict(
        macro_n=M3_N, macro_name=M3_NAME,
        headline="El noticiero eres tú, no el canal: 38% de los menores de 30 recibe noticias de creadores, y 77% de ellos nunca trabajó en periodismo.",
        fenomeno="El medio dejó de ser una institución y pasó a ser una persona. El 38% de los menores de 30 obtiene noticias de news influencers y el 77% de esos creadores nunca trabajó en periodismo — 84% opera en TikTok. La credibilidad se vuelve parasocial: confío en él, no en su fuente. El comportamiento: seguir a un creador como «mi» fuente y citarlo como autoridad.",
        hashtags="#newsinfluencer · #creadordenoticias · #fuente",
        triggers=[
            dict(stat="38%",
                 desc="De menores de 30 recibe noticias de news influencers; 77% sin experiencia periodística (84% en TikTok).",
                 source="Pew Research · 2024"),
            dict(stat="40%",
                 desc="Casi 40% de jóvenes EE.UU. recibe noticias de influencers — la cercanía gana a la credencial.",
                 source="CNN Business · 2024"),
            dict(stat="LATAM",
                 desc="Creadores de noticias LATAM («te explico la noticia») con audiencias millonarias en TikTok.",
                 source="TikTok · 2026"),
        ],
        signals=[
            dict(png="macro-3-0-tiktok-newsinfluencer-hashtag.png",
                 caption="Página hashtag #newsinfluencer en TikTok — grid de creadores de noticias con contador de vistas.",
                 source="TikTok · 2026",
                 url="https://www.tiktok.com/tag/newsinfluencer"),
            dict(png="macro-3-1-pew-news-influencers.png",
                 caption="Pew: 77% de news influencers sin experiencia periodística, 84% en TikTok. La credencial desapareció.",
                 source="Pew Research · 2025",
                 url="https://www.pewresearch.org/journalism/2025/12/03/young-adults-and-the-future-of-news/"),
            dict(png="macro-3-1-cnn-news-influencers.png",
                 caption="CNN Business: casi 40% de jóvenes EE.UU. recibe noticias de influencers — mayoría hombres e inclinados a la derecha.",
                 source="CNN Business · 2024",
                 url="https://www.cnn.com/2024/11/18/media/news-influencers-social-media-conservative-study"),
        ],
    ),
    # 3.2 — EL FEED PREMIA LA RABIA
    dict(
        macro_n=M3_N, macro_name=M3_NAME,
        headline="El feed premia la rabia: en 51,680 videos políticos, el contenido tóxico ganó más engagement. La indignación viraliza mejor que el matiz.",
        fenomeno="El algoritmo no es un espejo neutral. Un análisis de 51,680 videos políticos de 2024 encontró que el contenido tóxico atrae consistentemente más engagement. Hay evidencia causal: rerankear la animosidad partidista en el feed altera la polarización afectiva. El feed sube la temperatura emocional del hogar a propósito.",
        hashtags="#outragebait · #polarización · #indignación",
        triggers=[
            dict(stat="51,680",
                 desc="Videos políticos analizados en 2024: el contenido tóxico y partidista gana más engagement consistentemente.",
                 source="HKS Misinformation Review · 2024"),
            dict(stat="PNAS",
                 desc="Evidencia causal: rerankear la animosidad partidista en feeds altera la polarización afectiva de la gente.",
                 source="PNAS / PubMed · 2025"),
            dict(stat="Rabia",
                 desc="«Outrage bait» político como formato de alto alcance — la indignación viraliza mejor que el matiz.",
                 source="TikTok · 2026"),
        ],
        signals=[
            dict(png="macro-3-2-hks-toxic-politics-chart.png",
                 caption="Chart HKS: toxicidad y engagement en 51,680 videos políticos 2024 — lo tóxico gana consistentemente.",
                 source="HKS Misinformation Review · 2024",
                 url="https://misinforeview.hks.harvard.edu/article/toxic-politics-and-tiktok-engagement-in-the-2024-u-s-election/"),
            dict(png="macro-3-2-pubmed-reranking-polarization.png",
                 caption="Abstract PNAS: evidencia causal de que rerankear animosidad partidista en feeds altera la polarización afectiva.",
                 source="PNAS / PubMed · 2025",
                 url="https://pubmed.ncbi.nlm.nih.gov/41308156/"),
            dict(png="macro-3-2-tiktok-outragebait-hashtag.png",
                 caption="Página hashtag #outragebait en TikTok — formato de alto alcance que premia la indignación sobre el matiz.",
                 source="TikTok · 2026",
                 url="https://www.tiktok.com/tag/outragebait"),
        ],
    ),
    # 3.3 — LA NOTICIA EN 60 SEGUNDOS O NO EXISTE
    dict(
        macro_n=M3_N, macro_name=M3_NAME,
        headline="La noticia en 60 segundos o no existe: 55% de usuarios de TikTok se informa ahí (22% en 2020), y el evento que no entra en un clip no entra a la conversación.",
        fenomeno="El consumo político se comprimió al formato del feed. Antes informarse pedía tiempo de lectura. Ahora pide 60 segundos verticales. El 55% de los usuarios de TikTok obtiene noticias en la app, frente al 22% en 2020. Lo que no se explica en un clip corto se cae de la conversación. El debate completo quedó fuera del scroll.",
        hashtags="#en60segundos · #explainer · #tldr",
        triggers=[
            dict(stat="55%",
                 desc="De usuarios TikTok obtiene noticias en la app — era solo 22% en 2020. El clip es el nuevo noticiero.",
                 source="Pew Research · 2024"),
            dict(stat="80%",
                 desc="De los 18-24 dominicanos se informa por redes — el joven RD ya vive dentro de esta compresión.",
                 source="Código Casa · 2025"),
            dict(stat="60s",
                 desc="Los usuarios de TikTok prefieren entretenimiento sobre noticias — el clip compite con el scroll de ocio.",
                 source="Marketing Brew · 2024"),
        ],
        signals=[
            dict(png="macro-3-3-pew-social-media-news.png",
                 caption="Fact sheet Pew: 55% de usuarios TikTok obtiene noticias ahí vs 22% en 2020.",
                 source="Pew Research · 2024",
                 url="https://www.pewresearch.org/journalism/fact-sheet/social-media-and-news-fact-sheet/"),
            dict(png="macro-3-3-marketingbrew-tiktok-entertainment.png",
                 caption="Marketing Brew: usuarios TikTok prefieren entretenimiento sobre noticias según Pew.",
                 source="Marketing Brew · 2024",
                 url="https://www.marketingbrew.com/stories/2024/10/08/tiktok-users-prefer-entertainment-over-news-pew-finds"),
        ],
    ),
    # 3.4 — CIVISMO PERFORMATIVO: EL POST COMO PARTICIPACIÓN
    dict(
        macro_n=M3_N, macro_name=M3_NAME,
        headline="Postear es participar: el 70% de la Gen Z dice apoyar una causa, casi todo online. Compartir la story se siente como acción aunque rara vez salga del feed.",
        fenomeno="Para mucha gente el gesto digital reemplazó la acción offline. Antes participar tenía un costo físico: ir, marchar, organizarse. Ahora el estudio Montclair describe ese activismo como más performativo que sustantivo. Se comparte la story, se cambia la foto de perfil. Se siente como acción. Casi nunca cruza la pantalla.",
        hashtags="#performativeactivism · #slacktivism · #posteo",
        triggers=[
            dict(stat="70%",
                 desc="De Gen Z global apoya una causa, mayormente online — auge del activismo performativo.",
                 source="ShoutOut UK · 2025"),
            dict(stat="2024",
                 desc="El activismo Gen Z online suele ser más performativo que sustantivo (Montclair 2024).",
                 source="Montclair State University · 2024"),
            dict(stat="Post",
                 desc="«Performative activism» como crítica autorreflexiva y formato viral con alto engagement.",
                 source="TikTok · 2026"),
        ],
        signals=[
            dict(png="macro-3-4-tiktok-performative-activism.png",
                 caption="Página hashtag #performativeactivism en TikTok — crítica autorreflexiva del activismo de pantalla.",
                 source="TikTok · 2026",
                 url="https://www.tiktok.com/tag/performativeactivism"),
            dict(png="macro-3-4-montclair-performative-activism.png",
                 caption="Estudio Montclair 2024: activismo Gen Z online — más performativo que sustantivo.",
                 source="Montclair State University · 2024",
                 url="https://www.montclair.edu/college-of-communication-and-media/2024/12/05/negativity-activism-division-and-fatigue-gen-z-social-media-and-the-2024-election/"),
            dict(png="macro-3-4-tiktok-slacktivism-hashtag.png",
                 caption="Página hashtag #slacktivism en TikTok — debate sobre participación digital vs acción real.",
                 source="TikTok · 2026",
                 url="https://www.tiktok.com/tag/slacktivism"),
        ],
    ),
    # 3.5 — EL FEED MIDE LA GESTIÓN
    dict(
        macro_n=M3_N, macro_name=M3_NAME,
        headline="El feed mide la gestión: la evaluación del gobierno se arma en tiempo real con clips virales, donde la narrativa simple le gana a la data y el desmentido nunca alcanza al bulo.",
        fenomeno="La evaluación de un gobierno ya no espera al noticiero ni al informe. Las narrativas simples superan al mensaje institucional complejo y la desinformación corre más rápido que las aclaraciones oficiales en LATAM. Los motores de recomendación moldean política con efectos medibles. La percepción le gana a la data.",
        hashtags="#loqueprometió · #gestión · #narrativa",
        triggers=[
            dict(stat="Narrativa",
                 desc="Narrativas simplistas superan al mensaje complejo; la desinformación corre más rápido que las aclaraciones en LATAM.",
                 source="Security Journal Americas · 2026"),
            dict(stat="2024-25",
                 desc="Los motores de recomendación moldean política, crianza y fe con efectos medibles.",
                 source="Pew Research · 2024-2025"),
            dict(stat="46.6%",
                 desc="Ve el sistema como nada justo en RD — cuando partes de la desconfianza, el clip que confirma «no cumplieron» viaja sin fricción.",
                 source="Código Casa · 2025"),
        ],
        signals=[
            dict(png="macro-3-5-securityjournal-latam-2026.png",
                 caption="Security Journal Americas 2026: narrativas simplistas superan al mensaje institucional complejo en LATAM/Caribe.",
                 source="Security Journal Americas · 2026",
                 url="https://securityjournalamericas.com/caribbean-latin-american-security-2026/"),
        ],
    ),
]

if __name__ == "__main__":
    build_deck(DIVIDERS, MICROS, SCREENSHOTS, OUTPUT)
