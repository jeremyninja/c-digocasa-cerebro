#!/usr/bin/env python3
"""
fix_hallazgo_text.py
=====================
Aplica correcciones surgicales de texto a los slides de Hallazgo (slides 2, 10, 18, 26, 34)
para que coincidan con el .txt de hallazgos.

Cada corrección es un (slide, texto_actual, texto_correcto). El texto actual debe ser
único en el slide para que el reemplazo funcione.

USO:
    1. Edita la lista EDITS con tus cambios específicos
    2. Corre: python fix_hallazgo_text.py

CÓMO USARLO PARA UN PILAR DISTINTO:

Para cada slide de hallazgo (2, 10, 18, 26, 34):
    1. Abre el .txt y lee el bloque "HALLAZGO #XX" de la tensión correspondiente
    2. Compara con lo que dice el slide (mira el PDF generado)
    3. Para cada diferencia, agrega una entrada a EDITS:
        ("slide{N}.xml", "texto exacto que dice el slide", "texto correcto del .txt")

PROCESO PARA IDENTIFICAR DIFERENCIAS:

    a) Headline split → ¿coincide con el primer párrafo del hallazgo en el .txt?
    b) 3 stats → ¿los porcentajes redondeados coinciden? (47.8% → 48% es OK)
    c) Descripciones de stats → ¿el texto bajo cada stat coincide con el bullet del .txt?
    d) Citas inline (calidad 45.8%, salud 34.4%, etc.) → ¿se mantienen los decimales?
    e) Conclusión italic → ¿es una transcripción del .txt o tiene oraciones inventadas?
        SI tiene oraciones inventadas, eliminalas
    f) Source → ¿las preguntas referenciadas (P26, P54, P73) coinciden?
"""

from pathlib import Path

SLIDES_DIR = Path("/home/claude/unpacked/ppt/slides")


# =============================================================================
# EDITA ESTA LISTA CON LOS CAMBIOS ESPECÍFICOS DE TU DECK
# =============================================================================
#
# Formato: (slide_filename, old_string, new_string)
#
# Reglas:
#   - old_string debe ser único en el slide (si aparece 2+ veces, el script falla con WARNING)
#   - Los caracteres especiales en XML van escapados: " es &quot;, < es &lt;, > es &gt;
#   - Los espacios SÍ importan
#
# Tipos comunes de cambios:
#
#   1. Eliminar oraciones editoriales no presentes en el .txt:
#        ("slide2.xml",
#         "Texto que SÍ está en el .txt. Y luego una segunda oración inventada.",
#         "Texto que SÍ está en el .txt.")
#
#   2. Corregir punto vs coma en headlines:
#        ("slide2.xml",
#         "el dinero. Pero admiten",
#         "el dinero, pero admiten")
#
#   3. Corregir decimales en citas inline:
#        ("slide26.xml",
#         "calidad (46%) y salud (34%)",
#         "calidad (45.8%) y salud (34.4%)")
#
#   4. Corregir citas que cierran antes de tiempo:
#        ("slide2.xml",
#         "&quot;tener una casa propia&quot;",
#         "&quot;tener una casa propia, no alquilada&quot;")
#
# Ejemplos del deck Finanzas (T6-T10) — copia el patrón para tu pilar:

EDITS = [
    # ---------- SLIDE 2 — Tensión 6, Hallazgo #11 (EJEMPLO) ----------
    # Headline: punto → coma
    # ("slide2.xml",
    #  "Dicen que la paz vale más que el dinero. Pero admiten que ",
    #  "Dicen que la paz vale más que el dinero, pero admiten que "),

    # ---------- TUS EDITS AQUÍ ----------
    # ("slide2.xml", "old text", "new text"),
    # ("slide10.xml", "old text", "new text"),
    # ...
]


# =============================================================================
# LÓGICA — NO HACE FALTA EDITAR DEBAJO
# =============================================================================

def main():
    if not SLIDES_DIR.exists():
        print(f"ERROR: {SLIDES_DIR} no existe. Desempaca el .pptx primero.")
        return

    if not EDITS:
        print("⚠ No hay edits definidos. Edita la lista EDITS al inicio del script.")
        return

    print(f"Aplicando {len(EDITS)} correcciones de texto...\n")
    success = 0
    fail = 0

    for slide_name, old, new in EDITS:
        path = SLIDES_DIR / slide_name
        if not path.exists():
            print(f"  ✗ NO existe: {slide_name}")
            fail += 1
            continue

        content = path.read_text(encoding="utf-8")

        if old not in content:
            print(f"  ✗ NO encontrado en {slide_name}: {old[:80]!r}")
            fail += 1
            continue

        if content.count(old) > 1:
            print(f"  ⚠ AMBIGUO en {slide_name} ({content.count(old)}x): {old[:80]!r}")
            fail += 1
            continue

        new_content = content.replace(old, new, 1)
        path.write_text(new_content, encoding="utf-8")
        print(f"  ✓ {slide_name}: {old[:50]!r} → {new[:50]!r}")
        success += 1

    print(f"\n✓ {success} correcciones aplicadas")
    if fail > 0:
        print(f"✗ {fail} fallaron — revisa los warnings arriba")


if __name__ == "__main__":
    main()
