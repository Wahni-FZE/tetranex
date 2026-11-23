from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    create_custom_fields(
        {
            "Purchase Taxes and Charges Template": [
                {
                    "fieldname": "reverse_charge",
                    "label": "Reverse Charge Applicable",
                    "fieldtype": "Check",
                    "insert_after": "tax_category"
                }
            ]
        }
    )