// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.query_reports["Payment Register"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": "From Date",
            "fieldtype": "Date",
            "default": frappe.datetime.month_start()
        },
        {
            "fieldname": "to_date",
            "label": "To Date",
            "fieldtype": "Date",
            "default": frappe.datetime.get_today()
        },
        {
            "fieldname": "loan_id",
            "label": "Loan ID",
            "fieldtype": "Link",
            "options": "Loan"
        },
        {
            "fieldname": "payment_type",
            "label": "Payment Type",
            "fieldtype": "Link",
			"options": "Payment Type"
        },
        {
            "fieldname": "status",
            "label": "Payment Status",
            "fieldtype": "Link",
            "options": "Payment Status"
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
