// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.ui.form.on("Loan Application", {
    onload: function(frm) {
         if (frm.is_new()){
            if (frm.doc.application_date) {
                set_month_quarter_year(frm);
            }
         }
    },
	refresh(frm) {
        frm.add_custom_button(__('Back'), function () {
            frappe.set_route('List', 'Loan Application', 'List')
        })
        frm.add_custom_button(__('Home'), function () {
            frappe.set_route('loan-applications')
        })

        if (frm.is_new()){
            frappe.db.get_doc('Loan Settings', null).then(settings => {
                frm.set_value('interest_rate', settings.default_interest_rate);
                    refresh_field('interest_rate');

                frm.set_value('service_fee_rate', settings.service_fee);
                refresh_field('service_fee_rate');
            });
        }
	},
    loan_type (frm) {
        if (frm.doc.loan_type !== "Collateral Based") {
            frm.clear_table("collateral_items");
            frm.refresh_field("collateral_items");
            frm.set_value("value_of_items", 0);
            frm.set_value("number_of_items", 0);
        }
    },
    amount_owed: function(frm) {
        prepare_repayment_schedule(frm);
    },
    loan_tenure: function(frm) {
        prepare_repayment_schedule(frm);
    },
    start_date: function(frm) {
        prepare_repayment_schedule(frm);
    }
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

function set_month_quarter_year(frm) {
    // Get the Date of Joining value
    var application_date = frm.doc.application_date;
    
    // Convert the date string into a Date object
    var date = new Date(application_date);
    
    // Extract the year and month
    var year = date.getFullYear();
    var month = date.getMonth(); // Month is 0-based (0 = January, 1 = February, ...)
    var quarter = get_quarter(month);

    // Set the values in the respective fields
    frm.set_value('year', year);
    frm.set_value('month', get_month_name(month));
    frm.set_value('quarter', quarter);
}

// Helper function to get the quarter based on the month
function get_quarter(month) {
    if (month < 3) {
        return 'Q1';
    } else if (month < 6) {
        return 'Q2';
    } else if (month < 9) {
        return 'Q3';
    } else {
        return 'Q4';
    }
}

// Helper function to get the month name
function get_month_name(month) {
    var months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
    return months[month];
}

frappe.ui.form.on("Collateral Items", {
    collateral_items_add: function(frm, cdt, cdn) {
        update_collateral_totals(frm);
    },
    collateral_items_remove: function(frm, cdt, cdn) {
        update_collateral_totals(frm);
    },
    value: function(frm, cdt, cdn) {
        update_collateral_totals(frm);
    }
});

function update_collateral_totals(frm) {
    let total_value = 0;

    if (frm.doc.collateral_items && frm.doc.collateral_items.length > 0) {
        frm.doc.collateral_items.forEach(item => {
            total_value += flt(item.value);
        });
    }
    frm.set_value("value_of_items", total_value);
    frm.set_value("number_of_items", frm.doc.collateral_items.length || 0);
}

function prepare_repayment_schedule(frm) {
    frm.clear_table('repayment_schedule');

    if (!frm.doc.amount_owed || !frm.doc.loan_tenure || !frm.doc.application_date) {
        frm.refresh_field('repayment_schedule');
        return;
    }

    let total_amount = flt(frm.doc.amount_owed, 2);
    let tenure = frm.doc.loan_tenure;
    let application_date = frappe.datetime.str_to_obj(frm.doc.application_date);
    let installment_amount = flt(total_amount / tenure, 2);
    let remaining_balance = total_amount;

    for (let i = 0; i < tenure; i++) {
        let row = frm.add_child('repayment_schedule');

        row.payment_due_date = frappe.datetime.add_months(application_date, i + 1);
        row.payment_amount = installment_amount;
        row.principal_amount = installment_amount;
        row.principal_amount = total_amount
        row.remaining_balance = flt(remaining_balance, 2);

        remaining_balance = flt(remaining_balance - installment_amount, 2);

        row.status = "Pending";
    }

    frm.refresh_field('repayment_schedule');
}

/*
function prepare_repayment_schedule(frm) {
    frm.clear_table('repayment_schedule');

    if (!frm.doc.amount_owed || !frm.doc.loan_tenure || !frm.doc.application_date) {
        frm.refresh_field('repayment_schedule');
        return;
    }

    let total_amount = frm.doc.amount_owed;
    let tenure = frm.doc.loan_tenure;
    let application_date = frappe.datetime.str_to_obj(frm.doc.application_date);

    let installment_amount = flt(total_amount / tenure, 2);
    let remaining_balance = total_amount;

    for (let i = 0; i < tenure; i++) {
        let row = frm.add_child('repayment_schedule');
        remaining_balance = flt(remaining_balance - installment_amount, 2);

        row.payment_due_date = frappe.datetime.add_months(application_date, i + 1);
        row.payment_amount = installment_amount;
        row.principal_amount = installment_amount;
        row.remaining_balance = remaining_balance >= 0 ? remaining_balance : 0;
        row.status = "Pending";
    }
    frm.refresh_field('repayment_schedule');
}
*/