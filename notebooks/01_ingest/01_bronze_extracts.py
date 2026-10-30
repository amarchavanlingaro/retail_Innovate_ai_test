# Databricks notebook source
# MAGIC %md
# MAGIC # Retail platform setup
# MAGIC This notebook prepares catalogs, schemas, and recommended cluster settings for the retail medallion project.

# COMMAND ----------
from pyspark.sql import SparkSession

spark = SparkSession.getActiveSession()

catalog = "retail_analytics"
schema = "ops"

spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog}")
spark.sql(f"USE CATALOG {catalog}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {schema}")
spark.sql(f"USE SCHEMA {schema}")

print("Catalog and schema initialized successfully.")
