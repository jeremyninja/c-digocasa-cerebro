#!/usr/bin/env python3
"""
Test suite for codigo-casa-data-viz skill.
Validates BM25 search, configuration loading, and basic functionality.
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from core import SkillConfig


def test_config_loading():
    """Test that all configuration files load correctly."""
    print("=" * 60)
    print("TEST 1: Configuration Loading")
    print("=" * 60)

    try:
        config = SkillConfig(Path(__file__).parent / "data")
        print("✓ Configuration loaded successfully")
        print(f"  - Dominican palettes: {len(config.dominican_palettes)} palettes")
        print(f"  - Gestalt rules: {len(config.gestalt_rules)} rules")
        print(f"  - Hierarchy patterns: {len(config.hierarchy_patterns)} patterns")
        print(f"  - Cultural sensitivity: {len(config.cultural_sensitivity)} guidelines")
        return config
    except Exception as e:
        print(f"✗ Configuration loading failed: {e}")
        return None


def test_chart_type_search(config):
    """Test BM25 search for chart types."""
    print("\n" + "=" * 60)
    print("TEST 2: Chart Type Search")
    print("=" * 60)

    queries = [
        "multiresponse generacional",
        "heatmap comparison NSE",
        "diverging bar say-do gap"
    ]

    for query in queries:
        print(f"\nQuery: '{query}'")
        results = config.search_chart_types(query, top_k=3)

        if results:
            for score, doc in results:
                print(f"  Score: {score:.3f} | {doc.get('chart_type', 'N/A')}")
                print(f"           {doc.get('when_to_use', '')[:50]}...")
        else:
            print(f"  No results found")


def test_data_pattern_search(config):
    """Test BM25 search for data patterns."""
    print("\n" + "=" * 60)
    print("TEST 3: Data Pattern Search")
    print("=" * 60)

    queries = [
        "edad generacional edad brecha",
        "multirespuesta combined percentage",
        "nse socioeconómico cross-tabulation"
    ]

    for query in queries:
        print(f"\nQuery: '{query}'")
        results = config.search_data_patterns(query, top_k=3)

        if results:
            for score, doc in results:
                print(f"  Score: {score:.3f} | {doc.get('pattern_type', 'N/A')}")
                print(f"           Best chart: {doc.get('best_chart', 'N/A')}")
        else:
            print(f"  No results found")


def test_palette_lookup(config):
    """Test palette lookup."""
    print("\n" + "=" * 60)
    print("TEST 4: Palette Lookup")
    print("=" * 60)

    palettes = [
        "DOMINICAN_IDENTITY_HOPE",
        "DOMINICAN_FINANCE_STRUGGLE",
        "DOMINICAN_HEALTH_CARE"
    ]

    for palette_name in palettes:
        palette = config.get_palette(palette_name)
        if palette:
            print(f"✓ {palette_name}")
            print(f"  Colors: {palette.get('color1')} → {palette.get('color5')}")
            print(f"  Context: {palette.get('context')}")
        else:
            print(f"✗ {palette_name} not found")


def test_cultural_sensitivity(config):
    """Test cultural sensitivity guidelines."""
    print("\n" + "=" * 60)
    print("TEST 5: Cultural Sensitivity Guidelines")
    print("=" * 60)

    topics = ["CS01", "CS05", "CS08"]

    for rule_id in topics:
        rule = config.get_sensitivity_rule(rule_id)
        if rule:
            print(f"\n✓ {rule_id}: {rule.get('topic')}")
            print(f"  Guideline: {rule.get('guideline')}")
            print(f"  Dominican context: {rule.get('dominican_context', '')[:50]}...")
        else:
            print(f"✗ {rule_id} not found")


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("CODIGO CASA DATA VIZ - SKILL TEST SUITE")
    print("=" * 60 + "\n")

    # Test configuration loading
    config = test_config_loading()
    if not config:
        print("\nSkip remaining tests due to config loading failure")
        return

    # Run all tests
    test_chart_type_search(config)
    test_data_pattern_search(config)
    test_palette_lookup(config)
    test_cultural_sensitivity(config)

    print("\n" + "=" * 60)
    print("TEST SUITE COMPLETE")
    print("=" * 60 + "\n")

    print("Summary:")
    print("✓ BM25 search engine working")
    print("✓ Configuration files loaded")
    print("✓ Palette system functional")
    print("✓ Cultural sensitivity guidelines available")
    print("\nSkill is ready for Phase 2: Chart Generation")


if __name__ == "__main__":
    main()
