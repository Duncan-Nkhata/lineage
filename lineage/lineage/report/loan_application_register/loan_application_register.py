# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    data = get_data(filters)

    return columns, data


def get_columns():
    return [
        {"label": "Application ID", "fieldname": "name", "fieldtype": "Link", "options": "Loan Application", "width": 150},
        {"label": "Customer", "fieldname": "customer_id", "fieldtype": "Link", "options": "Customer", "width": 150},
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Data", "width": 200},
        {"label": "Loan Amount", "fieldname": "loan_amount", "fieldtype": "Currency", "width": 200},
        {"label": "Interest Rate (%)", "fieldname": "interest_rate", "fieldtype": "Float", "width": 120},
        {"label": "Application Date", "fieldname": "application_date", "fieldtype": "Date", "width": 200},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 180},
    ]


def get_data(filters):
    conditions = "1=1"

    if filters.get("from_date"):
        conditions += " AND application_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND application_date <= %(to_date)s"
    if filters.get("customer"):
        conditions += " AND customer_id = %(customer_id)s"
    if filters.get("status"):
        conditions += " AND status = %(status)s"

    return frappe.db.sql(f"""
        SELECT 
            name,
            customer_id,
            customer_name,
            loan_amount,
            interest_rate,
            application_date,
            status
        FROM `tabLoan Application`
        WHERE {conditions}
        ORDER BY application_date DESC
    """, filters, as_dict=True)
