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
            
            for payment in loan.repayment_schedule:
                else if loan.loan_tenure == 1:
                    if self.paid_amount < payment.payment_amount:
                        payment.payment_amount = payment.payment_amount - self.paid_amount
                        payment.remaining_balance = payment.remaining_balance - self.paid_amount
                        payment.status = "Partially Paid"
                    else if self.paid_amount == payment.payment_amount:
                        payment.remaining_balance = 0
                        payment.status = "Paid"
            
            """
            If Payment is partial for that month:
            a.)2 Months: Deducte the payment from the amount owed, and the outstanding amount should amount owed - paid amount.
            i)   Amount Owed is K6,900 over a period of 2 months.
            ii)  Amount Paid is K4,000 over a period of 2 months.
            iii) The new balance of K1,000 should be be divided by the remaning two months.
            
            🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁
            if loan.loan_tenure == 2:
                if payment.payment_amount > self.paid_amount and payment.idx == 1:
                    payment.payment_amount = payment.payment_amount - self.paid_amount
                    payment.status = "Partially Paid"
                else if payment.payment_amount < self.paid_amount:
                    payment.payment_amount = 
                    payment.status = "Partially Paid"
            
            b.)Months >= 3: Deducte the payment from the
            🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁
            else if loan.loan_tenure >= 3:
                pass
            
            c.)1 Month: If partial payment is made before the payment date
                i)  Amount Owed is K6,900 over a period of 1 month.
            ii)  Amount Paid is K4,000.
            iii) The new balance of K2,900 should be amount owed - amount paid.
            
            🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁
            
            """
            loan.save(ignore_permissions=True)

    def after_insert(self):
        pass
