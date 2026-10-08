import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    frappe.delete_doc_if_exists("Custom Field", "Request for Quotation-rfq_currency")

    create_custom_fields(
        {
            "Request for Quotation": [
                {
                    "fieldname": "customer",
                    "label": "Customer",
                    "fieldtype": "Link",
                    "options": "Customer",
                    "insert_after": "vendor",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "customer_rfq",
                    "label": "Customer RFQ",
                    "fieldtype": "Data",
                    "insert_after": "customer",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "project_name",
                    "label": "Project Name",
                    "fieldtype": "Data",
                    "insert_after": "customer_rfq",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "valid_till",
                    "label": "RFQ Closing Date",
                    "fieldtype": "Date",
                    "insert_after": "transaction_date",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "currency",
                    "label": "Currency",
                    "fieldtype": "Link",
                    "options": "Currency",
                    "insert_after": "valid_till",
                    "allow_on_submit": 1,
                },
                # ERPNext expects these on any doctype that has currency;
                # depends_on keeps them hidden when its form script toggles display
                {
                    "fieldname": "conversion_rate",
                    "label": "Exchange Rate",
                    "fieldtype": "Float",
                    "precision": "9",
                    "default": "1",
                    "hidden": 1,
                    "depends_on": "eval:false",
                    "insert_after": "currency",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "plc_conversion_rate",
                    "label": "Price List Exchange Rate",
                    "fieldtype": "Float",
                    "precision": "9",
                    "hidden": 1,
                    "depends_on": "eval:false",
                    "insert_after": "conversion_rate",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "price_list_currency",
                    "label": "Price List Currency",
                    "fieldtype": "Link",
                    "options": "Currency",
                    "hidden": 1,
                    "depends_on": "eval:false",
                    "insert_after": "plc_conversion_rate",
                    "allow_on_submit": 1,
                },
            ],
            "Supplier Quotation": [
                {
                    "fieldname": "customer",
                    "label": "Customer",
                    "fieldtype": "Link",
                    "options": "Customer",
                    "insert_after": "supplier_name",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "customer_rfq",
                    "label": "Customer RFQ",
                    "fieldtype": "Data",
                    "insert_after": "customer",
                    "allow_on_submit": 1,
                },
                {
                    "fieldname": "project_name",
                    "label": "Project Name",
                    "fieldtype": "Data",
                    "insert_after": "customer_rfq",
                    "allow_on_submit": 1,
                },
            ],
            "Quotation": [
                {
                    "fieldname": "project_name",
                    "label": "Project Name",
                    "fieldtype": "Data",
                    "insert_after": "customer_rfq",
                    "allow_on_submit": 1,
                },
            ],
        }
    )
