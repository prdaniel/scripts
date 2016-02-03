from datetime import datetime
import os
import glob
import subprocess
import optparse
import re
from Tkinter import *
    
def sendemail(bcc_addr_list,message,login,password):
    import smtplib,email,email.encoders,email.mime.text,email.mime.base
    header = email.MIMEMultipart.MIMEMultipart('alternative')
    header['From']  = from_addr
    header['Reply'] = reply_to_addr
    header['To'] = ',  '.join(to_addr_list)
    header['Cc'] = ',  '.join(cc_addr_list)
    baseline_date = datetime.today() 
    subject = 'Scheduled Maintence March 15, 2015'
    header['Subject']= subject
    header.attach(email.mime.text.MIMEText(message,'message'))
    fileMsg = email.mime.base.MIMEBase('application','attachment.txt')
    fileMsg.set_payload(file('C:/Daniel/dev/email/attachment.txt').read())
    email.encoders.encode_base64(fileMsg)
    fileMsg.add_header('Content-Disposition','attachment;filename=attachment.txt')
    header.attach(fileMsg)
    email_addr = to_addr_list + cc_addr_list + bcc_addr_list
    smtpserver='secure.emailsrvr.com:587'    
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    server.sendmail(from_addr, email_addr, header.as_string())
    server.quit()

login = raw_input('Email Address: ')
password = raw_input('Password: ')
file_email_addr = raw_input('Email Address File Location: ')
file_email_message = raw_input('Email Message File Location: ')
	
addresses = open(file_email_addr,'r')
bcc = []
for i in addresses:
    bcc.append(i.rstrip())
with open(file_email_message, 'r') as email:
    mailmessage = email.read()

from_addr    = 'dkennedy@thanxmedia.com'
to_addr_list = ['dkennedy@thanxmedia.com']
cc_addr_list = ['']
bcc_addr_list = bcc
reply_to_addr =''
    
sendemail(bcc,mailmessage,login,password)
	
'''
def show_entry_fields():
   sendemail(bcc,mailmessage,login,password)

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

login = Entry(master)
password = Entry(master)

login = login.grid(row=0, column=1)
password = password.grid(row=1, column=1)

Button(master, text='Login', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
'''    
    
