#!/usr/bin/env python3
"""Generate synthetic source extracts for the retail medallion demo."""

from pathlib import Path
import csv

BASE = Path(__file__).resolve().parents[1]
DATA_DIR = BASE / "data" / "bronze"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def write_orders():
    rows = [
        ["order_id", "order_date", "store_id", "channel", "sku", "qty", "unit_price", "customer_segment"],
        ["A1001", "2026-10-01", "S010", "store", "SKU-1001", 2, 34.99, "Loyalty"],
        ["A1002", "2026-10-01", "S011", "ecommerce", "SKU-2120", 1, 58.00, "New"],
        ["A1003", "2026-10-02", "S012", "store", "SKU-3307", 4, 27.50, "Value"],
        ["A1004", "2026-10-02", "S009", "ecommerce", "SKU-4421", 3, 95.50, "VIP"],
    ]

    with (DATA_DIR / "retail_orders.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_inventory():
    rows = [
        ["location_id", "sku", "on_hand", "reorder_point", "days_of_supply", "warehouse"],
        ["W100", "SKU-1001", 120, 80, 18, "RDC-1"],
        ["W101", "SKU-2120", 40, 55, 7, "RDC-2"],
        ["W102", "SKU-3307", 210, 110, 28, "RDC-1"],
        ["W103", "SKU-4421", 18, 50, 4, "RDC-3"],
    ]

    with (DATA_DIR / "inventory_snapshot.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_shipments():
    rows = [
        ["shipment_id", "supplier_id", "sku", "planned_date", "actual_date", "quantity", "on_time_flag", "defect_flag"],
        ["SH-901", "SUP-11", "SKU-1001", "2026-10-01", "2026-10-02", 350, "Y", "N"],
        ["SH-902", "SUP-21", "SKU-2120", "2026-10-02", "2026-10-04", 220, "N", "Y"],
        ["SH-903", "SUP-11", "SKU-3307", "2026-10-03", "2026-10-03", 500, "Y", "N"],
        ["SH-904", "SUP-54", "SKU-4421", "2026-10-03", "2026-10-05", 120, "N", "Y"],
    ]

    with (DATA_DIR / "supplier_shipments.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def write_returns():
    rows = [
        ["return_id", "order_id", "return_date", "sku", "quantity", "return_reason", "channel"],
        ["R-881", "A1001", "2026-10-04", "SKU-1001", 1, "size_mismatch", "store"],
        ["R-882", "A1002", "2026-10-05", "SKU-2120", 1, "defective", "ecommerce"],
        ["R-883", "A1003", "2026-10-05", "SKU-3307", 2, "late_delivery", "store"],
        ["R-884", "A1004", "2026-10-07", "SKU-4421", 1, "quality_issue", "ecommerce"],
    ]

    with (DATA_DIR / "returns_events.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


if __name__ == "__main__":
    write_orders()
    write_inventory()
    write_shipments()
    write_returns()
    print(f"Generated bronze extracts under {DATA_DIR}")
