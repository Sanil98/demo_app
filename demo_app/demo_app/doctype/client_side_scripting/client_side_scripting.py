# Copyright (c) 2024, dcode and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ClientSideScripting(Document):
	pass

	# @frappe.whitelist()
	# def frappe_call(msg):
	# 	import time
	# 	time.sleep(5)
	# 	frappe.msgprint(msg)
		# self.mobile_no=8932437634
		# self.email='sanilkumar@pradan.net'
		# return "Hi This msg from frappe_call"