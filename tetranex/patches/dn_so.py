from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    create_custom_fields(
        {
            "Delivery Note": [
                {
                    "fieldname": "custom_purchase_order",
                    "label": "Purchase Order",
                    "fieldtype": "Data",
                    "insert_after": "posting_time",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "contact_by",
                    "label": "Contact By",
                    "fieldtype": "Data",
                    "insert_after": "custom_purchase_order",
                    "allow_on_submit": 1,
                }
            ],
            "Sales Order": [
                {
                    "fieldname": "remarks",
                    "label": "Remarks",
                    "fieldtype": "Long Text",
                    "insert_after": "title",
                    "allow_on_submit": 1,
                }
            ]            
        }
    )
