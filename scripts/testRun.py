from testMod import EodTools
import optparse
import re
import os

parser = optparse.OptionParser()
parser.add_option('-i', '--app_id', dest='app_id', help='Application ID')
parser.add_option('-n', '--client_name', dest='client_name', help='Client\'s name ')
parser.add_option('-d', '--app_directory', dest='app_directory', help='Application\' base directory')
(options, args) = parser.parse_args()

options.app_id = 'discoverAuthoring'
options.client_name = 'discoverAuthoring'
options.app_directory = 'C:/Endeca/Apps/discoverAuthoring'

  
app_id = options.app_id
client_name = options.client_name
app_directory = options.app_directory

app = EodTools(app_id, client_name, app_directory)
valid = app.file_validation(100000,'items_salesmetrics.txt')
valid2 = app.file_validation(10,'items.txt')

if valid and valid2:
    app.run_complete_refresh()
else:
    os.remove('C:/Endeca/Apps/discoverAuthoring/logs/baseline_update.out')
    with open('C:/Endeca/Apps/discoverAuthoring/logs/baseline_update.out', 'a') as f:
        f.write('SEVERE Data File was too small. Baseline did not run.')
		
baseline_status = app.check_erros()

if baseline_status:
    app.sendemail(from_addr    = 'dkennedy@thanxmedia.com', 
                to_addr_list = ['dkennedy@thanxmedia.com'],
                cc_addr_list = [''],
                reply_to_addr ='', 
                failure      = baseline_status)


