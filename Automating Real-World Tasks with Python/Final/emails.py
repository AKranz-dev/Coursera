#!/usr/bin/env python3
from email.message import EmailMessage
import smtplib
import os.path
import mimetypes

def generate_email(attatchment):
    message = EmailMessage()

    
    sender = "automation@example.com"
    recipient = "student-01-6bb66a8e7d9c@example.com"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = attatchment
    attachment_filename = os.path.basename(attachment_path)

    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = "Upload Completed - Online Fruit Store"
    message.set_content(body)
    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),maintype='application',subtype='pdf',filename=attachment_filename)
    return message




def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()




