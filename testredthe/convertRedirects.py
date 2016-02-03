import os

#Converts the Workbench 2.1.2 redirects.xml file to Tools and Frameworks 11.1 json version.
           
import xml.etree.ElementTree as ET
kout = open("C:/Daniel/apps/ColeParmer/testredthe/_redirects.json","w")
tree = ET.parse("C:/Daniel/apps/ColeParmer/testredthe/tmi20110117.merch_rule_group_default_redirects.xml")
root = tree.getroot()
kout.write('{\n\t"redirects": [\n')
for merch_rules in root.findall('./MERCH_RULE'):
    url = merch_rules.find('./PROP/PVAL').text 
    for rule in merch_rules.findall('./MERCH_RULE_TRIGGER'):
        kout.write("\t\t{\n")
        kout.write('\t\t\t"searchTerms": ' + '"' + rule.find('KEYWORDS').text + '",\n')
        kout.write('\t\t\t"matchmode": ' + '"' +  rule.find('KEYWORDS').attrib["MODE"] + '",\n')
        kout.write('\t\t\t"url": ' + '"' + url + '"\n')
        kout.write("\t\t},\n")
kout.write('\n\t],\n\t"ecr:type": "redirect-group"\n}')


#Run the folowing to convert to 11.0.0
def redirects():
    inf = open('_redirects.json', 'r')
    outf = open('redirects.out', 'w')
    for line in inf:
        if '{' in line:
            outf.write(line.replace('\t\t','').replace('\n','~')+'\t"sling:resourceType": "endeca/redirect",~\t"priority": 10,~')
        elif 'searchTerms' in line:
            outf.write(line.replace('\t\t','').replace('searchTerms', 'keyword').replace('\n','~'))
        elif 'matchmode' in line:
            outf.write(line.replace('\t\t','').replace('\n','~')+'\t"inherit": "TRUE",~')
        elif 'url' in line:
            outf.write(line.replace('\t\t','').replace('\n','~'))
        elif '}' in line:
            outf.write(line.replace('\t\t},', '}'))
        else:
            pass
    outf.close()
    inf.close()
   
def makeRedirects():
    if not os.path.exists('redirects/'):
        os.makedirs('redirects/')
    infile = open('redirects.out')
    eachline = infile.readlines()
    eachline = eachline[:-1]
    global list
    list = []
    numlines=0
    for line in eachline:
        list.append(line.split('"keyword": "', 1)[-1].split('"')[0].replace(' ','_')+'.json')
        numlines+=1
    numlines=numlines-1
    index = 0
    count = 0
    while count < numlines:
        for i in list:
            newFile = open('redirects/'+i, 'w')
            newFile.write(eachline[index].replace('~','\n'))
            index+=1
            count+=1
    newFile.close()
    infile.close()
    
redirects()    
makeRedirects()

