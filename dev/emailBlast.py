from datetime import datetime
import os
import glob
import smtplib
import subprocess
import optparse
import re

    
def sendemail(bcc_addr_list,mailmessage):
    from_addr    = 'dkennedy@thanxmedia.com'
    to_addr_list = ['dkennedy@thanxmedia.com']
    cc_addr_list = ['']
    bcc_addr_list = bcc_addr_list
    reply_to_addr =''
    login        = 'dkennedy@thanxmedia.com'
    password     = 'DKThanx**'
    header  = 'From: %s\n' % from_addr
    header += 'reply-to: %s\n' % reply_to_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Bcc: %s\n' % ','.join(bcc_addr_list)
    subject = 'Scheduled Maintence March 15, 2015'
    header += 'Subject: %s\n\n' % subject
    message = header + mailmessage
    email_addr = to_addr_list + cc_addr_list + bcc_addr_list
    smtpserver='secure.emailsrvr.com:587'    
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    server.sendmail(from_addr, email_addr, message)
    server.quit()

file_email_addr = raw_input('Email Address File Location: ')
file_email_message = raw_input('Email Message File Location: ')
	
addresses = open(file_email_addr,'r')
bcc = []
for i in addresses:
    bcc.append(i.rstrip())
with open(file_email_message, 'r') as email:
    mailmessage = email.read()
	
sendemail(bcc,mailmessage)


    
    
