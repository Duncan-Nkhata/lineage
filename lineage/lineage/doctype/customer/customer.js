// Copyright (c) 2025, Vortex Technology and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customer", {
    onload: function(frm) {
         if (frm.is_new()){
            if (frm.doc.date_of_joining) {
                set_month_quarter_year(frm);
            }
    }
    },
 	refresh(frm) {
        frm.add_custom_button(__('Back'), function () {
            frappe.set_route('List', 'Customer', 'List')
        })
        frm.add_custom_button(__('Home'), function () {
            frappe.set_route('customers')
        })
        if (!frm.is_new()){
            if (frm.doc.status !== 'Suspended' && frm.doc.status !== 'Closed' && frm.doc.status !== 'Blacklisted') {
                frm.add_custom_button(__('New Loan'), function () {
                    frappe.new_doc('Loan Application', {
                        customer_id: frm.doc.name
                    });
                });
            }
            if (frm.doc.status !== 'Suspended' && frm.doc.status !== 'Closed' && frm.doc.status !== 'Inactive' && frm.doc.status !== 'Blacklisted') {
                frm.add_custom_button(__('Blacklist'), function () {
                    frappe.confirm(__('Are you sure you want to blacklist this customer?'),
                    function () {
                        frappe.call({
                            method: "lineage.tasks.blacklist",
                            args: {
                                self: frm.doc.name
                            },
                            callback: function (r) {
                                if (!r.exc) {
                                    frm.reload_doc();
                                }
                            }
                        });
                    },
                    function () {
                        frappe.msgprint(__('Blacklisting cancelled.'));
                    }
                );
                })
            }
            if (frm.doc.status !== 'Suspended' && frm.doc.status !== 'Closed' && frm.doc.status !== 'Inactive' && frm.doc.status !== 'Blacklisted') {
                frm.add_custom_button(__('Suspend'), function () {
                    frappe.confirm(__('Are you sure you want to suspend this customer?'),
                    function () {
                        frappe.call({
                            method: "lineage.tasks.suspend",
                            args: {
                                self: frm.doc.name
                            },
                            callback: function (r) {
                                if (!r.exc) {
                                    frm.reload_doc();
                                }
                            }
                        });
                    },
                    function () {
                        frappe.msgprint(__('Suspension cancelled.'));
                    }
                );
                })
            }
            if (frm.doc.status === 'Suspended' || frm.doc.status === 'Blacklisted') {
                frm.add_custom_button(__('Reactivate'), function () {
                    frappe.confirm(__('Are you sure you want to reactivate this customer?'),
                    function () {
                        frappe.call({
                            method: "lineage.tasks.reactivate",
                            args: {
                                self: frm.doc.name
                            },
                            callback: function (r) {
                                if (!r.exc) {
                                    frm.reload_doc();
                                }
                            }
                        });
                    },
                    function () {
                        frappe.msgprint(__('Reactivation cancelled.'));
                    }
                );
                });
            }
        }
    },
    salutation(frm) {
        update_full_name(frm);
    },
    first_name(frm) {
        update_full_name(frm);
    },
    last_name(frm) {
        update_full_name(frm);
    },
    date_of_birth: function(frm) {
        if (frm.doc.date_of_birth) {
            const dob = frappe.datetime.str_to_obj(frm.doc.date_of_birth);
            const today = frappe.datetime.str_to_obj(frappe.datetime.get_today());

            let age = today.getFullYear() - dob.getFullYear();
            const m = today.getMonth() - dob.getMonth();
            if (m < 0 || (m === 0 && today.getDate() < dob.getDate())) {
                age--;
            }

            frm.set_value('age', age);
        } else {
            frm.set_value('age', null);
        }
    },
    employment_status(frm) {
        if (frm.doc.employment_status === 'Employed') {
           frm.set_value('employer_name', '');
           frappe.refresh_field('employer_name');
            }
        }
    });

function update_full_name(frm) {
    let first_name = frm.doc.first_name || '';
    let last_name = frm.doc.last_name || '';
    let salutation = frm.doc.salutation || '';
    
    let full_name = `${salutation} ${first_name} ${last_name}`.trim();
    frm.set_value('full_name', full_name);
}

function set_month_quarter_year(frm) {
    // Get the Date of Joining value
    var date_of_joining = frm.doc.date_of_joining;
    
    // Convert the date string into a Date object
    var date = new Date(date_of_joining);
    
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