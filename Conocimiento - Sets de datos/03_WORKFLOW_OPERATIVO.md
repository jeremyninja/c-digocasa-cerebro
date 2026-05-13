# 03 · Workflow Operativo — Pasos para Montar un Deck

Este es el flujo paso a paso para llevar un deck Código Casa MED de "está medio armado" a "está listo para revisión final del cliente".

## Antes de empezar

**Recibes 2 archivos:**
1. Un `.txt` con los hallazgos estructurados (formato Código Casa)
2. Un `.pptx` con los 40 slides ya diseñados visualmente, pero con datos posiblemente desactualizados o placeholders

**Lo que necesitas hacer:**
1. Verificar consistencia entre ambos
2. Llenar placeholders vacíos
3. Aplicar fixes de diseño (kerning, intro labels, color de verbatims)
4. Cotejar todo dato cuantitativo del slide vs el .txt

## Fase 1 — Diagnóstico (15 min)

### Paso 1.1 — Lee el .txt completo
- Identifica las 5 tensiones del bloque
- Lee los hallazgos numerados (los #XX). Cada tensión tiene 1 hallazgo asignado.
- Lee los cruces de cada tensión
- Lee los Mapeos y Kits de Marca

### Paso 1.2 — Abre el .pptx y haz un walk-through visual
- Confirma que tiene 40 slides (5 tensiones × 8)
- Identifica los slides con **placeholders vacíos** (suelen decir "PLACEHOLDER" o "Aquí va el cruce: X por NSE")
- Identifica los slides de **conversación digital** que tienen verbatims (slides 5, 13, 21, 29, 37)
- Mira si los slides intro dicen "TENSIÓN 0X · [PILAR]" — si sí, hay que limpiarlos a solo "TENSIÓN 0X"

### Paso 1.3 — Haz una lista de cambios necesarios
Anota en una lista:
- [ ] Qué slides tienen placeholders sin llenar
- [ ] Si hay labels guía tipo "/ HALLAZGO ·" arriba de los slides
- [ ] Si los verbatims (@usernames) están en color verde lima en vez de blanco
- [ ] Si los slides intro tienen "· FINANZAS" (o el nombre de tu pilar) que hay que quitar
- [ ] Si los datos numéricos del slide coinciden con los del .txt

## Fase 2 — Fixes de Diseño Globales (10 min)

Aplica los cambios que afectan TODOS los slides:

### Paso 2.1 — Normalizar kerning a 0
- Muchos slides vienen con kerning loco (spc="100" hasta spc="700"). Hay que llevarlo todo a 0.
- Usa el script `scripts/apply_design_fixes.py`

### Paso 2.2 — Limpiar slides intro de tensión
- Los headers que dicen "TENSIÓN 0X · [PILAR]" deben quedar solo como "TENSIÓN 0X"
- El subtítulo y el headline grande NO se tocan

### Paso 2.3 — Eliminar labels guía
Si en los slides hay etiquetas pequeñas arriba que dicen:
- "/ HALLAZGO · TENSIÓN 0X"
- "/ CRUCE DE DATA · TENSIÓN 0X"
- "/ CONVERSACIÓN DIGITAL · TENSIÓN 0X"
- "/ CASO REFERENCIA · TENSIÓN 0X"

Hay que quitarlas todas. Estas son labels de guía interna, no van al cliente.

### Paso 2.4 — Verbatims a blanco
En los slides 5, 13, 21, 29, 37, los @usernames de los verbatims deben estar en **blanco** (`#FFFFFF`), no en verde lima (`#B8FF4D`).
La cápsula verde arriba de los slides 6/7 (Mapeo y Kit de Marca) **sí queda verde** — eso es elemento de diseño, no label guía.

## Fase 3 — Cotejo de Hallazgos (30-45 min)

Para cada uno de los 5 slides de hallazgo (2, 10, 18, 26, 34):

### Paso 3.1 — Compara headline
- Lee el slide
- Lee el bullet "Hallazgo #XX" del .txt
- Si la headline del slide difiere del enunciado del hallazgo, **gana el .txt**

### Paso 3.2 — Compara los 3 stats
- Verifica que las 3 cifras coincidan con los 3 bullets del hallazgo
- Verifica que las descripciones bajo cada cifra correspondan al bullet correcto
- Ojo con citas inline: si el slide dice "calidad (46%)" pero el .txt dice "calidad (45.8%)", el decimal se mantiene en la descripción inline (NO en el número grande)

### Paso 3.3 — Compara la conclusión
- La conclusión italic NO debe tener oraciones editoriales que no estén en el .txt
- Si el creativo metió una segunda oración tipo "La casa propia no se rinde como meta — se posterga como camino" pero el .txt no la tiene, **se elimina**
- Solo queda lo que el .txt sustenta

### Paso 3.4 — Verifica el source
- Debe coincidir con las preguntas referenciadas en los bullets (P26, P54, P73, etc.)
- Base 500 siempre

**Use el script:** `scripts/fix_hallazgo_text.py` para hacer los cambios sin pelearte con XML manual.

## Fase 4 — Construir Slides de Cruce (45-60 min)

Los slides 4, 12, 20, 28, 36 suelen llegar como placeholders vacíos. Hay que construirlos desde la tabla del .txt.

### Paso 4.1 — Para cada cruce, extrae la data
1. Lee el bloque "CRUCE TENSIÓN X" del .txt
2. Extrae la **tabla** completa
3. Lee el "ANÁLISIS (190 chars)"
4. Lee la "IDEA DE VISUALIZACIÓN"

### Paso 4.2 — Decide los 3 stats narrativos
Usa una de las 3 estrategias del Schema (`02_DATA_SCHEMA.md`):
- Extremo + extremo + diferencial
- Top + segundo + sorpresa
- Cifra + cifra + ratio

**Regla de oro:** los 3 stats deben **contar una historia juntos**, no ser 3 datos sueltos.

### Paso 4.3 — Escribe el headline
- Sintetiza la lectura del análisis 190 chars
- Split en plain + italic en la palabra clave
- Ejemplo: "El alquiler comprime a _ambos extremos por razones opuestas._"

### Paso 4.4 — Escribe las descripciones de cada stat
Cada stat tiene 3 partes (regular + bold + regular):
- Part 1: contexto ("del estrato ", "de los ", "es el ")
- Part 2 BOLD: la variable destacada ("E (<RD$10K)", "55+", "promedio nacional")
- Part 3: complemento informativo ("sufre violencia económica en su entorno familiar.")

### Paso 4.5 — Escribe la conclusión
Toma el análisis 190 chars y úsalo casi tal cual. Puedes acortar pero NO extender ni añadir interpretación nueva.

### Paso 4.6 — Source
- Pregunta del cruce + tipo de cruce + base
- Ejemplo: "Source: Código Casa — Estudio cuantitativo 2025 · P77 · Cruce por NSE · Base 500."

**Use el script:** `scripts/build_cruce_slides.py` que ya tiene el template visual incorporado.

## Fase 5 — Cotejo de Conversación Digital (15 min)

Para cada slide de Conv. Digital (5, 13, 21, 29, 37):

### Paso 5.1 — Verifica los KPIs
- Menciones, alcance, % del dataset/sentiment — todos deben coincidir con el .txt

### Paso 5.2 — Verifica los 3 quotes
- @usuario tal cual viene en el .txt
- Plataforma correcta (X/TWITTER vs TIKTOK vs INSTAGRAM)
- Texto exacto, ojo con comillas curvas

### Paso 5.3 — Verifica el headline
- Que sintetice la idea del párrafo de cierre del bloque conversación digital del .txt

## Fase 6 — Cotejo de Mapeo, Kit de Marca y Caso (20 min)

Estos suelen llegar bien porque el creativo copia del .txt:

### Paso 6.1 — Mapeo (slides 6, 14, 22, 30, 38)
- Verifica que las 3 ternas (verdad/oportunidad/detonador) coincidan con el .txt
- La cápsula verde arriba dice "Tensión 0X"

### Paso 6.2 — Kit de Marca (slides 7, 15, 23, 31, 39)
- Verifica situación, oportunidad clave, postura, verbo transformador
- Verifica que la nueva narrativa de marca esté ensamblada correctamente
- "[Tu marca]" entre corchetes

### Paso 6.3 — Caso Referencia (slides 8, 16, 24, 32, 40)
- Marca + país correctos
- Descripción coincide con el .txt
- Imagen suele ser placeholder — no es tu trabajo llenarla

## Fase 7 — QA Visual Final (10 min)

### Paso 7.1 — Generar el PDF y revisar todos los slides
Convertir el .pptx a PDF y mirar cada slide:
- Texto cortado o desbordado
- Cifras decimales muy largas (26.1% se ve gigante en el slot — redondéa a 26%)
- Comparaciones de tamaño visual entre slides equivalentes (los 5 hallazgos se deben ver homogéneos entre sí)

### Paso 7.2 — Checklist final
- [ ] Los 5 slides intro dicen solo "TENSIÓN 0X"
- [ ] Ningún slide tiene labels guía tipo "/ HALLAZGO ·"
- [ ] Los 5 slides hallazgo tienen 3 stats con la data del .txt
- [ ] Los 5 slides cruce tienen 3 stats con data real (no placeholders)
- [ ] Los 5 slides Conv. Digital tienen verbatims en blanco
- [ ] Kerning está en 0 en todo el deck
- [ ] Los slides Caso Referencia tienen el placeholder de imagen (lo llena la cuenta)

### Paso 7.3 — Generar thumbnails grid
Útil para enviar al creativo o al cliente como pre-revisión:
```
python /mnt/skills/public/pptx/scripts/thumbnail.py output.pptx final_
```
Genera 4 grids de 12 slides cada uno para review rápido.

## Tiempo total estimado

| Fase | Tiempo |
|------|--------|
| 1. Diagnóstico | 15 min |
| 2. Fixes de diseño globales | 10 min |
| 3. Cotejo hallazgos | 30-45 min |
| 4. Construir cruces | 45-60 min |
| 5. Cotejo conversación digital | 15 min |
| 6. Cotejo mapeo/kit/caso | 20 min |
| 7. QA visual | 10 min |
| **Total** | **~2.5 horas por deck** |

Si es la primera vez, suma 30-60 min de aprendizaje. Si ya hiciste 1 antes, baja a ~2 horas.

---

**Ver siguiente:** `04_DECISIONES_DE_DISENO.md` — reglas visuales no negociables.
