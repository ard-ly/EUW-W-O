# -*- coding:utf-8 -*-
# encoding: utf-8

# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import frappe, os
from frappe.model.document import Document
from frappe.utils import get_site_base_path
from frappe.utils.data import flt, nowdate, getdate, cint
from frappe.utils import cint, cstr, flt, nowdate, comma_and, date_diff, getdate



# def add_test_journal_entry():    
#     doc = frappe.new_doc("Journal Entry")
#     doc.voucher_type = 'Opening Entry'
#     doc.posting_date = getdate()

#     for i in range(2000):
#         doc.append('accounts', {
#             "account": 'Bank Account - EWL',
#             "debit": '1000',
#             "debit_in_account_currency": '1000'
#         })

#     doc.append('accounts', {
#         "account": '3300 - Opening Balance Equity - EWL',
#         "credit_in_account_currency": '2000000',
#         "credit": '2000000'
#     })

#     # doc.flags.ignore_permissions=True
#     # doc.flags.ignore_validate = True
#     # doc.flags.ignore_mandatory = True
#     doc.insert(ignore_permissions=True)

#     print('************************')
#     print("* Done *")
#     print('************************')



