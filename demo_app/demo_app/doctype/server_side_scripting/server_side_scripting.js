// Copyright (c) 2024, dcode and contributors
// For license information, please see license.txt

frappe.ui.form.on('Server Side Scripting', {
	enable: function(frm) {
		frm.call({
			doc: frm.doc,
			method: 'frm_call',
			args: {
				msg: "hello"
			},
			freeze: true,
			freeze_message:__('Calling frm_call Method'),
			callback: function(r) {
				// frappe.msgprint(r.message)
				// frappe.msgprint("server side calling compleated")
			}
		});
	}
});

// frappe.ui.form.on('Server Side Scripting', {
// 	enable: function(frm) {
// 		frappe.call({
// 			doc: frappe.call,
// 			method: "demo_app.demo_app.doctype.client_side_scripting.client_side_scripting.frappe_call",
// 			args: {
// 				msg: "hello"
// 			},
// 			freeze: true,
// 			freeze_message:__('Calling frappe_call Method'),
// 			callback: function(r) {
// 				frappe.msgprint(r.message)
// 			}
// 		});
// 	}
// });