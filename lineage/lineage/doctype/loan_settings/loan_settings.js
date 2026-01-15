// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.ui.form.on("Loan Settings", {
	refresh(frm) {
        frm.add_custom_button(__('Back'), function () {
            frappe.set_route('loans')
        })
        frm.add_custom_button(__('Home'), function () {
            frappe.set_route('home')
        })
	},
});
