# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class Loan(Document):
    def on_update(self):
        if self.status in ["Active", "Partially Disbursed", "Overdue"]:
            customer = frappe.get_doc("Customer", self.customer_id)
            customer.currently_owing = True
            row = customer.append('loan_history', {
                'loan_id': self.name,
                'loan_status': str(self.status),
                'loan_amount': self.loan_amount,
                'outstanding_amount': self.amount_owed,
                'paid_amount': 0,
                'application_id': self.name
            })
            customer.save(ignore_permissions=True)
