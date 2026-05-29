# Aprendizajes del Montador de Trends CC

Lecciones acumuladas con Jeremy mientras se montan los Trend Forecasts
de Código Casa. Si una regla aparece aquí, es porque ya se corrigió al
menos una vez. **Si entra en conflicto con `.claude/agents/montador-trends-cc.md`,
estos aprendizajes ganan.**

---

## 1. HEADLINE DEL TREND — 20pt FIJO

**Fecha del aprendizaje:** 2026-05-29 (corrección de Jeremy "no sé cuántas
veces te tengo que decir").

**Regla dura:**
- Headline del trend (nombre del trend en col-left) va **20pt FIJO**.
- Fuente: Instrument Serif Regular UPPERCASE, tracking 0, line-height 1.1.
- **NO 42pt. NO 50pt. NO auto-fit. NO escalado por longitud del headline.**
- Si el headline no entra en la caja, el problema lo resuelve el editor
  recortando el copy — NO el montador subiendo el tamaño.

**Por qué pasaba el bug:**
La versión vieja del DS decía "Instrument Serif 42–50pt auto-fit: si >120
chars baja a 42pt; si <80 chars sube a 50pt". Esa lógica "otherwise" se
eliminó por completo. **Cero excepciones.**

---

## 2. TRIGGERS — CIFRA ARRIBA, TEXTO ABAJO (stack vertical)

**Fecha del aprendizaje:** 2026-05-29.

**Regla dura:**
- Cada trigger en col-center es un bloque vertical con dos elementos:
  1. **Cifra arriba** (Instrument Serif 72–96pt o keyword italic 32–48pt).
  2. **Caja descriptiva abajo** (W170pt × H35pt, Poppins 10pt blanco).
- **NUNCA side-by-side.** No "cifra a la izquierda, caja a la derecha".
  Stack vertical siempre.
- Debajo de la caja descriptiva va la fuente inline (Poppins 7pt #666).

**Por qué pasaba el bug:**
Las versiones viejas mostraban dos diagramas inconsistentes: uno con
stack vertical (correcto) y otro con side-by-side (incorrecto). El
montador podía elegir cualquiera. Ahora **solo existe el vertical**.

---

## 3. FOTOS DE SEÑALES — 110×162pt (NO 149×220pt)

**Fecha del aprendizaje:** 2026-05-29 (las fotos se salían del slide
en Alimentación).

**Regla dura:**
- Cada foto de señal en col-right va **110×162pt EXACTO**.
- **NO 149×220pt** (ese tamaño es el viejo y desborda el slide).
- Ratio portrait preservado (110/162 = 0.679 ≈ 149/220 = 0.677).
- 3 fotos × 162pt = 486pt + ~15pt gap entre cada una = ~516pt total.
  Cabe holgado en el slide (540pt de altura útil).
- Cada foto sigue con badge "Click me" rojo `#FF2D2D` en esquina sup-der
  + hyperlink al URL del señales.md + caja caption 170×35pt al lado.

**Por qué pasaba el bug:**
Con 149×220pt, 3 fotos = 660pt vertical → desborda el slide de 540pt.
Visualmente las fotos se cortaban o se montaban encima del footer.

---

## Cómo aplica el montador estos aprendizajes en el script

```python
# 1. HEADLINE — siempre 20pt, sin condicionales
headline_tf.paragraphs[0].font.size = Pt(20)   # FIJO. SIN if. SIN else.
headline_tf.paragraphs[0].font.name = "Instrument Serif"
headline_tf.word_wrap = True

# 2. TRIGGERS — stack vertical por trigger
for i, trigger in enumerate(triggers):
    y_base = TRIGGERS_TOP + i * TRIGGER_BLOCK_HEIGHT
    # Cifra ARRIBA
    add_stat_text(slide, x=col_center_x, y=y_base,
                  text=trigger["stat"], font="Instrument Serif",
                  size=Pt(72), color=WHITE)
    # Caja descriptiva ABAJO
    add_desc_box(slide, x=col_center_x, y=y_base + STAT_HEIGHT,
                 w=Pt(170), h=Pt(35),
                 text=trigger["desc"], font="Poppins",
                 size=Pt(10), color=WHITE)
    # Fuente inline DEBAJO de la caja
    add_source(slide, x=col_center_x, y=y_base + STAT_HEIGHT + Pt(35),
               text=trigger["source"], size=Pt(7), color=GRAY)

# 3. FOTOS SEÑALES — 110×162pt
PHOTO_W = Pt(110)
PHOTO_H = Pt(162)
PHOTO_GAP = Pt(15)
for i, signal in enumerate(signals):
    y_photo = SIGNALS_TOP + i * (PHOTO_H + PHOTO_GAP)
    pic = slide.shapes.add_picture(signal["path"],
                                    left=col_right_x, top=y_photo,
                                    width=PHOTO_W, height=PHOTO_H)
    # Badge + hyperlink + caption box (170×35) al lado
```

---

## Histórico de corridas y qué falló

| Fecha | Capítulo | Bug detectado por Jeremy |
|-------|----------|--------------------------|
| 2026-05-29 | Alimentación | Headline 42–50pt en vez de 20pt; triggers side-by-side en vez de stack vertical; fotos 149×220pt desbordando el slide → **fix consolidado aquí** |

Cada vez que el montador corra de aquí en adelante debe **leer este
archivo antes de generar el script** y aplicar las 3 reglas duras sin
excepción.
