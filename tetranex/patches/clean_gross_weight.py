import frappe


def execute():
    if not frappe.db.has_column("Delivery Note Item", "gross_weight"):
        return

    # remove commas and extra spaces
    frappe.db.sql("""
        UPDATE `tabDelivery Note Item`
        SET gross_weight = TRIM(REPLACE(gross_weight, ',', ''))
        WHERE gross_weight IS NOT NULL
    """)

    # set blank, NULL, or non-numeric values to 0
    frappe.db.sql("""
        UPDATE `tabDelivery Note Item`
        SET gross_weight = '0'
        WHERE gross_weight IS NULL
           OR gross_weight = ''
           OR gross_weight NOT REGEXP '^-?[0-9]+([.][0-9]+)?$'
    """)