#!/usr/bin/env python3
"""
apply_design_fixes.py
======================
Aplica los fixes globales de diseño a un deck Código Casa MED desempacado:

1. Normaliza el kerning a spc="0" en todos los slides
2. Quita el "· [PILAR]" de los headers de slides intro (ej: "TENSIÓN 06 · FINANZAS" → "TENSIÓN 06")
3. Elimina los labels guía tipo "/ HALLAZGO ·", "/ CRUCE DE DATA ·", etc.
4. Cambia el color de los @usernames en slides de Conversación Digital de verde lima a blanco
5. Convierte los headlines de Hallazgo y Cruce a MAYÚSCULAS con tamaño AUTO según largo:
     <40 chars → 90pt   |   40-49 → 70pt   |   50-65 → 60pt
     66-80 → 50pt        |   >80 → 45pt
   La caja del headline se expande automáticamente para acomodar el texto.

USO:
    python apply_design_fixes.py

Antes de correr:
    - Tener el .pptx desempacado en /home/claude/unpacked/
    - Editar las constantes abajo si tu deck tiene una estructura distinta

ESTAS REGLAS APLICAN A CUALQUIER PILAR (Finanzas, Bienestar, Identidad, etc.)
porque son fixes de diseño globales, no específicos de data.
"""

import re
import os
from pathlib import Path

# =============================================================================
# CONFIGURACIÓN — EDITA SI TU DECK DIFIERE
# =============================================================================

# Carpeta de slides desempacados
SLIDES_DIR = Path("/home/claude/unpacked/ppt/slides")

# Patrones de labels guía a eliminar (todos los que empiecen con "/" arriba)
GUIDE_LABEL_PATTERNS = [
    r"/ HALLAZGO ·",
    r"/ CRUCE DE DATA ·",
    r"/ CONVERSACIÓN DIGITAL ·",
    r"/ CASO REFERENCIA ·",
]

# Patrones de "TENSIÓN 0X · [PILAR]" a limpiar a solo "TENSIÓN 0X".
# Edita esta lista con los pilares que aparezcan en tu deck.
INTRO_REPLACEMENTS = {
    # Finanzas
    "TENSIÓN 01 · FINANZAS": "TENSIÓN 01",
    "TENSIÓN 02 · FINANZAS": "TENSIÓN 02",
    "TENSIÓN 03 · FINANZAS": "TENSIÓN 03",
    "TENSIÓN 04 · FINANZAS": "TENSIÓN 04",
    "TENSIÓN 05 · FINANZAS": "TENSIÓN 05",
    # Si trabajas otro pilar, agrega aquí:
    # "TENSIÓN 06 · BIENESTAR": "TENSIÓN 06",
    # "TENSIÓN 07 · BIENESTAR": "TENSIÓN 07",
    # ...
}

# Slides donde van verbatims de social listening (cambia color a blanco)
# Por defecto: tensión X tiene su slide de Conv. Digital en posición 5 dentro del bloque
# Bloque T1 = slides 1-8, T2 = 9-16, T3 = 17-24, T4 = 25-32, T5 = 33-40
# Conv. Digital de cada uno = posición 5 → slides 5, 13, 21, 29, 37
SOCIAL_LISTENING_SLIDES = {
    "slide5.xml",
    "slide13.xml",
    "slide21.xml",
    "slide29.xml",
    "slide37.xml",
}

# Slides de Hallazgo y Cruce de Data — donde aplicar el headline 90pt MAYÚSCULAS
# Hallazgo en posición 2 → slides 2, 10, 18, 26, 34
# Cruce de Data en posición 4 → slides 4, 12, 20, 28, 36
HALLAZGO_AND_CRUCE_SLIDES = {
    "slide2.xml", "slide10.xml", "slide18.xml", "slide26.xml", "slide34.xml",
    "slide4.xml", "slide12.xml", "slide20.xml", "slide28.xml", "slide36.xml",
}

# Verde lima usado por error en verbatims (se cambia a blanco)
GREEN_HEX = "B8FF4D"
WHITE_HEX = "FFFFFF"


# =============================================================================
# FUNCIONES
# =============================================================================

def normalize_kerning(xml_content: str) -> str:
    """Replace any spc="N" with spc="0"."""
    return re.sub(r'spc="\d+"', 'spc="0"', xml_content)


def replace_intro_text(xml_content: str) -> str:
    """Remove '· [PILAR]' from intro slide headers."""
    for old, new in INTRO_REPLACEMENTS.items():
        xml_content = xml_content.replace(old, new)
    return xml_content


def remove_sp_with_text(xml_content: str, text_pattern: str) -> str:
    """
    Remove the entire <p:sp>...</p:sp> block that contains the given text.
    Used to delete guide labels.
    """
    sp_pattern = re.compile(
        r"      <p:sp>\n(?:.*?\n)*?      </p:sp>\n",
        re.DOTALL,
    )

    def keep_or_remove(match):
        block = match.group(0)
        if text_pattern in block:
            return ""
        return block

    return sp_pattern.sub(keep_or_remove, xml_content)


def green_to_white(xml_content: str) -> str:
    """Replace green text color (used incorrectly on @usernames) with white."""
    return xml_content.replace(
        f'srgbClr val="{GREEN_HEX}"',
        f'srgbClr val="{WHITE_HEX}"',
    )


def _extract_headline_text(xml_content: str) -> str:
    """
    Extrae el texto plano del headline (los runs con sz="3200") para medir su largo.
    Devuelve string vacío si no hay headline a 32pt.
    """
    # Busca todos los <a:t>...</a:t> dentro de runs con sz="3200"
    # El headline original viene a 32pt antes del upgrade
    matches = re.findall(
        r'<a:r>\s*<a:rPr[^>]*sz="3200"[^>]*>.*?<a:t(?:\s+xml:space="preserve")?>([^<]*)</a:t>.*?</a:r>',
        xml_content,
        flags=re.DOTALL,
    )
    return "".join(matches)


def _pick_headline_size(headline_text: str) -> tuple[str, str, str]:
    """
    Elige el tamaño óptimo del headline según su largo en caracteres.
    Retorna (size_hundredths, box_height_emu, label_for_log).

    La caja del headline en el template está en posición y=914400 (top),
    y los stats grandes empiezan a y=2651760. Eso da ~1737000 EMU de altura
    máxima disponible (~1.4 pulgadas, ~182pt). Las cajas y tamaños se eligen
    para que el texto NO invada el espacio de los stats.

    Tabla calibrada con pruebas visuales (deck Finanzas T6-T10 — todos los
    headlines son largos, 50-80 chars):
      <30 chars  → 70pt (1 línea, cabe holgado)
      30-44      → 55pt (2 líneas)
      45-65      → 42pt (2-3 líneas, cabe limpio)
      66-85      → 36pt (3 líneas)
      >85        → 30pt (3-4 líneas, raros)
    """
    n = len(headline_text.strip())
    # cy_emu corresponde al cy="..." del shape contenedor.
    # 1737000 es el máximo que cabe sin invadir los stats.
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


def upgrade_headline_to_uppercase(xml_content: str, slide_name: str = "") -> str:
    """
    Aplica el estándar visual nuevo a los headlines de Hallazgo y Cruce:
    - MAYÚSCULAS
    - Tamaño AUTO según largo del texto:
        <40 chars → 90pt   |   40-49 → 70pt   |   50-65 → 60pt
        66-80 → 50pt        |   >80 → 45pt
    - Caja contenedora del headline expandida proporcionalmente
    - Centrado vertical y horizontal (ya viene del template)

    Sólo se aplica a los slides de Hallazgo (2, 10, 18, 26, 34) y
    Cruce de Data (4, 12, 20, 28, 36).

    Si tu cliente insiste en 90pt independiente del largo, edita la función
    _pick_headline_size para que siempre retorne ("9000", "3657600", "90pt").
    Pero ojo: con headlines largos el texto se va a desbordar.
    """
    # Paso 1: extraer el texto actual del headline para decidir el tamaño
    headline_text = _extract_headline_text(xml_content)

    if not headline_text:
        # No se encontró headline a 32pt — no hacemos nada
        return xml_content

    size_hundredths, new_box_height, size_label = _pick_headline_size(headline_text)

    if slide_name:
        chars = len(headline_text.strip())
        print(f"      [headline auto-size] {slide_name}: {chars} chars → {size_label}")

    # Paso 2: cambiar tamaño 32pt → tamaño elegido
    xml_content = xml_content.replace('sz="3200"', f'sz="{size_hundredths}"')

    # Paso 3: expandir la caja del headline (solo la primera ocurrencia,
    # que es la del headline; las demás cy son de otros bloques del slide)
    OLD_HEADLINE_BOX_HEIGHT = 'cy="1280160"'
    NEW_BOX = f'cy="{new_box_height}"'
    xml_content = xml_content.replace(OLD_HEADLINE_BOX_HEIGHT, NEW_BOX, 1)

    # Paso 4: convertir a MAYÚSCULAS el contenido de los <a:t> dentro de runs
    # con el nuevo tamaño.
    def upper_in_run(match):
        run_xml = match.group(0)
        def upper_text(text_match):
            return f'<a:t>{text_match.group(1).upper()}</a:t>'
        run_xml = re.sub(r'<a:t>([^<]*)</a:t>', upper_text, run_xml)
        run_xml = re.sub(
            r'<a:t xml:space="preserve">([^<]*)</a:t>',
            lambda m: f'<a:t xml:space="preserve">{m.group(1).upper()}</a:t>',
            run_xml,
        )
        return run_xml

    xml_content = re.sub(
        rf'<a:r>\s*<a:rPr[^>]*sz="{size_hundredths}"[^>]*>.*?</a:r>',
        upper_in_run,
        xml_content,
        flags=re.DOTALL,
    )

    return xml_content


# Alias para compatibilidad con código que pueda llamar al nombre antiguo
upgrade_headline_to_90pt_uppercase = upgrade_headline_to_uppercase


def process_slide(slide_path: Path):
    """Apply all design fixes to a single slide XML."""
    content = slide_path.read_text(encoding="utf-8")
    original = content

    # 1. Normalize kerning (always)
    content = normalize_kerning(content)

    # 2. Clean intro headers
    content = replace_intro_text(content)

    # 3. Remove guide labels
    for pattern in GUIDE_LABEL_PATTERNS:
        content = remove_sp_with_text(content, pattern)

    # 4. Green to white on social listening slides
    if slide_path.name in SOCIAL_LISTENING_SLIDES:
        content = green_to_white(content)

    # 5. Upgrade headline to UPPERCASE + auto-size on Hallazgo and Cruce slides
    if slide_path.name in HALLAZGO_AND_CRUCE_SLIDES:
        content = upgrade_headline_to_uppercase(content, slide_path.name)

    if content != original:
        slide_path.write_text(content, encoding="utf-8")
        print(f"  ✓ modified: {slide_path.name}")
    else:
        print(f"    unchanged: {slide_path.name}")


def main():
    if not SLIDES_DIR.exists():
        print(f"ERROR: {SLIDES_DIR} no existe.")
        print("Primero desempaca el .pptx con:")
        print("  python /mnt/skills/public/pptx/scripts/office/unpack.py archivo.pptx /home/claude/unpacked/")
        return

    slides = sorted(
        SLIDES_DIR.glob("slide*.xml"),
        key=lambda p: int(re.search(r"\d+", p.name).group()),
    )
    print(f"Aplicando fixes globales a {len(slides)} slides...\n")
    for slide in slides:
        process_slide(slide)
    print("\n✓ Fixes globales aplicados.")


if __name__ == "__main__":
    main()
