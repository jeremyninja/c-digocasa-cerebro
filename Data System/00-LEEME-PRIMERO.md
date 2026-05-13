# LÉEME PRIMERO — System Updated · Código Casa

> **Versión:** 2026-05-04 (refresh post Cuestionario Cuantitativo Código Casa 2026)
> **Para:** uso interno NINJA / Claude Project / dashboard navegable (Fase 2)

## Qué cambió respecto al kit anterior

Esta es la **organización corregida** del corpus Código Casa. Reemplaza al kit anterior (`archivos-para-el-project/`) que tenía las preguntas mal asignadas en los pilares de **Mujer**, **Sistema de Creencias** y **Consumos**.

### Cambios concretos
1. **Cuestionario canónico:** ahora se usa `Cuestionario Cuantitativo Código Casa 2026.docx` (mayo 2026) como única fuente de verdad sobre la redacción y orden de las preguntas.
2. **11 pilares canónicos** reorganizados en este orden fijo:
   1. Familia e Identidad
   2. Salud y Bienestar
   3. Finanzas y Economía
   4. Consumos
   5. Alimentación
   6. Educación
   7. Roles de Género
   8. Política
   9. Sistema de Creencias
   10. Mujer
   11. Tecnología
3. **Numeración Q##:** las preguntas del cuestionario nuevo se numeran `Q01..Q64` siguiendo el orden del docx 2026. Cada derivado deja constancia del `P##` original (cuestionario 2024) para trazabilidad.
4. **11 focus groups** (antes 9): se incorporaron `fg-10-mixta-2024-11-21` y `fg-11-extendida-2024-11-26`.
5. **Pilares con data legada:** Educación, Roles de Género y Consumos no tienen preguntas nuevas en el cuestionario 2026, así que sus derivados se construyen tirando data de la BBDD madre original (cuestionario 2024). Cada pregunta marcada con `[origen: 2024]`.
6. **Preguntas nuevas sin tabular:** algunas preguntas del cuestionario 2026 son nuevas y aún no tienen frecuencias calculadas. Aparecen marcadas como `[Pendiente de tabulación · BBDD 2026]`.

## Estructura del system updated

```
system-updated/
├── 00-LEEME-PRIMERO.md              ← este archivo
├── 01-system-prompt.txt              ← reglas de respuesta (actualizadas)
├── ficha-tecnica.md                  ← metodología, muestra, mapa de FGs
├── cuestionario-cuanti.md            ← 64 preguntas Q01–Q64 organizadas por 11 pilares
├── guia-cuali.md                     ← guía de conversación (12 secciones)
└── derivados-por-pilar/
    ├── 01-familia-e-identidad.md
    ├── 02-salud-y-bienestar.md
    ├── 03-finanzas-y-economia.md
    ├── 04-consumos.md
    ├── 05-alimentacion.md
    ├── 06-educacion.md
    ├── 07-roles-de-genero.md
    ├── 08-politica.md
    ├── 09-sistema-de-creencias.md
    ├── 10-mujer.md
    └── 11-tecnologia.md
```

## Cómo usar este sistema

1. Cargar todos los archivos de `system-updated/` y la carpeta `BBDD madre/transcripciones-codigo-casa/` en el Claude Project.
2. Pegar `01-system-prompt.txt` como system prompt del Project.
3. Las queries deben referenciar **el pilar canónico**, no el archivo viejo. Ejemplo: "qué dice el pilar de Roles de Género sobre la división de tareas".
4. Si una respuesta cita un derivado, debe usar la convención: `Q## (P## anterior) — pilar.md`.

## Reglas de integridad heredadas (no negociables)

Todas las reglas del system prompt anterior siguen vigentes:
- Citar siempre fuente (archivo + speaker o cita textual).
- Distinguir cuanti de cuali explícitamente.
- Nunca inventar quotes.
- Cuanti = SD + Santiago + DN. Cuali = solo SD.
- NSE no taggeado en cuali.
- fg-03 monoparental es transcripción incompleta.
- Solo 4 capítulos tienen output editorial final: Identidad, Bienestar, Finanzas, Medios.
- Tono sobrio, sin marketing-speak.

## Trazabilidad

- Frecuencias originales: `BBDD madre/TABULACIONES_FAMILIAS_MODERNAS.xlsx` y `TABULACIONES_CRUCES_CODIGO_CASA.xlsx`.
- Cuestionario canónico: `BBDD madre/Cuestionario Cuantitativo Código Casa 2026.docx`.
- Guía cuali: `BBDD madre/Guía de Conversación - Familia Moderna - Copy.docx`.

Cualquier discrepancia entre los derivados y la BBDD madre se resuelve a favor de la BBDD madre.
