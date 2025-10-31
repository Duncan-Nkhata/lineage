# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    data = get_data(filters)

    return columns, data


def get_columns():
    return [
        {"label": _("Customer ID"), "fieldname": "name", "fieldtype": "Link", "options": "Customer", "width": 150},
        {"label": _("Full Name"), "fieldname": "full_name", "fieldtype": "Data", "width": 200},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 120},
        {"label": _("Sex"), "fieldname": "sex", "fieldtype": "Data", "width": 100},
        {"label": _("Phone Number"), "fieldname": "phone_number", "fieldtype": "Data", "width": 150},
        {"label": _("ID Number"), "fieldname": "id_number", "fieldtype": "Data", "width": 180},
        {"label": _("Nationality"), "fieldname": "nationality", "fieldtype": "Data", "width": 200},
        {"label": _("District"), "fieldname": "district", "fieldtype": "Data", "width": 200},
        {"label": _("Province"), "fieldname": "province", "fieldtype": "Data", "width": 200},
        {"label": _("Employment Status"), "fieldname": "employment_status", "fieldtype": "Data", "width": 150},
    ]


def get_data(filters):
    conditions = []
    values = {}

    if filters.get("customer_id"):
        conditions.append("name = %(customer_id)s")
        values["customer_id"] = filters["customer_id"]

    if filters.get("id_number"):
        conditions.append("id_number = %(id_number)s")
        values["id_number"] = filters["id_number"]

    if filters.get("district"):
        conditions.append("district = %(district)s")
        values["district"] = filters["district"]

    if filters.get("province"):
        conditions.append("province = %(province)s")
        values["province"] = filters["province"]

    if filters.get("nationality"):
        conditions.append("nationality = %(nationality)s")
        values["nationality"] = filters["nationality"]

    if filters.get("status"):
        conditions.append("status = %(status)s")
        values["status"] = filters["status"]

    if filters.get("sex"):
        conditions.append("sex = %(sex)s")
        values["sex"] = filters["sex"]

    if filters.get("employment_status"):
        conditions.append("employment_status = %(employment_status)s")
        values["employment_status"] = filters["employment_status"]

    if filters.get("from_date"):
        conditions.append("date_of_joining >= %(from_date)s")
        values["from_date"] = filters["from_date"]

    if filters.get("to_date"):
        conditions.append("date_of_joining <= %(to_date)s")
        values["to_date"] = filters["to_date"]

    condition_str = " AND ".join(conditions)
    if condition_str:
        condition_str = "WHERE " + condition_str

    query = f"""
        SELECT
            name,
            id_number,
            nationality,
            district,
            province,
            full_name,
            status,
            sex,
            phone_number,
            passport_nrc,
            employment_status
        FROM
            `tabCustomer`
        {condition_str}
        ORDER BY
            date_of_joining DESC
    """

    return frappe.db.sql(query, values, as_dict=True)

