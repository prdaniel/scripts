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
    
    def sendemail(self, from_addr, to_addr_list, cc_addr_list,reply_to_addr,failure,
                  smtpserver='smtp.emailsrvr.com:587'):
        header  = 'From: %s\n' % from_addr
        header += 'reply-to: %s\n' % reply_to_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        baseline_date = datetime.today() 
        update_status = 'SUCCESS'
        if failure:
            update_status = 'FAILURE'
        subject = '%s [%s] Endeca Production Baseline Update Notification' % (update_status, self.app_name)
        header += 'Subject: %s\n\n' % subject
        message = """Dear %s,
 
This is a notification that an Endeca event has occurred. 
 
Date:          %s
Status:        Baseline update %s
Account #:     %s
 
Please review the baseline_update.out log to determine where the error has occurred. This file can be found in the Endeca PTS folder (C:/Endeca/Apps/Pts/logs)
""" % (self.app_name, baseline_date.strftime("%Y/%m/%d %I:%M:%S %p CDT"), update_status.lower(), self.app_id)
        message = header + message
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login,password)
        problems = server.sendmail(from_addr, to_addr_list, message)
        server.quit()
        return problems
    		
    def check_erros(self):
        log_output = open(self.directory+'//logs/baseline_update.out', 'r')
        for line in log_output.readlines():
            if 'SEVERE' in line:
                print 'Baseline Failure: Refer to the baseline_update.out log for additional information'
                return True
	    
directory = 'C:/Daniel/apps/gamestop/dev/'
with open(directory+'log.out','w') as f:
    f.write('Data File Check:  \n')


    def file_validation(nlines, datafile):
	global filefailure
	with open(directory+'log.out','a') as f:
	    count = 0
	    for line in open(directory+datafile).xreadlines(  ): count += 1
	    if (count-1) < nlines:
		f.write ('do not run ' +datafile+'  too small\n')
		return False
	    else:
		f.write(datafile +' passed\n')
		return True

    def run_complete_refresh(self):
        try:
            print self.directory+'//control/run_complete_refresh'+self.postfix
            subprocess.Popen(self.directory + '//control/run_complete_refresh'+self.postfix + ' > ' + self.directory + '//logs/baseline_update.out').wait()
            return True
        except Exception:
            print 'error running baseline_update'+self.postfix
            pass
	
valid = file_validation(100000,'items_salesmetrics.txt')
valid2 = file_validation(10,'items.txt')

if valid and valid2:
    print 'Good'
else:
    print "bad" 

