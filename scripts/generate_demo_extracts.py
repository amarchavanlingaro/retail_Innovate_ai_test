#!/usr/bin/env python3
"""Generate synthetic retail and supply chain extracts for the medallion demo."""

from pathlib import Path
import csv

BASE = Path(__file__).resolve().parents[1]
DATA_DIR = BASE / "data" / "bronze"
DATA_DIR.mkdir(parents=True, exist_ok=True)

STORES = [
    ("S010", "Downtown Flagship", "Seattle", "WA", "Urban", "Store"),
    ("S011", "Northside Market", "Seattle", "WA", "Urban", "Store"),
    ("S012", "Riverside Plaza", "Portland", "OR", "Suburban", "Store"),
    ("S013", "Fremont Hub", "Denver", "CO", "Urban", "Store"),
    ("S014", "Stone Creek", "Austin", "TX", "Suburban", "Store"),
    ("S015", "Market Square", "Dallas", "TX", "Urban", "Store"),
    ("W100", "RDC Northwest", "Tacoma", "WA", "Distribution", "Warehouse"),
    ("W101", "RDC Central", "Kansas City", "MO", "Distribution", "Warehouse"),
    ("W102", "RDC South", "Dallas", "TX", "Distribution", "Warehouse"),
]

PRODUCTS = [
    ("SKU-1001", "Trail Pro Jacket", "Apparel", "Outerwear", "Men", 119.99, 1.0),
    ("SKU-2120", "Apex Running Shoe", "Footwear", "Athletic", "Women", 89.99, 1.0),
    ("SKU-3307", "Summit Water Bottle", "Accessories", "Hydration", "Unisex", 24.99, 1.0),
    ("SKU-4421", "Luma Smart Lamp", "Home", "Lighting", "Home", 149.99, 0.8),
    ("SKU-7012", "Harbor Laptop Sleeve", "Accessories", "Electronics", "Unisex", 39.99, 0.9),
    ("SKU-8816", "Evergreen Yoga Mat", "Fitness", "Lifestyle", "Women", 54.99, 0.7),
    ("SKU-9155", "Summit Travel Backpack", "Accessories", "Travel", "Unisex", 64.99, 0.9),
]

SUPPLIERS = [
    ("SUP-11", "NorthPeak Manufacturing", "Apparel", "Tier 1", "Domestic"),
    ("SUP-21", "Velocity Footwear Co.", "Footwear", "Tier 1", "Domestic"),
    ("SUP-54", "Helio Labs", "Home", "Tier 2", "Imported"),
    ("SUP-77", "Granite Packaging", "Accessories", "Tier 2", "Domestic"),
    ("SUP-88", "Summit Logistics Group", "Logistics", "Tier 1", "Domestic"),
]

CARRIERS = [
    ("CAR-1", "NorthStar Freight", "ground"),
    ("CAR-2", "BlueRoute Logistics", "express"),
    ("CAR-3", "RapidReach Transport", "ground"),
    ("CAR-4", "Coastal Parcel", "last_mile"),
]


def write_orders():
    rows = [
        ["order_id", "order_date", "store_id", "channel", "sku", "qty", "unit_price", "customer_segment", "order_status"],
        ["A1001", "2026-10-01", "S010", "store", "SKU-1001", 2, 34.99, "Loyalty", "fulfilled"],
        ["A1002", "2026-10-01", "S011", "ecommerce", "SKU-2120", 1, 58.00, "New", "fulfilled"],
        ["A1003", "2026-10-02", "S012", "store", "SKU-3307", 4, 27.50, "Value", "fulfilled"],
        ["A1004", "2026-10-02", "S009", "ecommerce", "SKU-4421", 3, 95.50, "VIP", "delayed"],
        ["A1005", "2026-10-03", "S013", "store", "SKU-7012", 5, 39.99, "Loyalty", "fulfilled"],
        ["A1006", "2026-10-03", "S014", "ecommerce", "SKU-8816", 2, 54.99, "New", "returned"],
        ["A1007", "2026-10-04", "S015", "store", "SKU-9155", 3, 64.99, "VIP", "fulfilled"],
        ["A1008", "2026-10-05", "S010", "ecommerce", "SKU-1001", 1, 119.99, "Loyalty", "shipped"],
        ["A1009", "2026-10-05", "S012", "store", "SKU-4421", 2, 149.99, "Value", "fulfilled"],
        ["A1010", "2026-10-06", "S013", "ecommerce", "SKU-8816", 4, 54.99, "New", "fulfilled"],
    ]

    with (DATA_DIR / "retail_orders.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_inventory():
    rows = [
        ["location_id", "sku", "on_hand", "reorder_point", "days_of_supply", "warehouse", "inventory_status"],
        ["W100", "SKU-1001", 120, 80, 18, "RDC-1", "healthy"],
        ["W101", "SKU-2120", 40, 55, 7, "RDC-2", "at_risk"],
        ["W102", "SKU-3307", 210, 110, 28, "RDC-1", "healthy"],
        ["W103", "SKU-4421", 18, 50, 4, "RDC-3", "critical"],
        ["W100", "SKU-7012", 90, 75, 16, "RDC-1", "healthy"],
        ["W101", "SKU-8816", 35, 45, 8, "RDC-2", "at_risk"],
        ["W102", "SKU-9155", 145, 90, 22, "RDC-1", "healthy"],
        ["W103", "SKU-1001", 60, 80, 10, "RDC-3", "at_risk"],
    ]

    with (DATA_DIR / "inventory_snapshot.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_shipments():
    rows = [
        ["shipment_id", "supplier_id", "sku", "planned_date", "actual_date", "quantity", "on_time_flag", "defect_flag", "carrier_id"],
        ["SH-901", "SUP-11", "SKU-1001", "2026-10-01", "2026-10-02", 350, "Y", "N", "CAR-1"],
        ["SH-902", "SUP-21", "SKU-2120", "2026-10-02", "2026-10-04", 220, "N", "Y", "CAR-2"],
        ["SH-903", "SUP-11", "SKU-3307", "2026-10-03", "2026-10-03", 500, "Y", "N", "CAR-1"],
        ["SH-904", "SUP-54", "SKU-4421", "2026-10-03", "2026-10-05", 120, "N", "Y", "CAR-3"],
        ["SH-905", "SUP-77", "SKU-7012", "2026-10-04", "2026-10-05", 200, "Y", "N", "CAR-4"],
        ["SH-906", "SUP-88", "SKU-8816", "2026-10-04", "2026-10-07", 180, "N", "N", "CAR-2"],
        ["SH-907", "SUP-11", "SKU-9155", "2026-10-05", "2026-10-05", 300, "Y", "N", "CAR-1"],
        ["SH-908", "SUP-54", "SKU-1001", "2026-10-05", "2026-10-08", 150, "N", "Y", "CAR-3"],
    ]

    with (DATA_DIR / "supplier_shipments.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_returns():
    rows = [
        ["return_id", "order_id", "return_date", "sku", "quantity", "return_reason", "channel", "return_resolution"],
        ["R-881", "A1001", "2026-10-04", "SKU-1001", 1, "size_mismatch", "store", "exchange"],
        ["R-882", "A1002", "2026-10-05", "SKU-2120", 1, "defective", "ecommerce", "refund"],
        ["R-883", "A1003", "2026-10-05", "SKU-3307", 2, "late_delivery", "store", "replacement"],
        ["R-884", "A1004", "2026-10-07", "SKU-4421", 1, "quality_issue", "ecommerce", "refund"],
        ["R-885", "A1006", "2026-10-08", "SKU-8816", 1, "size_mismatch", "ecommerce", "exchange"],
        ["R-886", "A1010", "2026-10-10", "SKU-8816", 2, "damaged", "ecommerce", "refund"],
    ]

    with (DATA_DIR / "returns_events.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_store_dim():
    rows = [["store_id", "store_name", "city", "state", "market_type", "store_type"]]
    rows.extend(STORES)

    with (DATA_DIR / "store_dim.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_product_dim():
    rows = [["sku", "product_name", "category", "sub_category", "segment", "list_price", "margin_share"]]
    rows.extend(PRODUCTS)

    with (DATA_DIR / "product_dim.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_supplier_dim():
    rows = [["supplier_id", "supplier_name", "category", "tier", "origin"]]
    rows.extend(SUPPLIERS)

    with (DATA_DIR / "supplier_dim.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_carrier_performance():
    rows = [
        ["carrier_id", "carrier_name", "mode", "on_time_rate", "delivery_cost_index", "exception_rate"],
        ["CAR-1", "NorthStar Freight", "ground", 0.96, 1.05, 0.03],
        ["CAR-2", "BlueRoute Logistics", "express", 0.87, 1.18, 0.08],
        ["CAR-3", "RapidReach Transport", "ground", 0.91, 1.09, 0.05],
        ["CAR-4", "Coastal Parcel", "last_mile", 0.88, 1.22, 0.09],
    ]

    with (DATA_DIR / "carrier_performance.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_pricing_events():
    rows = [
        ["price_event_id", "sku", "effective_date", "previous_price", "new_price", "promotion_type", "region"],
        ["PE-5001", "SKU-1001", "2026-10-01", 129.99, 119.99, "markdown", "West"],
        ["PE-5002", "SKU-2120", "2026-10-03", 94.99, 89.99, "promo", "West"],
        ["PE-5003", "SKU-4421", "2026-10-04", 169.99, 149.99, "clearance", "South"],
        ["PE-5004", "SKU-8816", "2026-10-02", 59.99, 54.99, "bundle", "Central"],
        ["PE-5005", "SKU-9155", "2026-10-06", 74.99, 64.99, "promo", "South"],
    ]

    with (DATA_DIR / "pricing_events.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_fulfillment_events():
    rows = [
        ["fulfillment_id", "order_id", "warehouse_id", "carrier_id", "ship_date", "delivery_date", "status", "sla_met"],
        ["F-2101", "A1001", "W100", "CAR-1", "2026-10-01", "2026-10-03", "delivered", "Y"],
        ["F-2102", "A1002", "W101", "CAR-2", "2026-10-01", "2026-10-05", "delivered", "N"],
        ["F-2103", "A1003", "W102", "CAR-3", "2026-10-02", "2026-10-04", "delivered", "Y"],
        ["F-2104", "A1004", "W103", "CAR-3", "2026-10-02", "2026-10-09", "in_transit", "N"],
        ["F-2105", "A1010", "W101", "CAR-4", "2026-10-06", "2026-10-08", "delivered", "Y"],
    ]

    with (DATA_DIR / "fulfillment_events.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_readme():
    readme = """# Bronze source extracts

This directory contains synthetic operational extracts for retail analytics and supply chain risk monitoring.

Included tables:

- retail_orders.csv
- inventory_snapshot.csv
- supplier_shipments.csv
- returns_events.csv
- store_dim.csv
- product_dim.csv
- supplier_dim.csv
- carrier_performance.csv
- pricing_events.csv
- fulfillment_events.csv

These sample files are designed to simulate realistic retail and supply chain activity for medallion architecture testing and AI-driven audit narratives.
"""
    (DATA_DIR / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    write_orders()
    write_inventory()
    write_shipments()
    write_returns()
    write_store_dim()
    write_product_dim()
    write_supplier_dim()
    write_carrier_performance()
    write_pricing_events()
    write_fulfillment_events()
    write_readme()
    print(f"Generated realistic bronze extracts under {DATA_DIR}")
