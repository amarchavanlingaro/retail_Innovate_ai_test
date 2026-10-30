# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze ingestion layer
# MAGIC This notebook loads retail source extracts into the Bronze layer.

# COMMAND ----------
from pathlib import Path

from pyspark.sql import SparkSession

spark = SparkSession.getActiveSession()

base_path = "/Workspace/Users/your-user@company.com/retail_Innovate_ai_test/data/bronze"

files = {
    "bronze_orders": "retail_orders.csv",
    "bronze_inventory": "inventory_snapshot.csv",
    "bronze_supplier_shipments": "supplier_shipments.csv",
    "bronze_returns": "returns_events.csv",
}

for table_name, file_name in files.items():
    df = spark.read.option("header", True).csv(f"{base_path}/{file_name}")
    df.write.mode("overwrite").saveAsTable(table_name)
    print(f"Loaded {file_name} into {table_name}")
