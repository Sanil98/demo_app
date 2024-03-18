// Copyright (c) 2024, dcode and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {
	// refresh: function(frm) {
		// frappe.msgprint("Hello Sanil")
		// frappe.throw("this is a error..")
	// },

	// onload:function(frm){
	// 	frappe.msgprint("Hello Sanil from 'onload' event")
	// }

	// validate:function(frm){
	// 	frappe.throw("Hello Sanil from 'validate' event")
	// }

	// before_save:function(frm){
	// 	frappe.throw("Hello Sanil from 'before_save' event")
	// }

	// after_save: function(frm){
	// 	frappe.throw("Hello Sanil from 'after_save' event")
	// }

	// enable: function(frm){
	// 	frappe.throw("Hello Sanil from 'enable' fieldname event")
	// },

	// age:function(frm){
	// 	frappe.msgprint("Hello Sanil from 'age' fieldname event")
	// }

	// family_members_on_form_rendered:function(frm){
	// 	frappe.msgprint("Hello Sanil from 'family_member' child table rendered event")
	// }

	// before_submit: function(frm){
	// 		frappe.throw("Hello Sanil from 'before_submit'  event") //this not working -now done
	// 	}

	// on_submit: function(frm){
	// 	frappe.msgprint("Hello Sanil from 'on_submit'  event") //this not working -Now Done
	// }

	// before_cancel: function(frm){
	// 	frappe.throw("Hello Sanil from 'before_cancel'  event") //this not working -Now Done
	// },

	// after_cancel: function(frm){
	// 		frappe.msgprint("Hello Sanil from 'after_cancel'  event") //this not working -Now Done
	// 	}



// frappe.ui.form.on('Family Members', {

// 	// name1:function(frm){
// 	// 	frappe.msgprint("Hello sanil from child doctype 'name1' event")
// 	// },

// 	age(frm,cdt,cdn){
// 		frappe.msgprint("Hello sanil from 'age' child doctype fieldname event")
// 	}
// });

	// after_save: function(frm){
	// 		frappe.msgprint(__("The Full name is '{0}'",[frm.doc.first_name+" "+frm.doc.middle_name+" "+frm.doc.last_name]))

	// 		for (let row of frm.doc.family_members){
	// 			frappe.msgprint(__("{0}.The Family Member name is '{1}' and relation is '{2}' ",[row.idx,row.name1,row.relation]))
	// 		}
	// 	},
		// refresh:function(frm){
		// 	frm.set_intro("Now you can create a new Client side Scripting doctype")

		// 	if (frm.is_new()){
		// 		frm.set_intro("Now you can create a new client side scripting doctype")
		// 	}
		// },

	//////////////////////////////////////////////////	 frm.set_value ////////////////////////////////////

		// validate:function(frm){
		// 	frm.set_value('full_name',frm.doc.first_name +""+ frm.doc.middle_name+" "+frm.doc.last_name)
					
		// 	let row=frm.add_child('family_members',{
		// 		name1:"Krishna",
		// 		relation:'Father',
		// 		age:56,
		// 	})
		// },


	enable:function(frm){
		frm.set_df_property('first_name','reqd',1) 
		// frm.refresh_field('first_name');
		frm.set_df_property('middle_name','read_only',1)
		// frm.refresh_field('middle_name');
		frm.toggle_reqd('age',true)
	},

	// drop down
	refresh:function(frm){
		// frm.add_custom_button('Click Me Button',()=>{
		// 	frappe.msgprint(__('You clicked me !'));
		// })

		frm.add_custom_button('Click Me 1',()=>{
			frappe.msgprint(__('You clicked 1 !!'));
		},'click button')

		frm.add_custom_button('Click Me 2',()=>{
			frappe.msgprint(__('You clicked 2 !!'));
		},'click button')

		frm.add_custom_button('Click Me 3',()=>{
			frappe.msgprint(__('You clicked 3 !!'));
		},'click button')

		frm.add_custom_button('Click Me 4',()=>{
			frappe.msgprint(__('You clicked 4 !!'));
		},'click button')
	}

});


