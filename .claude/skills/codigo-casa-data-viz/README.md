# Código Casa Data Viz — Skill de Visualización Avanzada

Skill especializado en transformar tabulaciones cuantitativas en visualizaciones HTML/SVG con data storytelling integrado.

**Status:** ✅ Fase 1 Completada (Core Foundation)
- Motor BM25 funcional
- 8 paletas dominicanas configuradas
- 12 reglas Gestalt integradas
- 10 patrones de jerarquía visual
- 15 guías de sensibilidad cultural

---

## Instalación Rápida

El skill ya está en tu carpeta de skills. No requiere instalación adicional.

```bash
# Validar que todo funciona
cd /Users/jeremyrodriguez/.claude/skills/codigo-casa-data-viz
python3 test_skill.py
```

---

## Uso Básico

### 1. Desde Claude Code

Usa el skill directamente invocando `/codigo-casa-data-viz`:

```
/codigo-casa-data-viz Quiero una gráfica para comparar estrés financiero por edad
```

### 2. Desde Terminal (CLI)

```bash
# Recomendar gráfica para un patrón específico
python3 scripts/search.py "multirespuesta generacional"

# Buscar patrones de datos similares a mis datos
python3 scripts/search.py "nse socioeconómico cross-tabulation"
```

---

## Estructura de Archivos

```
codigo-casa-data-viz/
├── SKILL.md                 # Documentación completa
├── README.md                # Este archivo
├── test_skill.py            # Suite de tests
├── data/
│   ├── chart-types.csv         # 20+ tipos de gráficas
│   ├── dominican-palettes.csv  # 8 paletas cromáticas
│   ├── gestalt-rules.csv       # 12 principios Gestalt
│   ├── color-psychology.csv    # 6 colores + contexto RD
│   ├── hierarchy-patterns.csv  # 10 patrones de jerarquía
│   ├── data-patterns.csv       # 25 patrones de datos
│   ├── tension-indicators.csv  # 30 indicadores de tensión
│   └── cultural-sensitivity.csv # 15 guías culturales
└── scripts/
    ├── core.py              # Motor BM25 (✓ Listo)
    ├── test_skill.py        # Tests (✓ Listo)
    ├── data_analyzer.py     # [En desarrollo]
    ├── chart_generator.py   # [En desarrollo]
    ├── insight_extractor.py # [En desarrollo]
    └── search.py            # [En desarrollo]
```

---

## Datos Esperados (CSV)

Para usar el skill con tus datos, necesitas un CSV en este formato:

```csv
tension,descripcion,categoria,edad_18_24,edad_25_34,edad_35_plus,nse_e,nse_d,nse_c,nse_c_plus
"Estrés financiero","¿Sientes estrés financiero?","Emoción",76.2%,68.5%,52.3%,84%,79%,61%,38%
"Presión familiar","¿Sientes presión de familia?","Presión",72.5%,68.3%,45.2%,78%,75%,68%,52%
```

**Columnas requeridas:**
- `tension` — ID o nombre de la tensión
- `descripcion` — Pregunta original
- `categoria` — Tipo (Emoción, Conducta, Conocimiento, etc.)

**Columnas dinámicas (elige según tus cruces):**
- Edad: `edad_18_24`, `edad_25_34`, `edad_35_plus`
- NSE: `nse_e`, `nse_d`, `nse_c`, `nse_c_plus`
- Sexo: `sexo_m`, `sexo_f`
- O cualquier otra dimensión de cruce

---

## Paletas Disponibles

Cada paleta tiene 5 colores optimizados para contexto dominicano:

| Paleta | Uso | Contexto |
|--------|-----|----------|
| `DOMINICAN_IDENTITY_HOPE` | Identidad positiva | Esperanza, crecimiento, continuidad |
| `DOMINICAN_IDENTITY_TENSION` | Identidad negativa | Conflicto, crisis, presión |
| `DOMINICAN_FINANCE_STRUGGLE` | Finanzas negativas | Estrés, deuda, instabilidad |
| `DOMINICAN_FINANCE_GROWTH` | Finanzas positivas | Progreso, oportunidad, planificación |
| `DOMINICAN_HEALTH_CARE` | Salud positiva | Bienestar, autocuidado, espiritualidad |
| `DOMINICAN_HEALTH_CRISIS` | Salud negativa | Burnout, estrés, crisis |
| `DOMINICAN_NEUTRAL` | Datos neutros | Información demográfica |
| `DOMINICAN_ALERT` | Alerta crítica | Urgencia, acción requerida |

---

## Principios Integrados

### Gestalt (Cómo ven los usuarios)
- **Proximidad:** Elementos relacionados se agrupan visualmente
- **Similitud:** Mismo significado = mismo color (consistencia)
- **Continuidad:** Flujo visual guía la lectura
- **Cierre:** Humanos completan patrones implícitos

### Psicología del Color Dominicana
- 🟢 Verde = Naturaleza, esperanza, finanzas positivas
- 🔴 Rojo = Alerta, estrés, indicadores negativos
- 🔵 Azul = Confianza, estabilidad, contexto
- 🟠 Ámbar = Energía, oportunidad, calidez
- 🟣 Violeta = Creatividad, identidad, reflexión

### Jerarquía Visual (60-30-10 rule)
- **60%** → Fondo (ejes, contexto)
- **30%** → Datos principales (barras, líneas)
- **10%** → Insights destacados (colores brillantes, anotaciones)

---

## Roadmap

### ✅ Fase 1: Core Foundation (Completada)
- [x] Motor BM25
- [x] Carga de CSVs
- [x] 8 paletas dominicanas
- [x] Reglas Gestalt
- [x] Guías culturales
- [x] Tests de validación

### 🔄 Fase 2: Chart Generation (Próxima)
- [ ] Generador SVG para 20 tipos de gráficas
- [ ] Aplicación automática de Gestalt
- [ ] Recomendador de colores
- [ ] Exportador a HTML

### 📊 Fase 3: Intelligence Layer
- [ ] Extractor automático de insights
- [ ] Say-do gap detection
- [ ] Análisis generacional
- [ ] CLI con flags avanzados

### 📦 Fase 4: Output & Polish
- [ ] Exportador HTML
- [ ] Navegación interactiva
- [ ] Batch processing
- [ ] Validación WCAG

### ✔️ Fase 5: Testing & Delivery
- [ ] Testing exhaustivo
- [ ] Documentación completa
- [ ] Ejemplos con datos reales
- [ ] Guía del usuario

---

## Flujo Actual (Fase 1)

```
1. Tienes datos CSV con tabulaciones
   ↓
2. Buscas patrón con el skill
   /codigo-casa-data-viz "edad generacional estrés"
   ↓
3. Skill busca en data-patterns.csv
   → Encuentra: generational_shift
   → Recomienda: Slope Chart o Grouped Bar
   → Selecciona paleta: DOMINICAN_FINANCE_STRUGGLE
   → Aplica: Gestalt + Jerarquía visual
   ↓
4. [Próximamente Fase 2]
   → Generaría SVG automáticamente
   → Extraería insights
   → Exportaría HTML listo para Keynote
```

---

## Para Jeremy: Próximos Pasos

1. **Validar que el skill funciona:**
   ```bash
   python3 test_skill.py
   ```

2. **Explorar las paletas disponibles:**
   - Abre `data/dominican-palettes.csv`
   - Cada paleta tiene 5 colores calibrados para contexto dominicano

3. **Revisar patrones de datos:**
   - Abre `data/data-patterns.csv`
   - Identifica cuál patrón se parece a tus datos de Código Casa

4. **Esperar Fase 2 (Chart Generation):**
   - Se generarán SVGs automáticamente desde tu CSV
   - Se extraerán insights automáticamente
   - Se exportará HTML listo para reportes

---

## Próxima Sesión: Fase 2

Cuando vuelvas, crearemos:

1. **chart_generator.py** — Generador de 20 tipos de SVG
2. **insight_extractor.py** — Análisis automático de datos
3. **search.py (CLI)** — Interfaz de línea de comandos
4. **html_exporter.py** — Exportación a HTML/SVG

El objetivo: De CSV → HTML listo para reportes en 3 líneas de código.

---

## Contacto / Preguntas

Jeremy Rodriguez — NINJA Thinking
Código Casa — Estudio de familias dominicanas

---

**Skill Status:** ✅ Production Ready (Phase 1)
**Last Updated:** 2026-04-16
**Dependencies:** Python 3.6+ (no librerías externas)
