import os

#Converts the Workbench 2.1.2 thesaurus.xml file to Tools and Frameworks 11.1 json version.

new = open("C:/Daniel/apps/ColeParmer/testredthe/_thesaurus.json", 'w')
new.write('{\n\t"ecr:type": "thesaurus",\n\t"thesaurus-entries": [\n')
new.close()

old = open("C:/Daniel/apps/ColeParmer/testredthe/tmi20110117.thesaurus.xml", 'r')
new = open("C:/Daniel/apps/ColeParmer/testredthe/_thesaurus.json", 'a')

flag = 1
flog = 1
for line in old:
    fromm = line.split('<THESAURUS_FORM_FROM>', 1)[-1].split('</THESAURUS_FORM_FROM>')[0]
    too = line.split('<THESAURUS_FORM_TO>', 1)[-1].split('</THESAURUS_FORM_TO>')[0]
    twoway = line.split('<THESAURUS_FORM>', 1)[-1].split('</THESAURUS_FORM>')[0]
    if line.startswith('   <THESAURUS_ENTRY_ONEWAY>'):
        flag = 0
    if line.startswith('   </THESAURUS_ENTRY_ONEWAY>'):
        new.write('\t\t\t],\n\t\t},')
        flag = 1
    if not flag and not line.startswith('   <THESAURUS_ENTRY_ONEWAY>'):
        if '<THESAURUS_FORM_FROM>' in line:
            new.write('\n\t\t{\n\t\t\t"searchTerms": "'+fromm.rstrip()+'",\n\t\t\t"type": "one-way",\n\t\t\t"synonyms": [\n')
        elif '<THESAURUS_FORM_TO>' in line:
            new.write('\t\t\t\t"'+too.rstrip()+'",\n')
    if line.startswith('   <THESAURUS_ENTRY>'):
        new.write('\t\t{\n\t\t\t"synonyms": [\n')
        flog = 0
    if line.startswith('   </THESAURUS_ENTRY>'):
        new.write('\t\t\t],\n\t\t\t"type": "multi-way"\n\t\t},\n')
        flog = 1
    if not flog and not line.startswith('   <THESAURUS_ENTRY>'):
            new.write('\t\t\t\t"'+twoway+'",\n')
new.write('\n\t]\n}')    
new.close()

#Run the following to convert to 11.0.0
def thesaurus():
    inf = open('_thesaurus.json', 'r')
    outf = open('thesaurus.out', 'w')
    for line in inf:
        if '{' in line:
            outf.write(line.replace('\t\t','').replace('\n','~')+'\t"sling:resourceType" : "endeca/thesaurus",~\t"jcr:primaryType": "endeca:unstructured",~')
        elif 'searchTerms' in line:
            outf.write(line.replace('\t\t','').replace('searchTerms', 'trigger').replace('\n','~'))
        elif 'synonyms' in line:
            outf.write(line.replace('\t\t','').replace('synonyms', 'forms').rstrip())
        elif 'type' in line:
            outf.write(line.replace('\t\t','').replace('\n','~'))
        elif ']' in line:
            outf.write(line.replace('\t\t\t', '').replace('\n','~'))
        elif '}' in line:
            outf.write(line.replace('\t\t},', '}'))
        else:
            outf.write(line.replace('\t\t', '').rstrip())
    outf.close()
    inf.close()
   
def makeThesaurus():
    if not os.path.exists('thesaurus'):
        os.makedirs('thesaurus')
    infile = open('thesaurus.out')
    eachline = infile.readlines()
    eachline = eachline[:-1]
    global list2
    list2 = []
    numlines=0
    for line in eachline:
        list2.append(line.replace('/',' ').split('["', 1)[-1].split('"')[0].replace(' ','_')+'.json')
        numlines+=1
    numlines=numlines-1
    index = 0
    count = 0
    while count < numlines: #find the line count and replace 310
        for i in list2:
            newFile = open('thesaurus/'+i, 'w')
            newFile.write(eachline[index].replace('~','\n').replace(',]', ']'))
            index+=1
            count+=1
    newFile.close()
    infile.close()

thesaurus()
makeThesaurus()