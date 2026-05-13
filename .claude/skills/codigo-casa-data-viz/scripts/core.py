#!/usr/bin/env python3
"""
Core BM25 engine for codigo-casa-data-viz skill.
Implements BM25 search over CSV configuration files.
Adapted from ui-ux-pro-max pattern for domain-specific data visualization.
"""

import csv
import json
import math
from pathlib import Path
from collections import defaultdict
import re


class BM25Engine:
    """BM25 search engine for configuration CSVs."""

    def __init__(self, csv_path, key_column, search_columns, min_score=0.5):
        """
        Initialize BM25 engine.

        Args:
            csv_path: Path to CSV file
            key_column: Column name with unique identifiers
            search_columns: List of column names to search in
            min_score: Minimum BM25 score to return results
        """
        self.csv_path = Path(csv_path)
        self.key_column = key_column
        self.search_columns = search_columns
        self.min_score = min_score

        # BM25 parameters
        self.k1 = 1.5  # Term frequency saturation
        self.b = 0.75   # Length normalization

        self.documents = []  # List of all rows
        self.idf = {}        # Inverse document frequency
        self.doc_length = {} # Document lengths per document

        self._load_csv()
        self._compute_idf()

    def _load_csv(self):
        """Load CSV file and index it."""
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.documents.append(row)
                # Calculate document length (total tokens across search columns)
                length = sum(len(self._tokenize(row.get(col, "")))
                           for col in self.search_columns)
                self.doc_length[len(self.documents) - 1] = length

    def _tokenize(self, text):
        """Simple tokenization: lowercase, split on whitespace/punctuation."""
        text = text.lower()
        # Split on whitespace and punctuation, remove empty
        tokens = re.findall(r'\b[a-záéíóúñ0-9]+\b', text)
        return tokens

    def _compute_idf(self):
        """Compute inverse document frequency for all terms."""
        term_doc_count = defaultdict(int)
        all_terms = set()

        # Count how many documents contain each term
        for doc in self.documents:
            doc_terms = set()
            for col in self.search_columns:
                tokens = self._tokenize(doc.get(col, ""))
                doc_terms.update(tokens)

            for term in doc_terms:
                term_doc_count[term] += 1
                all_terms.add(term)

        # Compute IDF for each term
        n_docs = len(self.documents)
        for term in all_terms:
            # BM25 IDF formula
            self.idf[term] = math.log(
                (n_docs - term_doc_count[term] + 0.5) /
                (term_doc_count[term] + 0.5) + 1.0
            )

    def _compute_bm25_score(self, tokens, doc_idx):
        """Compute BM25 score for a query against a document."""
        doc = self.documents[doc_idx]
        doc_tokens = []

        for col in self.search_columns:
            tokens_in_col = self._tokenize(doc.get(col, ""))
            doc_tokens.extend(tokens_in_col)

        score = 0.0
        doc_len = self.doc_length[doc_idx]
        avg_doc_len = sum(self.doc_length.values()) / len(self.doc_length) if self.doc_length else 1

        for token in tokens:
            # Count occurrences of token in document
            token_freq = doc_tokens.count(token)
            if token_freq == 0:
                continue

            idf_score = self.idf.get(token, 0)

            # BM25 formula
            numerator = idf_score * token_freq * (self.k1 + 1)
            denominator = token_freq + self.k1 * (1 - self.b + self.b * (doc_len / avg_doc_len))
            score += numerator / denominator

        return score

    def search(self, query, top_k=5):
        """
        Search for documents matching the query.

        Args:
            query: Search query string
            top_k: Return top K results

        Returns:
            List of tuples (score, document_dict)
        """
        query_tokens = self._tokenize(query)

        if not query_tokens:
            return []

        # Score all documents
        scores = []
        for doc_idx in range(len(self.documents)):
            score = self._compute_bm25_score(query_tokens, doc_idx)
            if score >= self.min_score:
                scores.append((score, doc_idx))

        # Sort by score descending
        scores.sort(key=lambda x: x[0], reverse=True)

        # Return top k with documents
        results = []
        for score, doc_idx in scores[:top_k]:
            results.append((score, self.documents[doc_idx]))

        return results


class SkillConfig:
    """Manages all skill configuration CSVs."""

    def __init__(self, data_dir):
        """Initialize configuration manager."""
        self.data_dir = Path(data_dir)

        # Initialize BM25 engines for each CSV
        self.chart_types_search = BM25Engine(
            self.data_dir / "chart-types.csv",
            key_column="no",
            search_columns=["data_type", "chart_type", "when_to_use"]
        )

        self.data_patterns_search = BM25Engine(
            self.data_dir / "data-patterns.csv",
            key_column="pattern_type",
            search_columns=["pattern_type", "description", "keywords", "data_structure"]
        )

        self.tension_indicators_search = BM25Engine(
            self.data_dir / "tension-indicators.csv",
            key_column="tension_id",
            search_columns=["pilar", "tension_name", "metric_keywords"]
        )

        self.cultural_sensitivity = self._load_csv_dict(
            self.data_dir / "cultural-sensitivity.csv",
            key_column="sensitivity_id"
        )

        self.dominican_palettes = self._load_csv_dict(
            self.data_dir / "dominican-palettes.csv",
            key_column="name"
        )

        self.gestalt_rules = self._load_csv_list(
            self.data_dir / "gestalt-rules.csv"
        )

        self.hierarchy_patterns = self._load_csv_dict(
            self.data_dir / "hierarchy-patterns.csv",
            key_column="pattern_id"
        )

    def _load_csv_dict(self, csv_path, key_column):
        """Load CSV as dictionary keyed by specific column."""
        result = {}
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = row.pop(key_column)
                result[key] = row
        return result

    def _load_csv_list(self, csv_path):
        """Load CSV as list of dictionaries."""
        result = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                result.append(row)
        return result

    def search_chart_types(self, query, top_k=5):
        """Search for chart type recommendations."""
        return self.chart_types_search.search(query, top_k=top_k)

    def search_data_patterns(self, query, top_k=5):
        """Search for data pattern recommendations."""
        return self.data_patterns_search.search(query, top_k=top_k)

    def search_tensions(self, query, top_k=5):
        """Search for tension indicators."""
        return self.tension_indicators_search.search(query, top_k=top_k)

    def get_palette(self, palette_name):
        """Get palette by name."""
        return self.dominican_palettes.get(palette_name)

    def get_sensitivity_rule(self, rule_id):
        """Get cultural sensitivity rule."""
        return self.cultural_sensitivity.get(rule_id)

    def export_to_json(self, output_path=None):
        """Export all configuration to JSON for inspection."""
        config = {
            "dominican_palettes": self.dominican_palettes,
            "gestalt_rules": self.gestalt_rules,
            "hierarchy_patterns": self.hierarchy_patterns,
            "cultural_sensitivity": self.cultural_sensitivity,
        }

        json_str = json.dumps(config, ensure_ascii=False, indent=2)

        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(json_str)

        return json_str


# Utility functions for CLI
def get_skill_config():
    """Get configuration from default location."""
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"
    return SkillConfig(data_dir)


if __name__ == "__main__":
    # Quick test
    config = get_skill_config()

    # Test search
    results = config.search_chart_types("multiresponse generacional")
    print("Chart type search results:")
    for score, doc in results:
        print(f"  Score: {score:.2f} | {doc.get('chart_type', 'N/A')}")

    # Test palette
    palette = config.get_palette("DOMINICAN_FINANCE_STRUGGLE")
    print(f"\nPalette DOMINICAN_FINANCE_STRUGGLE: {palette}")
