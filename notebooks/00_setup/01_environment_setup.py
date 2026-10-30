CREATE CATALOG IF NOT EXISTS retail_analytics;
USE CATALOG retail_analytics;
CREATE SCHEMA IF NOT EXISTS retail_analytics.ops;
USE SCHEMA retail_analytics.ops;

CREATE TABLE IF NOT EXISTS bronze_orders (
  order_id STRING,
  order_date DATE,
  store_id STRING,
  channel STRING,
  sku STRING,
  qty INT,
  unit_price DECIMAL(10,2),
  customer_segment STRING,
  ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE IF NOT EXISTS bronze_inventory (
  location_id STRING,
  sku STRING,
  on_hand INT,
  reorder_point INT,
  days_of_supply INT,
  warehouse STRING,
  ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE IF NOT EXISTS bronze_supplier_shipments (
  shipment_id STRING,
  supplier_id STRING,
  sku STRING,
  planned_date DATE,
  actual_date DATE,
  quantity INT,
  on_time_flag STRING,
  defect_flag STRING,
  ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE IF NOT EXISTS bronze_returns (
  return_id STRING,
  order_id STRING,
  return_date DATE,
  sku STRING,
  quantity INT,
  return_reason STRING,
  channel STRING,
  ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE IF NOT EXISTS gold_inventory_health (
  date DATE,
  sku STRING,
  location_id STRING,
  on_hand INT,
  fill_rate DECIMAL(5,4),
  days_of_supply INT,
  risk_level STRING
);

CREATE TABLE IF NOT EXISTS gold_supplier_performance (
  supplier_id STRING,
  on_time_delivery_rate DECIMAL(5,4),
  defect_rate DECIMAL(5,4),
  avg_lead_time_days DOUBLE,
  risk_band STRING
);

CREATE TABLE IF NOT EXISTS gold_returns_summary (
  date DATE,
  channel STRING,
  return_rate DECIMAL(5,4),
  return_reason STRING,
  volume INT
);
