from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    create_custom_fields(
        {
            "Delivery Note": [
                {
                    "fieldname": "type_of_package",
                    "label": "Type of Package",
                    "fieldtype": "Data",
                    "insert_after": "total_qty",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "package_in_total",
                    "label": "Package in Total",
                    "fieldtype": "Data",
                    "insert_after": "type_of_package",
                    "allow_on_submit": 1,
                }
            ]            
        }
    )
