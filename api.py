# auth_api.py

import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def login(username, password):
    try:
        # Authenticate the user
        frappe.local.login_manager.authenticate(username, password)

        # Check if the user is authenticated
        if frappe.local.session.user:
            return {"status": "success", "user": frappe.local.session.user}
        else:
            return {"status": "failed", "message": "Invalid credentials"}

    except frappe.AuthenticationError as e:
        return {"status": "failed", "message": str(e)}

    except Exception as e:
        frappe.log_error(_("Error in login API: {0}".format(str(e))))
        return {"status": "failed", "message": "An error occurred during authentication"}

# Example usage:
# http://your-erpnext-instance/api/method/your-app-name.auth_api.login?username=admin&password=admin
