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
class OperationalRiskReview:
    domain: str = "retail_operations"
    findings: List[str] = field(default_factory=list)

    def assess(self, context: Dict[str, Any]) -> Dict[str, Any]:
        recommended_actions = []

        if context.get("inventory_fill_rate", 0) < 0.96:
            self.findings.append("Inventory coverage is below target and is constraining order fulfillment capacity.")
            recommended_actions.append("Review replenishment policies and prioritize stock recovery for high-velocity SKUs.")

        if context.get("otd_service_level", 0) < 0.92:
            self.findings.append("On-time delivery performance is below the established service threshold.")
            recommended_actions.append("Assess warehouse and carrier performance with a focus on exception backlog resolution.")

        if context.get("supplier_defect_rate", 0) > 0.03:
            self.findings.append("Supplier quality variance is contributing to rework and downstream cost risk.")
            recommended_actions.append("Escalate supplier quality review and validate inbound inspection controls.")

        if context.get("returns_rate", 0) > 0.12:
            self.findings.append("Return intensity is elevated and may indicate product-fit or service issues.")
            recommended_actions.append("Analyze return drivers by category and channel to improve post-purchase handling.")

        if not self.findings:
            self.findings.append("No material operating issues were identified in the reviewed time window.")

        return {
            "domain": self.domain,
            "summary": "Operational review across retail execution, fulfillment, and supply chain performance.",
            "findings": self.findings,
            "recommendations": recommended_actions,
            "status": "review_required" if recommended_actions else "monitoring",
        }
