# Scrapper Playbook — Team Trends CC

> Learnings tácticos para que `scrapper-trends-cc` capture señales en
> **TikTok, AdAge y TrendWatching** usando la sesión autenticada del
> usuario en Chrome, sin caer en bloqueos ni romper ToS.
> Documento de referencia obligatoria para el scrapper.

---

## REGLA #1 (la más importante) — Cada screenshot apunta a un ELEMENTO VISUAL, no a texto

**El screenshot debe mostrar una imagen, gráfico, foto, frame de
video, infografía, producto, dashboard con métrica visible o ad
creative — NUNCA un párrafo de prosa en bloque.**

Si lo único que muestra el screenshot es texto justificado, está mal
capturado. El cliente abre el deck y ve una caja de letras donde
esperaba evidencia visual.

### Qué SÍ capturar por tipo de señal

| Tipo de señal | QUÉ capturar (visual obligatorio) |
|---------------|-----------------------------------|
| **Video TikTok / Reel / YouTube** | Frame del video con persona/escena visible. Usar `thumbnail_url` del oembed o frame al segundo 1-3. NO la página de comentarios |
| **Post Instagram** | La imagen/carousel del post. NO la caption ni comentarios |
| **Estudio Pew / McKinsey / OECD** | El **gráfico o infografía** del paper (bar/line/pie chart). Buscar la página del PDF con la viz. NO el abstract en prosa |
| **Noticia de prensa** | La **hero image** del artículo (foto editorial, retrato, escena), arriba del fold. NO los párrafos |
| **Reporte de industria (Statista, Grand View)** | El **gráfico/chart** del reporte. NO la tabla en texto |
| **Lanzamiento de marca / producto** | La **imagen del producto** o **ad creative**. NO el press release |
| **Hashtag TikTok con métricas** | La **página del hashtag con contador visible + grid de top videos**. NO solo el header con número |
| **Innovation card TrendWatching** | La **card visual con imagen + número + label**. NO el body expandido |
| **Caso de marca en AdAge** | El **still del comercial o lockup de campaña**. NO los párrafos de análisis |
| **Verbatim viral / tweet** | El **post completo con foto/avatar/UI**. NO solo el texto |
| **Dashboard / contador** | El widget con número grande + gráfica. NO una pantalla de texto |

### Qué NO capturar (rojo absoluto)

- ❌ Párrafos de texto sin imagen embebida
- ❌ Body de un artículo después del hero image
- ❌ Tabla HTML pura sin chart
- ❌ Lista de bullets sin viz
- ❌ Página de resultados de búsqueda con results en texto plano
- ❌ Comentarios o threads sin la imagen original del post
- ❌ Captions o descriptions sin la foto/video del post
- ❌ Headers de página con solo el título tipográfico (excepto si
  el título ES el statement visual, ver excepción abajo)

### Test del screenshot
Antes de guardar, pregúntate: **"¿Esta imagen funciona como ilustración
en una slide de 149×220pt sin necesidad de leer el contenido?"**
Si la respuesta es no → recapturas o descartas la señal.

### Cómo encontrar el visual cuando la fuente es texto-pesada

1. **Buscar la hero image del artículo** — casi todos los medios
   tienen foto destacada arriba. Capturar esa zona.
2. **Para papers/PDFs:** abrir y scrollear hasta encontrar la
   figura 1, figura 2, gráfico de barras, infografía. Capturar esa
   página completa.
3. **Para hashtags/métricas TikTok:** combinar header con número
   grande + grid visual de top videos. El número solo no convence;
   el grid de videos sí.
4. **Para marcas/productos:** ir a la página oficial del producto o
   a la newsroom con el ad still, no a la cobertura editorial.
5. **Para reportes (Statista, McKinsey, Grand View):** buscar la
   "data viz" o "charts" del report. Si el report es behind paywall,
   buscar la versión free preview que casi siempre tiene 1-2 charts.
6. **Para AdAge / Adweek artículos:** el hero del artículo casi
   siempre tiene un still de comercial o packshot. Capturar ese.

### Si la señal no tiene visual disponible
Si después de explorar la URL principal + 2 búsquedas alternativas no
encuentras un visual válido → **devolver la señal al hunter** con nota
`SIN VISUAL — buscar fuente alternativa`. **No capturar texto en bloque
como reemplazo.** Mejor 8 señales con visuales que 10 señales con
3 cajas de texto.

### Excepción legítima: tipografía monumental como visual
Si la señal es un **hero stat o manifesto tipográfico** donde el texto
grande ES el statement visual (billboard NYT que dice "60% IN 5 YEARS"
a tamaño completo, portada de revista con título dominante, pull quote
de un report a tipografía hero), capturarlo es válido — pero debe ser
**tipografía monumental que funcione visualmente**, NO un párrafo
justified.

---

## Principio operativo

**Chrome MCP > Bash scraping > Computer-use.**
El usuario ya tiene sesiones iniciadas en Chrome para AdAge,
TrendWatching y (opcionalmente) TikTok. El camino correcto es
**reutilizar esa sesión vía la extensión Chrome MCP**
(`mcp__Claude_in_Chrome__*`), no levantar headless Puppeteer/Playwright
nuevo. Eso resuelve el 90% de los problemas de login y reduce el
fingerprinting.

Si Chrome MCP no está conectado: pedir al usuario que active la
extensión antes de continuar. **No intentes**: (a) parsear cookies a
mano, (b) abrir headless Chromium, (c) usar APIs de terceros tipo
Bright Data sin OK del usuario. Es overkill para un flujo de ≤100
captures por capítulo.

---

## Cómo opera Chrome MCP en este flujo

Tools disponibles (deferred, cargar con `ToolSearch` query
`"claude-in-chrome"`):

| Tool | Cuándo |
|------|--------|
| `mcp__Claude_in_Chrome__list_connected_browsers` | Verificar que Chrome del usuario está conectado |
| `mcp__Claude_in_Chrome__navigate` | Abrir URL en pestaña |
| `mcp__Claude_in_Chrome__find` | Buscar elementos por texto / selector |
| `mcp__Claude_in_Chrome__get_page_text` / `read_page` | Leer contenido renderizado |
| `mcp__Claude_in_Chrome__read_network_requests` | Inspeccionar JSON cargado en background |
| `mcp__Claude_in_Chrome__resize_window` | Ajustar viewport a 596×880 px (ratio 149:220 @3x) |
| `mcp__Claude_in_Chrome__gif_creator` / screenshot via DevTools | Capturar imagen |

**Verificar antes de cada sesión:** llamar
`list_connected_browsers` para confirmar que Chrome del usuario está
ahí. Si no, pedir activar la extensión.

---

## AdAge (`adage.com`)

### Acceso
- Login por Google SSO con la cuenta del usuario.
- Una vez logueado en Chrome, el cookie `adage_session` queda 30 días.
  No expira en 24h como la mayoría de paywalls.
- La paywall es **soft** — el HTML completo del artículo se carga
  aunque no estés logueado, pero el CSS lo oculta. Estando logueado
  Chrome MCP ve el texto completo sin truco.

### Cómo buscar
1. URL de búsqueda directa:
   `https://adage.com/search?keywords={query}` (URL-encoded).
2. Filtros recomendados desde la propia UI:
   - **Date:** Last 12 months / Last 2 years
   - **Content type:** Article, News, Datacenter
3. Para temas concretos usar el slug de tag:
   `https://adage.com/tag/{slug}` (ej. `gen-z`, `tiktok`, `genai`,
   `family-marketing`).

### Capturar señal
- Abrir el artículo, esperar carga completa (`wait_for` selector
  `article`).
- Encuadrar la región del hero image + headline + dek + byline.
- Resize del viewport a 596 px de ancho × 880 px de alto antes del
  screenshot para forzar layout móvil (más limpio para el ratio
  149:220).
- Capturar y guardar como
  `screenshots/trends-{capitulo}/macro-{N}-{M}-adage-{slug}.png`.

### Anti-trampas
- **No** uses la versión `print/` ni `cached/` — pierden la
  identidad visual y el cliente cuando vea el deck no las reconoce.
- **No** capturas con la cookie banner visible. Hacer click en
  "Accept" antes de la captura. AdAge tiene cookie banner sticky
  inferior que arruina el screenshot si no se cierra.

---

## TrendWatching (`app.trendwatching.com`)

### Acceso
- Login propio (no Google SSO). Una vez logueado, sesión persiste
  ~14 días.
- Toda la app es SPA (React). El HTML inicial es vacío — hay que
  esperar a que el JS renderice. Usar `wait_for_selector` antes de
  leer/capturar.

### Cómo buscar
1. Dashboard de búsqueda en
   `https://app.trendwatching.com/search?q={query}`.
2. Categorías relevantes para Código Casa:
   - **Macro-trends** — corren paralelo a nuestras 3 macros
   - **Innovations** — feed de marcas con casos concretos (gold para
     señales de inversión)
   - **Hashtags & Signals** — útil para validar que un hashtag está
     siendo trackeado por TW
3. Filtros: región (Global / LATAM / Caribbean), date range,
   industry.

### Capturar señal
- Cada Innovation Card tiene formato vertical natural — el ratio
  149:220 sale casi limpio sin recorte.
- Capturar la card individual (no la lista completa).
- Si el contenido es "Premium Locked" para tu plan, marca la señal
  como `LOCKED` y devuélvela al hunter para sustituirla. No fuerces.

### Anti-trampas
- **No** descargues PDFs de reports completos como señal — el cliente
  ya tiene acceso, y reutilizar el PDF entero rompe el ToS de
  redistribución de TW.
- **Cita siempre** el título exacto del Innovation + fecha de
  publicación en el footer inline. TW exige attribution.

---

## TikTok (`tiktok.com`)

Este es el más sensible. Resumen de 2026:

- **TikTok no tiene API pública gratis** para terceros. La oficial
  (Display API) requiere aplicación de empresa.
- **Detección anti-bot ML-based:** canvas + WebGL fingerprinting,
  timing de scroll, mouse path. Bloqueos por IP/sesión tras pocas
  requests anónimas.
- **NO scrapear logueado** con la cuenta personal del usuario — riesgo
  real de ban permanente.

### Estrategia recomendada (low-risk, low-volume)

Estamos capturando ≤30-50 videos por capítulo. Es **bajo volumen** y
**uso editorial** (citamos + linkeamos al original). Esto cae en el
uso normal de un navegador humano. Tres reglas:

1. **Anónimo o cuenta separada.** Chrome MCP debe estar en una
   ventana sin login a TikTok (o con cuenta secundaria nunca usada
   para nada importante).
2. **Ritmo humano:** mínimo 5-10 segundos entre captures.
   Implementa con `wait` entre `navigate` calls.
3. **Captura la página pública, no descargues el video.** El
   deliverable es un screenshot — no necesitamos el archivo .mp4.

### URLs útiles

| Patrón | Uso |
|--------|-----|
| `https://www.tiktok.com/@{user}/video/{id}` | Video específico (del bundle del hunter) |
| `https://www.tiktok.com/tag/{hashtag}` | Página de hashtag — muestra views totales + top videos |
| `https://www.tiktok.com/discover/{topic}` | Página discover por tema |
| `https://www.tiktok.com/embed/v2/{video_id}` | Embed oficial — **menos detección que la página completa**, ideal para screenshot |
| `https://www.tiktok.com/oembed?url={url}` | Endpoint oembed (JSON con metadata pública, sin login) |

### Capturar señal de TikTok

Workflow recomendado:
1. **Validar el link** con `oembed`: hacer fetch a
   `https://www.tiktok.com/oembed?url={video_url}`.
   - Si devuelve JSON con `title`, `author_name`, `thumbnail_url`
     → el video existe y es público
   - Si 404 → el video se borró, marcar señal `DESCARTADA`
2. **Capturar imagen:** dos opciones, en orden:
   - **Opción A (preferida):** usar el `thumbnail_url` del oembed
     como base — es PNG/JPG hosted por TikTok, sin riesgo de
     detección. Descarga directa con `WebFetch` o `curl`.
   - **Opción B:** si necesitas el frame con el creator + caption
     visible, usar `mcp__Claude_in_Chrome__navigate` a la URL
     embed (`/embed/v2/`), esperar 3-5s, screenshot.
3. **Recortar al ratio 149:220** con `sips`:
   ```bash
   sips --cropToHeightWidth 880 596 raw.png --out final.png
   ```

### Hashtag pages para métricas

Cuando el hunter necesita `[TIKTOK] #livingalone 2.5B views`:
- Navegar `https://www.tiktok.com/tag/{hashtag}` con Chrome MCP
- Leer el contador de views del header
- Capturar la card del header (formato vertical natural)
- Las cifras de views están en el DOM como `data-e2e="challenge-vuser"`
  o texto plano — `find` + `get_page_text` funciona

### Anti-trampas TikTok

- **No** intentes "infinite scroll" en feed personal. Eso es señal
  fuerte de bot.
- **No** uses `tiktok-scraper` npm package ni Bright Data sin OK
  explícito de Jeremy.
- **Sí** prioriza el oembed endpoint para metadata — es público,
  oficial, y nunca falla por anti-bot.
- **No** captures contenido de menores visibles. Si el video muestra
  un niño identificable, descarta y marca `requiere reemplazo —
  contenido sensible`.

---

## Buenas prácticas transversales

### Naming de screenshots
```
screenshots/trends-{capitulo}/macro-{N}-{M}-{plataforma}-{slug-señal}.png
```
Ejemplos:
- `macro-1-1-tiktok-dogelthy-perrhijo.png`
- `macro-2-3-adage-amazon-rufus.png`
- `macro-3-2-trendwatching-sadbeige-card.png`

### Tamaño exacto del screenshot
- **Target:** 149pt × 220pt para PPT
- **Equivale a @3x retina:** 596 × 880 px
- **Comando de recorte (sips, macOS nativo, sin deps):**
  ```bash
  sips --cropToHeightWidth 880 596 input.png --out output.png
  ```
- **Si la fuente es horizontal (ej. tweet):** recortar al centro
  vertical. No estirar — pixela.

### Cierre de banners antes de capturar
Cookie banners arruinan el 30% de los screenshots si no se cierran.
Antes de cada captura:
```js
// vía Chrome MCP javascript_tool
['accept', 'agree', 'aceptar', 'close', 'got it', 'ok'].forEach(t => {
  document.querySelectorAll('button').forEach(b => {
    if (b.innerText.toLowerCase().includes(t)) b.click();
  });
});
```

### Verificación de freshness (regla 2024+)
Cada link verificado debe tener fecha visible. Si Chrome MCP no la
encuentra:
- Para artículos: buscar `<meta property="article:published_time">`
- Para TikTok: el oembed devuelve `upload_date`
- Si después de 2 intentos no se confirma fecha → señal marcada
  `requiere fecha — verificar manualmente`. **No asumir** que es
  reciente porque el URL parece nuevo.

### Ritmo entre captures
- AdAge / TrendWatching (autenticado): sin delay forzado, ritmo
  humano normal
- TikTok (anónimo): **mínimo 5s entre `navigate` calls**, mejor
  randomizar 5-12s

### Cuándo devolver al hunter
Devuelves la señal completa si:
- El link está roto y no hay equivalente verificable
- El contenido no carga sin login adicional
- La fecha es <2024 y el hunter no marcó `[HISTÓRICO · CONTRASTE]`
- Es contenido sensible (menores identificables, violencia gráfica)

No sustituyas por algo "parecido". Mejor descartar y que el hunter
ajuste el bundle.

---

## Tabla de decisión rápida

| Quiero capturar... | Plataforma | Herramienta primaria | Fallback |
|---|---|---|---|
| Artículo de marketing | AdAge / Adweek / Campaign | Chrome MCP autenticado | curl + cookies extraídas |
| Innovation card | TrendWatching | Chrome MCP autenticado | screenshot manual + paste |
| Video TikTok | TikTok | oembed thumbnail | Chrome MCP en `/embed/v2/` anónimo |
| Página de hashtag | TikTok | Chrome MCP anónimo | screenshot manual |
| Post Instagram | Instagram | Chrome MCP autenticado (post público) | oembed |
| Hilo Reddit | Reddit | WebFetch a URL `.json` | Chrome MCP |
| Producto e-commerce | Amazon / Chewy / etc | Chrome MCP anónimo | WebFetch |

---

## Qué NO está permitido (rojo absoluto)

- ❌ Levantar headless Chromium con perfil del usuario sin pedirlo
- ❌ Reusar cookies de Chrome del usuario en un script Python sin OK
- ❌ Scrapear TikTok logueado con la cuenta personal de Jeremy
- ❌ Descargar archivos de video (.mp4) — solo capturas de imagen
- ❌ Usar APIs de pago (Bright Data, Scrapfly) sin autorización
- ❌ Saltar paywalls con Archive.org o 12ft.io — usamos la sesión
  legítima
- ❌ Capturar contenido de menores identificables
- ❌ Redistribuir PDFs completos de reports de TrendWatching
