# Copyright (c) 2023, InshaSiS Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.core.doctype.communication.email import make

def after_insert(doc,method):
	""" Send email notifications when Issue is created """
	
	subject = f"""Ticket created for Issue {doc.name}"""
	customer_email= frappe.db.get_value("Customer", doc.customer, "email_id")
	client_body = f"""Dear Customer {doc.customer},
						Your appointment has been scheduled for failure product inspection on Date {doc.posting_date}.
						Thanks for using our services.
						Contact Services Center
						Phone :Xxxxxxxxxxxx
						Email: hisense@jkrinfra.com"""
	

	make(subject = subject,content=client_body,
		recipients=customer_email,
		send_email=True, sender="crm@inshasis.in")
	frappe.msgprint("Issue Ticket Creation Email Has Been Sent")

