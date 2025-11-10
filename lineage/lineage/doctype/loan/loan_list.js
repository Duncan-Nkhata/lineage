// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.listview_settings['Loan'] = {
	get_indicator: function(doc) {
		const status_colors = {
			"Awaiting Disbursement": "orange",
            "On Hold": "orange",
            "Active": "green",
            "Partially Disbursed": "blue",
            "Defaulted": "red",
            "Written Off": "red",
            "Settled": "green"
		};
		return [__(doc.status), status_colors[doc.status], "status,=,"+doc.status];
	},

	onload: function(list_view) {
		$('.col-lg-2.layout-side-section').hide();
		
		list_view.page.add_inner_button(__("Home"), function () {
			frappe.set_route('loans')
		}
	)}
}