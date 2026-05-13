---
name: codigo-casa-data-viz
description: "Visualización avanzada de datos cuantitativos con Gestalt + Psicología del color. Genera 20+ tipos de gráficas SVG HTML/SVG desde CSV con insights automáticos, optimizado para Código Casa (estudios dominicanos)."
type: data-visualization
---

# Skill: Visualización Avanzada de Datos — Código Casa

Especializado en transformar tabulaciones cuantitativas (CSV) en visualizaciones HTML/SVG con data storytelling integrado. Incluye:

- **20+ tipos de gráficas** (Stacked Bar, Grouped Bar, Heatmap, Waterfall, Bullet, Slope, etc.)
- **Principios Gestalt aplicados** (proximidad, similitud, continuidad, cierre)
- **Psicología del color dominicana** (8-10 paletas sensibles culturalmente)
- **Jerarquía visual automática** (60-30-10 rule)
- **Insights automáticos** (say-do gaps, brechas generacionales, outliers)
- **Sensibilidad cultural** (contexto dominicano, NINJA Thinking)

## Estructura de Archivos

```
codigo-casa-data-viz/
├── SKILL.md                      # Documentación (este archivo)
├── data/
│   ├── chart-types.csv          # Tipos de gráficas (20+)
│   ├── dominican-palettes.csv   # Paletas culturales
│   ├── gestalt-rules.csv        # Principios Gestalt
│   ├── color-psychology.csv     # Psicología del color
│   ├── hierarchy-patterns.csv   # Jerarquía visual
│   ├── data-patterns.csv        # Patrones de datos Código Casa
│   ├── tension-indicators.csv   # Indicadores de tensión
│   └── cultural-sensitivity.csv # Guías culturales
├── scripts/
│   ├── core.py                  # Motor BM25 + utilities
│   ├── data_analyzer.py         # Análisis automático de datos
│   ├── chart_generator.py       # Generador SVG
│   ├── gestalt_applier.py       # Aplicación Gestalt
│   ├── color_recommender.py     # Recomendador de colores
│   ├── insight_extractor.py     # Extracción de insights
│   ├── search.py                # CLI principal
│   └── html_exporter.py         # Exportador HTML
├── templates/
│   ├── chart-templates/         # Templates SVG por tipo
│   ├── report-template.html     # Layout base
│   └── styles.css               # Estilos
└── examples/
    ├── sample-data/             # Datos de ejemplo
    └── generated-reports/       # Reportes generados
```

## Cómo Usar

### Uso Básico: Recomendar Gráfica

```bash
python3 scripts/search.py "multirespuesta generacional NSE" --chart-recommend
```

**Output:** Top 3 gráficas recomendadas + paleta + jerarquía visual

### Uso Intermedio: Generar Gráfica Individual

```bash
python3 scripts/search.py "Identidad jóvenes" \
  --chart-recommend \
  --pilar "Identidad" \
  --input "datos-identidad.csv" \
  --output "reports/identidad-tension-01.html"
```

**Output:** HTML con gráfica SVG incrustada + insights automáticos

### Uso Avanzado: Batch de Gráficas

```bash
python3 scripts/batch_generator.py \
  --input "codigo-casa-data.csv" \
  --output-dir "reports/" \
  --include-insights \
  --format "html+svg"
```

**Output:** Carpeta `reports/` con 30-40 gráficas organizadas por pilar/tensión

## Estructura de Entrada (CSV)

### Formato Esperado

```csv
tension,descripcion,categoria,edad_18_24,edad_25_34,edad_35_plus,nse_e,nse_d,nse_c,nse_c_plus,sexo_m,sexo_f,n,notas
"Estrés financiero","¿Sientes estrés financiero?","Emoción",76.2%,68.5%,52.3%,84%,79%,61%,38%,71%,73%,500,"Multirespuesta"
```

### Columnas Obligatorias

- `tension` — ID de tensión (ej: "Estrés financiero")
- `descripcion` — Pregunta original
- `categoria` — Tipo de dato (Emoción, Conducta, Conocimiento, etc.)

### Columnas Dinámicas (Dimensiones)

- Edad: `edad_18_24`, `edad_25_34`, `edad_35_plus`
- NSE: `nse_e`, `nse_d`, `nse_c`, `nse_c_plus`
- Sexo: `sexo_m`, `sexo_f`
- O cualquier otra dimensión de cruce

### Columnas Opcionales

- `n` — Tamaño de muestra
- `notas` — Contexto (ej: "Say-Do gap", "Multirespuesta")
- `muestra_base` — Base específica para el dato

## Tipos de Gráficas Soportadas

### Primarias (Prioritarias para Código Casa)

| # | Tipo | Casos de Uso | Ejemplo |
|---|------|-------------|---------|
| 1 | Stacked Bar | Multirespuesta, composición | "76% combinado reporta estrés" |
| 2 | Grouped Bar | Comparación generacional | Edad 18-24 vs 25-34 vs 35+ |
| 3 | Percentage Bar | 100% stacked, proporción | Distribución por categoría |
| 4 | Heatmap | Cruces multidimensionales | NSE × Edad × Indicador |
| 5 | Bullet Chart | Indicadores vs. meta | Estrés real vs. esperado |
| 6 | Waterfall | Descomposición | Cómo se acumula estrés |
| 7 | Scatter + Bubble | Distribución de hallazgos | Outliers, patrones |
| 8 | Diverging Bar | Positivo vs. Negativo | Acuerdo/Desacuerdo |
| 9 | Waffle | Proporción visual 10×10 | 76 de 100 personas |
| 10 | Slope | Cambio generacional | Tendencia 18-24 → 35+ |

### Secundarias (Apoyo)

11. Line (tendencias temporales)
12. Area (acumulativas)
13. Box Plot (distribución estadística)
14. Violin Plot (densidad)
15. Radar (múltiples variables)
16. Sankey (flujos)
17. Treemap (jerarquía proporcional)
18. Sunburst (drilling)
19. Chord (relaciones cíclicas)
20. Gauge (escala 0-100)

## Sistema de Recomendación Automático

### Proceso

1. **Detección**: Analiza estructura CSV → identifica tipo de dato
2. **Búsqueda**: BM25 en `data-patterns.csv` → encontrar patrones similares
3. **Filtrado**: Aplica reglas culturales (sensibilidad dominicana)
4. **Ranking**: Top 3 gráficas + alternativas
5. **Paleta**: Selecciona dominican-palettes.csv según pilar + contexto
6. **Jerarquía**: Aplica 60-30-10 rule

### Output

```json
{
  "recommended": "Grouped Bar",
  "alternatives": ["Heatmap", "Bullet Chart"],
  "palette": "DOMINICAN_IDENTITY_HOPE",
  "colors": ["#16A34A", "#2563EB", "#F59E0B"],
  "hierarchy": {
    "primary_insight_size": "400px",
    "secondary_data_size": "300px",
    "background_size": "150px"
  },
  "insights": {
    "headline": "76% de jóvenes (18-24) reportan estrés financiero, vs. 45% en 35+",
    "gap": "31 puntos porcentuales de brecha generacional",
    "cultural_context": "Crisis de vivienda y empleo juvenil en RD intensifica presión"
  }
}
```

## Principios de Diseño Integrados

### Gestalt (Cómo los usuarios agrupan información)

- **Proximidad**: Categorías similares agrupadas visualmente cerca
- **Similitud**: Mismo significado = mismo color (consistencia)
- **Continuidad**: Flujo visual descendente = percepción de fuerza
- **Cierre**: Humanos completan patrones implícitos (backgrounds sutiles)

### Psicología del Color Dominicana

| Color | Contexto RD | Uso Típico | Contraste |
|-------|-----------|-----------|----------|
| #16A34A | Naturaleza/Caña | Finanzas positivas, Esperanza | f0f2f4 |
| #EF4444 | Alerta/Estrés | Indicadores de tensión, Problema | f0f2f4 |
| #2563EB | Confianza/Cielo | Contexto, Trasfondo, Estabilidad | f0f2f4 |
| #F59E0B | Sol/Energía | Hallazgos positivos, Oportunidad | 03060a |
| #A855F7 | Creatividad | Identidad, Bienestar, Reflexión | f0f2f4 |
| #D946EF | Pasión | Datos emocionales, Compromiso | f0f2f4 |

### Jerarquía Visual (60-30-10 Rule)

- **60%** → Fondo (ejes, contexto, etiquetas) — Gray, baja opacidad
- **30%** → Datos principales (barras, líneas) — Color medio
- **10%** → Insights destacados (anotaciones, color brillante) — Paleta saturada

## Data Storytelling Automático

El skill extrae automáticamente:

- **Headline** — El dato más importante (máx. 1 línea)
- **Key Findings** — Valores extremos, patrones, outliers
- **Say-Do Gap** — "Dicen X, pero hacen Y"
- **Generational Shift** — Análisis de brecha por edad
- **Cultural Context** — Interpretación específica del contexto dominicano
- **Takeaway** — Implicación accionable para negocio/policy

### Ejemplo

**Input CSV:**
```
tension,edad_18_24,edad_25_34,edad_35_plus
"Estrés financiero",76.2%,68.5%,52.3%
```

**Output Automático:**

```markdown
## Hallazgo Clave
76% de jóvenes dominicanos (18-24) reportan estrés financiero,
vs. 45% en mayores de 35. Brecha de 31 puntos porcentuales.

## Contexto Dominicano
Crisis de vivienda y desempleo juvenil intensifican presión
financiera en RD más que en contextos comparables de LATAM.
Deuda como "plan de vida" se inicia temprano.

## Implicación
Políticas de inclusión financiera deben priorizar 18-34 años.
```

## Validación y Accesibilidad

Todos los gráficas cumplen con:

- ✅ **WCAG 2.1 AA** (contraste mínimo 4.5:1)
- ✅ **Daltonismo** (sin dependencia de rojo/verde)
- ✅ **Alt text** (SVG con descripciones textuales)
- ✅ **Tipografía** (sans-serif, tamaño mínimo 12px)
- ✅ **Densidad de datos** (máx. 5 series por gráfica)

## Flujo de Trabajo Típico para Jeremy (Código Casa)

### 1. Preparar datos

```bash
# Exportar tabulación en CSV con estructura estándar
# (tension, edad_*, nse_*, sexo_*, etc.)
```

### 2. Generar visualizaciones

```bash
python3 scripts/batch_generator.py \
  --input "codigo-casa-tabulaciones.csv" \
  --output-dir "reports/" \
  --include-insights
```

### 3. Output

Carpeta `reports/` lista con:
- `index.html` — Navegación integrada
- `identidad/tension-01.html`, `tension-02.html`, ... (10)
- `finanzas/` — 10 tensiones
- `bienestar/` — 10 tensiones

Cada HTML contiene:
- Gráfica principal (SVG)
- Insights automáticos
- 2-3 gráficas de apoyo
- Metadata cultural
- **Listo para Keynote/PDF**

## Ejemplos de Salida

### Reporte Individual

```html
<div class="tension-card" data-pilar="identidad" data-tension="01">
  <h2>Confusión de Roles</h2>
  
  <svg viewBox="0 0 800 400" class="main-chart">
    <!-- Grouped Bar Chart generado automáticamente -->
  </svg>
  
  <div class="insight-primary">
    <strong>Hallazgo clave:</strong> 72% de jóvenes reportan confusión 
    de roles, vs. 45% en 35+. Brecha generacional de 27pp.
  </div>
  
  <div class="supporting-charts">
    <svg class="heatmap"><!-- NSE × Edad --></svg>
    <svg class="diverging"><!-- Say-Do Gap --></svg>
  </div>
</div>
```

## Archivos de Configuración (data/*.csv)

### chart-types.csv
Define 20+ tipos de gráficas con metadata:
- DataType, ChartType, WhenToUse, ColorGuidance, Accessibility

### dominican-palettes.csv
8-10 paletas cromáticas:
- Name (ej: DOMINICAN_IDENTITY_HOPE)
- Colors (lista de 5-6 colores)
- Context (Identidad, Finanzas, Bienestar)
- Sentiment (Positivo, Negativo, Neutro)

### data-patterns.csv
30 patrones típicos de Código Casa:
- PatternType (multirespuesta, generacional, NSE, etc.)
- DataStructure (cómo se ve en CSV)
- BestChart (gráfica recomendada)
- Example

### Otros CSVs
- `gestalt-rules.csv` — 12 principios Gestalt con weight score
- `color-psychology.csv` — 6 colores × contexto dominicano
- `hierarchy-patterns.csv` — 10 patrones de jerarquía visual
- `tension-indicators.csv` — 30 indicadores de tensión por pilar
- `cultural-sensitivity.csv` — 15 guías para sensibilidad dominicana

## Dependencias

- Python 3.6+
- Librerías estándar (csv, json, pathlib, statistics)
- **Sin dependencias externas** (maxima compatibilidad)

## Testing

```bash
# Test 1: Recomendación
python3 scripts/search.py "multirespuesta generacional" --chart-recommend

# Test 2: Generación de gráfica
python3 scripts/search.py "Identidad jóvenes" \
  --input examples/sample-data/identidad-sample.csv \
  --output test-output.html

# Test 3: Batch
python3 scripts/batch_generator.py \
  --input examples/sample-data/codigo-casa-full.csv \
  --output-dir examples/generated-reports/

# Test 4: Validación WCAG
python3 scripts/validate_a11y.py examples/generated-reports/
```

## Flujo de Desarrollo

**Fase 1** → Core Foundation (BM25 + CSV loading)
**Fase 2** → Chart Generation (SVG generators)
**Fase 3** → Intelligence Layer (Insights automáticos)
**Fase 4** → Output (HTML export)
**Fase 5** → Testing (WCAG, batch processing)

## Roadmap

- [x] Arquitectura base
- [ ] BM25 engine + CSV loading
- [ ] 20 tipos de gráficas
- [ ] Principios Gestalt
- [ ] Psicología del color dominicana
- [ ] Insights automáticos
- [ ] HTML exporter
- [ ] Validación WCAG
- [ ] Batch processing
- [ ] Documentación completa

## Contacto / Preguntas

Jeremy Rodriguez — NINJA Thinking
Código Casa — Estudio de familias dominicanas
