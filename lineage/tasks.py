# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import getdate, today
from datetime import datetime

@frappe.whitelist()
def suspend(self):
    doc = frappe.get_doc("Customer", self)
    frappe.errprint(doc.status)
    doc.status = "Suspended"
    doc.save(ignore_permissions=True)
    frappe.msgprint(_("Customer: {0} has been suspended.").format(doc.name))

@frappe.whitelist()
def blacklist(self):
     doc = frappe.get_doc("Customer", self)
     doc.status = "Blacklisted"
     doc.save(ignore_permissions=True)
     frappe.msgprint(_("Customer: {0} has been blacklisted.").format(doc.name))

@frappe.whitelist()
def reactivate(self):
     doc = frappe.get_doc("Customer", self)
     doc.status = "Active"
     doc.save(ignore_permissions=True)
     frappe.msgprint(_("Customer: {0} has been reactivated.").format(doc.name))

def newLoan(self):
     pass
