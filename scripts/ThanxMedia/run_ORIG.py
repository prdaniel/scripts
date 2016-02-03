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
valid_file = app.file_validation(200000)

if valid_file:
    app.load_baseline_data()
    app.baseline_update()

app.archive_baseline(delete=False)
baseline_status = app.check_erros()

app.sendemail(from_addr    = 'noreply@thanxmedia.com', 
                to_addr_list = ['cris.j.pina@gmail.com'],
                cc_addr_list = [''],
                reply_to_addr ='helpdesk@thanxmedia.com', 
                login        = 'noreply@thanxmedia.com',
                password     = 'n0!bl0sm',
                failure      = baseline_status)


