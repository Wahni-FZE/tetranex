from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    create_custom_fields(
        {
            "Sales Invoice": [
                {
                    "fieldname": "hs_code",
                    "label": "HS Code",
                    "fieldtype": "Data",
                    "insert_after": "due_date",
                    "allow_on_submit": 1,
                }
            ],
            "Delivery Note": [
                {
                    "fieldname": "hs_code",
                    "label": "HS Code",
                    "fieldtype": "Data",
                    "insert_after": "posting_time",
                    "allow_on_submit": 1,
                }
            ],
            "Delivery Note Item": [
                {
                    "fieldname": "gross_weight",
                    "label": "Gross Weight",
                    "fieldtype": "Data",
                    "insert_after": "weight_uom",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "volume",
                    "label": "Volume",
                    "fieldtype": "Data",
                    "insert_after": "gross_weight",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "package_size",
                    "label": "Package Size",
                    "fieldtype": "Data",
                    "insert_after": "volume",
                    "allow_on_submit": 1,
                }
            ]
        }
    )
