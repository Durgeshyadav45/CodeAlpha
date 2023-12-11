import os
from email.message import EmailMessage
import ssl    #security layer
import smtplib

email_sender="senderm313@gmail.com"
email_password="majz ldbj huuu wpqr"
email_reciever="durgeshkyadav04@gmail.com"

subject="this is automated email sender"

body="""
hey!!! I have created a automated email sender.
and it is working very efficiently.....
and this is my mail

"""
em=EmailMessage()

em['from'] = email_sender
em['to'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465 ,context=context) as smtp: # this is a server
       smtp.login(email_sender,email_password)
       smtp.sendmail(email_sender,email_reciever,em.as_string())