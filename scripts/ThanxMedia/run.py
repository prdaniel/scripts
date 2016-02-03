from eodtools import EodTools
import optparse
import re
import os

parser = optparse.OptionParser()
parser.add_option('-i', '--app_id', dest='app_id', help='Application ID')
parser.add_option('-n', '--client_name', dest='client_name', help='Client\'s name ')
parser.add_option('-d', '--app_directory', dest='app_directory', help='Application\' base directory')
(options, args) = parser.parse_args()

if options.app_id is None:
    options.app_id = raw_input('Enter a name for your application (tmi20130621):\r\n')

while not re.match("^[A-Za-z0-9_-]*$", options.app_id):
    print 'Invalid Name, does not conform [A-Za-z0-9_-]'
    options.app_id = raw_input('Enter a name for your application (tmi20130621):\r\n')
        
if options.client_name is None:
    options.client_name = raw_input('Client Name:\r\n')

while not re.match("^[A-Za-z0-9_-]*$", options.client_name):
    print 'Invalid Name, does not conform [A-Za-z0-9_-]'
    options.client_name = raw_input('Application Name:\r\n')
        
if options.app_directory is None:
    options.app_directory = raw_input('Deployment directory:\r\n')

while not os.path.exists(options.app_directory):
    print 'Directory does not exist'
    options.app_directory = raw_input('Deployment directory:\r\n')
  
app_id = options.app_id
client_name = options.client_name
app_directory = options.app_directory

app = EodTools(app_id, client_name, app_directory)
#if you want to delete the files from the baseline directory once they are archived, pass the "delete=True" argument
valid_file = app.file_validation(36519)
valid_file_MA = app.file_validation_MA(132548)
valid_file_MH = app.file_validation_MH(472)
valid_file_PA = app.file_validation_MB(300)
if valid_file and valid_file_MA and valid_file_MH and valid_file_MB:
    app.run_complete_refresh()
else:
    os.remove('C:/Endeca/apps/Discover/logs/baseline_update.out')
    with open('C:/Endeca/apps/Discover/logs/baseline_update.out', 'a') as f:
        f.write('SEVERE Data File was too small. Baseline did not run.')

app.archive_baseline(delete=False)
baseline_status = app.check_erros()

app.sendemail(from_addr    = 'dkenned23@gmail.com', 
            to_addr_list = ['dkenned23@gmail.com', 'msias@thanxmedia.com'],
            cc_addr_list = [''],
            reply_to_addr ='dkenned23@gmail.com', 
            login        = 'dkenned23@gmail.com',
            password     = 'DK3nn3dy23!',
            failure      = baseline_status)


