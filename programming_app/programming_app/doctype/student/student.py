import frappe
from frappe.model.document import Document


class Student(Document):
	def after_insert(self):
		if not frappe.db.exists("User", self.email):
			user = frappe.get_doc({
				"doctype": "User",
				"email": self.email,
				"first_name": self.first_name,
				"last_name": self.last_name,
				"roles": [{"role": "Student"}]
			})
			user.insert(ignore_permissions = True)

	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"

	def on_trash(self):
		user = frappe.get_all(
        "User",
        filters={"email": self.email},
        fields=["name"],
        limit=1
    )
		if user:
			frappe.delete_doc("User", user[0]["name"], ignore_permissions=True)

	



