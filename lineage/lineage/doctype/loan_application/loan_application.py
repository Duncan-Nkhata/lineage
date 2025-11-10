# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LoanApplication(Document):
    def after_insert(self):
        doc = frappe.new_doc("ToDo")
        doc.priority = "High"
        doc.status = "Open"
        doc.allocated_to = frappe.session.user
        doc.reference_type = "Loan Application"
        doc.reference_name = self.name
        doc.description = f"Assignment for {self.name}"
        doc.insert(ignore_permissions=True)

    def on_update(self):
        if self.status == "Approved":
            if frappe.db.exists("Loan", {"loan_application": self.name}):
                return
            doc = frappe.new_doc("Loan")
            doc.status = "Awaiting Disbursement"
            doc.loan_application = self.name
            doc.loan_amount = self.loan_amount
            doc.service_fee = self.service_fee
            doc.interest = self.interest
            doc.interest_rate = self.interest_rate
            doc.total_amount = self.amount_owed
            doc.outstanding_amount = self.amount_owed
            doc.amount_received = self.disbursement_amount
            doc.customer_id = self.customer_id
            doc.customer_id_number = self.customer_id_number
            doc.customer_name = self.customer_name
            doc.customer_phone_number = self.customer_phone_number
            doc.customer_email = self.customer_email
            doc.application_id = self.name
            doc.loan_type = self.loan_type
            doc.application_status = self.status
            
            doc.kin_full_name = self.nok_name
            doc.kin_phone_number = self.nok_phone_number
            doc.kin_relationship = self.nok_relationship
            doc.kin_email = self.nok_email_address
            
            
            doc.insert(ignore_permissions=True)
            doc.submit()

            customer = frappe.get_doc("Customer", self.customer_id)
            customer.status = "Active"
            customer.save(ignore_permissions=True)
