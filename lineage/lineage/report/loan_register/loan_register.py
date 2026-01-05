# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    data = get_data(filters)

    return columns, data


def get_columns():
    return [
        {"label": "Loan ID", "fieldname": "name", "fieldtype": "Link", "options": "Loan", "width": 150},
        {"label": "Customer", "fieldname": "customer_id", "fieldtype": "Link", "options": "Customer", "width": 150},
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Data", "width": 180},

        {"label": "Loan Amount", "fieldname": "loan_amount", "fieldtype": "Currency", "width": 120},
        {"label": "Disbursed Amount", "fieldname": "disbursed_amount", "fieldtype": "Currency", "width": 130},
        {"label": "Paid Amount", "fieldname": "paid_amount", "fieldtype": "Currency", "width": 120},
        {"label": "Outstanding Amount", "fieldname": "outstanding_amount", "fieldtype": "Currency", "width": 150},

        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 120},
        {"label": "Created On", "fieldname": "creation", "fieldtype": "Datetime", "width": 150},
    ]


def get_data(filters):
    conditions = "1=1"

    # ⬇️ Using document creation date for filtering
    if filters.get("from_date"):
        conditions += " AND DATE(creation) >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND DATE(creation) <= %(to_date)s"
    if filters.get("customer"):
        conditions += " AND customer = %(customer)s"
    if filters.get("status"):
        conditions += " AND status = %(status)s"

    return frappe.db.sql(f"""
        SELECT
            name,
            customer_id,
            customer_name,
            loan_amount,
            disbursed_amount,
            paid_amount,
            outstanding_amount,
            status,
            creation
        FROM `tabLoan`
        WHERE {conditions}
        ORDER BY creation DESC
    """, filters, as_dict=True)
