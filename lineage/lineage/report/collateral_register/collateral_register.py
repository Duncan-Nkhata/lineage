# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    columns = [
        {"label": "Collateral ID", "fieldname": "collateral_id", "fieldtype": "Data", "width": 150},
        {"label": "Collateral Type", "fieldname": "type", "fieldtype": "Data", "width": 150},
        {"label": "Collateral Condition", "fieldname": "condition", "fieldtype": "Data", "width": 150},
        {"label": "Collateral Value", "fieldname": "value", "fieldtype": "Currency", "width": 150},
        {"label": "Collateral Status", "fieldname": "status", "fieldtype": "Data", "width": 130},
        {"label": "Loan ID", "fieldname": "loan_id", "fieldtype": "Link", "options": "Loan", "width": 150},
        {"label": "Date Added", "fieldname": "creation", "fieldtype": "Date", "width": 130},
    ]

    data = get_data(filters)
    return columns, data


def get_data(filters):
    conditions = "WHERE docstatus < 2"
    values = {}

    # Date filters
    if filters.get("from_date"):
        conditions += " AND creation >= %(from_date)s"
        values["from_date"] = filters.get("from_date")

    if filters.get("to_date"):
        conditions += " AND creation <= %(to_date)s"
        values["to_date"] = filters.get("to_date")

    # Collateral Status filter
    if filters.get("status"):
        conditions += " AND status = %(status)s"
        values["status"] = filters.get("status")

    # Collateral Type filter
    if filters.get("type"):
        conditions += " AND type = %(type)s"
        values["type"] = filters.get("type")

    # Collateral Condition filter
    if filters.get("condition"):
        conditions += " AND condition = %(condition)s"
        values["condition"] = filters.get("condition")

    query = f"""
        SELECT
            name AS collateral_id,
            type,
            `condition`,
            `value`,
            status,
            loan_id,
            DATE(creation) AS creation
        FROM `tabCollateral`
        {conditions}
        ORDER BY creation DESC
    """

    return frappe.db.sql(query, values, as_dict=1)

