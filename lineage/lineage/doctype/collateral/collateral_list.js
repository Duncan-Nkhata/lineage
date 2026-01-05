// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.listview_settings['Collateral'] = {
	get_indicator: function(doc) {
		const status_colors = {
			"In Use": "green",
			"Returned": "blue",
			"Overdue": "orange",
			"Liquidated": "red",
            "Defaulted": "purple"
		};
		return [__(doc.status), status_colors[doc.status], "status,=,"+doc.status];
	},

	onload: function(list_view) {
		$('.col-lg-2.layout-side-section').hide();
		
		list_view.page.add_inner_button(__("Home"), function () {
			frappe.set_route('collateral(s)')
		}
	)}
}