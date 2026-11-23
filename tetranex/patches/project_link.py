from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    create_custom_fields(
        {
            "Request for Quotation": [
                {
                    "fieldname": "project",
                    "label": "Project",
                    "fieldtype": "Link",
                    "options": "Project",
                    "insert_after": "project_name",
                    "allow_on_submit": 1,
                },
            ],
            "Quotation": [
                {
                    "fieldname": "project",
                    "label": "Project",
                    "fieldtype": "Link",
                    "options": "Project",
                    "insert_after": "project_name",
                    "allow_on_submit": 1,
                },
            ],
        }
    )
