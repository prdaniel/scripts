from datetime import datetime
import os
import glob
import zipfile
import smtplib
import subprocess
import urllib2
import socket
import shutil



site = 'http://localhost:8006/gamestop-service-authoring/json/pages/browse'
status = open("status.txt", 'w')
try:
    status.write(urllib2.urlopen(site).read())
except Exception:
    pass
status.close()
if 'RedirectAwareContentInclude' in open('status.txt').read() and '@error' not in open('status.txt').read():
    print "Pass"
	#subprocess.Popen(self.directory + 'control/promote_content'+self.postfix + ' > ' + self.directory + 'logs/promote_content.out').wait()
    #return True
else:
    print "Fail"
    #with open(self.directory+'logs/promote_content.out', 'a') as f:
        #f.write('SEVERE Authoring Assembler is invalid. Experience Manager changes were not pushed to the Live Assembler apps.\nCheck the Authoring response at http://localhost:8006/gamestop-service-authoring/json/pages/browse\n')
        #return False
	
