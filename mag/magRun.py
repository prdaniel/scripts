from GameStopMod import EodTools
from datetime import datetime
import optparse
import re
import os
import socket


parser = optparse.OptionParser()
parser.add_option('-i', '--app_id', dest='app_id', help='Application ID')
parser.add_option('-n', '--client_name', dest='client_name', help='Client\'s name ')
parser.add_option('-d', '--app_directory', dest='app_directory', help='Application\' base directory')
(options, args) = parser.parse_args()

options.app_id = 'PTS'
options.client_name = 'PTS'
options.app_directory = 'C:/Endeca/Apps/PTS/'

  
app_id = options.app_id
client_name = options.client_name
app_directory = options.app_directory


app = EodTools(app_id, client_name, app_directory)

with open(options.app_directory+'logs/baseline_update.out', 'w') as f:
    preprocess_date = datetime.today() 
    f.write(preprocess_date.strftime("%Y/%m/%d %I:%M:%S %p CDT")+'\nStarting Data Preprocessing\n')

valid = app.file_validation(1042,'pts.hierarchy.txt')
valid2 = app.file_validation(2587741,'pts.attributes.txt')
valid3 = app.file_validation(239,'morse.hierarchy.txt')
valid4 = app.file_validation(342841,'morse.attributes.txt')
valid5 = app.file_validation(468145,'items.txt')


if valid and valid2 and valid3 and valid4 and valid5:
    print 'Data checks PASSED\nRunning Baseline Update Process...'
    app.archive_baseline(delete=False)
    app.run_complete_refresh()
    #app.promote_content()
else:
    print 'Baseline Preprocessing Failed'
	
baseline_status = app.check_erros()

if baseline_status:
    app.sendemail(from_addr    = 'dkennedy@thanxmedia.com', 
                to_addr_list = ['dkennedy@thanxmedia.com'],
                cc_addr_list = [''],
                reply_to_addr ='',
                login        = 'dkennedy@thanxmedia.com',
                password     = 'DKThanx**',
                failure      = baseline_status)


