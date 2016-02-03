#Converts the Workbench 2.1.2 thesaurus.xml file to Tools and Frameworks 11.1 json version.

new = open("C:/Endeca/apps/OFI/config/pipeline/_thesaurus.json", 'w')
new.write('{\n\t"ecr:type": "thesaurus",\n\t"thesaurus-entries": [\n')
new.close()

old = open("C:/Endeca/apps/OFI/config/pipeline/OFI.thesaurus.xml", 'r')
new = open("C:/Endeca/apps/OFI/config/pipeline/_thesaurus.json", 'a')

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

