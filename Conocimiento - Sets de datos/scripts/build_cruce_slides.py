#!/usr/bin/env python3
"""
build_cruce_slides.py
======================
Construye los 5 slides de Cruce de Data (slides 4, 12, 20, 28, 36) usando un slide
de Hallazgo como template visual. Reemplaza placeholders vacíos con datos reales
del .txt.

CÓMO FUNCIONA:

1. Toma el slide 2 (un Hallazgo cualquiera) como plantilla
2. Reemplaza cada pieza de contenido con un marcador único ({{STAT1}}, {{HEADLINE_PLAIN}}, etc.)
3. Para cada cruce (4, 12, 20, 28, 36), llena los marcadores con los datos específicos
4. Sobrescribe los slides placeholder con los slides cruce ya armados

USO:
    1. Edita el dict CRUCES con los datos de cada cruce
    2. Corre: python build_cruce_slides.py

ESTRUCTURA DE DATOS PARA CADA CRUCE:

    {
        "HEADLINE_PLAIN":  "El estrato más bajo sufre violencia económica al ",
        "HEADLINE_ITALIC": "doble del promedio.",

        "STAT1":           "44%",                  # número grande (3-4 chars máximo)
        "STAT1_P1":        "del estrato ",         # parte regular
        "STAT1_P2_BOLD":   "E (&lt;RD$10K)",       # parte bold (variable destacada)
        "STAT1_P3":        " sufre violencia económica en su entorno familiar.",  # parte regular

        "STAT2":           "20%",
        "STAT2_P1":        "es el ",
        "STAT2_P2_BOLD":   "promedio nacional",
        "STAT2_P3_FULL":   " de violencia económica en familias dominicanas.",

        "STAT3":           "2.3x",
        "STAT3_P1":        "más violencia vive el ",
        "STAT3_P2_BOLD":   "estrato E",
        "STAT3_P3":        " que el promedio. La pobreza agrava el abuso.",

        "CONCLUSION":      "...",                  # del análisis 190 chars
        "SOURCE":          "Source: ...",          # con la pregunta y el cruce
        "SLIDE_NAME_ATTR": 'name="Slide 4"',       # número del slide
    }

CARACTERES ESPECIALES EN XML:
    - "  →  &quot;
    - <  →  &lt;
    - >  →  &gt;
    - &  →  &amp;
"""

from pathlib import Path
import re

SLIDES_DIR = Path("/home/claude/unpacked/ppt/slides")
TEMPLATE_SLIDE = SLIDES_DIR / "slide2.xml"  # cualquier slide de hallazgo sirve


# =============================================================================
# CONFIGURACIÓN — Templates para reemplazar texto del slide 2 con marcadores
# =============================================================================
#
# Estos son los textos del slide 2 (template) que se reemplazan con marcadores.
# Si tu slide template viene de otro deck con diferentes textos, edita esta lista
# para que coincida con los textos reales de tu plantilla.

TEMPLATE_TO_MARKER = [
    # Source completo (más específico primero)
    ("Source: Código Casa — Estudio cuantitativo 2025 · P26, P54, P73 · Base 500.",
     "{{SOURCE}}"),

    # Conclusión italic
    ("La tranquilidad financiera emerge como el verdadero sueño dominicano, desplazando aspiraciones materiales.",
     "{{CONCLUSION}}"),

    # Headline split
    ("Dicen que la paz vale más que el dinero, pero admiten que ", "{{HEADLINE_PLAIN}}"),
    ("sin dinero no hay paz.", "{{HEADLINE_ITALIC}}"),

    # Stat 1 description (3 partes)
    ("nombra ", "{{STAT1_P1}}"),
    ("la economía", "{{STAT1_P2_BOLD}}"),
    (" como factor #1 de estrés, superando inseguridad, crianza y tiempo personal.", "{{STAT1_P3}}"),

    # Stat 2 description
    ("señala como ideal de vivienda ", "{{STAT2_P1}}"),
    ("&quot;tener una casa propia, no alquilada&quot;", "{{STAT2_P2_BOLD}}"),

    # Stat 3 description
    ("se siente ", "{{STAT3_P1}}"),
    ("&quot;nada preparado&quot;", "{{STAT3_P2_BOLD}}"),
    (" para la estabilidad financiera a largo plazo.", "{{STAT3_P3}}"),

    # Stats grandes (números)
    ("<a:t>48%</a:t>", "<a:t>{{STAT1}}</a:t>"),
    ("<a:t>46%</a:t>", "<a:t>{{STAT2}}</a:t>"),
    ("<a:t>62%</a:t>", "<a:t>{{STAT3}}</a:t>"),

    # Slide name attribute
    ('name="Slide 2"', '{{SLIDE_NAME_ATTR}}'),
]


# =============================================================================
# EDITA ESTE DICT CON LOS DATOS DE TUS CRUCES
# =============================================================================
#
# Las claves son los números de slide (4, 12, 20, 28, 36).
# Los valores son los datos para cada cruce.
#
# IMPORTANTE: cuida la longitud de los stats grandes — el slot visual soporta
# 3-4 caracteres. Si tu dato es "26.1%" se va a desbordar; usa "26%" y mete el
# decimal preciso en la descripción inline.

CRUCES = {
    # ---------- EJEMPLO: Tensión 6 — Violencia económica por NSE ----------
    # Comenta o borra este ejemplo y agrega los tuyos
    4: {
        "HEADLINE_PLAIN":  "El estrato más bajo sufre violencia económica al ",
        "HEADLINE_ITALIC": "doble del promedio.",
        "STAT1":           "44%",
        "STAT1_P1":        "del estrato ",
        "STAT1_P2_BOLD":   "E (&lt;RD$10K)",
        "STAT1_P3":        " sufre violencia económica en su entorno familiar.",
        "STAT2":           "20%",
        "STAT2_P1":        "es el ",
        "STAT2_P2_BOLD":   "promedio nacional",
        "STAT2_P3_FULL":   " de violencia económica en familias dominicanas.",
        "STAT3":           "2.3x",
        "STAT3_P1":        "más violencia vive el ",
        "STAT3_P2_BOLD":   "estrato E",
        "STAT3_P3":        " que el promedio. La pobreza agrava el abuso.",
        "CONCLUSION":      "Donde no hay casa propia ni ingreso estable, el dinero se convierte en mecanismo de control. La pobreza agrava el abuso.",
        "SOURCE":          "Source: Código Casa — Estudio cuantitativo 2025 · P77 · Cruce por NSE · Base 500.",
        "SLIDE_NAME_ATTR": 'name="Slide 4"',
    },

    # 12: { ... },
    # 20: { ... },
    # 28: { ... },
    # 36: { ... },
}


# =============================================================================
# LÓGICA — NO HACE FALTA EDITAR DEBAJO
# =============================================================================

def build_marked_template(template_xml: str) -> str:
    """Convierte el slide template en una plantilla con marcadores únicos."""
    result = template_xml
    for old_str, marker in TEMPLATE_TO_MARKER:
        if old_str not in result:
            print(f"  ⚠ NO encontrado en template: {old_str[:60]!r}")
            continue
        if result.count(old_str) > 1:
            print(f"  ⚠ AMBIGUO ({result.count(old_str)}x): {old_str[:60]!r}")
            continue
        result = result.replace(old_str, marker, 1)

    # Caso especial: stat 2 part 3 es "." en el template — lo reemplazamos
    # buscando el primer "<a:t>.</a:t>" después del marcador del bold de stat 2
    anchor = "{{STAT2_P2_BOLD}}</a:t>"
    target = "<a:t>.</a:t>"
    if anchor in result:
        idx = result.index(anchor)
        pos = result.find(target, idx)
        if pos != -1:
            result = result[:pos] + "<a:t>{{STAT2_P3_FULL}}</a:t>" + result[pos + len(target):]

    return result


def fill_template(marked: str, cruce_data: dict) -> str:
    """Llena la plantilla marcada con los datos del cruce."""
    result = marked
    for key, value in cruce_data.items():
        marker = "{{" + key + "}}"
        if marker not in result:
            print(f"  ⚠ Marcador no encontrado: {marker}")
            continue
        result = result.replace(marker, value)
    return result


def _pick_headline_size(headline_text: str) -> tuple[str, str, str]:
    """
    Elige el tamaño óptimo del headline según su largo en caracteres.
    Retorna (size_hundredths, box_height_emu, label_for_log).

    La caja del headline en el template está en posición y=914400 (top),
    y los stats grandes empiezan a y=2651760. Eso da ~1737000 EMU de altura
    máxima disponible. Las cajas y tamaños se eligen para que el texto NO
    invada el espacio de los stats.

    Tabla calibrada con pruebas visuales del deck Finanzas T6-T10:
      <30 chars  → 70pt (1 línea, cabe holgado)
      30-44      → 55pt (2 líneas)
      45-65      → 42pt (2-3 líneas, cabe limpio)
      66-85      → 36pt (3 líneas)
      >85        → 30pt (3-4 líneas)
    """
    n = len(headline_text.strip())
    if n < 30:
        return "7000", "1280160", "70pt"
    elif n < 45:
        return "5500", "1500000", "55pt"
    elif n < 66:
        return "4200", "1737000", "42pt"
    elif n < 86:
        return "3600", "1737000", "36pt"
    else:
        return "3000", "1737000", "30pt"


def upgrade_headline_auto_size(xml: str, headline_text: str = "", slide_label: str = "") -> str:
    """
    Aplica el estándar visual nuevo a los headlines de Hallazgo y Cruce:
    - MAYÚSCULAS (las strings ya deberían venir en mayúsculas desde CRUCES,
      pero igual hacemos uppercase por si acaso)
    - Tamaño AUTO según largo del texto del headline
    - Caja contenedora se expande proporcionalmente al tamaño elegido
    - Centrado al centro del slide (ya viene del template)

    El template original tiene el headline a 32pt (sz="3200"). Este método lo
    cambia al tamaño óptimo según el largo del headline pasado.
    """
    size_hundredths, new_box_height, size_label = _pick_headline_size(headline_text)

    if slide_label:
        chars = len(headline_text.strip())
        print(f"      [headline auto-size] slide{slide_label}: {chars} chars → {size_label}")

    # Cambiar tamaño 32pt → tamaño elegido
    xml = xml.replace('sz="3200"', f'sz="{size_hundredths}"')

    # Expandir caja contenedora del headline
    xml = xml.replace('cy="1280160"', f'cy="{new_box_height}"', 1)

    return xml


def main():
    if not TEMPLATE_SLIDE.exists():
        print(f"ERROR: {TEMPLATE_SLIDE} no existe.")
        return

    if not CRUCES:
        print("⚠ No hay cruces definidos. Edita el dict CRUCES al inicio del script.")
        return

    template_xml = TEMPLATE_SLIDE.read_text(encoding="utf-8")
    print("Construyendo plantilla marcada desde slide 2...")
    marked = build_marked_template(template_xml)

    expected_markers = [
        "{{HEADLINE_PLAIN}}", "{{HEADLINE_ITALIC}}",
        "{{STAT1}}", "{{STAT1_P1}}", "{{STAT1_P2_BOLD}}", "{{STAT1_P3}}",
        "{{STAT2}}", "{{STAT2_P1}}", "{{STAT2_P2_BOLD}}", "{{STAT2_P3_FULL}}",
        "{{STAT3}}", "{{STAT3_P1}}", "{{STAT3_P2_BOLD}}", "{{STAT3_P3}}",
        "{{CONCLUSION}}", "{{SOURCE}}", "{{SLIDE_NAME_ATTR}}",
    ]
    missing = [m for m in expected_markers if m not in marked]
    if missing:
        print(f"\n⚠ Marcadores faltantes en plantilla: {missing}")
        print("  Esto puede pasar si el slide 2 (template) tiene textos diferentes")
        print("  al esperado. Verifica TEMPLATE_TO_MARKER.")
        return

    print(f"\nLlenando {len(CRUCES)} slides de cruce...")
    for slide_num, cruce_data in CRUCES.items():
        # Aplicar regla nueva: HEADLINE en MAYÚSCULAS
        cruce_data = dict(cruce_data)  # copy para no mutar el original
        if "HEADLINE_PLAIN" in cruce_data:
            cruce_data["HEADLINE_PLAIN"] = cruce_data["HEADLINE_PLAIN"].upper()
        if "HEADLINE_ITALIC" in cruce_data:
            cruce_data["HEADLINE_ITALIC"] = cruce_data["HEADLINE_ITALIC"].upper()

        # Calcular largo total del headline (plain + italic) para auto-size
        headline_text = (
            cruce_data.get("HEADLINE_PLAIN", "") +
            cruce_data.get("HEADLINE_ITALIC", "")
        )

        new_xml = fill_template(marked, cruce_data)

        # Aplicar headline MAYÚSCULAS + tamaño auto según largo
        new_xml = upgrade_headline_auto_size(new_xml, headline_text, str(slide_num))

        leftover = re.findall(r"\{\{[A-Z0-9_]+\}\}", new_xml)
        if leftover:
            print(f"  ⚠ slide{slide_num}.xml — marcadores sin llenar: {set(leftover)}")
            continue

        out_path = SLIDES_DIR / f"slide{slide_num}.xml"
        out_path.write_text(new_xml, encoding="utf-8")
        print(f"  ✓ slide{slide_num}.xml — {cruce_data['STAT1']} | {cruce_data['STAT2']} | {cruce_data['STAT3']}")

    print(f"\n✓ {len(CRUCES)} cruces construidos.")
    print("  Headlines: MAYÚSCULAS centrado, tamaño auto según largo (45-90pt)")


if __name__ == "__main__":
    main()
