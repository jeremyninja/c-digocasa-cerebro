#!/usr/bin/env python3
"""
CLI for codigo-casa-data-viz skill.
Search, recommend, and generate charts from the command line.
"""

import sys
import argparse
import json
import csv
from pathlib import Path
from typing import List, Dict

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from core import SkillConfig
from chart_generator import ChartConfig, ChartGenerator, create_chart
from gestalt_applier import GestaltApplier
from color_recommender import ColorRecommender


class ChartRecommender:
    """Recommends charts based on data patterns and pillar context."""

    def __init__(self):
        data_dir = Path(__file__).parent.parent / "data"
        self.config = SkillConfig(data_dir)
        self.gestalt = GestaltApplier(data_dir)
        self.colors = ColorRecommender(data_dir)

    def recommend_chart(self, query: str, pilar: str = None,
                       top_k: int = 3) -> List[Dict]:
        """
        Recommend chart types for a query.

        Args:
            query: Description of data or desired visualization
            pilar: Optional pillar context (Identidad, Finanzas, Bienestar)
            top_k: Number of recommendations

        Returns:
            List of chart recommendations
        """
        # Search chart types
        chart_results = self.config.search_chart_types(query, top_k=top_k)
        # Search data patterns
        pattern_results = self.config.search_data_patterns(query, top_k=top_k)

        recommendations = []

        # Process chart results
        for score, chart_doc in chart_results:
            chart_type = chart_doc.get("chart_type", "unknown")
            data_type = chart_doc.get("data_type", "unknown")

            # Get Gestalt recommendation
            gestalt_rec = self.gestalt.get_gestalt_recommendation(
                chart_type, "general"
            )

            # Get color palette
            palette = self.colors.recommend_palette(pilar or "Finanzas", "neutral")

            recommendation = {
                "rank": len(recommendations) + 1,
                "chart_type": chart_type,
                "data_type": data_type,
                "relevance_score": round(score, 3),
                "when_to_use": chart_doc.get("when_to_use", ""),
                "gestalt_principles": [
                    p["principle"] for p in gestalt_rec.get("primary_principles", [])
                ],
                "recommended_palette": palette.get("palette_name") if palette else None,
                "colors": [
                    palette.get("color1"),
                    palette.get("color2"),
                    palette.get("color3")
                ] if palette else [],
            }
            recommendations.append(recommendation)

        return recommendations

    def analyze_csv(self, csv_path: str) -> Dict:
        """
        Analyze a CSV file to detect data structure.

        Args:
            csv_path: Path to CSV file

        Returns:
            Dictionary with analysis results
        """
        csv_file = Path(csv_path)
        if not csv_file.exists():
            return {"error": f"File not found: {csv_path}"}

        analysis = {
            "file": csv_path,
            "rows": 0,
            "columns": [],
            "column_types": {},
            "suggested_visualizations": [],
        }

        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            columns = reader.fieldnames or []
            analysis["columns"] = columns
            analysis["column_types"] = {col: "unknown" for col in columns}

            # Count rows and detect column types
            row_count = 0
            for row in reader:
                row_count += 1

                # Detect column types
                for col, value in row.items():
                    if not value:
                        continue

                    try:
                        float(value.strip('%'))
                        analysis["column_types"][col] = "numeric"
                    except ValueError:
                        analysis["column_types"][col] = "text"

            analysis["rows"] = row_count

        # Suggest visualizations based on structure
        numeric_cols = [c for c, t in analysis["column_types"].items() if t == "numeric"]

        if len(numeric_cols) > 2:
            analysis["suggested_visualizations"] = [
                "stacked_bar",
                "heatmap",
                "percentage_bar"
            ]
        elif len(numeric_cols) == 2:
            analysis["suggested_visualizations"] = [
                "grouped_bar",
                "scatter"
            ]
        elif len(numeric_cols) == 1:
            analysis["suggested_visualizations"] = [
                "bar_chart",
                "percentage_bar"
            ]

        return analysis

    def generate_from_csv(self, csv_path: str, chart_type: str,
                         categories: List[str], pilar: str = "Finanzas",
                         title: str = None) -> str:
        """
        Generate a chart from CSV data.

        Args:
            csv_path: Path to CSV file
            chart_type: Type of chart to generate
            categories: List of column names to visualize
            pilar: Pillar context (for color selection)
            title: Optional chart title

        Returns:
            SVG string
        """
        csv_file = Path(csv_path)
        if not csv_file.exists():
            return f"<!-- Error: File not found: {csv_path} -->"

        # Load CSV data
        data = []
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        if not data:
            return "<!-- Error: No data in CSV -->"

        # Get palette
        color_recommender = ColorRecommender(
            Path(__file__).parent.parent / "data"
        )
        palette_data = color_recommender.recommend_palette(pilar, "neutral")
        palette = [
            palette_data.get("color1"),
            palette_data.get("color2"),
            palette_data.get("color3"),
            palette_data.get("color4"),
            palette_data.get("color5"),
        ] if palette_data else ["#00c875", "#579bfc", "#ffcb00", "#ff642e", "#bb3354"]

        # Create chart config
        if title is None:
            title = f"{chart_type.replace('_', ' ').title()} Chart"

        config = ChartConfig(
            chart_type=chart_type,
            title=title,
            subtitle=f"Código Casa - {pilar}",
            palette=palette
        )

        # Generate chart
        try:
            svg = create_chart(chart_type, data, categories, config)
            return svg
        except Exception as e:
            return f"<!-- Error generating chart: {str(e)} -->"


def main():
    parser = argparse.ArgumentParser(
        description="Código Casa Data Viz - Advanced chart generation CLI"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search for chart recommendations")
    search_parser.add_argument("query", help="Search query (data pattern or visualization type)")
    search_parser.add_argument("--pilar", default="Finanzas",
                             help="Pillar context (Identidad, Finanzas, Bienestar)")
    search_parser.add_argument("--top-k", type=int, default=3,
                             help="Number of recommendations to return")

    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze CSV file structure")
    analyze_parser.add_argument("file", help="Path to CSV file")

    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate chart from CSV")
    gen_parser.add_argument("file", help="Path to CSV file")
    gen_parser.add_argument("--chart-type", default="stacked_bar",
                          help="Type of chart (stacked_bar, grouped_bar, heatmap, etc.)")
    gen_parser.add_argument("--categories", nargs="+", required=True,
                          help="Column names to visualize")
    gen_parser.add_argument("--pilar", default="Finanzas",
                          help="Pillar context")
    gen_parser.add_argument("--title", help="Chart title")
    gen_parser.add_argument("--output", help="Output SVG file path")

    args = parser.parse_args()

    recommender = ChartRecommender()

    if args.command == "search":
        print("\n" + "=" * 70)
        print("CHART RECOMMENDATIONS")
        print("=" * 70)
        print(f"Query: {args.query}")
        print(f"Pilar: {args.pilar}")
        print()

        recommendations = recommender.recommend_chart(
            args.query, args.pilar, args.top_k
        )

        for rec in recommendations:
            print(f"[{rec['rank']}] {rec['chart_type'].upper()}")
            print(f"    Relevance: {rec['relevance_score']}")
            print(f"    When to use: {rec['when_to_use'][:60]}...")
            print(f"    Gestalt principles: {', '.join(rec['gestalt_principles'])}")
            print(f"    Palette: {rec['recommended_palette']}")
            print()

        print("=" * 70)

    elif args.command == "analyze":
        print("\n" + "=" * 70)
        print("CSV ANALYSIS")
        print("=" * 70)

        analysis = recommender.analyze_csv(args.file)

        if "error" in analysis:
            print(f"Error: {analysis['error']}")
        else:
            print(f"File: {analysis['file']}")
            print(f"Rows: {analysis['rows']}")
            print(f"Columns: {', '.join(analysis['columns'])}")
            print()
            print("Column types:")
            for col, col_type in analysis["column_types"].items():
                print(f"  {col}: {col_type}")
            print()
            print("Suggested visualizations:")
            for viz in analysis["suggested_visualizations"]:
                print(f"  - {viz}")
            print()
            print("=" * 70)

    elif args.command == "generate":
        print("\n" + "=" * 70)
        print("GENERATING CHART")
        print("=" * 70)
        print(f"File: {args.file}")
        print(f"Chart type: {args.chart_type}")
        print(f"Categories: {', '.join(args.categories)}")
        print()

        svg = recommender.generate_from_csv(
            args.file,
            args.chart_type,
            args.categories,
            args.pilar,
            args.title
        )

        if args.output:
            output_file = Path(args.output)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(svg)
            print(f"✓ Chart saved to: {args.output}")
        else:
            print(svg)

        print("=" * 70)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
