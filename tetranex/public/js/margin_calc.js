frappe.ui.form.on("Quotation", {
	// new quotation made from a Supplier Quotation: supplier quote price = supplier's rate
	onload(frm) {
		if (!frm.is_new() || !frm.doc.supplier_quotation) return;
		(frm.doc.items || []).forEach((row) => {
			if (!row.supplier_quote_price) row.supplier_quote_price = row.rate;
		});
		frm.refresh_field("items");
	},

	// margin above the table applies to every item
	selling_margin(frm) {
		(frm.doc.items || []).forEach((row) => {
			frappe.model.set_value(row.doctype, row.name, "selling_margin", frm.doc.selling_margin);
		});
	},
});

frappe.ui.form.on("Quotation Item", {
	items_add(frm, cdt, cdn) {
		if (frm.doc.selling_margin) {
			frappe.model.set_value(cdt, cdn, "selling_margin", frm.doc.selling_margin);
		}
	},

	supplier_quote_price(frm, cdt, cdn) {
		set_rate_from_margin(cdt, cdn);
	},

	selling_margin(frm, cdt, cdn) {
		// margin only matters when there is a quote price
		if (locals[cdt][cdn].supplier_quote_price) {
			set_rate_from_margin(cdt, cdn);
		}
	},
});

function set_rate_from_margin(cdt, cdn) {
	const row = locals[cdt][cdn];

	// calculation is done on the server
	frappe.call({
		method: "tetranex.margin_calc.get_rate",
		args: {
			supplier_quote_price: row.supplier_quote_price || 0,
			selling_margin: row.selling_margin || 0,
			price_list_rate: row.price_list_rate || 0,
		},
		callback(r) {
			if (locals[cdt] && locals[cdt][cdn]) {
				frappe.model.set_value(cdt, cdn, "rate", r.message);
			}
		},
	});
}
