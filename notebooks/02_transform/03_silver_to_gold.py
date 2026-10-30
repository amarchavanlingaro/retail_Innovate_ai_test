# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze to Silver transformation
# MAGIC Applies standardization and quality checks for key retail operational entities.

# COMMAND ----------
from pyspark.sql import functions as F
from pyspark.sql import SparkSession

spark = SparkSession.getActiveSession()

# Example bronze sources
orders = spark.table("bronze_orders")
inventory = spark.table("bronze_inventory")
shipments = spark.table("bronze_supplier_shipments")
returns = spark.table("bronze_returns")

orders_clean = orders.withColumn("qty", F.col("qty").cast("int")) \
    .withColumn("unit_price", F.col("unit_price").cast("decimal(10,2)")) \
    .withColumn("order_date", F.to_date(F.col("order_date")))

inventory_clean = inventory.withColumn("on_hand", F.col("on_hand").cast("int")) \
    .withColumn("reorder_point", F.col("reorder_point").cast("int"))

shipments_clean = shipments.withColumn("planned_date", F.to_date(F.col("planned_date"))) \
    .withColumn("actual_date", F.to_date(F.col("actual_date")))

returns_clean = returns.withColumn("return_date", F.to_date(F.col("return_date")))

orders_clean.write.mode("overwrite").saveAsTable("silver_orders")
inventory_clean.write.mode("overwrite").saveAsTable("silver_inventory")
shipments_clean.write.mode("overwrite").saveAsTable("silver_supplier_shipments")
returns_clean.write.mode("overwrite").saveAsTable("silver_returns")

print("Silver layer tables created successfully.")
