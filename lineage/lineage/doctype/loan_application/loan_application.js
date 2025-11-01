// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.ui.form.on("Loan Application", {
	refresh(frm) {
        frm.add_custom_button(__('Back'), function () {
            frappe.set_route('List', 'Loan Application', 'List')
        })
        frm.add_custom_button(__('Home'), function () {
            frappe.set_route('loan_applications')
        })

        frappe.db.get_doc('Loan Settings', null).then(settings => {
            frm.set_value('interest_rate', settings.default_interest_rate);
                refresh_field('interest_rate');

            frm.set_value('service_fee_rate', settings.service_fee);
            refresh_field('service_fee_rate');
        });
	},
});

frappe.ui.form.on('Loan Application', {
    loan_amount: refresh_calculations,
    interest_rate: refresh_calculations,
    service_fee_rate: refresh_calculations,
    loan_tenure: refresh_calculations
});

function refresh_calculations(frm) {
    let loan_amount = frm.doc.loan_amount || 0;
    let interest_rate = frm.doc.interest_rate || 0;
    let service_fee_rate = frm.doc.service_fee_rate || 0;
    let loan_tenure = frm.doc.loan_tenure || 0;

    // Calculate interest (simple interest)
    let interest = (loan_amount * interest_rate * loan_tenure) / 100;

    // Service fee
    let service_fee = (loan_amount * service_fee_rate) / 100;

    // Total owed
    let amount_owed = loan_amount + interest;

    // Disbursement
    let disbursement_amount = loan_amount - service_fee;

    frm.set_value('interest', interest);
    frm.set_value('service_fee', service_fee);
    frm.set_value('amount_owed', amount_owed);
    frm.set_value('disbursement_amount', disbursement_amount);
}
