// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.query_reports["Loan Application Register"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": "From Date",
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1)
        },
        {
            "fieldname": "to_date",
            "label": "To Date",
            "fieldtype": "Date",
            "default": frappe.datetime.get_today()
        },
        {
            "fieldname": "customer",
            "label": "Customer",
            "fieldtype": "Link",
            "options": "Customer"
        },
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Link",
            "options": "Loan Application Status"
        }
    ],
	
	onload: function(report) {
        report.page.add_inner_button(__("Back"), function() {
            frappe.set_route('reports');
            window.location.reload();
        });

        report.page.add_inner_button(__("Clear Filters"), function () {
            frappe.query_report.filters.forEach(filter => filter.set_value(""));
        });
    }
};
