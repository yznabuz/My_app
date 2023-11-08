# Copyright (c) 2023, yzn and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class Car(Document):
	def validate(self):
		car_plate=self.car_plate
		if len(car_plate)!=8:
			frappe.throw(_("Car plate must be like this form abcd-123"))
		if car_plate[4]!="-" or car_plate[:4].isalpha()==False or car_plate[5:].isnumeric()==False:
			frappe.throw(_("Car plate must be like this form abcd-123"))
