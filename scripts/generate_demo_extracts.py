from typing import Dict, List


def generate_insight_summary(metrics: Dict[str, float]) -> List[str]:
    insights = []

    if metrics.get("inventory_fill_rate", 1.0) < 0.96:
        insights.append("Inventory optimization is the highest-priority operational risk for service-level stability.")

    if metrics.get("otd_service_level", 1.0) < 0.92:
        insights.append("Carrier and warehouse execution are likely suppressing promised service outcomes.")

    if metrics.get("supplier_defect_rate", 0.0) > 0.03:
        insights.append("Supplier quality variance is contributing to cost and rework risk in downstream operations.")

    if metrics.get("returns_rate", 0.0) > 0.12:
        insights.append("High return intensity merits merchandising and customer experience review by category.")

    if not insights:
        insights.append("The operating system is stable, but a governance review should confirm data trust before scaling AI automation.")

    return insights
