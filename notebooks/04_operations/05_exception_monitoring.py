# Databricks notebook source
# MAGIC %md
# MAGIC # Operational exception monitoring
# MAGIC This notebook reviews operating metrics and highlights business exceptions for planning and execution teams.

# COMMAND ----------
from retail_innovate_ai_test.medallion import OperationalRiskReview

context = {
    "inventory_fill_rate": 0.937,
    "otd_service_level": 0.899,
    "supplier_defect_rate": 0.048,
    "returns_rate": 0.134,
}

review = OperationalRiskReview(domain="retail_supply_chain")
report = review.assess(context)

print(report)
