file =  open("C:/Daniel/apps/ColeParmer/thesaurus_redirects/tmi20110117.merch_rule_group_default_redirects.xml","r")
out = open("C:/Daniel/apps/ColeParmer/thesaurus_redirects/tmi20110117.merch_rule_group_default_redirects2.xml","w")

for line in file:
    out.write(line.replace("'","\\'"))