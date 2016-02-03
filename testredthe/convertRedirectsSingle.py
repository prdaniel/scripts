#Converts the Workbench 2.1.2 redirects.xml file to Tools and Frameworks 11.1 json version.
import xml.etree.ElementTree as ET

#Escapes single quotes for json format
file =  open("C:/Daniel/apps/ColeParmer/thesaurus_redirects/tmi20110117.merch_rule_group_default_redirects.xml","r")
out = open("C:/Daniel/apps/ColeParmer/thesaurus_redirects/tmi20110117.merch_rule_group_default_redirectsTMP.xml","w")

for line in file:
    out.write(line.replace("\\","").replace("'","\\'"))
file.close()
out.close()

#Converts xml to json
kout = open("C:/Daniel/apps/ColeParmer/thesaurus_redirects/_redirects.json","w")
tree = ET.parse("C:/Daniel/apps/ColeParmer/thesaurus_redirects/tmi20110117.merch_rule_group_default_redirectsTMP.xml")
root = tree.getroot()
kout.write("{\n\t'redirects': [\n")
for merch_rules in root.findall('./MERCH_RULE'):
    url = merch_rules.find('./PROP/PVAL').text 
    for rule in merch_rules.findall('./MERCH_RULE_TRIGGER'):
        kout.write('\t\t{\n')
        kout.write("\t\t\t'searchTerms': " + "'" + rule.find("KEYWORDS").text + "',\n")
        kout.write("\t\t\t'matchmode': " + "'" +  rule.find("KEYWORDS").attrib['MODE'] + "',\n")
        kout.write("\t\t\t'url': " + "'" + url + "'\n")
        kout.write('\t\t},\n')
kout.write("\n\t],\n\t'ecr:type': 'redirect-group'\n}")