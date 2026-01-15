// Copyright (c) 2026, Vortex Technology and contributors
// For license information, please see license.txt

frappe.ui.form.on("Branch", {
	refresh(frm) {
        frm.add_custom_button(__('Back'), function () {
            frappe.set_route('List', 'Branch', 'List')
        })
        frm.add_custom_button(__('Home'), function () {
            frappe.set_route('branches')
        })
	},
});
