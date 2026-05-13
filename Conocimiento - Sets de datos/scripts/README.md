# Scripts — Cómo Usarlos

Estos 3 scripts automatizan los cambios más repetitivos. Están en Python y se corren desde la línea de comandos.

## Cuándo usar cada uno

| Script | Cuándo |
|--------|--------|
| `apply_design_fixes.py` | Siempre. Es lo primero que se corre en cualquier deck. |
| `fix_hallazgo_text.py` | Cuando el texto de un Hallazgo en el slide difiere del .txt. |
| `build_cruce_slides.py` | Cuando los slides de cruce vienen como placeholders y hay que construirlos. |

## Cómo se corren

Todos los scripts asumen que tienes:
1. Un `.pptx` que vas a modificar
2. Acceso a las herramientas de pptx que vienen con el ambiente (skill `pptx`)

### Workflow estándar

```bash
# 1. Copia el .pptx a la carpeta de trabajo
cp /ruta/al/archivo.pptx /home/claude/deck.pptx

# 2. Desempaca
python /mnt/skills/public/pptx/scripts/office/unpack.py /home/claude/deck.pptx /home/claude/unpacked/

# 3. Aplica fixes globales (siempre)
python apply_design_fixes.py

# 4. Si hay que corregir texto de hallazgos:
python fix_hallazgo_text.py

# 5. Si hay que construir cruces:
python build_cruce_slides.py

# 6. Reempaca
python /mnt/skills/public/pptx/scripts/clean.py /home/claude/unpacked/
python /mnt/skills/public/pptx/scripts/office/pack.py /home/claude/unpacked/ /home/claude/output.pptx --original /home/claude/deck.pptx

# 7. (Opcional) Genera PDF para QA visual
python /mnt/skills/public/pptx/scripts/office/soffice.py --headless --convert-to pdf /home/claude/output.pptx
```

## Cosas que tienes que personalizar por deck

Cada script tiene una sección al inicio donde se definen los datos específicos del deck. **NO se pueden correr sin antes editarlos para tu caso.**

### `apply_design_fixes.py`
- Generalmente NO requiere edición. Aplica las mismas reglas a todos los decks.
- Lo único que podrías cambiar: la lista de slides donde van verbatims (por defecto: 5, 13, 21, 29, 37) si tu deck tiene otra numeración.

### `fix_hallazgo_text.py`
- **Requiere edición intensiva.** Aquí defines lista por lista cada cambio de texto.
- Cada entrada tiene formato: `(slide_filename, old_string, new_string)`.
- Editas la sección `EDITS` con tus cambios específicos.

### `build_cruce_slides.py`
- **Requiere edición intensiva.** Aquí defines los datos de cada slide de cruce.
- Editas la sección `CRUCES` con un dict por cada slide (4, 12, 20, 28, 36).
- Cada cruce define: headline, 3 stats con sus 3 partes, conclusión, source.

## Ayuda — qué hacer si algo falla

### Error: "String to replace not found"
Significa que el texto que buscas reemplazar no existe exactamente en el XML del slide. Causas comunes:
1. El texto ya fue modificado en una corrida previa
2. Hay un caracter especial diferente (comilla curva vs comilla recta, guion largo vs guion medio)
3. El texto está dividido entre múltiples runs `<a:r>` por formateo diferente

**Solución:** abre el slide.xml manualmente con un editor y busca el texto. Verás cómo está realmente escrito.

### Error: "Marker not found"
Significa que tu plantilla no tiene un marcador esperado. Causas comunes:
1. La sección `TEMPLATE_TO_MARKER` no incluye todos los reemplazos
2. El template visual cambió y ya no tiene el texto original que se buscaba

**Solución:** verifica que el slide template (slide 2 por defecto) tenga todos los textos que `TEMPLATE_TO_MARKER` espera reemplazar.

### El PDF se ve raro / texto desbordado
Los scripts cambian texto pero no cajas. Si pones más texto del que cabe, se desborda. Soluciones:
- Reduce el texto
- Redondea números
- Si el problema es estructural, hay que editar las dimensiones de la caja en el XML

## Limitaciones

Estos scripts:
- **No** crean slides nuevos desde cero
- **No** insertan imágenes
- **No** modifican layouts maestros
- **No** validan automáticamente que el texto coincide con el .txt — eso lo haces tú

Si necesitas algo de eso, hay que escalar a alguien técnico o hacerlo manualmente en PowerPoint.
