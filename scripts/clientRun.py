from coleparmerMod import EodTools
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

options.app_id = 'tmi20150305'
options.client_name = 'coleparmer'
options.app_directory = '/usr/local/endeca/apps/tmi20150305/'

  
app_id = options.app_id
client_name = options.client_name
app_directory = options.app_directory


app = EodTools(app_id, client_name, app_directory)

print 'Running load_baseline_test_data.sh'
app.load_baseline()

with open(options.app_directory+'logs/baseline_update.out', 'w') as f:
    preprocess_date = datetime.today() 
    f.write(preprocess_date.strftime("%Y/%m/%d %I:%M:%S %p CDT")+'\nStarting Data Preprocessing\n')

valid1 = app.file_validation(10233,'AttributePrecedence.txt')
valid2 = app.file_validation(800570,'attributes.txt')
valid3 = app.file_validation(2865,'autodim.txt')
valid4 = app.file_validation(300375,'brands.txt')
valid5 = app.file_validation(221013,'catalogmap.txt')
valid6 = app.file_validation(1044,'content.txt')
valid7 = app.file_validation(24079,'cppath_ca.txt')
valid8 = app.file_validation(23308,'cppath_cpuk.txt')
valid9 = app.file_validation(4741,'cppath_davis.txt')
valid10 = app.file_validation(23483,'cppath_in.txt')
valid11 = app.file_validation(428,'cppath_mf.txt')
valid12 = app.file_validation(32109,'cppath_us.txt')
valid13 = app.file_validation(9847,'hierarchy_ca.txt')
valid14 = app.file_validation(17067,'hierarchy_cp.txt')
valid15 = app.file_validation(9580,'hierarchy_cpuk.txt')
valid16 = app.file_validation(4608,'hierarchy_davis.txt')
valid17 = app.file_validation(9617,'hierarchy_in.txt')
valid18 = app.file_validation(377,'hierarchy_mflex.txt')
valid19 = app.file_validation(54013,'main.txt')
valid20 = app.file_validation(110781,'TechInfo.txt')
valid21 = app.file_validation(15327,'techinfoarticleAttr.txt')
valid22 = app.file_validation(667,'techinfoarticledata.txt')

print 'Checking Data Files'
if valid1 and valid2 and valid3 and valid4 and valid5 and valid6 and valid7 and valid8 and valid9 and valid10 and valid11 and valid12 and valid13 and valid14 and valid15 and valid16 and valid17 and valid18 and valid19 and valid20 and valid21 and valid21:
    print 'All Data Files Passed'
    print 'Archiving Data'
    app.archive_baseline(delete=False)
    print 'Running Dimension Creation Process' 
    app.dimension_creation()
    print 'Running Baseline Update' 
    app.run_complete_refresh()
    print 'Running Promote Content' 
    app.promote_content()
    # The CDN Purge occurs in the promote_content.sh script
else:
    print 'Baseline Preprocessing Failed'
	
baseline_status = app.check_erros()

if baseline_status:
    app.sendemail(from_addr    = 'notify@thanxmedia.com', 
                to_addr_list = ['notify@thanxmedia.com','slinne@coleparmer.com','usveh.ebusalerts@thermo.com','max.nadjari@coleparmer.com','binoy.edathiparambil@coleparmer.com','dkennedy@thanxmedia.com','domalley@thanxmedia.com'],
		cc_addr_list = [''],
                reply_to_addr ='',
                login        = 'tech@thanxmedia.com',
                password     = '222Thanx',
                failure      = baseline_status)


