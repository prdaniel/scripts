file =  open("C:/Endeca/apps/OFI/config/pipeline/OFI.merch_rule_group_OFIRedirects.xml","r")
out = open("C:/Endeca/apps/OFI/config/pipeline/OFI.merch_rule_group_OFIRedirects2.xml","w")

for line in file:
    out.write(line.replace("'","\\'"))