from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    create_custom_fields(
        {
            "Quotation": [
                {
                    "fieldname": "customer_rfq",
                    "label": "Customer RFQ",
                    "fieldtype": "Data",
                    "insert_after": "transaction_date",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "selling_margin",
                    "label": "Selling Margin",
                    "fieldtype": "Percent",
                    "insert_after": "last_scanned_warehouse",
                    "allow_on_submit": 1,
                },
            ],
            "Quotation Item": [
                {
                    "fieldname": "supplier_quote_price",
                    "label": "Supplier Quote Price",
                    "fieldtype": "Currency",
                    "options": "currency",
                    "insert_after": "base_price_list_rate",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "selling_margin",
                    "label": "Selling Margin",
                    "fieldtype": "Percent",
                    "insert_after": "supplier_quote_price",
                    "allow_on_submit": 1,
                },
            ],
            "Delivery Note": [
                {
                    "fieldname": "customer_rfq",
                    "label": "Customer RFQ",
                    "fieldtype": "Data",
                    "insert_after": "hs_code",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "total_volume",
                    "label": "Total Volume",
                    "fieldtype": "Data",
                    "insert_after": "total_qty",
                    "allow_on_submit": 1,
                }
            ],
            "Delivery Note Item": [
                {
                    "fieldname": "hs_code",
                    "label": "HS Code",
                    "fieldtype": "Data",
                    "insert_after": "package_size",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "country_of_origin",
                    "label": "Country Of Origin",
                    "fieldtype": "Link",
                    "options": "Country",
                    "insert_after": "hs_code",
                    "allow_on_submit": 1,
                },
            ],
            "Sales Order": [
                {
                    "fieldname": "customer_rfq",
                    "label": "Customer RFQ",
                    "fieldtype": "Data",
                    "insert_after": "transaction_date",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "bank_account",
                    "label": "Bank",
                    "fieldtype": "Link",
                    "options": "Bank Account",
                    "insert_after": "delivery_date",
                    "allow_on_submit": 1,
                },
            ],
            "Sales Invoice": [
                {
                    "fieldname": "customer_rfq",
                    "label": "Customer RFQ",
                    "fieldtype": "Data",
                    "insert_after": "hs_code",
                    "allow_on_submit": 1,
                }
            ],
        }
    )
