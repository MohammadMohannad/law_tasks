# Copyright (c) 2023, Mohammad Muhannad and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Tasks(Document):
    pass

# @frappe.whitelist()
# def get_events(start, end, filters=None):
#     if not filters:
#         filters = {}

#     events = frappe.get_all(
#         "Tasks",
#         filters={
#             "assignment_date": [">=", start],
#             "completion_date": ["<", end],
#             **filters,
#         },
#         fields=["task_name", "assignment_date", "completion_date"],
#     )

#     return events
