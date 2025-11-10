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

        frm.add_custom_button(__('Make Payment'), function () {
            frappe.set_route('loans')
        })
	},
});
