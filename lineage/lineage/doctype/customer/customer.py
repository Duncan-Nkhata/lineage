# Copyright (c) 2025, Vortex Technology and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, today
from datetime import datetime

def get_month_name(month_num):
    raise NotImplementedError


class Customer(Document):
	def after_insert(self):
		months = [
			"January", "February", "March", "April", "May", "June",
			"July", "August", "September", "October", "November", "December"
		]
		current_date = today()
		current_year = getdate(current_date).year
		current_month_num = getdate(current_date).month
		current_month = months[current_month_num - 1]

		if self.year == current_year and self.month == current_month:
			self.new_customer = True
			self.save(ignore_permissions=True)

	def validate(self):
		pass

	def on_update(self):
		pass
