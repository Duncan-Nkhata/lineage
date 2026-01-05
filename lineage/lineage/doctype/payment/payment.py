# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class Payment(Document):
    def validate(self):
        if self.loan_status not in ["Awaiting Disbursement", "Partially Disbursed"] and self.payment_type == "Loan Disbursement":
            frappe.throw(_("Loan is not eligible for disbursement. Current status: {0}").format(self.loan_status))
        
        if self.status == "Approved":
            if self.payment_type == "Loan Disbursement":
                loan = frappe.get_doc("Loan", self.loan_id)
                disbursed_amount = loan.disbursed_amount + self.total_amount
                if (loan.disbursed_amount + self.total_amount) == loan.disbursement_amount:
                    loan.status = "Active"
                    frappe.msgprint("Loan is now active ✅.")
                elif (loan.disbursed_amount + self.total_amount) < loan.disbursement_amount:
                    loan.status = "Partially Disbursed"
                loan.disbursed_amount = disbursed_amount
                loan.save(ignore_permissions=True)
        elif self.status == "Confirmed":
            if self.payment_type == "Loan Repayment":
                loan = frappe.get_doc("Loan", self.loan_id)
                paid_amount = loan.paid_amount + self.total_amount
                new_balance = loan.outstanding_amount - self.total_amount
                
                if paid_amount == loan.total_amount:
                    loan.status = "Settled"
                    frappe.msgprint("Loan is now closed ✅.")
                loan.paid_amount = paid_amount
                loan.outstanding_amount = new_balance
                loan.save(ignore_permissions=True)
        
        if self.status in ["Approved", "Confirmed"]:
            loan = frappe.get_doc("Loan", self.loan_id)
            customer = frappe.get_doc("Customer", loan.customer_id)
            for row in customer.loan_history:
                if row.loan_id == loan.name:
                    row.loan_status = loan.status
                    row.outstanding_amount = loan.outstanding_amount
                    row.paid_amount = loan.paid_amount
                customer.save(ignore_permissions=True)
                
    def on_update(self):
        if self.status in ["Approved", "Confirmed"]:
            loan = frappe.get_doc("Loan", self.loan_id)
            row = loan.append('payment_history', {
                'payment_id': self.name,
                'payment_type': self.payment_type,
                'paid_amount': self.total_amount,
                'payment_date': self.payment_date
            })
            loan.save(ignore_permissions=True)
