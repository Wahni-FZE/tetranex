from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    create_custom_fields(
        {
            "Supplier Quotation": [
                {
                    "fieldname": "custom_shipping_address",
                    "label": "Custom Shipping Address",
                    "fieldtype": "Link",
                    "options": "Address",
                    "insert_after": "shipping_address",
                    "allow_on_submit": 1,
                }
            ]
        }
    )
