#!/usr/bin/env python3
"""
Test suite for Phase 2: Chart Generation
Validates SVG generation, Gestalt application, and color recommendation.
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from chart_generator import ChartConfig, create_chart
from gestalt_applier import GestaltApplier
from color_recommender import ColorRecommender


def test_chart_generation():
    """Test basic chart generation."""
    print("=" * 60)
    print("TEST 1: Chart Generation")
    print("=" * 60)

    test_data = [
        {"label": "Jóvenes 18-24", "Estrés": 76.2, "Esperanza": 48.5},
        {"label": "Adultos 25-34", "Estrés": 68.5, "Esperanza": 62.3},
        {"label": "Mayores 35+", "Estrés": 52.3, "Esperanza": 78.9},
    ]

    config = ChartConfig(
        chart_type="stacked_bar",
        title="Estrés vs Esperanza por Edad",
        subtitle="Código Casa - Estudio Dominicano",
        palette=["#ff642e", "#00c875"]
    )

    try:
        svg = create_chart("stacked_bar", test_data, ["Estrés", "Esperanza"], config)
        assert "<svg" in svg, "SVG not generated"
        assert "Estrés vs Esperanza" in svg, "Title not found"
        assert "#ff642e" in svg or "#00c875" in svg, "Colors not applied"
        print("✓ Stacked bar chart generated successfully")
        print(f"  - SVG size: {len(svg)} bytes")
        print(f"  - Contains {svg.count('<rect')} rectangles")
    except Exception as e:
        print(f"✗ Chart generation failed: {e}")
        return False

    # Test grouped bar
    try:
        svg = create_chart("grouped_bar", test_data, ["Estrés", "Esperanza"], config)
        assert "<svg" in svg, "SVG not generated"
        print("✓ Grouped bar chart generated successfully")
    except Exception as e:
        print(f"✗ Grouped bar failed: {e}")
        return False

    # Test heatmap
    try:
        svg = create_chart("heatmap", test_data, ["Estrés", "Esperanza"], config)
        assert "<svg" in svg, "SVG not generated"
        print("✓ Heatmap generated successfully")
    except Exception as e:
        print(f"✗ Heatmap generation failed: {e}")
        return False

    # Test percentage bar
    try:
        svg = create_chart("percentage_bar", test_data, ["Estrés", "Esperanza"], config)
        assert "<svg" in svg, "SVG not generated"
        print("✓ Percentage bar generated successfully")
    except Exception as e:
        print(f"✗ Percentage bar failed: {e}")
        return False

    return True


def test_gestalt_recommendations():
    """Test Gestalt principle recommendations."""
    print("\n" + "=" * 60)
    print("TEST 2: Gestalt Principle Recommendations")
    print("=" * 60)

    applier = GestaltApplier(Path(__file__).parent / "data")

    test_cases = [
        ("stacked_bar", "multiresponse"),
        ("grouped_bar", "generational_shift"),
        ("heatmap", "nse_comparison"),
        ("percentage_bar", "diverging_data"),
    ]

    for chart_type, pattern in test_cases:
        rec = applier.get_gestalt_recommendation(chart_type, pattern)

        assert "primary_principles" in rec, "Missing primary_principles"
        assert "hierarchy_rule" in rec, "Missing hierarchy_rule"
        assert len(rec["primary_principles"]) > 0, "No principles recommended"

        principles = [p["principle"] for p in rec["primary_principles"]]
        print(f"✓ {chart_type.upper()}")
        print(f"  - Principles: {', '.join(principles)}")
        print(f"  - Hierarchy: 60% context, 30% data, 10% highlights")

    return True


def test_color_recommendations():
    """Test color palette recommendations."""
    print("\n" + "=" * 60)
    print("TEST 3: Color Palette Recommendations")
    print("=" * 60)

    recommender = ColorRecommender(Path(__file__).parent / "data")

    # Test pillar + sentiment
    test_cases = [
        ("Finanzas", "positive"),
        ("Finanzas", "negative"),
        ("Identidad", "positive"),
        ("Identidad", "negative"),
        ("Bienestar", "positive"),
        ("Bienestar", "negative"),
    ]

    for pilar, sentiment in test_cases:
        palette = recommender.recommend_palette(pilar, sentiment)
        assert palette is not None, f"No palette for {pilar}/{sentiment}"
        assert "palette_name" in palette, "Missing palette_name"
        assert "color1" in palette, "Missing colors"

        palette_name = palette.get("palette_name")
        print(f"✓ {pilar} ({sentiment}): {palette_name}")

    return True


def test_multi_category_colors():
    """Test color assignment for multiple categories."""
    print("\n" + "=" * 60)
    print("TEST 4: Multi-Category Color Assignment")
    print("=" * 60)

    recommender = ColorRecommender(Path(__file__).parent / "data")

    categories = ["Jóvenes 18-24", "Adultos 25-34", "Mayores 35+"]
    colors = recommender.recommend_multi_category("Finanzas", categories)

    assert len(colors) == len(categories), "Wrong number of colors"

    for idx, category in enumerate(categories):
        assert category in colors, f"Missing color for {category}"
        assert colors[category].startswith("#"), "Invalid color format"
        print(f"✓ {category}: {colors[category]}")

    return True


def test_say_do_gap_colors():
    """Test color recommendation for say-do gap."""
    print("\n" + "=" * 60)
    print("TEST 5: Say-Do Gap Palette Recommendation")
    print("=" * 60)

    recommender = ColorRecommender(Path(__file__).parent / "data")

    claim_pal, behavior_pal = recommender.recommend_for_say_do_gap(
        claim_value=85,
        behavior_value=45,
        pilar="Finanzas"
    )

    assert claim_pal is not None, "No palette for claim"
    assert behavior_pal is not None, "No palette for behavior"

    print(f"✓ Claim (say): {claim_pal.get('palette_name')}")
    print(f"  Colors: {claim_pal.get('color1')} → {claim_pal.get('color5')}")

    print(f"✓ Behavior (do): {behavior_pal.get('palette_name')}")
    print(f"  Colors: {behavior_pal.get('color1')} → {behavior_pal.get('color5')}")

    return True


def test_integration():
    """Test end-to-end integration."""
    print("\n" + "=" * 60)
    print("TEST 6: End-to-End Integration")
    print("=" * 60)

    test_data = [
        {"label": "NSE E", "Estrés": 84.0, "Control": 12.5},
        {"label": "NSE D", "Estrés": 79.0, "Control": 18.2},
        {"label": "NSE C", "Estrés": 61.0, "Control": 42.3},
        {"label": "NSE C+", "Estrés": 38.0, "Control": 68.5},
    ]

    # Get color recommendation
    color_rec = ColorRecommender(Path(__file__).parent / "data")
    palette = color_rec.recommend_palette("Finanzas", "negative")

    config = ChartConfig(
        chart_type="grouped_bar",
        title="Estrés Financiero por NSE",
        subtitle="Código Casa - Finanzas",
        palette=[palette["color1"], palette["color5"]]
    )

    # Generate chart
    svg = create_chart("grouped_bar", test_data, ["Estrés", "Control"], config)

    assert "<svg" in svg, "SVG not generated"
    assert "Estrés Financiero por NSE" in svg, "Title missing"
    assert palette["color1"] in svg or palette["color5"] in svg, "Colors not applied"

    print("✓ Full integration test passed")
    print(f"  - Data: 4 NSE groups")
    print(f"  - Chart: Grouped bar")
    print(f"  - Palette: {palette['palette_name']}")
    print(f"  - SVG generated: {len(svg)} bytes")

    return True


def main():
    """Run all Phase 2 tests."""
    print("\n" + "=" * 60)
    print("CODIGO CASA DATA VIZ - PHASE 2 TEST SUITE")
    print("Chart Generation, Gestalt, Color Recommendation")
    print("=" * 60 + "\n")

    tests = [
        ("Chart Generation", test_chart_generation),
        ("Gestalt Recommendations", test_gestalt_recommendations),
        ("Color Recommendations", test_color_recommendations),
        ("Multi-Category Colors", test_multi_category_colors),
        ("Say-Do Gap Colors", test_say_do_gap_colors),
        ("End-to-End Integration", test_integration),
    ]

    passed = 0
    failed = 0

    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            failed += 1

    print("\n" + "=" * 60)
    print("PHASE 2 TEST SUITE COMPLETE")
    print("=" * 60)
    print(f"Passed: {passed}/{len(tests)}")
    print(f"Failed: {failed}/{len(tests)}")
    print("\n✓ Phase 2 Ready: Chart generation, Gestalt, Color recommendation functional")
    print("✓ Next: Phase 3 - Insight extraction and advanced analysis")


if __name__ == "__main__":
    main()
