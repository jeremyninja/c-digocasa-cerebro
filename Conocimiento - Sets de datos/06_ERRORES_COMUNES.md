# 06 · Errores Comunes — Lo que NO Hay que Hacer

Documento de lecciones aprendidas de la primera ronda del deck Finanzas. Léelo antes de empezar para no repetir errores.

## 1. Errores de fidelidad al .txt (los más graves)

### Error #1.1 — Inventar oraciones editoriales

**Qué pasó:**
El creativo agregó oraciones bonitas a las conclusiones italic que sonaban bien pero no estaban en el .txt.

**Ejemplo real (T6, slide 2):**
- ✅ Texto del .txt: "La tranquilidad financiera emerge como el verdadero sueño dominicano, desplazando aspiraciones materiales."
- ❌ Texto en el slide: "La tranquilidad financiera emerge como el verdadero sueño dominicano, desplazando aspiraciones materiales. **La casa propia no se rinde como meta — se posterga como camino.**"

La segunda oración **no existía en el .txt**. Era buena prosa pero era invención.

**Regla:** si una oración no está en el `.txt`, no debe estar en el slide. Punto.

### Error #1.2 — Redondear citas inline en descripciones

**Qué pasó:**
El slide redondeaba decimales de citas dentro de descripciones cuando NO debía.

**Ejemplo real (T9, slide 26):**
- ✅ Texto del .txt: "calidad (45.8%) y salud (34.4%)"
- ❌ Texto en el slide: "calidad (46%) y salud (34%)"

Las descripciones de stat sí mantienen decimales. Solo el número grande (96pt) redondea.

### Error #1.3 — Cambiar palabras del .txt sin razón visual

**Qué pasó:**
El creativo "mejoraba" frases del .txt que ya estaban bien.

**Ejemplos reales (T8):**
- ✅ .txt: "comidas fuera de casa como el gasto discrecional #1 en su hogar"
- ❌ Slide: "comidas fuera de casa como el gasto discrecional #1 del hogar"

Diferencia mínima, pero mejor mantener el original cuando no hay razón para cambiarlo.

### Error #1.4 — Recortar comillas mal

**Qué pasó:**
El slide cortaba la cita cuando el .txt tenía la frase completa entre comillas.

**Ejemplo real (T6, slide 2):**
- ✅ .txt: 'señala como ideal de vivienda **"tener una casa propia, no alquilada"**.'
- ❌ Slide: 'señala como ideal de vivienda **"tener una casa propia"**, no alquilada.'

La comilla cierra antes de tiempo; la frase "no alquilada" queda fuera de la cita aunque el .txt la incluye.

## 2. Errores de placeholder

### Error #2.1 — Dejar slides sin llenar

**Qué pasó:**
Los 5 slides de "Cruce de Data" llegaron como placeholders ("Aquí va el cruce: X por NSE") y nadie los llenó.

**Por qué pasa:**
El equipo creativo monta el deck visual antes de que research procese todos los cruces. Quedan en cola. Si no hay un proceso explícito de cierre, se quedan así.

**Cómo evitarlo:**
- En la fase de diagnóstico, identifica TODOS los placeholders
- Confirma con research si hay cruces pendientes en el .txt
- Construye los cruces faltantes (hay un script para esto)

### Error #2.2 — Confundir placeholder con elemento de diseño

**Cuál es la diferencia:**
- **Placeholder real:** caja punteada con texto tipo "Aquí va X" o "PLACEHOLDER" arriba — hay que llenar
- **Elemento de diseño:** caja con borde sólido o sin borde, contenido real (aunque no haya imagen aún) — se queda

**Ejemplo:** los slides Caso Referencia (8, 16, 24, 32, 40) tienen un placeholder de imagen marcado con `[ AGREGAR IMAGEN ]`. Eso NO es tu trabajo llenarlo — lo hace la cuenta o el creativo.

## 3. Errores de diseño

### Error #3.1 — Kerning loco

**Qué pasó:**
Muchos slides venían con `spc="100"` hasta `spc="700"` aplicado a headers como "TENSIÓN 0X · FINANZAS" y a labels guía. Hacía el deck verse inconsistente.

**Cómo evitarlo:**
Pasar siempre `apply_design_fixes.py` al inicio de la sesión.

### Error #3.2 — Verbatims en verde lima

**Qué pasó:**
Los @usernames de los verbatims venían en verde lima. El verde lima debe usarse solo para la cápsula "Tensión 0X" en Mapeo y Kit de Marca.

**Cómo evitarlo:**
Pasar `apply_design_fixes.py`. Cambia los `B8FF4D` a `FFFFFF` en los slides de Conversación Digital.

### Error #3.3 — Labels guía visibles para el cliente

**Qué pasó:**
Los slides traían labels arriba tipo "/ HALLAZGO · TENSIÓN 0X" o "/ CRUCE DE DATA · TENSIÓN 0X" que son notas internas para el equipo, no para el cliente.

**Cómo evitarlo:**
Pasar `apply_design_fixes.py`. Borra todos los labels guía.

### Error #3.4 — Decimales gigantes

**Qué pasó:**
Al construir slides de cruce, intenté poner "26.1%" como número grande. El slot visual no lo soportó: el "%" se desbordaba a una segunda línea, rompiendo el layout.

**Ejemplo real (T10, slide 36 — primera versión):**
- "26.1%" se dividió como "26.1" + "%" en líneas separadas
- "25.9%" igual

**Solución:**
Redondeé a "26%" y mantuve el dato exacto en la descripción inline.

**Regla:** los stats grandes están pensados para 3-4 caracteres. Si el dato real tiene más, redondea o reformula (ej: "14-19%" → "14%" + el rango en la descripción).

## 4. Errores de proceso

### Error #4.1 — No leer el .txt completo antes de empezar

Si no has leído el .txt entero, no entiendes qué historia está contando el deck. Vas a tomar decisiones sobre qué stats destacar sin contexto.

**Mínimo absoluto:** leer las 5 tensiones completas antes de tocar el primer slide.

### Error #4.2 — Trabajar slide por slide en orden

Mejor agrupar por **tipo de cambio**, no por slide:
1. Primero: aplicar fixes globales (kerning, intro, verbatims color)
2. Luego: cotejar todos los hallazgos
3. Luego: construir todos los cruces
4. Luego: cotejar conversación digital
5. Por último: QA visual completo

Esto es más rápido y evita inconsistencias entre slides equivalentes.

### Error #4.3 — No hacer QA visual al final

Es fácil que un cambio de texto rompa un layout (ej: una conclusión que se hace 3 líneas en vez de 2 y empuja el source). Siempre genera el PDF y revisa cada slide al final.

## 5. Errores específicos del corpus Código Casa

### Error #5.1 — Mezclar segmentaciones

**Qué pasó:**
Un cruce dice "P77 · Cruce por NSE" pero el slide intenta narrar también una lectura por edad. Eso requiere otro cruce, no se puede inferir.

**Regla:** el cruce del slide es el cruce que el .txt describe. Si el cliente quiere otra lectura, hay que pedirle al equipo de research el cruce nuevo. No se infiere de la tabla.

### Error #5.2 — Confundir cuanti con cuali en el slide

**Qué pasó:**
Un cruce por NSE basado en cuanti se montó como "según los focus groups del estrato E". Eso es falso — el cuali no tiene NSE taggeado por sesión.

**Regla:** las cifras de los slides Hallazgo y Cruce vienen de cuanti (n=500). Las quotes de Consumer Voice vienen de cuali. **Nunca se mezclan atribuciones.**

Ver el system prompt de Código Casa para el detalle de las reglas geográficas y de NSE.

### Error #5.3 — Atribuciones cualitativas inventadas

**Qué pasó:**
Si una quote tiene atribución `-- Grupo Biparental Hijos Adultos`, esa atribución es la real. No se cambia por "Grupo Familias Mixtas" porque suene mejor.

## 6. Lo que SÍ se puede editorializar

No todo es rigidez. Hay licencias creativas que sí están permitidas:

✅ **Redondear porcentajes a entero** en los stats grandes (47.8% → 48%)
✅ **Acortar la conclusión** del análisis 190 chars (no extenderla)
✅ **Reescribir la headline** del slide para que tenga split plain/italic, conservando el sentido del bullet del hallazgo
✅ **Decidir qué 3 stats narrativos extraer de una tabla cruzada** (estrategia editorial)
✅ **Bold selectivo en una palabra clave** dentro de descripciones de stat
✅ **Imágenes en slides Caso Referencia** (lo hace cuenta/creativo, no research)

## 7. Cuándo pedir ayuda

Si te enfrentas a alguno de estos casos, **escala antes de seguir**:

- El .txt tiene un cruce mencionado pero la tabla no está completa → falta data, pídele a research
- Una tipología de FG referenciada en una quote no aparece en la ficha técnica del estudio → verificar
- El número de un stat en el .txt no coincide con lo que cierra de la tabla → bug del .txt, pedir aclaración
- El cliente pidió un slide nuevo que no está en el formato 8-slides-por-tensión → escalar al PM del proyecto, no improvisar
- La data del cuanti dice una cosa y la conversación digital dice lo opuesto → eso ES la tensión cultural; no se "resuelve", se redacta como contradicción explícita

---

**Vuelve a:** `README.md` para el índice general.
