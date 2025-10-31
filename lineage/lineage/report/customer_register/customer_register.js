// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.query_reports["Customer Register"] = {
    "filters": [
        {
            "fieldname": "customer_id",
            "label": __("Customer ID"),
            "fieldtype": "Link",
            "options": "Customer",
            "reqd": 0
        },
        {
            "fieldname": "id_number",
            "label": __("ID Number"),
            "fieldtype": "Data"
        },
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "reqd": 0,
            // First day of the current month
            "default": frappe.datetime.month_start(frappe.datetime.get_today())
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "reqd": 0,
            // Today's date
            "default": frappe.datetime.get_today()
        },
        {
            "fieldname": "status",
            "label": __("Status"),
            "fieldtype": "Link",
            "options": "Customer Status"
        },
        {
            "fieldname": "sex",
            "label": __("Sex"),
            "fieldtype": "Select",
            "options": "\nMale\nFemale"
        },
        {
            "fieldname": "employment_status",
            "label": __("Employment Status"),
            "fieldtype": "Link",
            "options": "Employment Status"
        },
        {
            "fieldname": "nationality",
            "label": __("Nationality"),
            "fieldtype": "Link",
            "options": "Nationality"
        },
        {
            "fieldname": "district",
            "label": __("District"),
            "fieldtype": "Link",
            "options": "District"
        },
        {
            "fieldname": "province",
            "label": __("Province"),
            "fieldtype": "Link",
            "options": "Province"
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
}
