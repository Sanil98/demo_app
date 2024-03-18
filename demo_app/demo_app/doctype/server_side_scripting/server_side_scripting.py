# Copyright (c) 2024, dcode and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ServerSideScripting(Document):
    # pass

							######		1.# server side Events #########
	# def validate(self):
	# 	frappe.msgprint('Hello Frappe')

	# def before_save(self):
	# 	frappe.throw("Hello Sanil from 'before_save' event")
	
	# def before_insert(self):
	# 	frappe.throw("Hello Sanil from 'before_insert' event")

	# def after_insert(self):
	# 	frappe.throw("Hello Sanil from 'after_insert' event")

	# def on_update(self):
	# 	frappe.msgprint("Hello Sanil from 'on_update' event")

	# def before_submit(self):
	# 	frappe.msgprint("Hello Sanil from 'before_submit' ")

	# def on_submit(self):
	# 	frappe.msgprint("Hello Sanil from 'on_submit'")

	# def on_cancel(self):
	# 	frappe.msgprint("Hello Sanil from 'on_cancel'")

	# def on_trash(self):
	# 	frappe.msgprint("Hello Sanil from 'on_trash'")  # after delet
	
	# def after_delete(self):
	# 	frappe.msgprint("Hello Sanil from 'after_delete'")  # after_delete


	# def validate(self):
	# 	frappe.msgprint(("Hello my full_name is '{0}' ").format(self.first_name +" "+ self.middle_name+" "+self.last_name))
					
						##################### 2.value fetching #############	

	# def validate(self):
		
	# 	for row in self.get("family_members"):
			
	# 		frappe.msgprint(("{0}.The Family Member name is '{1}' and relation is '{2}' ").format(row.idx,row.name1,row.relation))

							############ 3.frappe.get_doc(doctype,name)  ###################

	# def validate(self):
	# 	self.get_document()

	# def get_document(self):
	# 	doc=frappe.get_doc('Client Side Scripting', self.client_side_doc)
	# 	frappe.msgprint(("The First Name is {0} and age is {1}").format(doc.first_name,doc.age))
		
	# 	for row in doc.get("family_members"):
			
	# 		frappe.msgprint(("{0}.The Family Member name is '{1}' and relation is '{2}' ").format(row.idx,row.name1,row.relation))

			##### 4.Server Side Scripting || new_doc() & delete_doc() #######

	# frappe.new_doc(doctype)

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc=frappe.new_doc("Client Side Scripting")
	# 	doc.first_name='Pradan'
	# 	doc.last_name='NGO'
	# 	doc.age=23
	# 	doc.append("family_members",{
	# 		"name1":"Utpal",
	# 		"relation":"Founder",
	# 		"age":40
	# 	})
	# 	doc.insert()
    
		# some escape hatches that can be used to skip certain check
	# doc.insert(

	# 	ignore_permissions=True #ignore write permission during insert
	# 	ignore_links=True, #ignore link validation in the document
	# 	ignor_if_duplicate=True, # don't insert if DuplicateEntryError is thrown
	# 	ignore_mandatory=True # insert even if mendetory field are not set
	# )
	
	


		######################### 5.frappe.delete_doc(doctype,name) ######################

	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting','PR-0027')
    
	# def validate(self):
	# 	self.save_document()

							############### 6.Server Side Scripting Document Methods doc.save()  ###############

	# def save_document(self):
	# 	doc=frappe.new_doc("Client Side Scripting")
	# 	doc.first_name='kelvin'
	# 	doc.age=23
	# 	doc.save()

	# 	doc.save(
	# 		ignore_permissions=True #ignore write permission during insert
	# 		ignore_version=True # do not create a version record
	# 	)
    
	# doc.db_set()
    
	# def validate(self):
	# 	self.db_set_document()

	# def db_set_document(self):
	# 	doc=frappe.get_doc('Client Side Scripting', 'PR-0028')
	# 	doc.db_set('age',50)


						# 7.Database API #
		
		# frappe.db.get_list 
		# frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)

	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc=frappe.db.get_list('Client Side Scripting',
	# 		filters={'enable':1
	# 		},
	# 		fields=['first_name', 'age'])
	# 	for d in doc:
	# 		frappe.msgprint(_("The parent first name is {0} and age is {1}").format(d.first_name,d.age))

		#### 8. frappe.db.get_value(doctype, name, fieldname) or frappe.db.get_value(doctype,filters,fieldname)#########
			
	# def validate(self):
	# 	self.get_value()

	
	# def	get_value(self):
	# 	first_name, age = frappe.db.get_value('Client Side Scripting', 'PR-0027', ['first_name', 'age'])
	# 	frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(first_name, age))
	# 9.
    
	# def validate(self):
	# 	self.set_value()


	# def	set_value(self):
	# 	frappe.db.set_value('Client Side Scripting', 'PR-0027',  'age',25)
	# 	first_name, age = frappe.db.get_value('Client Side Scripting', 'PR-0027', ['first_name', 'age'])
	# 	frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(first_name, age))

		# 10.
	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting','PR-0029'):
	# 		frappe.msgprint(_("The document exits in Database"))
	# 	else:
	# 		frappe.msgprint(_("The document does not exits in Database"))

			################# frappe.db.count(doctype,filters) ##########################

	# def validate(self):
	# 	doc_count= frappe.db.count('Client Side Scripting',{'enable':1}) #True
	# 	frappe.msgprint(_("The Enable Document is {0}").format(doc_count))

	# def validate(self):
	# 	self.sql()

	# def sql(self):
	# 	data=frappe.db.sql("""select  first_name,age from `tabClient Side Scripting` where enable = 1""", as_dict=1)
	# 	# data=frappe.db.sql("select  first_name,age from `tabClient Side Scripting` where enable = 1", as_dict=1)
		
	# 	for d in data:
	# 		frappe.msgprint(_("The Parent First Name Is {0} and age is {1}").format(d.first_name,d.first_age))

	@frappe.whitelist()
	def frm_call(self,msg):
		import time
		time.sleep(5)
		# frappe.msgprint(msg)
		self.mobile_no=8932437634
		self.email='sanilkumar@pradan.net'
		return "Hi This msg from frm_call"
