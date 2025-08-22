import frappe
import json

# Student custom api

@frappe.whitelist()
def get_all_students():
    students = frappe.get_all(
        "Student",
        fields = ["name", "first_name", "last_name", "full_name", "email", "gender", "date_of_birth"]
    )
    return students

@frappe.whitelist()
def get_student_lite(student_id):
    student = frappe.db.get_value(
        "Student",
        student_id,
        ["name", "first_name", "last_name", "full_name", "email", "gender", "date_of_birth"],
        as_dict = True
    )
    guardian_details = frappe.get_all(
        "Student Parent",
        filters = {"parent":student_id, "parenttype":"Student"},
        fields = ["full_name", "relationship"]
    )
    student["guardian_details"] = guardian_details
    return student


@frappe.whitelist(methods=["POST"])
def create_student():
    if frappe.request and frappe.request.data:
        data = json.loads(frappe.request.data)
    student = frappe.get_doc({
        "doctype": "Student",
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "email": data.get("email"),
        "gender": data.get("gender"),
        "date_of_birth": data.get("date_of_birth"),
        "guardian_details": data.get("guardian_details", [])
    })
    student.insert()
    frappe.db.commit()
    return{
        "message": f"Student {student.full_name} created successfully"
    }

@frappe.whitelist(methods=["DELETE"])
def delete_student(student_id):
    student = frappe.get_doc("Student", student_id)
    student.delete()
    frappe.db.commit()
    return{
        "message": f"Student {student.full_name} deleted successfully"
    }

# teacher custom api
@frappe.whitelist()
def get_all_teachers():
    teachers = frappe.get_all(
        "Teacher",
        fields= ["first_name", "last_name", "full_name","gender","department", "phone_number", "email"],
        order_by="creation desc"
    )
    return teachers


@frappe.whitelist()
def get_teacher_lite(teacher_id):
    teacher = frappe.db.get_value(
        "Teacher",
        teacher_id,
        ["name", "first_name", "last_name", "full_name", "gender", "department", "phone_number", "email"],
        as_dict=True
    )
    return teacher

@frappe.whitelist(methods=["POST"])
def create_teacher():
    if frappe.request and frappe.request.data:
        data = json.loads(frappe.request.data)
    teacher = frappe.get_doc({
        "doctype":"Teacher",
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "gender": data.get("gender"),
        "department": data.get("department"),
        "email": data.get("email"),
        "phone_number": data.get("phone_number")
    })
    teacher.insert()
    frappe.db.commit()
    return{
        "messsage":f"Teacher {teacher.full_name} created successfully"
    }

@frappe.whitelist(methods=["DELETE"])
def delete_teacher(teacher_id):
    teacher = frappe.get_doc("Teacher", teacher_id)
    teacher.delete()
    frappe.db.commit()
    return{
        "message": f"Teacher {teacher.full_name} deleted successfully"
    }

# class custom api

@frappe.whitelist()
def get_all_classes():
    classes = frappe.get_all(
        "Class",
        fields = ["name","class_name","class_teacher","maximum_students"]
    )
    return classes

@frappe.whitelist()
def get_class_lite(class_id):
    Class = frappe.db.get_value(
        "Class",
        class_id,
        ["name","class_name","class_teacher","maximum_students"],
        as_dict = True
    )
    class_subjects = frappe.get_all(
        "Class Subjects",
        filters = {"parent":class_id, "parenttype":"Class"},
        fields= ["subject_name","subject_teacher","description"]
    )
    Class["class_subjects"] = class_subjects
    return Class

@frappe.whitelist(methods=["POST"])
def create_class():
    if frappe.request and frappe.request.data:
        data = json.loads(frappe.request.data)
    Class = frappe.get_doc({
        "doctype": "Class",
        "class_name": data.get("class_name"),
        "class_teacher": data.get("class_teacher"),
        "maximum_students": data.get("maximum_students"),
        "class_subjects": data.get("class_subjects",[])
    })
    Class.insert()
    frappe.db.commit()
    return{
        "message": f"Class {Class.class_name} created succesfully"
    }
@frappe.whitelist(methods=["DELETE"])
def delete_class(class_id):
    Class = frappe.get_doc("Class",class_id)
    Class.delete()
    frappe.db.commit()
    return{
        "message": f"Class {Class.class_name} deleted successfully"
    }