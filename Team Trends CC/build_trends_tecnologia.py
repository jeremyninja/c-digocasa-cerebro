"""
build_trends_tecnologia.py — Capítulo 08 TECNOLOGÍA

SOLO DATOS. Todo el layout vive en trends_deck_engine.py (el "CSS" central).
Para cambiar espaciado/tamaños/fuentes NO toques este archivo — edita el motor
y TODOS los capítulos se actualizan idénticos.
"""

from pathlib import Path
from trends_deck_engine import build_deck

BASE        = Path("/Users/jeremyrodriguez/Documents/Cerebro/Código Casa/Team Trends CC")
SCREENSHOTS = BASE / "screenshots" / "trends-tecnologia"
OUTPUT      = BASE / "outputs" / "trends-tecnologia-forecast.pptx"

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
    # 1.1 — El adulto LATAM trabaja, factura y estudia desde un solo teléfono
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="El adulto LATAM trabaja, factura y estudia desde un solo teléfono, y nunca toca una laptop: la única computadora que tendrá ya está en su mano.",
         fenomeno="El hogar multi-dispositivo del siglo XX asumía que ibas acumulando: PC, tablet, consola. Esa escalera se saltó. La penetración de internet en RD llegó a 88.6% mientras la computadora sigue siendo minoritaria. Plataformas como Rappi, Uber y Workana hacen del móvil la oficina del trabajador joven LATAM.",
         hashtags="#trabajodesdeelcelular · #soloconmicelular · #emprenderdominicana",
         triggers=[
             dict(stat="88.6%",  desc="Penetración de internet en RD (10.2M usuarios); la computadora sigue minoritaria en el hogar.", source="DataReportal · 2025"),
             dict(stat="US$6.2B", desc="Proyección economía gig ride-hailing LATAM en 2025; +24% de altas desde ciudades secundarias.", source="Konvoy VC / UNDP LATAM · 2025"),
             dict(stat="20.8%",  desc="Hogares RD con computadora vs 92.4% con celular — el móvil es la única computadora.", source="Código Casa · 2025"),
         ],
         signals=[
             dict(png="macro-1-1-datareportal-digital-2025-rd.png",
                  caption="Portada Digital 2025 RD con métricas de penetración internet 88.6% y dispositivos.",
                  source="DataReportal · 2025",
                  url="https://datareportal.com/reports/digital-2025-dominican-republic"),
             dict(png="macro-1-1-konvoy-latam-gig-economy.png",
                  caption="Newsletter Konvoy: logos gig LATAM (Rappi, Uber, iFood) y market share ride-hailing 2019-2022.",
                  source="Konvoy VC · 2025",
                  url="https://www.konvoy.vc/newsletters/latams-local-gig-economy"),
             dict(png="macro-1-1-tiktok-tag-emprenderdominicana.png",
                  caption="Hashtag #emprenderdominicana en TikTok — negocios dominicanos gestionados desde el teléfono.",
                  source="TikTok · 2026",
                  url="https://www.tiktok.com/tag/emprenderdominicana"),
         ]),

    # 1.2 — Ganar en dólares desde el cuarto
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="Ganar en dólares desde el cuarto: el joven LATAM se inventa una carrera sin oficina, sin empleador fijo y sin país que lo amarre.",
         fenomeno="La carrera tradicional asumía una empresa, una ciudad y un horario. El gig remoto cross-border rompió las tres. Las altas en plataformas freelance subieron 24% desde ciudades tier-2 y tier-3 en LATAM. Costa Rica, México y Colombia ya lanzaron visas de nómada digital de hasta un año.",
         hashtags="#nomadadigital · #cobroendolares · #trabajoremotord",
         triggers=[
             dict(stat="+24%",   desc="Altas en plataformas gig desde ciudades tier-2/tier-3 en LATAM y SE Asia.", source="HRStacks / Konvoy · 2025"),
             dict(stat="#1",     desc="Workana se consolida como plataforma freelance líder para nómadas en Sudamérica.", source="GigExchange / Holafly · 2025"),
             dict(stat="1 año",  desc="Costa Rica, México y Colombia lanzan visas de nómada digital de hasta 1 año.", source="Holafly · 2025"),
         ],
         signals=[
             dict(png="macro-1-2-tiktok-tag-nomadadigital.png",
                  caption="Hashtag #nomadadigital en TikTok — lifestyle remoto y trabajo desde cualquier país.",
                  source="TikTok · 2026",
                  url="https://www.tiktok.com/tag/nomadadigital"),
             dict(png="macro-1-2-hrstacks-gig-statistics.png",
                  caption="Estadísticas gig economy HRStacks — crecimiento freelance +24% desde ciudades secundarias.",
                  source="HRStacks · 2025",
                  url="https://www.hrstacks.com/gig-economy-freelance-work-statistics/"),
             dict(png="macro-1-2-holafly-nomada-digital-latam.png",
                  caption="Artículo Holafly sobre plataformas de trabajo remoto y visas de nómada digital LATAM.",
                  source="Holafly · 2025",
                  url="https://esim.holafly.com/digital-nomad/digital-nomad-jobs/"),
         ]),

    # 1.3 — El teléfono fijo se murió sin que nadie lo llorara
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="El teléfono fijo se murió sin que nadie lo llorara: hoy se forma un hogar y nadie pregunta dónde se pone la línea.",
         fenomeno="Inaugurar la adultez poniendo la línea fija era un rito del siglo XX. Ese rito desapareció sin reemplazo simbólico. El landline se extingue globalmente y los hogares jóvenes nacen mobile-only. INDOTEL reporta +24% en uso de internet móvil en RD. WhatsApp pasó a ser la infraestructura de comunicación del hogar.",
         hashtags="#sintelefonofijo · #soloWhatsApp · #conectividadrd",
         triggers=[
             dict(stat="+24%",   desc="Uso de internet móvil en RD (INDOTEL); conectividad 100% móvil-céntrica.", source="INDOTEL · 2025"),
             dict(stat="6.2%",   desc="De hogares RD conserva teléfono fijo — nadie está reponiéndolo.", source="Código Casa · 2025"),
             dict(stat="2026",   desc="El landline se extingue globalmente; hogares jóvenes nacen mobile-only.", source="Microsoft On the Issues · ene 2026"),
         ],
         signals=[
             dict(png="macro-1-3-indotel-conectividad-movil-24.png",
                  caption="Nota oficial INDOTEL sobre +24% uso internet móvil en RD — fuente primaria local.",
                  source="INDOTEL · 2025",
                  url="https://indotel.gob.do/indotel-revela-incremento-en-los-niveles-de-conectividad-fija-y-movil-en-la-republica-dominicana-un-aumento-de-un-24-en-uso-de-internet-movil-en-rd/"),
             dict(png="macro-1-3-microsoft-ai-economy-mobile.png",
                  caption="Blog Microsoft 2026: análisis adopción global de IA y brecha digital por conectividad móvil.",
                  source="Microsoft On the Issues · ene 2026",
                  url="https://blogs.microsoft.com/on-the-issues/2026/01/08/global-ai-adoption-in-2025/"),
             dict(png="macro-1-3-mercadolibre-rd-celulares.png",
                  caption="Celulares en MercadoLibre RD — el mercado móvil que reemplazó al teléfono fijo.",
                  source="MercadoLibre RD · 2025",
                  url="https://www.mercadolibre.com.do"),
         ]),

    # 1.4 — Saber promptear es la nueva alfabetización
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="Saber promptear es la nueva alfabetización: la brecha ya no es tener internet, es manejar la IA. El que no la usa queda marcado como atrasado.",
         fenomeno="Antes la competencia adulta se medía en leer, después en usar Excel. Ahora la frontera se corre a la IA. Microsoft describe una brecha digital que se ensancha entre quien domina la IA y quien no. Ya hay +122M de personas usando herramientas gen-AI cada día. En RD, INDOTEL adjudicó capacitación digital para 100,000 beneficiarios.",
         hashtags="#aprenderIA · #habilidadesdigitales · #upskilling",
         triggers=[
             dict(stat="+122M",  desc="Personas usan herramientas gen-AI cada día; 1 de cada 6 globalmente.", source="DemandSage · 2026"),
             dict(stat="100K",   desc="Beneficiarios INDOTEL en capacitación de habilidades digitales en RD.", source="INDOTEL Plan Bianual 2025-2026"),
             dict(stat="2026",   desc="La adopción de IA abre brecha digital que se ensancha entre quien la domina y quien no.", source="Microsoft On the Issues · ene 2026"),
         ],
         signals=[
             dict(png="macro-1-4-tiktok-tag-aprendia.png",
                  caption="Hashtag #aprendia en TikTok — grid de videos sobre aprendizaje de IA en español.",
                  source="TikTok · 2026",
                  url="https://www.tiktok.com/tag/aprendia"),
             dict(png="macro-1-4-demandsage-genai-statistics.png",
                  caption="Dashboard DemandSage: +122M usuarios diarios gen-AI, 1 de cada 6 personas globalmente.",
                  source="DemandSage · 2026",
                  url="https://www.demandsage.com/generative-ai-statistics/"),
             dict(png="macro-1-4-indotel-capacitacion-digital.png",
                  caption="Sección INDOTEL acceso e infraestructura — Plan Bianual 2025-2026, capacitación 100K beneficiarios.",
                  source="INDOTEL · 2025",
                  url="https://indotel.gob.do/acceso-e-infraestructura/"),
         ]),

    # 1.5 — La consola murió de pie en la sala
    dict(macro_n=M1_N, macro_name=M1_NAME,
         headline="La consola murió de pie en la sala: el ocio adulto se mudó del living al teléfono en la cama, y el cuarto de juegos familiar dejó de ser algo que se aspira.",
         fenomeno="La consola más la TV grande marcaban el hogar acomodado. Ese centro de ocio se desarmó. Menos del 10% de hogares LATAM tiene consola next-gen; el gaming se volvió íntimo, móvil y constante. El mercado gaming LATAM cerró 2025 en US$25.7B con el mobile dominando.",
         hashtags="#mobilegaming · #gamerrd · #jugardesdeelcelular",
         triggers=[
             dict(stat="US$25.7B", desc="Mercado gaming LATAM en 2025; el mobile dominó por adopción de smartphone sobre consola.", source="MarketDataForecast · 2025"),
             dict(stat="<10%",   desc="De hogares LATAM posee consola next-gen; 300M+ gamers, casi todos móviles.", source="LAVGA / Terra · 2025"),
             dict(stat="89.9%",  desc="De jugadores brasileños que topan con juegos monetizados pagan al menos una vez.", source="Pesquisa Game Brasil · 2025"),
         ],
         signals=[
             dict(png="macro-1-5-tiktok-tag-mobilegaming.png",
                  caption="Hashtag #mobilegaming en TikTok — gameplay móvil dominante en LATAM.",
                  source="TikTok · 2026",
                  url="https://www.tiktok.com/tag/mobilegaming"),
             dict(png="macro-1-5-marketdataforecast-latam-videogames.png",
                  caption="Reporte MarketDataForecast: gaming LATAM US$25.7B con mobile dominante sobre consola.",
                  source="MarketDataForecast · 2025",
                  url="https://www.marketdataforecast.com/market-reports/latin-america-video-game-market"),
             dict(png="macro-1-5-terra-latam-gaming-market.png",
                  caption="Análisis Terra LATAM gaming market — breakdown plataformas: consola <10%, mobile líder.",
                  source="Terra Localizations · jul 2025",
                  url="https://terralocalizations.com/2025/07/03/latin-american-gaming-market-power/"),
         ]),

    # ── Macro 2 ──────────────────────────────────────────────────────────────
    # 2.1 — El banco real ya no tiene edificio
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="El banco real ya no tiene edificio: cientos de miles de dominicanos mueven toda su plata desde una app y a eso no le llaman fintech, le llaman normal.",
         fenomeno="La banca era un edificio al que ibas. Dejó de serlo. Neobancos como Qik y wallets como tPago volvieron la app el banco principal de cientos de miles de dominicanos: Qik superó 600,000 clientes, tPago 556,000, y la banca digital RD creció 20% interanual.",
         hashtags="#qikrd · #pagocontelefono · #neobanco",
         triggers=[
             dict(stat="600K",   desc="Clientes Qik; tPago 556,000 registrados; banca digital RD +20% interanual.", source="Global Finance / FinTech Times · 2026"),
             dict(stat="US$7.91B", desc="Pagos digitales RD proyectados para 2028, creciendo 9.07% anual.", source="Statista · 2024-2028"),
             dict(stat="50+",    desc="Fintechs operando en RD (vs 20 en 2018) con respaldo regulatorio del BCRD.", source="Global Finance · 2025"),
         ],
         signals=[
             dict(png="macro-2-1-fintechtimes-rd-2026.png",
                  caption="FinTech Times: foto aérea Santo Domingo + 'Fintech Landscape of the Dominican Republic in 2026'.",
                  source="The FinTech Times · 2026",
                  url="https://thefintechtimes.com/fintech-landscape-of-the-dominican-republic-in-2026/"),
             dict(png="macro-2-1-statista-digital-payments-rd.png",
                  caption="Dashboard Statista: proyección pagos digitales RD a US$7.91B con chart 2018-2030.",
                  source="Statista · 2025",
                  url="https://www.statista.com/outlook/dmo/fintech/digital-payments/dominican-republic"),
             dict(png="macro-2-1-tiktok-tag-qikrd.png",
                  caption="Hashtag #qikrd en TikTok — onboarding y demos cotidianas de pago móvil dominicano.",
                  source="TikTok · 2026",
                  url="https://www.tiktok.com/tag/qikrd"),
         ]),

    # 2.2 — El cuerpo de la familia se volvió un panel de datos
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="El cuerpo de la familia se volvió un panel de datos: el reloj cuenta el sueño y los pasos, y la consulta médica pasó a ser una videollamada.",
         fenomeno="La salud entraba al hogar como cita: ibas al doctor. El wearable la convirtió en métrica que vive en la muñeca. El mercado de dispositivos médicos wearables va hacia US$499.2B en 2035 (CAGR 21.6%). En LATAM hay demanda alta de smartwatches por urbanización y conciencia de salud.",
         hashtags="#smartwatch · #telemedicina · #saluddigital",
         triggers=[
             dict(stat="US$499B", desc="Mercado wearables médicos para 2035, CAGR 21.6% — de nicho a consumer health.", source="MarketsandMarkets / PRNewswire · 2025"),
             dict(stat="LATAM",  desc="Philips despliega biosensores cardíacos post-alta en Argentina; teleconsulta masiva Colombia y Brasil.", source="MarketDataForecast LATAM · 2025"),
             dict(stat="21.6%",  desc="CAGR del mercado wearables médicos — demanda LATAM por urbanización y salud.", source="Maximize Market Research · 2025"),
         ],
         signals=[
             dict(png="macro-2-2-prnewswire-wearables-499b.png",
                  caption="PRNewswire: mercado wearables médicos US$499.2B para 2035, CAGR 21.6%, con pie chart de segmentación.",
                  source="MarketsandMarkets via PRNewswire · 2025",
                  url="https://www.prnewswire.com/news-releases/wearable-medical-devices-market-poised-for-usd-499-2-billion-by-2035--growing-at-a-cagr-21-6--strategic-insights-for-cxos-and-healthcare-leaders-302579862.html"),
             dict(png="macro-2-2-marketdataforecast-latam-digital-health.png",
                  caption="Reporte salud digital LATAM — telesalud y wearables, crecimiento y actores clave en la región.",
                  source="MarketDataForecast · 2025",
                  url="https://www.marketdataforecast.com/market-reports/latin-america-digital-health-market"),
             dict(png="macro-2-2-maximize-latam-wearables.png",
                  caption="Reporte wearables LATAM: charts de segmentación por producto y geografía, CAGR por mercado.",
                  source="Maximize Market Research · 2025",
                  url="https://www.maximizemarketresearch.com/market-report/wearable-medical-devices-market-latin-america/2245/"),
         ]),

    # 2.3 — La casa empezó a tener oídos
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="La casa empezó a tener oídos: cámaras, bombillos y bocinas con voz entran al hogar urbano LATAM, y el dueño la maneja desde el sofá hablándole en voz alta.",
         fenomeno="El smart home era lujo gringo de película. Dejó de serlo. Cámaras, bombillos, cerraduras y bocinas con voz entran a hogares urbanos LATAM por seguridad y por status: el mercado va de US$3.4B (2025) a US$8.2B+, y 45% de hogares urbanos de clase media ya compró un producto smart.",
         hashtags="#smarthome · #alexarutina · #domotica",
         triggers=[
             dict(stat="US$3.4B", desc="Smart home LATAM en 2025, camino a US$8.2B+; 45% hogares urbanos clase media ya compró un smart device.", source="IMARC / NextMSC · 2025"),
             dict(stat="+38%",   desc="México lidera la región con +38% interanual en ventas de dispositivos conectados.", source="NextMSC · 2025"),
             dict(stat="90.8%",  desc="Penetración de smart home en hogares sudamericanos llegará a 90.8% en 2029.", source="Statista · 2026"),
         ],
         signals=[
             dict(png="macro-2-3-statista-smarthome-southamerica.png",
                  caption="Dashboard Statista Smart Home Sudamérica: Revenue 2018-2029 por segmento, proyección 90.8% penetración.",
                  source="Statista Market Insights · abr 2026",
                  url="https://www.statista.com/outlook/cmo/smart-home/south-america"),
             dict(png="macro-2-3-imarc-smart-home-latam.png",
                  caption="Reporte IMARC smart home LATAM: market overview US$3.4B 2025, 45% hogares urbanos.",
                  source="IMARC Group · 2025",
                  url="https://www.imarcgroup.com/latin-america-smart-home-market"),
             dict(png="macro-2-3-nextmsc-mexico-smarthome.png",
                  caption="Reporte NextMSC smart home México: +38% interanual en ventas de dispositivos conectados.",
                  source="NextMSC · 2025",
                  url="https://www.nextmsc.com/report/mexico-smart-home-market"),
         ]),

    # 2.4 — Llega el momento incómodo: ya no le pides a la IA que recomiende
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="Llega el momento incómodo: ya no le pides a la IA que recomiende, le pides que compre. Rufus ejecuta solo al precio objetivo y el humano solo pone las reglas.",
         fenomeno="La IA recomendaba; tú decidías y comprabas. Esa frontera se está cruzando. Rufus llegó a 250M usuarios al mes (+140% interanual) y ahora compra autónomamente al precio objetivo. El reto medible es la confianza: 48% confiaría en IA para recomendar productos, pero solo 20% para que compre por ellos.",
         hashtags="#agenticAI · #compraautomatica · #shoppingbot",
         triggers=[
             dict(stat="250M",   desc="Usuarios/mes de Rufus, +140% interanual; ahora compra autónomamente al precio objetivo.", source="AWS / NovaData · 2026"),
             dict(stat="48%",    desc="Confiaría en IA para recomendar productos — pero solo 20% para que compre. El 28% es el campo de batalla.", source="AI Trends Study 2026 (n=1,037)"),
             dict(stat="2026",   desc="OpenAI lanza Operator (clic/scroll/orden) con eBay, Instacart, Etsy; Amazon pivota Alexa a compra agéntica.", source="CNBC · may 2026"),
         ],
         signals=[
             dict(png="macro-2-4-novadata-rufus-250m.png",
                  caption="NovaData: Rufus 250M usuarios/mes y auto-compra al precio objetivo — hero visual de producto Amazon.",
                  source="NovaData · 2025",
                  url="https://novadata.io/resources/news/amazon-rufus-agentic-auto-buy-250-million-users"),
             dict(png="macro-2-4-forrester-agentic-commerce.png",
                  caption="Forrester: 'Power Couple OpenAI + Amazon' — brecha de confianza 48%/20% en agentic commerce.",
                  source="Forrester · mar 2026",
                  url="https://www.forrester.com/blogs/power-couple-openai-amazon-may-have-just-won-consumer-agentic-commerce/"),
             dict(png="macro-2-4-cnbc-amazon-alexa-shopping-agent.png",
                  caption="CNBC: Amazon abandona Rufus chatbot en favor de Alexa Shopping Agent — compra agéntica.",
                  source="CNBC · may 2026",
                  url="https://www.cnbc.com/2026/05/13/amazon-ditches-rufus-ai-chatbot-in-favor-of-alexa-shopping-agent.html"),
         ]),

    # 2.5 — Los padres son los power users que nadie vio venir
    dict(macro_n=M2_N, macro_name=M2_NAME,
         headline="Los padres son los power users que nadie vio venir: usan ChatGPT más que quien no tiene hijos, y no para la tarea, sino para el menú, los berrinches y sus propias emociones.",
         fenomeno="ChatGPT empezó haciendo la tarea escolar. Terminó copilotando el hogar. Un estudio de OpenAI con Harvard reporta que 79% de padres usa IA frente a 54% de no-padres. Lo que hacen es concreto: planear comidas, redactar la lista del súper, manejar un berrinche, gestionar sus propias emociones.",
         hashtags="#chatgptmama · #IAenlacasa · #parentingAI",
         triggers=[
             dict(stat="79%",    desc="De padres usa IA vs 54% de no-padres; uso no laboral pasó de 53% (jun-2024) a +70% (2025).", source="OpenAI + Harvard (Deming) · sept 2025"),
             dict(stat="5.8%",   desc="Brasil concentra 5.8% del uso global de ChatGPT; México 4.1%, Colombia 1.6% — LATAM activo.", source="DemandSage · 2026"),
             dict(stat="2026",   desc="Padres usan ChatGPT para planear comidas, listas de súper, berrinches y gestión emocional.", source="Boston Globe / CNBC · 2026"),
         ],
         signals=[
             dict(png="macro-2-5-bostonglobe-ai-parenthood-79.png",
                  caption="Boston Globe Magazine: fotografía editorial y dato 79% de padres usa IA vs 54% no-padres.",
                  source="The Boston Globe Magazine · ene 2026",
                  url="https://www.bostonglobe.com/2026/01/14/magazine/ai-tools-modern-parenthood/"),
             dict(png="macro-2-5-cnbc-ai-parenting-chatbots.png",
                  caption="CNBC: padres usando chatbots para crianza — comidas, berrinches y gestión emocional.",
                  source="CNBC · ene 2026",
                  url="https://www.cnbc.com/2026/01/22/when-how-to-use-ai-chatbots-for-parenting-advice-researcher.html"),
             dict(png="macro-2-5-demandsage-chatgpt-latam.png",
                  caption="DemandSage: estadísticas ChatGPT 2026 con datos LATAM — Brasil 5.8%, México 4.1% del uso global.",
                  source="DemandSage · 2026",
                  url="https://www.demandsage.com/chatgpt-statistics/"),
         ]),

    # ── Macro 3 ──────────────────────────────────────────────────────────────
    # 3.1 — El feed se volvió góndola
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="El feed se volvió góndola: en LATAM el lo vi y lo compré ahí mismo corre a US$20B y reemplaza la lista de compras por el haul de impulso.",
         fenomeno="La compra arrancaba con una lista. Ahora arranca con un scroll. TikTok Shop convierte el feed en góndola sin fricción — belleza, hogar, accesorios — y ya es ~20% del social commerce. En LATAM los usuarios pasan +70 min/día en la app y el social commerce se proyecta a US$172.4B en 2025.",
         hashtags="#tiktokmehizocomprar · #tiktokshop · #haul",
         triggers=[
             dict(stat="~20%",   desc="TikTok Shop del social commerce en 2025 — el feed como góndola sin fricción.", source="EMARKETER · 2025"),
             dict(stat="+70 min", desc="Usuarios LATAM en TikTok por día; categorías top: belleza, skincare, accesorios, hogar.", source="Awisee · 2025"),
             dict(stat="US$172B", desc="Social commerce LATAM en 2025; +60% sigue influencers que recomiendan o venden.", source="GlobeNewswire / Galileo · 2026"),
         ],
         signals=[
             dict(png="macro-3-1-emarketer-tiktokshop-20pct.png",
                  caption="EMARKETER: bar chart 'TikTok Shop Retail Ecommerce Sales US 2023-2027' — ~20% del social commerce.",
                  source="EMARKETER · 2025",
                  url="https://www.emarketer.com/press-releases/tiktok-shop-makes-up-nearly-20-of-social-commerce-in-2025/"),
             dict(png="macro-3-1-awisee-tiktokshop-latam.png",
                  caption="Awisee: TikTok Shop en LATAM — hero con categorías top (belleza, hogar, accesorios).",
                  source="Awisee · 2025",
                  url="https://awisee.com/blog/tiktok-shop-in-latin-america/"),
             dict(png="macro-3-1-tiktok-tag-tiktokmehizocomprar.png",
                  caption="Hashtag #tiktokmehizocomprar en TikTok — el haul de impulso como comportamiento masivo.",
                  source="TikTok · 2026",
                  url="https://www.tiktok.com/tag/tiktokmehizocomprar"),
         ]),

    # 3.2 — Tu hijo ya tiene un mejor amigo que nunca lo contradice
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="Tu hijo ya tiene un mejor amigo que nunca lo contradice: 72% de adolescentes usó un compañero de IA y 1 de cada 4 le confía secretos reales. La familia compite por su intimidad con un chatbot.",
         fenomeno="El confidente del adolescente era un amigo, un hermano, a veces un padre. Llegó un competidor diseñado para nunca contradecirlo. 72% de adolescentes ya usó compañeros de IA; 23% les confía bastante o completamente; 25% comparte nombre, ubicación y secretos reales.",
         hashtags="#characterai · #aicompanion · #aifriend",
         triggers=[
             dict(stat="72%",    desc="De adolescentes usó compañeros de IA; 23% les confía bastante/completamente; 25% comparte datos reales.", source="Common Sense Media · jul 2025 (n=1,060)"),
             dict(stat="33%",    desc="De adolescentes prefiere hablar con IA que con personas para temas serios.", source="Common Sense Media · 2025"),
             dict(stat="2026",   desc="Demandas contra Character.AI por daño emocional a menores; APA alerta reformateo del vínculo afectivo.", source="Axios / APA · 2026"),
         ],
         signals=[
             dict(png="macro-3-2-commonsense-ai-companions-72pct.png",
                  caption="Common Sense Media: 'Nearly 3 in 4 Teens Have Used AI Companions' — hallazgos clave del estudio n=1,060.",
                  source="Common Sense Media · jul 2025",
                  url="https://www.commonsensemedia.org/press-releases/nearly-3-in-4-teens-have-used-ai-companions-new-national-survey-finds"),
             dict(png="macro-3-2-commonsense-ai-companions-report.png",
                  caption="Reporte completo Common Sense Media sobre AI companions — datos de confianza y uso regular de adolescentes.",
                  source="Common Sense Media · 2025",
                  url="https://www.commonsensemedia.org/press-releases/nearly-3-in-4-teens-have-used-ai-companions-new-national-survey-finds"),
             dict(png="macro-3-2-tiktok-tag-characterai.png",
                  caption="Hashtag #characterai en TikTok — adolescentes mostrando sus conversaciones con AI companions.",
                  source="TikTok · 2026",
                  url="https://www.tiktok.com/tag/characterai"),
         ]),

    # 3.3 — El feed reemplazó a la abuela como autoridad
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="El feed reemplazó a la abuela como autoridad: lo que se cocina y cómo se cría lo dicta la pantalla, y después se cruza con ChatGPT para confirmarlo.",
         fenomeno="La autoridad de cómo cocinar y criar venía de la abuela, de la madre, de la tradición. Se mudó al feed. Las recetas virales, los 'what I feed my kid' y los consejos de crianza del scroll reemplazan a la transmisión familiar. 15% de consumidores globales compra un producto solo porque es tendencia en TikTok.",
         hashtags="#recetatiktok · #whatmykideats · #cocinaviral",
         triggers=[
             dict(stat="79%",    desc="De padres usa IA para planear comidas y crianza — el feed + ChatGPT como co-autoridad doméstica.", source="OpenAI + Harvard · 2025"),
             dict(stat="15%",    desc="De consumidores globales compra productos solo porque son tendencia en TikTok.", source="SAP Emarsys · 2025"),
             dict(stat="Top",    desc="Hogar y comida entre las categorías top de TikTok Shop LATAM; recetas y crianza dominan el feed.", source="Awisee · 2025"),
         ],
         signals=[
             dict(png="macro-3-3-bostonglobe-feed-crianza.png",
                  caption="Boston Globe Magazine: padres usando IA para planear comidas y crianza — el feed como co-autoridad.",
                  source="The Boston Globe Magazine · ene 2026",
                  url="https://www.bostonglobe.com/2026/01/14/magazine/ai-tools-modern-parenthood/"),
             dict(png="macro-3-3-awisee-feed-recetas-hogar.png",
                  caption="Awisee: categorías top de TikTok Shop LATAM — hogar y comida entre las principales.",
                  source="Awisee · 2025",
                  url="https://awisee.com/blog/tiktok-shop-in-latin-america/"),
             dict(png="macro-3-3-tiktok-tag-recetatiktok.png",
                  caption="Hashtag #recetatiktok en TikTok — recetas virales que reemplazan la transmisión culinaria familiar.",
                  source="TikTok · 2026",
                  url="https://www.tiktok.com/tag/recetatiktok"),
         ]),

    # 3.4 — El mismo feed que vende también estafa
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="El mismo feed que vende también estafa: el phishing por WhatsApp y los esquemas cripto entran por el grupo familiar y van directo a los mayores.",
         fenomeno="La infraestructura digital del hogar es también su superficie de ataque más vulnerable. LATAM subió 108% interanual en amenazas cibernéticas en Q1 2025. Meta desactivó ~8M de cuentas ligadas a centros de estafa. En grupos públicos de WhatsApp latinos circularon 3,000+ mensajes fraudulentos alcanzando 192,000+ usuarios.",
         hashtags="#estafawhatsapp · #fraudedigital · #ciberseguridadrd",
         triggers=[
             dict(stat="+108%",  desc="LATAM interanual en amenazas cibernéticas (Q1 2025); ingeniería social vía phishing como driver.", source="Industrial Cyber · 2025"),
             dict(stat="~8M",    desc="Cuentas desactivadas por Meta ligadas a centros de estafa que apuntan a personas mayores.", source="The Hacker News / Malwarebytes · 2025"),
             dict(stat="3K+",    desc="Mensajes fraudulentos en grupos públicos de WhatsApp latinos (ene-sept 2025), 192,000+ usuarios alcanzados.", source="DDIA · 2025"),
         ],
         signals=[
             dict(png="macro-3-4-industrialcyber-latam-phishing.png",
                  caption="Industrial Cyber: incremento ransomware y phishing en LATAM +108% Q1 2025 — hero gráfico '1 in 3'.",
                  source="Industrial Cyber · 2025",
                  url="https://industrialcyber.co/reports/latin-america-sees-sharp-rise-in-ransomware-hacktivist-attacks-in-2025-amid-expanding-fraud-and-phishing-threats/"),
             dict(png="macro-3-4-hackernews-meta-scam-tools.png",
                  caption="The Hacker News: Meta desactiva 8M cuentas de estafa y lanza herramientas de protección para mayores.",
                  source="The Hacker News · oct 2025",
                  url="https://thehackernews.com/2025/10/meta-rolls-out-new-tools-to-protect.html"),
             dict(png="macro-3-4-ddia-whatsapp-scam-latinos.png",
                  caption="DDIA: 3,000+ mensajes fraudulentos en grupos WhatsApp latinos — investigación sobre estafas a adultos mayores.",
                  source="DDIA · 2025",
                  url="https://ddia.org/en/whatsapp-weaponized-how-scammers-target-us-latinos-part3"),
         ]),

    # 3.5 — El niño vive en el feed y la barrera llega tarde
    dict(macro_n=M3_N, macro_name=M3_NAME,
         headline="El niño vive en el feed y la barrera llega tarde: solo la mitad de los padres usa controles parentales, y la familia descubre después qué consumió el hijo.",
         fenomeno="La preocupación por las pantallas es alta; el uso de controles, bajo. Solo 51% de padres usa controles parentales en tablets, 47% en smartphones y 35% en consolas. En RD, 89% de usuarios de internet accede a redes diariamente en un país con 88.6% de penetración: el menor accede al algoritmo temprano y poco mediado.",
         hashtags="#controlparental · #crianzadigital · #screentime",
         triggers=[
             dict(stat="51%",    desc="De padres usa controles parentales en tablets; 47% en smartphones; 35% en consolas.", source="FOSI · 2025"),
             dict(stat="89%",    desc="De usuarios de internet en RD accede a redes sociales diariamente — exposición infantil temprana.", source="DataReportal · 2025"),
             dict(stat="26.4%",  desc="De hogares RD no usa ningún mecanismo de protección infantil digital.", source="Código Casa · 2025"),
         ],
         signals=[
             dict(png="macro-3-5-fosi-parental-controls-51pct.png",
                  caption="FOSI 2025: controles parentales subutilizados — datos clave 51% tablets, 47% smartphones, 35% consolas.",
                  source="FOSI · 2025",
                  url="https://fosi.org/parental-controls-for-online-safety-are-underutilized-new-study-finds/"),
             dict(png="macro-3-5-apa-screentime-children.png",
                  caption="APA: press release vinculando screen time con problemas emocionales infantiles en círculo vicioso.",
                  source="APA · jun 2025",
                  url="https://www.apa.org/news/press/releases/2025/06/screen-time-problems-children"),
             dict(png="macro-3-5-datareportal-rd-redes-diario.png",
                  caption="DataReportal Digital 2025 RD: 89% accede a redes diariamente — contexto de exposición infantil.",
                  source="DataReportal · 2025",
                  url="https://datareportal.com/reports/digital-2025-dominican-republic"),
         ]),
]

if __name__ == "__main__":
    build_deck(DIVIDERS, MICROS, SCREENSHOTS, OUTPUT)
