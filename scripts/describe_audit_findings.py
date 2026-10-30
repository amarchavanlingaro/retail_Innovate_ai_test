#!/usr/bin/env python3
"""Seed a minimal dataset for local validation of the retail package."""

from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA_DIR = BASE / "data" / "gold"
DATA_DIR.mkdir(parents=True, exist_ok=True)

README = """# Gold layer

This directory is reserved for curated, business-facing tables such as:

- sales_by_store
- inventory_health
- supplier_performance
- fulfillment_service_score
- return_rate_by_category

These layers are intended for consumption by dashboards, downstream ML features, and AI-driven insight layers.
"""

(DATA_DIR / "README.md").write_text(README, encoding="utf-8")
print(f"Created Gold layer placeholder at {DATA_DIR}")
