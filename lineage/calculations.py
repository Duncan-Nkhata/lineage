# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import getdate, today
from datetime import datetime

@frappe.whitelist()
def settings():
    settings = frappe.get_doc("Loan Settings")
    return settings.as_dict()
