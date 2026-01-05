// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.ui.form.on("Loan", {
	refresh(frm) {
        frm.add_custom_button(__('Back'), function () {
            frappe.set_route('List', 'Loan', 'List')
        })
        frm.add_custom_button(__('Home'), function () {
            frappe.set_route('loans')
        })

        if (frm.doc.status === "Awaiting Disbursement" || frm.doc.status === "Partially Disbursed") {    
            frm.add_custom_button(__('Disburse Funds'), function () {
                frappe.new_doc('Payment', {
                        customer_id: frm.doc.custoemr_id,
                        payment_type: 'Loan Disbursement',
                        loan_id: frm.doc.name
                });
            })
        }

        if (frm.doc.status === "Active") {
            frm.add_custom_button(__('Make Payment'), function () {
            frappe.new_doc('Payment', {
                customer_id: frm.doc.custoemr_id,
                payment_type: 'Loan Repayment',
                loan_id: frm.doc.name
                });
            })
        }

        if (frm.doc.status !== "Withdrawn" && frm.doc.status === "Awaiting Disbursement") {
            frm.add_custom_button(__('Withdraw'), function () {
            frm.set_value('status', 'Withdrawn');
            frappe.refresh_field('status');
            frappe.msgprint(__('Loan has been marked as Withdrawn.'));
        })
        }
	},
});
