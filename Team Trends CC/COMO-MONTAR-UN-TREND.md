# Cómo montar el Trend Forecast de un capítulo — Team Trends CC

Flujo de 4 agentes para producir el **Trend Forecast completo de un
capítulo Código Casa** = 3 macros × 5 micros = **15 micro-trends +
3 bloques macro = 18 piezas**. Replica el formato del MED Familia
e Identidad (líneas 1639-2151 del .txt original).

---

## Setup mínimo

Antes de arrancar definir:

1. **Capítulo** — uno de los 11 pilares canónicos Código Casa:
   `familia-identidad` · `bienestar` · `finanzas` · `alimentacion` ·
   `roles-genero` · `consumos` · `educacion` · `tecnologia` ·
   `creencias` · `opiniones-politicas` · `mujer`
2. **(Opcional) Foco temático** dentro del capítulo (ej. "Roles de
   Género con foco en masculinidad joven")
3. **Slug** kebab-case: `trends-{capitulo}` (ej. `trends-roles-genero`)

---

## Data estática (no se modifica)

`Agentes Trends/macrofuerzas-codigo-casa.md` — las 3 macros canónicas:
1. **INVENTOLOGÍA DE LA ADULTEZ** — *"Un mundo en crisis está
   reescribiendo qué significa ser adulto y formar familia."*
2. **LOS HERNÁNDEZ ARE PROMPTED** — *"El dominicano ya entró al mundo
   prompteado. Solo no lo nombra así."*
3. **ALGORITMO DEL HOGAR** — *"El feed se sentó en la mesa y nadie le
   ofreció silla."*

El hunter, el editor cultural y el montador **siempre** leen este
archivo antes de operar.

---

## Los 4 agentes en orden

### 1. `hunter-trends-cc` (opus)
- Lee `macrofuerzas-codigo-casa.md` (regla 0)
- Caza en GLOBAL + LATAM + RD (cada dato tag `[GLOBAL]`/`[LATAM]`/
  `[LOCAL · DOMINICAN PROOF]`)
- Freshness 2024+ (excepto `[HISTÓRICO · CONTRASTE]`)
- 5 micros × 3 macros = 15 micros + 3 bloques macro
- Tesis ≤250 chars por micro + bundle 6–10 señales por micro

→ Output: `outputs/trends-{capitulo}-hunter.md`

### 2. `scrapper-trends-cc` (sonnet)
- Verifica links de las 100+ señales candidatas
- Screenshots **W149pt × H220pt** (596×880px @3x)
- Naming: `screenshots/trends-{capitulo}/macro-{N}-{M}-{slug-señal}.png`

→ Output: `outputs/trends-{capitulo}-señales.md`
+ `screenshots/trends-{capitulo}/*.png`

### 3. `editor-cultural-cc` (opus)
- Lee `macrofuerzas-codigo-casa.md` para anclar taglines canónicos
- Aplica `voz-jeremy` + `humanizador-es` (obligatorios)
- Redacta 3 bloques macro (formato MED: comportamiento, triggers,
  contrast, transformation, ask yourself, 3 pruebas)
- Redacta 15 micros (formato MED: NOMBRE ≤190 chars + tagline +
  FENÓMENO + DATA Y SEÑALES + HASHTAGS + THE CONTRAST + 3 PRUEBAS +
  3 NEEDS)

→ Output: `outputs/trends-{capitulo}-editado.md`

### 4. `montador-trends-cc` (sonnet)
- Construye deck de **18 slides** (espejo MED Familia):
  - 3 slides intro macro (1 por macro)
  - 15 slides micro (3 columnas DS Código Casa)
- DS: fondo `#0D0D0D`, Instrument Serif 50pt UPPERCASE tracking 0
  para headlines, Poppins 8pt blanco line-spacing 1.0 para body,
  fotos 149×220pt con hyperlink + badge "Click me"

→ Outputs:
- `outputs/trends-{capitulo}-forecast.pptx`
- `outputs/trends-{capitulo}-forecast.pdf` (QA)
- `build_trends_{capitulo}.py` (script re-buildable)

---

## Slash command

```text
/flujo-trends {capitulo}
```

Ejemplos:
- `/flujo-trends roles-genero`
- `/flujo-trends familia-identidad`
- `/flujo-trends alimentacion`
- `/flujo-trends bienestar`

El command ejecuta los 4 pasos en orden con 3 checkpoints obligatorios
(validación hunter → validación scrapping → visto bueno antes de
montar).

---

## Estructura de carpetas

```
Agentes Trends/
├── COMO-MONTAR-UN-TREND.md          (este archivo)
├── DESIGN-SYSTEM-TRENDS.md          (DS completo Código Casa Trends)
├── macrofuerzas-codigo-casa.md      (DATA ESTÁTICA — no modificar sin OK)
├── hunter-trends-cc.md              (source agent)
├── scrapper-trends-cc.md            (source agent)
├── editor-cultural-cc.md            (source agent)
├── montador-trends-cc.md            (source agent)
├── outputs/
│   ├── trends-{capitulo}-hunter.md
│   ├── trends-{capitulo}-señales.md
│   ├── trends-{capitulo}-editado.md
│   ├── trends-{capitulo}-forecast.pptx
│   └── trends-{capitulo}-forecast.pdf
└── screenshots/
    └── trends-{capitulo}/
        ├── macro-1-0-{slug}.png   (bloque macro 1)
        ├── macro-1-1-{slug}.png   (micro 1.1)
        ├── macro-1-2-{slug}.png   (micro 1.2)
        ├── ...
        └── macro-3-5-{slug}.png   (micro 3.5)
```

---

## Reglas innegociables del flujo

- **Read obligatorio de `macrofuerzas-codigo-casa.md`** en hunter,
  editor cultural y montador. Sin eso no operan.
- **15 micros exactos** = 5 por macro. Ni 14 ni 16.
- **Cero macros nuevas.** Solo Inventología / Hernández Prompted /
  Algoritmo del Hogar.
- **Tag geo en cada dato:** `[LOCAL · DOMINICAN PROOF]` / `[LATAM]` /
  `[GLOBAL]` / `[TIKTOK]`.
- **Freshness 2024+** salvo `[HISTÓRICO · CONTRASTE]` en bloque
  "The contrast".
- **Cero invención.** Sin stat → `PENDIENTE`. Sin link → señal
  descartada. Sin verbatim FG → no se cita Código Casa.
- **Voz Jeremy + humanizador-es** aplicados en el editor cultural.
- **Outputs siempre en `Agentes Trends/outputs/`.**
