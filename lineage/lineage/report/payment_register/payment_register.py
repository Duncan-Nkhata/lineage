# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    return get_columns(), get_data(filters)


def get_columns():
    return [
        {"label": "Payment Date", "fieldname": "payment_date", "fieldtype": "Date", "width": 160},
        {"label": "Payment ID", "fieldname": "name", "fieldtype": "Link", "options": "Payment", "width": 150},
        {"label": "Paid Amount", "fieldname": "total_amount", "fieldtype": "Currency", "width": 200},
        {"label": "Payment Type", "fieldname": "payment_type", "fieldtype": "Data", "width": 200},
        {"label": "Loan ID", "fieldname": "loan_id", "fieldtype": "Link", "options": "Loan", "width": 150},
        {"label": "Payment Status", "fieldname": "status", "fieldtype": "Data", "width": 130}
    ]


def get_data(filters):
    conditions = "1=1"

    # Filter by creation date (first day of current month → today)
    if filters.get("from_date"):
        conditions += " AND DATE(payment_date) >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND DATE(payment_date) <= %(to_date)s"

    # Optional filters
    if filters.get("loan_id"):
        conditions += " AND loan_id = %(loan_id)s"
    if filters.get("payment_type"):
        conditions += " AND payment_type = %(payment_type)s"
    if filters.get("status"):
        conditions += " AND status = %(status)s"

    return frappe.db.sql(
        f"""
        SELECT
            payment_date,
            name,
            total_amount,
            payment_type,
            loan_id,
            status
        FROM `tabPayment`
        WHERE {conditions}
        ORDER BY creation DESC
        """,
        filters,
        as_dict=True,
    )
