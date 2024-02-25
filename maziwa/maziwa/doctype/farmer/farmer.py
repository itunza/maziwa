# Copyright (c) 2024, ewanyoike and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Farmer(Document):
	def before_save(self):
		self.full_names = f'{self.first_name} {self.middle_name or ""} {self.last_name}'
		
