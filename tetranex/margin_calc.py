import frappe
from frappe.utils import flt


@frappe.whitelist()
def get_rate(supplier_quote_price=0, selling_margin=0, price_list_rate=0):
    """Rate = Supplier Quote Price + Selling Margin %. No quote price: price list rate."""
    if not flt(supplier_quote_price):
        return flt(price_list_rate)

    rate = flt(supplier_quote_price) * (1 + flt(selling_margin) / 100)
    return flt(rate, frappe.get_precision("Quotation Item", "rate"))
