def redirects():
    inf = open('_redirects.json', 'r')
    outf = open('redirects.out', 'w')
    global list
    list = []
    for line in inf:
        if '{' in line:
            outf.write(line.replace('\t\t','').replace('\n','~')+'\t"sling:resourceType": "endeca/redirect",~\t"priority": 10,~')
        elif 'searchTerms' in line:
            list.append(line.split('"searchTerms": "', 1)[-1].split('",')[0].replace(' ','_')+'.json')
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
    infile = open('redirects.out')
    eachline = infile.readlines()
    index = 0
    count = 0
    while count < 117:
        for i in list:
            newFile = open('redirects/'+i, 'w')
            newFile.write(eachline[index].replace('~','\n'))
            index+=1
            count+=1
    newFile.close()
    infile.close()
    
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
    infile = open('thesaurus.out')
    eachline = infile.readlines()
    global list2
    list2 = []
    for line in eachline:
        list2.append(line.replace('/',' ').split('["', 1)[-1].split('"')[0].replace(' ','_')+'.json')
    index = 0
    count = 0
    while count < 310:
        for i in list2:
            newFile = open('thesaurus/'+i, 'w')
            newFile.write(eachline[index].replace('~','\n').replace(',]', ']'))
            index+=1
            count+=1
    newFile.close()
    infile.close()
  