# Databricks notebook source
# MAGIC %md
# MAGIC # Executive KPI dashboard
# MAGIC Used for retail oversight, store performance, and supply chain health monitoring.

# COMMAND ----------
from pyspark.sql import SparkSession

spark = SparkSession.getActiveSession()

inventory = spark.table("gold_inventory_health")
shipments = spark.table("gold_supplier_performance")
returns = spark.table("gold_returns_summary")

print("Inventory health table sample:")
inventory.show(10, truncate=False)

print("Supplier performance table sample:")
shipments.show(10, truncate=False)

print("Return summary table sample:")
returns.show(10, truncate=False)
