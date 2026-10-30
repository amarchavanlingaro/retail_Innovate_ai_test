# Databricks notebook source
# MAGIC %md
# MAGIC # Silver to Gold transformation
# MAGIC Creates curated tables for KPI reporting and operational analytics.

# COMMAND ----------
from pyspark.sql import functions as F
from pyspark.sql import SparkSession

spark = SparkSession.getActiveSession()

orders = spark.table("silver_orders")
inventory = spark.table("silver_inventory")
shipments = spark.table("silver_supplier_shipments")
returns = spark.table("silver_returns")

# KPI: inventory fill-rate approximation by SKU and location
inventory_health = inventory.select(
    F.current_date().alias("date"),
    F.col("sku"),
    F.col("location_id"),
    F.col("on_hand"),
    (F.col("on_hand") / (F.col("reorder_point") + 1)).alias("fill_rate"),
    F.col("days_of_supply"),
    F.when(F.col("on_hand") < F.col("reorder_point"), "risk").otherwise("healthy").alias("risk_level")
)

inventory_health.write.mode("overwrite").saveAsTable("gold_inventory_health")

# KPI: supplier on-time delivery and defects
supplier_performance = shipments.groupBy("supplier_id").agg(
    (F.sum(F.when(F.col("on_time_flag") == "Y", 1).otherwise(0)) / F.count("shipment_id")).alias("on_time_delivery_rate"),
    (F.sum(F.when(F.col("defect_flag") == "Y", 1).otherwise(0)) / F.count("shipment_id")).alias("defect_rate"),
    F.avg(F.datediff(F.col("actual_date"), F.col("planned_date")).cast("double")).alias("avg_lead_time_days")
).withColumn("risk_band", F.when(F.col("defect_rate") > 0.03, "watch").otherwise("stable"))

supplier_performance.write.mode("overwrite").saveAsTable("gold_supplier_performance")

# KPI: returns summary
returns_summary = returns.groupBy(F.to_date(F.col("return_date")).alias("date"), F.col("channel"), F.col("return_reason")).agg(
    F.sum("quantity").alias("volume")
).withColumn("return_rate", F.when(F.col("volume") > 0, F.col("volume") / 10).otherwise(0))

returns_summary.write.mode("overwrite").saveAsTable("gold_returns_summary")

print("Gold tables created successfully.")
