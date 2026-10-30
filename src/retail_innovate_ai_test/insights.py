from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class BronzeLayer:
    source_name: str
    raw_tables: List[str] = field(default_factory=list)

    def ingest_snapshot(self, table_name: str, columns: List[str]) -> Dict[str, Any]:
        return {
            "layer": "bronze",
            "source": self.source_name,
            "table": table_name,
            "columns": columns,
            "status": "loaded",
            "quality_checks": ["schema_inferred", "null_scan", "ingestion_timestamp_added"],
        }


@dataclass
class SilverLayer:
    domain: str
    business_rules: List[str] = field(default_factory=list)

    def standardize(self, table_name: str) -> Dict[str, Any]:
        return {
            "layer": "silver",
            "domain": self.domain,
            "table": table_name,
            "status": "standardized",
            "business_rules_applied": self.business_rules,
        }


@dataclass
class GoldLayer:
    use_case: str
    kpis: List[str] = field(default_factory=list)

    def curate(self, table_name: str) -> Dict[str, Any]:
        return {
            "layer": "gold",
            "use_case": self.use_case,
            "table": table_name,
            "status": "curated",
            "kpis": self.kpis,
        }


@dataclass
class AIAuditor:
    domain: str = "retail_supply_chain"
    findings: List[str] = field(default_factory=list)

    def assess(self, context: Dict[str, Any]) -> Dict[str, Any]:
        recommended_actions = []

        if context.get("inventory_fill_rate", 0) < 0.96:
            self.findings.append("Inventory fill-rate is below target and may jeopardize order fulfillment.")
            recommended_actions.append("Tighten replenishment triggers and review slow-moving SKUs with aging stock." )

        if context.get("otd_service_level", 0) < 0.92:
            self.findings.append("On-time delivery performance is below the service threshold.")
            recommended_actions.append("Prioritize carrier performance review and delivery exception backlog cleanup.")

        if context.get("supplier_defect_rate", 0) > 0.03:
            self.findings.append("Supplier defects are creating downstream quality expense and replacement costs.")
            recommended_actions.append("Escalate to supplier quality reviews and validate incoming inspection controls.")

        if context.get("returns_rate", 0) > 0.12:
            self.findings.append("Return rates are elevated and may signal merchandising or product fit issues.")
            recommended_actions.append("Analyze category-level return drivers and improve post-purchase satisfaction workflows.")

        if not self.findings:
            self.findings.append("No material risk signals were detected in the assessed operational window.")

        return {
            "domain": self.domain,
            "summary": "AI-backed audit review across retail operations and supply chain resilience.",
            "findings": self.findings,
            "recommendations": recommended_actions,
            "status": "review_required" if recommended_actions else "monitoring",
        }
