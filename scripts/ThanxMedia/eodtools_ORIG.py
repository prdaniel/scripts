from datetime import datetime
import os
import glob
import zipfile
import smtplib
import subprocess

class EodTools:


    def __init__(self, app_id, app_name, directory):
        self.app_id = app_id
        self.app_name = app_name
        self.directory = directory
        self.postfix = '.sh'
        if os.name == 'nt': self.postfix = '.bat'
        
    def archive_baseline(self, delete=False):     
        backup_date = datetime.today()  
        zip = zipfile.ZipFile(self.directory+'//archive/baseline-'+backup_date.strftime("%Y%m%dT%H%M%S")+'.zip', 'w')
        for name in glob.glob(self.directory+'//test_data//baseline//*'):
            zip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
            if delete:
                os.remove(name)
    
    
    def sendemail(self, from_addr, to_addr_list, cc_addr_list,reply_to_addr,
                  login, password, failure,
                  smtpserver='secure.emailsrvr.com:587'):
        header  = 'From: %s\n' % from_addr
        header += 'reply-to: %s\n' % reply_to_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        baseline_date = datetime.today() 
        update_status = 'SUCCESS'
        if failure:
            update_status = 'FAILURE'
        subject = '%s [%s] EOD Baseline Update Notification' % (update_status, self.app_name)
        header += 'Subject: %s\n\n' % subject
        message = """Dear %s,
 
This is a notification that an Endeca On Demand event has occurred. 
 
Date:          %s
Process Name:  Baseline update
Status:        Baseline update %s
Account #:     %s
 
If there has been a failure status, the Thanx Media support team has already been notified.
 
If you have any further questions or concerns, please do not hesitate to contact us via phone at the number listed below or reply to this email.
 
Thank you,
 
Thanx Media Help Desk
helpdesk@thanxmedia.com
785.292.9290
""" % (self.app_name, baseline_date.strftime("%Y/%m/%d %I:%M:%S %p CDT"), update_status.lower(), self.app_id)
        message = header + message
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login,password)
        problems = server.sendmail(from_addr, to_addr_list, message)
        server.quit()
        return problems
    
    
    def weekly_clean_up(self):
        print 'delete homie'
       
        
    def check_erros(self):
        log_output = open(self.directory+'//logs/baseline_update.out', 'r')
        for line in log_output.readlines():
            if 'SEVERE' in line:
                return True
    
    def file_validation(self, nlines, fsize=False):
        if fsize:
            statinfo = os.stat(self.directory+'//test_data/baseline/items.txt')
            if nline < statinfo.st_size:
                print 'do not run', statinfo.st_size
                return False
        else:
            count = 0
            for line in open(self.directory+'//test_data/baseline/items.txt').xreadlines(  ): count += 1
            if nlines < (count-1):
                print 'do not run'
                return False
        return True
    
    
    def load_baseline_data(self):
        try:
            subprocess.Popen(self.directory+'//control/load_baseline_test_data'+self.postfix).wait()
            return True
        except Exception:
            print 'error running load_baseline_test_data'+self.postfix
            pass
            
            
    def baseline_update(self):
        try:
            print self.directory+'//control/baseline_update'+self.postfix
            subprocess.Popen(self.directory + '//control/baseline_update'+self.postfix + ' > ' + self.directory + '//logs/baseline_update.out').wait()
            return True
        except Exception:
            print 'error running baseline_update'+self.postfix
            pass
