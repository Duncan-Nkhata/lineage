// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment", {
	refresh(frm) {
        frm.add_custom_button(__('Back'), function () {
            frappe.set_route('List', 'Payment', 'List')
        })
        frm.add_custom_button(__('Home'), function () {
            frappe.set_route('payments')
        })
	},
    payment_type(frm) {
        if (frm.doc.payment_type === 'Loan Disbursement') {
            frm.set_value('status', 'Pending Approval');
            frappe.refresh_field('status');

        } else if (frm.doc.payment_type === 'Loan Repayment') {
            frm.set_value('status', 'Pending Confirmation');
            frappe.refresh_field('status');
        }
    },
    payment_date(frm) {
        if (frm.doc.payment_date > frappe.datetime.get_today()) {
            frappe.msgprint('Payment Date cannot come after todays date.');
            frm.set_value('payment_date', '');
            frappe.refresh_field('payment_date');
        }
    },
    total_amount(frm) {
        if ((frm.doc.total_amount + frm.doc.disbursed_amount) > frm.doc.disbursement_amount && frm.doc.payment_type === 'Loan Disbursement') {
            frappe.msgprint('The payment amount cannot exceed the dibursement amount.');
            frm.set_value('total_amount', '');
            frappe.refresh_field('total_amount');
        }
    },
    loan_id(frm) {
        if ((frm.doc.total_amount + frm.doc.disbursed_amount) > frm.doc.disbursement_amount && frm.doc.payment_type === 'Loan Disbursement') {
            frappe.msgprint('The payment amount cannot exceed the dibursement amount.');
            frm.set_value('total_amount', '');
            frappe.refresh_field('total_amount');
        }
    }
});
