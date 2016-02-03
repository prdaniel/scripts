from datetime import datetime
import os
import glob
import zipfile
import smtplib
import subprocess
import urllib2
import socket
import shutil
import smtplib,email,email.encoders,email.mime.text,email.mime.base

class EodTools:

    def __init__(self, app_id, app_name, directory):
        self.app_id = app_id
        self.app_name = app_name
        self.directory = directory
        self.postfix = '.sh'
        if os.name == 'nt': self.postfix = '.bat'

    def archive_baseline(self, delete=False):     
        backup_date = datetime.today()  
        zip = zipfile.ZipFile(self.directory+'archive/baseline-'+backup_date.strftime("%Y%m%dT%H%M%S")+'.zip', 'w')
        for name in glob.glob(self.directory+'test_data/baseline/*'):
            zip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
            if delete:
                os.remove(name)

    def file_validation(self,nlines, datafile):
        if os.path.exists(self.directory+'test_data/baseline/'+datafile):
	        with open(self.directory+'logs/baseline_update.out','a') as f:
	            count = 0
	            for line in open(self.directory+'test_data/baseline/'+datafile).xreadlines(  ): count += 1
	            if (count-1) < nlines:
			    f.write('SEVERE Baseline did not run '+datafile+' does not exist.\n')
		            return False
	            else:
		            f.write(datafile+' '+str(nlines)+' lines PASSED\n')
		            return True
        else:
            with open(self.directory+'logs/baseline_update.out','a') as f:
                f.write('SEVERE Baseline did not run '+datafile+' does not exist.\n')
                return False
    		
    def check_erros(self):
        log_output = open(self.directory+'logs/baseline_update.out', 'r')
        for line in log_output.readlines():
            if 'SEVERE' in line or 'WARNING: Failed to obtain lock.' in line:
                print 'Baseline Failure: Refer to the baseline_update.out log for additional information'
                return True
				
    def dimension_creation(self):
        try:
	    subprocess.Popen('/usr/local/endeca/apps/tmi20150305/test_data/dimensions_creation.sh').wait()
	    subprocess.Popen('/usr/local/endeca/apps/tmi20150305/test_data/dimensions_creation_content.sh').wait()
	    return True
        except Exception:
            print 'error running dimension creation'+self.postfix
            return False
	
    def load_baseline(self):
        try:
	    subprocess.Popen('/usr/local/endeca/apps/tmi20150305/control/load_baseline_test_data.sh').wait()
	    return True
        except Exception:
	    print Exception
            print 'error running load_baseline_test_data'+self.postfix
            return False

    def run_complete_refresh(self):
        try:
	    with open("/usr/local/endeca/apps/tmi20150305/logs/baseline_update.out","wb") as out:
		subprocess.Popen('/usr/local/endeca/apps/tmi20150305/control/run_complete_refresh.sh', stdout=out).wait()
		return True
        except Exception:
            print 'error running baseline_update'+self.postfix
            return False
	
    def promote_content(self):
        site = 'http://thunderball-indexer.endecaondemand.net:8006/coleparmer-service-authoring/json/pages/us/browse'
        status = open(self.directory + 'logs/status.txt', 'w')
        try:
            status.write(urllib2.urlopen(site).read())
        except Exception:
            pass
        status.close()
        if 'refinementCrumbs' in open(self.directory + 'logs/status.txt').read():
	    with open("/usr/local/endeca/apps/tmi20150305/logs/baseline_update.out","a") as out:
		subprocess.Popen('/usr/local/endeca/apps/tmi20150305/control/promote_content.sh', stdout=out).wait()
		return True
        else:
            with open(self.directory+'logs/baseline_update.out', 'a') as f:
                f.write('SEVERE Authoring Assembler is invalid. Experience Manager changes were not pushed to the Live Assembler apps.\nCheck the Authoring response at http://thunderball-indexer.endecaondemand.net:8006/coleparmer-service-authoring/json/pages/us/browse\n')
                return False

    def sendemail(self, from_addr, to_addr_list, cc_addr_list,reply_to_addr, login, password, failure, smtpserver='smtp.sendgrid.net:25'):
	header = email.MIMEMultipart.MIMEMultipart('alternative')
        header['From']  = from_addr
        header['Reply'] = reply_to_addr
        header['To'] = ',  '.join(to_addr_list)
        header['Cc'] = ',  '.join(cc_addr_list)
        baseline_date = datetime.today() 
        update_status = 'SUCCESS'
        if failure:
            update_status = 'FAILURE'
        subject = '%s [%s] Endeca Production Baseline Update Notification' % (update_status, self.app_name)
        header['Subject']= subject
        message = """Dear %s,
 
This is a notification that an Endeca event has occurred. 
 
Date:          %s
Status:        Baseline update %s
Account #:     %s
 
Please review the attached baseline_update.out log to determine where the error has occurred.
""" % (self.app_name, baseline_date.strftime("%Y/%m/%d %I:%M:%S %p CDT"), update_status.lower(), self.app_id)
	header.attach(email.mime.text.MIMEText(message,'message'))
	fileMsg = email.mime.base.MIMEBase('application','baseline_update.out')
	fileMsg.set_payload(file(self.directory+'logs/baseline_update.out').read())
	email.encoders.encode_base64(fileMsg)
	fileMsg.add_header('Content-Disposition','attachment;filename=baseline_update.out')
	header.attach(fileMsg)

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login,password)
        problems = server.sendmail(from_addr, to_addr_list, header.as_string())
        server.quit()
        return problems
  
