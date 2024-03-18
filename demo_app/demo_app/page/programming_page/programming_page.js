frappe.pages['programming-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo Page',
		single_column: true
	});

	// add code ....
	page.set_title('My Page')
	page.set_indicator('Done', 'green')

	let $btn =page.set_primary_action('New' ,() => frappe.msgprint("Clicked Now"),'octicon octicon-plus')

	let $btnOne =page.set_secondary_action('Refresh' ,() => frappe.msgprint("Clicked Refresh"),'octicon octicon-plus')

	page.add_menu_item('Send Email',() => frappe.msgprint('Clicked Send Email'))
	page.add_action_item('Delete',() => frappe.msgprint('Clicked Delete'))
	
	let field = page.add_field({
		label:'Status',
		fieldtype:'Select',
		fieldname:'status',
		options:[
			'Open',
			'Closed',
			'Cancelled'
		],
		change(){
			frappe.msgprint(field.get_value());
		}
	});

	//render the  external html page or app css
	// $ (frappe.render_template("programming_page",{})).appendTo(page.body);


	$ (frappe.render_template("programming_page",{
		data:["Hi Frappe","sanil"]
	})).appendTo(page.body);
}
