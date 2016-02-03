import urllib2

#Writes the the json source to a text file
site = 'http://moonraker-webserver-a.endecaondemand.net/Andys-Auto-Sport-service/json/pages/browse'
status = open("status.txt", 'w')
status.write(urllib2.urlopen(site).read())
status.close()
#Checks if refinementCrumbs' is present in the status.txt file
if 'refinementCrumbs' in open('status.txt').read():
    app.promote_content()
else:
    checkR = False
    with open('C:/Endeca/apps/GameStopUS/logs/baseline_update.out', 'a') as f:
        f.write('Authoring Assembler Service Invalid. EM configurations were not promoted to Live\n')
