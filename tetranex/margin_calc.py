import frappe
from frappe import _
from frappe.utils import flt


@frappe.whitelist()
def get_rate(supplier_quote_price=0, selling_margin=0, price_list_rate=0):
    """Rate = Supplier Quote Price / (1 - Selling Margin %). No quote price: price list rate.

    e.g. 100 at 20% margin: 100 / (1 - 0.20) = 125
    """
    if not flt(supplier_quote_price):
        return flt(price_list_rate)

    if flt(selling_margin) >= 100:
        frappe.throw(_("Selling Margin must be less than 100%"))

    rate = flt(supplier_quote_price) / (1 - flt(selling_margin) / 100)
    return flt(rate, frappe.get_precision("Quotation Item", "rate"))
