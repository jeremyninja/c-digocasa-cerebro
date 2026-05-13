#!/usr/bin/env python3
"""
Color Recommender for codigo-casa-data-viz.
Maps pillars and data patterns to appropriate Dominican color palettes.
"""

import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

sys.path.insert(0, str(Path(__file__).parent))
from core import SkillConfig


class ColorRecommender:
    """Recommends Dominican color palettes based on context."""

    def __init__(self, data_dir: Path = None):
        """Initialize with skill configuration."""
        if data_dir is None:
            data_dir = Path(__file__).parent.parent / "data"
        self.config = SkillConfig(data_dir)

    def recommend_palette(self, pilar: str, sentiment: str = "neutral") -> Optional[Dict]:
        """
        Recommend a palette based on pillar and sentiment.

        Args:
            pilar: One of "Identidad", "Finanzas", "Bienestar"
            sentiment: One of "positive", "negative", "neutral", "alert"

        Returns:
            Dictionary with palette name and color list, or None if not found
        """
        # Map pilar + sentiment to palette name
        palette_map = {
            ("Identidad", "positive"): "DOMINICAN_IDENTITY_HOPE",
            ("Identidad", "negative"): "DOMINICAN_IDENTITY_TENSION",
            ("Finanzas", "positive"): "DOMINICAN_FINANCE_GROWTH",
            ("Finanzas", "negative"): "DOMINICAN_FINANCE_STRUGGLE",
            ("Bienestar", "positive"): "DOMINICAN_HEALTH_CARE",
            ("Bienestar", "negative"): "DOMINICAN_HEALTH_CRISIS",
            ("neutral", "neutral"): "DOMINICAN_NEUTRAL",
            ("alert", "alert"): "DOMINICAN_ALERT",
        }

        palette_name = palette_map.get((pilar, sentiment))
        if palette_name is None:
            # Fallback to neutral
            palette_name = "DOMINICAN_NEUTRAL"

        palette = self.config.get_palette(palette_name)
        if palette:
            palette["palette_name"] = palette_name
        return palette

    def recommend_by_threshold(self, pilar: str, value: float,
                              positive_threshold: float = 50.0) -> Optional[Dict]:
        """
        Recommend palette based on data value and threshold.

        Args:
            pilar: One of "Identidad", "Finanzas", "Bienestar"
            value: Numeric value (0-100 or percentage)
            positive_threshold: Value above this is considered positive

        Returns:
            Recommended palette
        """
        sentiment = "positive" if value >= positive_threshold else "negative"
        return self.recommend_palette(pilar, sentiment)

    def recommend_by_tension(self, tension_name: str) -> Optional[Dict]:
        """
        Recommend palette based on tension type.

        Args:
            tension_name: Name of the tension (e.g., "Estrés financiero")

        Returns:
            Recommended palette
        """
        # Search for tension in tension indicators
        tension_results = self.config.search_tensions(tension_name, top_k=1)

        if tension_results:
            score, tension_doc = tension_results[0]
            pilar = tension_doc.get("pilar", "neutral")

            # Determine sentiment based on tension type
            negative_keywords = ["estrés", "presión", "ansiedad", "crisis", "miedo", "riesgo"]
            tension_lower = tension_name.lower()
            is_negative = any(kw in tension_lower for kw in negative_keywords)

            sentiment = "negative" if is_negative else "positive"
            return self.recommend_palette(pilar, sentiment)

        return self.recommend_palette("neutral", "neutral")

    def recommend_multi_category(self, pilar: str, categories: List[str],
                                 sentiments: List[str] = None) -> Dict[str, List[str]]:
        """
        Recommend color assignments for multiple categories.

        Args:
            pilar: One of "Identidad", "Finanzas", "Bienestar"
            categories: List of category names
            sentiments: Optional list of sentiments per category

        Returns:
            Dictionary mapping category → color
        """
        if sentiments is None:
            sentiments = ["neutral"] * len(categories)

        # Get base palette
        palette = self.recommend_palette(pilar, "neutral")
        if not palette:
            # Fallback to default palette
            palette = {
                "palette_name": "DOMINICAN_NEUTRAL",
                "color1": "#037f4c",
                "color2": "#579bfc",
                "color3": "#ffcb00",
                "color4": "#ff642e",
                "color5": "#bb3354"
            }

        # Extract colors in order
        colors = [
            palette.get("color1", "#037f4c"),
            palette.get("color2", "#579bfc"),
            palette.get("color3", "#ffcb00"),
            palette.get("color4", "#ff642e"),
            palette.get("color5", "#bb3354"),
        ]

        # Assign colors to categories (cycle if more categories than colors)
        color_mapping = {}
        for idx, category in enumerate(categories):
            color_mapping[category] = colors[idx % len(colors)]

        return color_mapping

    def get_palette_info(self, palette_name: str) -> Optional[Dict]:
        """Get detailed information about a palette."""
        palette = self.config.get_palette(palette_name)
        if palette:
            # Add color list for convenience
            colors = [
                palette.get("color1"),
                palette.get("color2"),
                palette.get("color3"),
                palette.get("color4"),
                palette.get("color5"),
            ]
            palette["colors"] = [c for c in colors if c]
        return palette

    def analyze_data_sentiment(self, data: List[Dict], value_column: str) -> str:
        """
        Analyze data to determine overall sentiment.

        Args:
            data: List of data dictionaries
            value_column: Column name with numeric values

        Returns:
            Sentiment: "positive", "negative", or "mixed"
        """
        values = []
        for row in data:
            try:
                val = float(row.get(value_column, 0))
                values.append(val)
            except (ValueError, TypeError):
                pass

        if not values:
            return "neutral"

        avg_value = sum(values) / len(values)

        # Threshold: >60 is positive, <40 is negative, in between is mixed
        if avg_value > 60:
            return "positive"
        elif avg_value < 40:
            return "negative"
        else:
            return "mixed"

    def get_contrasting_palette(self, base_palette_name: str) -> Optional[Dict]:
        """Get a contrasting palette for comparison."""
        contrasts = {
            "DOMINICAN_IDENTITY_HOPE": "DOMINICAN_IDENTITY_TENSION",
            "DOMINICAN_IDENTITY_TENSION": "DOMINICAN_IDENTITY_HOPE",
            "DOMINICAN_FINANCE_GROWTH": "DOMINICAN_FINANCE_STRUGGLE",
            "DOMINICAN_FINANCE_STRUGGLE": "DOMINICAN_FINANCE_GROWTH",
            "DOMINICAN_HEALTH_CARE": "DOMINICAN_HEALTH_CRISIS",
            "DOMINICAN_HEALTH_CRISIS": "DOMINICAN_HEALTH_CARE",
        }

        contrast_name = contrasts.get(base_palette_name)
        if contrast_name:
            return self.config.get_palette(contrast_name)
        return None

    def recommend_for_say_do_gap(self, claim_value: float,
                                behavior_value: float,
                                pilar: str = "Finanzas") -> Tuple[Dict, Dict]:
        """
        Recommend palettes for say-do gap comparison.

        Args:
            claim_value: What people say (0-100)
            behavior_value: What people do (0-100)
            pilar: Pillar context

        Returns:
            Tuple of (claim_palette, behavior_palette)
        """
        claim_sentiment = "positive" if claim_value > 50 else "negative"
        behavior_sentiment = "positive" if behavior_value > 50 else "negative"

        claim_palette = self.recommend_palette(pilar, claim_sentiment)
        behavior_palette = self.recommend_palette(pilar, behavior_sentiment)

        # If they're the same, adjust one to be lighter/more opaque
        return (claim_palette, behavior_palette)

    def get_wcag_contrasts(self, palette_name: str) -> Dict[str, str]:
        """Get WCAG AA compliance info for palette."""
        palette = self.get_palette_info(palette_name)
        if palette:
            return {
                "palette": palette_name,
                "wcag_compliance": palette.get("wcag_aa_compliance", "unknown"),
                "notes": palette.get("accessibility_notes", "")
            }
        return {}


def get_color_for_category(category: str, pilar: str = "neutral") -> str:
    """
    Quick function to get a color for a single category.

    Args:
        category: Category name
        pilar: Optional pillar context

    Returns:
        Hex color string
    """
    recommender = ColorRecommender()

    # Try to detect sentiment from category name
    negative_keywords = ["estrés", "presión", "riesgo", "problema", "crisis"]
    is_negative = any(kw in category.lower() for kw in negative_keywords)

    sentiment = "negative" if is_negative else "positive"
    palette = recommender.recommend_palette(pilar, sentiment)

    if palette:
        return palette.get("color1", "#579bfc")
    return "#579bfc"  # Fallback


if __name__ == "__main__":
    recommender = ColorRecommender()

    # Test 1: Recommend by pillar + sentiment
    print("Test 1: Palette for Finanzas + Negative")
    palette = recommender.recommend_palette("Finanzas", "negative")
    if palette:
        print(f"  Palette: {palette['palette_name']}")
        print(f"  Colors: {[palette['color1'], palette['color2'], palette['color3']]}")

    # Test 2: Multi-category assignment
    print("\nTest 2: Multi-category colors")
    categories = ["Jóvenes 18-24", "Adultos 25-34", "Mayores 35+"]
    colors = recommender.recommend_multi_category("Finanzas", categories)
    for cat, color in colors.items():
        print(f"  {cat}: {color}")

    # Test 3: Say-do gap
    print("\nTest 3: Say-Do Gap Palettes")
    claim_pal, behavior_pal = recommender.recommend_for_say_do_gap(85, 45, "Finanzas")
    print(f"  Claim (dicen): {claim_pal['palette_name']}")
    print(f"  Behavior (hacen): {behavior_pal['palette_name']}")
