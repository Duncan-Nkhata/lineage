// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.listview_settings['Branch'] = {
	get_indicator: function(doc) {
		const status_colors = {
			"Active": "orange",
            "under Maintenance": "orange",
            "Inactive": "red"
		};
		return [__(doc.status), status_colors[doc.status], "status,=,"+doc.status];
	},

	onload: function(list_view) {
		list_view.page.add_inner_button(__("Home"), function () {
			frappe.set_route('branches')
		}
	)}
}