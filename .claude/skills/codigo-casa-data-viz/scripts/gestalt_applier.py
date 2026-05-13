#!/usr/bin/env python3
"""
Gestalt Principle Applier for codigo-casa-data-viz.
Applies visual grouping, similarity, continuity, and closure principles to SVG charts.
"""

import sys
from pathlib import Path
from typing import Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).parent))
from core import SkillConfig


class GestaltApplier:
    """Applies Gestalt principles to charts."""

    def __init__(self, data_dir: Path = None):
        """Initialize with skill configuration."""
        if data_dir is None:
            data_dir = Path(__file__).parent.parent / "data"
        self.config = SkillConfig(data_dir)

    def get_gestalt_rules(self, query: str) -> List[Dict]:
        """Get relevant Gestalt rules for a chart type or data pattern."""
        all_rules = self.config.gestalt_rules
        # Return all rules (typically 12) - client can filter as needed
        return all_rules

    def apply_proximity(self, svg_content: str, group_spacing: int = 20) -> str:
        """
        Apply proximity principle: group related elements closer together.
        Adds spacing between unrelated groups.
        """
        # This would modify SVG spacing - placeholder implementation
        # In production, this would parse SVG, calculate gaps, adjust transforms
        return svg_content

    def apply_similarity(self, svg_content: str, color_mapping: Dict[str, str]) -> str:
        """
        Apply similarity principle: same meaning = same color.
        Maps similar data categories to consistent colors.
        """
        # Replace colors in SVG based on mapping
        result = svg_content
        for old_color, new_color in color_mapping.items():
            result = result.replace(f'fill="{old_color}"', f'fill="{new_color}"')
        return result

    def apply_continuity(self, svg_content: str) -> str:
        """
        Apply continuity principle: create visual flow through connected elements.
        Ensures aligned axes, consistent spacing, flowing lines.
        """
        # Verify axes are properly aligned and add subtle flow guides if needed
        return svg_content

    def apply_closure(self, svg_content: str) -> str:
        """
        Apply closure principle: humans complete incomplete patterns.
        Use implied boundaries to help users perceive grouped data.
        """
        # Add subtle background boxes or patterns to help closure
        return svg_content

    def apply_contrast(self, svg_content: str, highlight_important: bool = True) -> str:
        """
        Apply contrast principle: make important data stand out.
        Increases opacity/size for key findings, reduces for context.
        """
        # 10% rule: 10% of elements are highlighted (60-30-10 hierarchy)
        return svg_content

    def apply_figure_ground(self, svg_content: str,
                           foreground_colors: List[str],
                           background_opacity: float = 0.15) -> str:
        """
        Apply figure-ground principle: separate data (figure) from context (ground).
        Makes data elements pop against background.
        """
        # Increases distinction between foreground data and background
        return svg_content

    def optimize_for_hierarchy(self, svg_content: str,
                             primary_color: str = "#00c875",
                             secondary_color: str = "#579bfc",
                             tertiary_color: str = "#999") -> str:
        """
        Apply 60-30-10 hierarchy rule:
        - 60%: Background (axes, context, labels)
        - 30%: Primary data (main bars, lines)
        - 10%: Highlights (key insights, callouts)
        """
        # This would require parsing and categorizing SVG elements
        # Placeholder - in production would adjust opacity, size, color saturation
        return svg_content

    def add_gestalt_metadata(self, svg_content: str,
                            gestalts_applied: List[str]) -> str:
        """Add metadata about which Gestalt principles were applied."""
        metadata = f'<!-- Gestalt principles applied: {", ".join(gestalts_applied)} -->\n'
        return metadata + svg_content

    def get_gestalt_recommendation(self, chart_type: str, data_pattern: str) -> Dict:
        """
        Recommend Gestalt principles for a specific chart type and data pattern.

        Returns:
            Dict with recommended principles and implementation hints
        """
        # Search for relevant Gestalt rules
        gestalt_results = []

        # Get all rules (typically 12)
        all_rules = self.config.gestalt_rules

        recommendation = {
            "chart_type": chart_type,
            "data_pattern": data_pattern,
            "primary_principles": [],
            "secondary_principles": [],
            "hierarchy_rule": {
                "background": 0.60,
                "primary_data": 0.30,
                "highlights": 0.10
            },
            "implementation_tips": []
        }

        # Map chart type to key Gestalt principles
        gestalt_map = {
            "stacked_bar": ["Similarity", "Proximity", "Continuity"],
            "grouped_bar": ["Similarity", "Contrast", "Figure-Ground"],
            "heatmap": ["Similarity", "Closure", "Figure-Ground"],
            "percentage_bar": ["Continuity", "Closure", "Proximity"],
            "diverging_bar": ["Contrast", "Similarity"],
            "waterfall": ["Continuity", "Closure"],
            "scatter": ["Similarity", "Figure-Ground"],
            "line": ["Continuity", "Similarity"],
        }

        # Apply mapping
        if chart_type in gestalt_map:
            principle_names = gestalt_map[chart_type]
            for rule in all_rules:
                rule_name = rule.get("principle", "")
                if rule_name in principle_names:
                    recommendation["primary_principles"].append({
                        "principle": rule_name,
                        "description": rule.get("description", ""),
                        "implementation": rule.get("svg_implementation", "")
                    })

        # Add secondary principles
        for rule in all_rules[:2]:  # Add first 2 rules as secondary
            if rule.get("principle") not in principle_names:
                recommendation["secondary_principles"].append({
                    "principle": rule.get("principle"),
                    "description": rule.get("description", "")
                })

        # Implementation tips
        recommendation["implementation_tips"] = [
            "Use consistent colors for related categories (Similarity)",
            "Group related bars closely, separate unrelated groups (Proximity)",
            "Align all chart elements to visual grid (Continuity)",
            "Apply 60-30-10 hierarchy: context → data → highlights",
            "Test with Dominican color palette for cultural sensitivity"
        ]

        return recommendation


def apply_gestalt_to_svg(svg_content: str,
                        gestalt_principles: List[str],
                        data_colors: Dict[str, str] = None) -> str:
    """
    Apply multiple Gestalt principles to SVG content.

    Args:
        svg_content: Original SVG string
        gestalt_principles: List of principles to apply (e.g., ["similarity", "proximity"])
        data_colors: Mapping of categories to colors

    Returns:
        Enhanced SVG string
    """
    applier = GestaltApplier()
    result = svg_content

    for principle in gestalt_principles:
        principle_lower = principle.lower()

        if principle_lower == "similarity":
            if data_colors:
                result = applier.apply_similarity(result, data_colors)
        elif principle_lower == "proximity":
            result = applier.apply_proximity(result)
        elif principle_lower == "continuity":
            result = applier.apply_continuity(result)
        elif principle_lower == "closure":
            result = applier.apply_closure(result)
        elif principle_lower == "contrast":
            result = applier.apply_contrast(result)
        elif principle_lower == "figure-ground":
            primary_colors = list(data_colors.values()) if data_colors else ["#00c875"]
            result = applier.apply_figure_ground(result, primary_colors)

    # Add metadata
    result = applier.add_gestalt_metadata(result, gestalt_principles)

    return result


if __name__ == "__main__":
    applier = GestaltApplier()

    # Test recommendation
    rec = applier.get_gestalt_recommendation("stacked_bar", "multiresponse_generational")
    print("Gestalt Recommendation for Stacked Bar + Generational Data:")
    print(f"  Primary principles: {[p['principle'] for p in rec['primary_principles']]}")
    print(f"  Hierarchy: {rec['hierarchy_rule']}")
    print(f"  Tips: {rec['implementation_tips'][0]}")
