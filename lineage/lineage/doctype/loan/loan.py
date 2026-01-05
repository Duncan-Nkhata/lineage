# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class Loan(Document):
    def on_update(self):
        customer = frappe.get_doc("Customer", self.customer_id)
        if self.status in ["Pending Disbursement", "Active", "Partially Disbursed", "Overdue"]:
            customer.currently_owing = True
            row = customer.append('loan_history', {
                'loan_id': self.name,
                'loan_status': str(self.status),
                'loan_amount': self.loan_amount,
                'outstanding_amount': self.total_amount,
                'paid_amount': 0,
                'application_id': self.name
            })
            customer.save(ignore_permissions=True)
            
        elif self.status in ["Settled", "Written Off"]:
            customer = frappe.get_doc("Customer", self.customer_id)
            customer.currently_owing = False
            customer.save(ignore_permissions=True)
