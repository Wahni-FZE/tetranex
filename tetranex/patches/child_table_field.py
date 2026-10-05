from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    create_custom_fields(
        {
            "Sales Invoice Item": [
                {
                    "fieldname": "hs_code",
                    "label": "HS Code",
                    "fieldtype": "Data",
                    "insert_after": "item_name",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "country_of_origin",
                    "label": "Country of Origin",
                    "fieldtype": "Data",
                    "insert_after": "hs_code",
                    "allow_on_submit": 1,
                },
            ],
            "Delivery Note Item": [
                {
                    "fieldname": "custom_purchase_order",
                    "label": "Purchase Order",
                    "fieldtype": "Data",
                    "insert_after": "item_name",
                    "allow_on_submit": 1,
                }
            ],
        }
    )
