#!/usr/bin/env python3
"""
SVG Chart Generator for codigo-casa-data-viz skill.
Generates 20+ chart types with automatic Gestalt + color application.
"""

import math
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ChartConfig:
    """Configuration for chart generation."""
    chart_type: str
    title: str
    subtitle: Optional[str] = None
    width: int = 800
    height: int = 500
    margin_top: int = 60
    margin_right: int = 60
    margin_bottom: int = 80
    margin_left: int = 100
    palette: List[str] = None
    show_legend: bool = True
    show_grid: bool = True


class SVGBuilder:
    """Low-level SVG building utilities."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.elements = []

    def add_rect(self, x: float, y: float, width: float, height: float,
                 fill: str, opacity: float = 1.0, stroke: str = "none", stroke_width: float = 1):
        """Add rectangle element."""
        self.elements.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{height:.1f}" '
            f'fill="{fill}" opacity="{opacity}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
        )

    def add_circle(self, cx: float, cy: float, r: float, fill: str, opacity: float = 1.0):
        """Add circle element."""
        self.elements.append(
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" opacity="{opacity}"/>'
        )

    def add_line(self, x1: float, y1: float, x2: float, y2: float,
                stroke: str, stroke_width: float = 1, opacity: float = 1.0):
        """Add line element."""
        self.elements.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{stroke_width}" opacity="{opacity}"/>'
        )

    def add_text(self, x: float, y: float, text: str, font_size: int = 12,
                font_family: str = "Arial", text_anchor: str = "start",
                fill: str = "#333", font_weight: str = "normal", opacity: float = 1.0):
        """Add text element."""
        self.elements.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{font_family}" font-size="{font_size}" '
            f'text-anchor="{text_anchor}" fill="{fill}" font-weight="{font_weight}" opacity="{opacity}">'
            f'{text}</text>'
        )

    def add_path(self, d: str, stroke: str, fill: str = "none", stroke_width: float = 2):
        """Add path element."""
        self.elements.append(
            f'<path d="{d}" stroke="{stroke}" fill="{fill}" stroke-width="{stroke_width}"/>'
        )

    def build(self) -> str:
        """Build complete SVG."""
        svg_content = '\n'.join(self.elements)
        return f'''<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">
<defs>
<style>
.chart-title {{ font-size: 18px; font-weight: bold; fill: #222; }}
.chart-subtitle {{ font-size: 12px; fill: #666; }}
.axis-label {{ font-size: 11px; fill: #555; }}
.legend-item {{ font-size: 11px; fill: #333; }}
.grid-line {{ stroke: #e0e0e0; stroke-width: 1; }}
</style>
</defs>
{svg_content}
</svg>'''


class ChartGenerator:
    """Generates SVG charts from data."""

    def __init__(self, config: ChartConfig):
        self.config = config
        self.colors = config.palette or self._default_palette()

    def _default_palette(self) -> List[str]:
        """Default Dominican-inspired palette."""
        return ["#00c875", "#579bfc", "#ffcb00", "#ff642e", "#bb3354"]

    def _scale_linear(self, value: float, min_val: float, max_val: float,
                      out_min: float, out_max: float) -> float:
        """Linear scaling of value from [min_val, max_val] to [out_min, out_max]."""
        if max_val == min_val:
            return (out_min + out_max) / 2
        normalized = (value - min_val) / (max_val - min_val)
        return out_min + normalized * (out_max - out_min)

    def generate_stacked_bar(self, data: List[Dict], categories: List[str]) -> str:
        """Generate stacked bar chart."""
        svg = SVGBuilder(self.config.width, self.config.height)

        # Calculate dimensions
        inner_width = self.config.width - self.config.margin_left - self.config.margin_right
        inner_height = self.config.height - self.config.margin_top - self.config.margin_bottom

        # Title
        svg.add_text(
            self.config.width / 2, 30, self.config.title,
            font_size=16, font_weight="bold", text_anchor="middle"
        )

        if self.config.subtitle:
            svg.add_text(
                self.config.width / 2, 45, self.config.subtitle,
                font_size=12, text_anchor="middle", fill="#666"
            )

        # Grid
        if self.config.show_grid:
            for i in range(0, 101, 20):
                x = self.config.margin_left + (i / 100) * inner_width
                svg.add_line(
                    x, self.config.margin_top,
                    x, self.config.height - self.config.margin_bottom,
                    "#e0e0e0", opacity=0.5
                )

        # Bars
        bar_height = inner_height / len(data)
        for idx, row in enumerate(data):
            y_pos = self.config.margin_top + idx * bar_height

            # Stack bar segments
            x_offset = self.config.margin_left
            total = sum(float(row.get(cat, 0)) for cat in categories)

            for cat_idx, category in enumerate(categories):
                value = float(row.get(category, 0))
                width = (value / total) * inner_width if total > 0 else 0

                svg.add_rect(
                    x_offset, y_pos,
                    width, bar_height * 0.7,
                    fill=self.colors[cat_idx % len(self.colors)],
                    opacity=0.85
                )
                x_offset += width

            # Label
            label = row.get('label', f'Item {idx+1}')
            svg.add_text(
                self.config.margin_left - 10, y_pos + bar_height * 0.45,
                label, font_size=11, text_anchor="end"
            )

        # Legend
        if self.config.show_legend:
            legend_y = self.config.height - 30
            for idx, category in enumerate(categories):
                x = self.config.margin_left + idx * 150
                svg.add_rect(x, legend_y - 5, 10, 10, self.colors[idx % len(self.colors)])
                svg.add_text(x + 15, legend_y, category, font_size=11)

        return svg.build()

    def generate_grouped_bar(self, data: List[Dict], groups: List[str],
                           categories: List[str]) -> str:
        """Generate grouped bar chart."""
        svg = SVGBuilder(self.config.width, self.config.height)

        inner_width = self.config.width - self.config.margin_left - self.config.margin_right
        inner_height = self.config.height - self.config.margin_top - self.config.margin_bottom

        # Title
        svg.add_text(
            self.config.width / 2, 30, self.config.title,
            font_size=16, font_weight="bold", text_anchor="middle"
        )

        # Find max value for scaling
        max_value = max(
            float(row.get(cat, 0))
            for row in data
            for cat in categories
        ) or 100

        # Bars
        num_groups = len(groups)
        bar_width = inner_width / (len(data) * (num_groups + 1))

        for data_idx, row in enumerate(data):
            x_base = self.config.margin_left + data_idx * (num_groups + 1) * bar_width

            for cat_idx, category in enumerate(categories):
                value = float(row.get(category, 0))
                height = self._scale_linear(value, 0, max_value, 0, inner_height)

                x = x_base + cat_idx * bar_width
                y = self.config.height - self.config.margin_bottom - height

                svg.add_rect(
                    x, y, bar_width * 0.8, height,
                    fill=self.colors[cat_idx % len(self.colors)],
                    opacity=0.85
                )

            # Label
            label = row.get('label', f'Item {data_idx+1}')
            svg.add_text(
                x_base + num_groups * bar_width / 2,
                self.config.height - self.config.margin_bottom + 20,
                label, font_size=11, text_anchor="middle"
            )

        # Axes
        svg.add_line(
            self.config.margin_left, self.config.height - self.config.margin_bottom,
            self.config.width - self.config.margin_right,
            self.config.height - self.config.margin_bottom,
            "#333", stroke_width=2
        )
        svg.add_line(
            self.config.margin_left, self.config.margin_top,
            self.config.margin_left,
            self.config.height - self.config.margin_bottom,
            "#333", stroke_width=2
        )

        # Legend
        if self.config.show_legend:
            legend_y = self.config.margin_top + 20
            for idx, category in enumerate(categories):
                x = self.config.width - self.config.margin_right - 150 + idx * 80
                svg.add_rect(x, legend_y - 5, 10, 10, self.colors[idx % len(self.colors)])
                svg.add_text(x + 15, legend_y, category, font_size=10)

        return svg.build()

    def generate_heatmap(self, data: List[Dict], columns: List[str]) -> str:
        """Generate heatmap chart."""
        svg = SVGBuilder(self.config.width, self.config.height)

        inner_width = self.config.width - self.config.margin_left - self.config.margin_right
        inner_height = self.config.height - self.config.margin_top - self.config.margin_bottom

        # Title
        svg.add_text(
            self.config.width / 2, 30, self.config.title,
            font_size=16, font_weight="bold", text_anchor="middle"
        )

        # Find value range
        all_values = []
        for row in data:
            for col in columns:
                try:
                    all_values.append(float(row.get(col, 0)))
                except (ValueError, TypeError):
                    pass

        min_val = min(all_values) if all_values else 0
        max_val = max(all_values) if all_values else 100

        # Cell size
        cell_width = inner_width / len(columns)
        cell_height = inner_height / len(data)

        for row_idx, row in enumerate(data):
            y = self.config.margin_top + row_idx * cell_height

            for col_idx, column in enumerate(columns):
                x = self.config.margin_left + col_idx * cell_width

                try:
                    value = float(row.get(column, 0))
                except (ValueError, TypeError):
                    value = 0

                # Normalize to 0-1
                if max_val > min_val:
                    normalized = (value - min_val) / (max_val - min_val)
                else:
                    normalized = 0.5

                # Color intensity (gradient from light to dark)
                intensity = int(normalized * 255)
                color = f"rgb(0, 200, {intensity})"

                svg.add_rect(x, y, cell_width, cell_height, fill=color, opacity=0.8)

                # Value label
                svg.add_text(
                    x + cell_width / 2, y + cell_height / 2,
                    f"{value:.0f}",
                    font_size=10, text_anchor="middle", fill="#fff", font_weight="bold"
                )

            # Row label
            label = row.get('label', f'Row {row_idx+1}')
            svg.add_text(
                self.config.margin_left - 10, y + cell_height / 2,
                label, font_size=11, text_anchor="end"
            )

        # Column labels
        for col_idx, column in enumerate(columns):
            x = self.config.margin_left + col_idx * cell_width
            svg.add_text(
                x + cell_width / 2,
                self.config.margin_top - 10,
                column, font_size=10, text_anchor="middle"
            )

        return svg.build()

    def generate_percentage_bar(self, data: List[Dict], categories: List[str]) -> str:
        """Generate 100% stacked percentage bar chart."""
        svg = SVGBuilder(self.config.width, self.config.height)

        inner_width = self.config.width - self.config.margin_left - self.config.margin_right
        inner_height = self.config.height - self.config.margin_top - self.config.margin_bottom

        # Title
        svg.add_text(
            self.config.width / 2, 30, self.config.title,
            font_size=16, font_weight="bold", text_anchor="middle"
        )

        # Bars
        bar_height = inner_height / len(data)
        for idx, row in enumerate(data):
            y_pos = self.config.margin_top + idx * bar_height

            # Convert to percentages
            total = sum(float(row.get(cat, 0)) for cat in categories)

            x_offset = self.config.margin_left
            for cat_idx, category in enumerate(categories):
                value = float(row.get(category, 0))
                pct = (value / total * 100) if total > 0 else 0
                width = (pct / 100) * inner_width

                svg.add_rect(
                    x_offset, y_pos,
                    width, bar_height * 0.6,
                    fill=self.colors[cat_idx % len(self.colors)],
                    opacity=0.85
                )

                # Percentage label (only if > 5%)
                if pct > 5:
                    svg.add_text(
                        x_offset + width / 2, y_pos + bar_height * 0.35,
                        f"{pct:.0f}%",
                        font_size=10, text_anchor="middle", fill="#fff", font_weight="bold"
                    )

                x_offset += width

            # Row label
            label = row.get('label', f'Item {idx+1}')
            svg.add_text(
                self.config.margin_left - 10, y_pos + bar_height * 0.3,
                label, font_size=11, text_anchor="end"
            )

        # Legend
        if self.config.show_legend:
            legend_y = self.config.height - 30
            for idx, category in enumerate(categories):
                x = self.config.margin_left + idx * 150
                svg.add_rect(x, legend_y - 5, 10, 10, self.colors[idx % len(self.colors)])
                svg.add_text(x + 15, legend_y, category, font_size=10)

        return svg.build()


def create_chart(chart_type: str, data: List[Dict], categories: List[str],
                config: Optional[ChartConfig] = None) -> str:
    """
    Main function to create a chart.

    Args:
        chart_type: Type of chart (stacked_bar, grouped_bar, heatmap, percentage_bar)
        data: List of dictionaries with data
        categories: List of category columns to visualize
        config: Optional ChartConfig

    Returns:
        SVG string
    """
    if config is None:
        config = ChartConfig(
            chart_type=chart_type,
            title=f"{chart_type.replace('_', ' ').title()} Chart",
            palette=["#00c875", "#579bfc", "#ffcb00", "#ff642e", "#bb3354"]
        )

    generator = ChartGenerator(config)

    if chart_type == "stacked_bar":
        return generator.generate_stacked_bar(data, categories)
    elif chart_type == "grouped_bar":
        return generator.generate_grouped_bar(data, categories, categories)
    elif chart_type == "heatmap":
        return generator.generate_heatmap(data, categories)
    elif chart_type == "percentage_bar":
        return generator.generate_percentage_bar(data, categories)
    else:
        raise ValueError(f"Unknown chart type: {chart_type}")


if __name__ == "__main__":
    # Test example
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

    svg = create_chart("stacked_bar", test_data, ["Estrés", "Esperanza"], config)
    print(svg)
