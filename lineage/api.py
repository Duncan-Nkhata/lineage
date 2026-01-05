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
    
@frappe.whitelist()
def value_of_loans():
    total = 0
    loans = frappe.db.get_all(
        "Loan",
        filters={"status": ["in", ["Active", "Partially Disbursed", "Overdue"]]},
        fields=["outstanding_amount"]
    )

    for loan in loans:
        total += loan.outstanding_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }
    
@frappe.whitelist()
def value_of_active_loans():
    total = 0
    loans = frappe.db.get_all(
        "Loan",
        filters={"status": "Active"},
        fields=["outstanding_amount"]
    )

    for loan in loans:
        total += loan.outstanding_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }

@frappe.whitelist()
def value_of_overdue_loans():
    total = 0
    loans = frappe.db.get_all(
        "Loan",
        filters={"status": "Overdue"},
        fields=["outstanding_amount"]
    )

    for loan in loans:
        total += loan.outstanding_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }
    
@frappe.whitelist()
def value_of_paid_loans():
    total = 0
    loans = frappe.db.get_all(
        "Loan",
        filters={"status": "Settled"},
        fields=["loan_amount"]
    )

    for loan in loans:
        total += loan.loan_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }

@frappe.whitelist()
def value_of_payments():
    total = 0
    payments = frappe.db.get_all(
        "Payment",
        filters={"status": "Confirmed"},
        fields=["total_amount"]
    )

    for payment in payments:
        total += payment.total_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }

@frappe.whitelist()
def value_of_loan_disbursements():
    total = 0
    payments = frappe.db.get_all(
        "Payment",
        filters={"status": "Approved", "payment_type": "Loan Disbursement"},
        fields=["total_amount"]
    )

    for payment in payments:
        total += payment.total_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }

@frappe.whitelist()    
def value_of_loan_repayments():
    total = 0
    payments = frappe.db.get_all(
        "Payment",
        filters={"status": "Confirmed", "payment_type": "Loan Repayment"},
        fields=["total_amount"]
    )

    for payment in payments:
        total += payment.total_amount or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }

@frappe.whitelist()
def value_of_collateral():
    total = 0
    collateral = frappe.db.get_all(
        "Collateral",
        filters={"status": "In Use"},
        fields=["value"]
    )

    for item in collateral:
        total += item.value or 0
        
    return {
        "value": total,
        "fieldtype": "Currency",
        }
