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
});
