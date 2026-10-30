# Databricks notebook source
# MAGIC %md
# MAGIC # AI Audit recommendations
# MAGIC Uses operational metrics to generate a risk narrative and recommended actions.

# COMMAND ----------
from retail_innovate_ai_test.medallion import AIAuditor

context = {
    "inventory_fill_rate": 0.937,
    "otd_service_level": 0.899,
    "supplier_defect_rate": 0.048,
    "returns_rate": 0.134,
}

auditor = AIAuditor(domain="retail_supply_chain")
report = auditor.assess(context)

print(report)
