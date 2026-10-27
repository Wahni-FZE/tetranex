from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    create_custom_fields(
        {
            "Delivery Note": [
                {
                    "fieldname": "total_dimensions",
                    "label": "Total Dimensions",
                    "fieldtype": "Data",
                    "insert_after": "total_qty",
                    "allow_on_submit": 1,
                }
            ]
        }
    )
