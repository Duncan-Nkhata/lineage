// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.ui.form.on("Collateral", {
    refresh(frm) {
        frm.add_custom_button(__('Back'), function () {
            frappe.set_route('List', 'Collateral', 'List')
        })
        frm.add_custom_button(__('Home'), function () {
            frappe.set_route('collateral(s)')
        })
        if (frm.doc.loan_status === "Defaulted" && frm.doc.status !== "Liquidated") {    
            frm.add_custom_button(__('Liquidate'), function () {
                frm.set_value('status', 'Liquidated');
                frappe.refresh_field('status');
            })
        }

        if (frm.doc.loan_status === "Withdrawn" && frm.doc.status !== "Returned") {    
            frm.add_custom_button(__('Return'), function () {
                frm.set_value('status', 'Returned');
                frappe.refresh_field('status');
            })
        }
    }
});
