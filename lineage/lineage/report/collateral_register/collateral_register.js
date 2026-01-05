// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt
frappe.query_reports["Collateral Register"] = {
    "filters": [
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            default: frappe.datetime.month_start(),
            reqd: 1
        },
        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date",
            default: frappe.datetime.get_today(),
            reqd: 1
        },
        {
            fieldname: "status",
            label: __("Collateral Status"),
            fieldtype: "Link",
            options: "Collateral Status",
            reqd: 0
        },
        {
            fieldname: "type",
            label: __("Collateral Type"),
            fieldtype: "Link",
            options: "Collateral Type",
            reqd: 0
        },
        {
            fieldname: "condition",
            label: __("Collateral Condition"),
            fieldtype: "Link",
            options: "Collateral Condition",
            reqd: 0
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
