# Knowledge Pack — Montar Decks de Tensiones desde Hallazgos

**Para:** Gabriela
**Producto:** Código Casa MED — formato de 5 tensiones por pilar
**Fuente de verdad:** un archivo `.txt` con hallazgos estructurados que viene del equipo de research

---

## 1. Qué es este documento

Esta guía explica cómo armar un deck de 5 tensiones (40 slides) a partir de un archivo de hallazgos `.txt`. El proceso fue desarrollado con el pilar de **Finanzas** y aquí está consolidado para replicarlo con cualquier otro pilar (Bienestar, Identidad, Roles de Género, Tecnología, etc.) o cualquier otro set de datos similar.

**No es un manual técnico de PowerPoint.** Es un workflow operativo: qué data necesitas, cómo se mapea al deck, qué reglas de diseño aplicar y cómo evitar los errores que ya cometí en la primera ronda.

## 2. Archivos en este pack

```
knowledge_para_gabriela/
│
├── README.md                          ← este documento
├── 01_ESTRUCTURA_DEL_DECK.md          ← qué tipo de slide hay y qué contiene cada uno
├── 02_DATA_SCHEMA.md                  ← qué data necesitas del .txt para llenar el deck
├── 03_WORKFLOW_OPERATIVO.md           ← pasos en orden para montar un deck nuevo
├── 04_DECISIONES_DE_DISENO.md         ← reglas visuales no negociables
├── 05_EJEMPLO_TRABAJADO_T6.md         ← cómo se llenó la Tensión 6 desde el txt
├── 06_ERRORES_COMUNES.md              ← lo que NO hay que hacer (lecciones aprendidas)
│
├── template_master.pptx               ← el deck T6-10 final como template visual
├── txt_referencia_finanzas.txt        ← el .txt fuente como ejemplo de formato
│
└── scripts/
    ├── README.md                      ← cómo usar los scripts
    ├── apply_design_fixes.py          ← kerning, intro labels, verbatims a blanco
    ├── fix_hallazgo_text.py           ← corregir texto de hallazgos vs el .txt
    └── build_cruce_slides.py          ← construir slides de cruce desde plantilla
```

## 3. Cuándo usar este pack

Usalo cuando recibas:
- Un `.txt` de hallazgos en el formato Código Casa (5 tensiones por pilar, hallazgos numerados, cruces tabulados, conversación digital, mapeo de oportunidades, caso referencia, narrativa de marca)
- Un `.pptx` ya diseñado por el equipo creativo con los 40 slides estructurados pero con datos posiblemente desactualizados o placeholders vacíos

**No lo uses si:**
- El `.txt` tiene un formato distinto al de Código Casa MED — ahí el schema no aplica
- El `.pptx` no sigue la estructura de 5 tensiones × 8 slides + intro = 40 slides
- Lo que necesitas es crear un deck desde cero (este pack asume que ya hay un deck visual en pie)

## 4. Lo más importante en una sola frase

> **El `.txt` es la fuente de verdad. Si algo no está en el `.txt`, no debe estar en el deck. Si algo está en el `.txt` y no está en el deck, es un dato faltante que hay que montar.**

## 5. Cómo leer este pack

**Si nunca has hecho esto:** lee en orden 01 → 02 → 03 → 05. El 04 y 06 son referencia.

**Si ya recibiste el `.txt` y `.pptx` y solo quieres empezar:** salta directo a `03_WORKFLOW_OPERATIVO.md`.

**Si ya empezaste y tienes una duda específica:** ve al archivo numerado correspondiente (estructura, data, diseño, errores).

---

**Última actualización:** Abril 2026, basado en el trabajo del deck Familia & Finanzas T1-T10.
