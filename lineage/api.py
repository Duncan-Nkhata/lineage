# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

@frappe.whitelist()
def value_of_approved():
    total = 0
    loan_apps = frappe.db.get_all(
        "Loan Application",
        filters={"status": "Approved"},
        fields=["loan_amount"]
    )

    for app in loan_apps:
        total += app.loan_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }
    
@frappe.whitelist()
def value_of_ur():
    total = 0
    loan_apps = frappe.db.get_all(
        "Loan Application",
        filters={"status": "Under Review"},
        fields=["loan_amount"]
    )

    for app in loan_apps:
        total += app.loan_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }
    
@frappe.whitelist()
def value_of_pr():
    total = 0
    loan_apps = frappe.db.get_all(
        "Loan Application",
        filters={"status": "Pending Review"},
        fields=["loan_amount"]
    )

    for app in loan_apps:
        total += app.loan_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }

@frappe.whitelist()
def value_of_rej():
    total = 0
    loan_apps = frappe.db.get_all(
        "Loan Application",
        filters={"status": "Rejected"},
        fields=["loan_amount"]
    )

    for app in loan_apps:
        total += app.loan_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }
    
