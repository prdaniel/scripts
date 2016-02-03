file1 = open('/usr/local/endeca/ToolsAndFrameworks/11.0.0/sitemap_generator/samples/xml_lumber/sitemap/navigation0.xml', 'r')
eneperf = open('/usr/local/endeca/ToolsAndFrameworks/11.0.0/sitemap_generator/samples/xml_lumber/sitemap/eneperf_prod.log', 'w')
for line in file1:
    if '<loc>' in line:
        eneperf.write(line.replace('   <loc>','').replace('</loc>',''))
eneperf.close()
file1.close()

file2 = open('/usr/local/endeca/ToolsAndFrameworks/11.0.0/sitemap_generator/samples/xml_lumber/sitemap/searchterm0.xml', 'r')
eneperf = open('/usr/local/endeca/ToolsAndFrameworks/11.0.0/sitemap_generator/samples/xml_lumber/sitemap/eneperf_prod.log', 'a')
for line in file2:
    if '<loc>' in line:
        eneperf.write(line.replace('   <loc>','').replace('</loc>',''))
eneperf.close()
file2.close()

file3 = open('/usr/local/endeca/ToolsAndFrameworks/11.0.0/sitemap_generator/samples/xml_lumber/sitemap/searchterm1.xml', 'r')
eneperf = open('/usr/local/endeca/ToolsAndFrameworks/11.0.0/sitemap_generator/samples/xml_lumber/sitemap/eneperf_prod.log', 'a')
for line in file3:
    if '<loc>' in line:
        eneperf.write(line.replace('   <loc>','').replace('</loc>',''))
eneperf.close()
file3.close()
