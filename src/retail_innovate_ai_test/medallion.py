from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class RetailConfig:
    catalog: str = "retail_analytics"
    schema: str = "ops"
    bronze_table_prefix: str = "bronze_"
    silver_table_prefix: str = "silver_"
    gold_table_prefix: str = "gold_"
    ai_audit_enabled: bool = True
    tolerance: Dict[str, float] = None

    def __post_init__(self):
        if self.tolerance is None:
            object.__setattr__(
                self,
                "tolerance",
                {
                    "inventory_fill_rate": 0.96,
                    "otd_service_level": 0.92,
                    "supplier_defect_rate": 0.03,
                    "returns_rate": 0.12,
                },
            )


RETAIL_CONFIG = RetailConfig()
