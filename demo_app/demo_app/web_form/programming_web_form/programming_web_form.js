frappe.ready(function() {
	// Event binding can be done here, if needed

	frappe.web_form.after_load = () => {
		frappe.msgprint("Please fill all values carefully");
	};

	frappe.web_form.after_load = () =>{
		frappe.web_form.on('enable',(field,value)=>{
			frappe.msgprint('Hi User');
		});

		frappe.web_form.on('dob',(field,value)=>{
			if (value){
				dob=new Date(value);
				var today =new Date();
				var age=Math.floor((today-dob)/ (365 * 24 * 60 * 60 * 1000));
				frappe.web_form.set_value("age",[age])
			}
		});
	}

	frappe.web_form.validate = () =>{
		email_id=frappe.web_form.get_value("email");
		var pattern =/^\d*(?:\.\d{1,2})?$/;
	}
	
});
