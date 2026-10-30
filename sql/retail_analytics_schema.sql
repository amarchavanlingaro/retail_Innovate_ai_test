#!/usr/bin/env python3
"""Simple CLI used to describe an audit narrative from operational metrics."""

from collections import OrderedDict
import json


def describe(metrics):
    findings = OrderedDict()
    findings["inventory_fill_rate"] = "Below target" if metrics.get("inventory_fill_rate", 1.0) < 0.96 else "On plan"
    findings["otd_service_level"] = "At risk" if metrics.get("otd_service_level", 1.0) < 0.92 else "Healthy"
    findings["supplier_defect_rate"] = "Elevated" if metrics.get("supplier_defect_rate", 0.0) > 0.03 else "Controlled"
    findings["returns_rate"] = "Elevated" if metrics.get("returns_rate", 0.0) > 0.12 else "Within tolerance"
    return findings


if __name__ == "__main__":
    example = {
        "inventory_fill_rate": 0.937,
        "otd_service_level": 0.899,
        "supplier_defect_rate": 0.048,
        "returns_rate": 0.134,
    }
    print(json.dumps(describe(example), indent=2))
