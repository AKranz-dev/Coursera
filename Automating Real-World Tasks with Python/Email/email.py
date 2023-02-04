# #Usint the email.message.EmailMessage class to create an empty message
#  from email.message import EmailMessage
#  message = EmailMessage()
#  print(message)

# #Adding the To, From, Subject, and body
#  message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
#  print(message)
# From: me@example.com
# To: you@example.com
# Subject: Greetings from me@example.com to you@example.com!
#  body = """Hey there! I'm learning to send emails using Python!"""
#  message.set_content(body)


# #Printing a message object shows all of it's stuff! Note the Content-Type and Content-Transfer-Encoding are headers that get added when using the .set_content() method which is used when adding a body to the message.
#  print(message)
# From: me@example.com
# To: you@example.com
# Subject: Greetings from me@example.com to you@example.com!
# MIME-Version: 1.0
# Content-Type: text/plain; charset="utf-8"
# Content-Transfer-Encoding: 7bit

# Hey there!

# I'm learning to send email using Python!


# #Using the mimetype module to guess what MIME type and subtype to use for the attachment you want to send via email
#  import os.path
#  attachment_path = "/tmp/example.png"
#  attachment_filename = os.path.basename(attachment_path)
#  import mimetypes
#  mime_type, _ = mimetypes.guess_type(attachment_path)
#  print(mime_type)
# image/png #When you print the mime_type, it outputs the MIME type and the subtype seperated by a slash, respectively (MIME Type/Subtype)


# #Splitting the mime_type string into 2 seperate strings (to be used as the MIME Type and the Subtype)
#  mime_type, mime_subtype = mime_type.split('/', 1)
#  print(mime_type)
# image
#  print(mime_subtype)
# png




# #A full example - each part of the message has its own MIMEType/Subtype - e.g. the body is text/plain, the message as a whole is multipart/mixed, the attatchment is image/png
#  with open(attachment_path, 'rb') as ap:
#      message.add_attachment(ap.read(),
#                             maintype=mime_type,
#                             subtype=mime_subtype,
#                             filename=os.path.basename(attachment_path))
 
#  print(message)
# Content-Type: multipart/mixed; boundary="===============5350123048127315795=="

# --===============5350123048127315795==
# Content-Type: text/plain; charset="utf-8"
# Content-Transfer-Encoding: 7bit

# Hey there!

# I'm learning to send email using Python!

# --===============5350123048127315795==
# Content-Type: image/png
# Content-Transfer-Encoding: base64
# Content-Disposition: attachment; filename="example.png"
# MIME-Version: 1.0

# iVBORw0KGgoAAAANSUhEUgAAASIAAABSCAYAAADw69nDAAAACXBIWXMAAAsTAAALEwEAmpwYAAAg
# AElEQVR4nO2dd3wUZf7HP8/M9k2nKIJA4BCUNJKgNJWIBUUgEggCiSgeVhA8jzv05Gc5z4KHiqin
# eBZIIBDKIXggKIeCRCAhjQAqx4UiCARSt83uzDy/PzazTDZbwy4BnHde+9qZydNn97Pf5/uUIZRS
# (We deleted a bunch of lines here)
# wgAAAABJRU5ErkJggg==

# --===============5350123048127315795==--


# #importing smtplib to send email and setting localhost as our mail server
# import smtplib
# mail_server = smtplib.SMTP('localhost')

# #Using the getpass module to get a password.
# import getpass
# mail_pass = getpass.getpass('Password? ')

# #using the login method to login to our smtp server
# mail_server.login(sender, mail_pass)
# (235, b'2.7.0 Accepted')

# #Sending a message - returns a dictionary of any recipient that werent able to receive the message
# mail_server.send_message(message)

# #Close the connection to the mail server
# mail_server.quit()



