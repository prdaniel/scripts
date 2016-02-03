import os

#Prompts the user to input the client name for the pipeline files. Typing tmi20130815 would result to tmi20130815.thesaurus.xml
client = raw_input('Input Client Name:  ')

#Get properties and dimensions from the pipeline.epx and writes them to a csv file
file = open("pipeline.epx", "r")
propFile = open("tmp/propFile.csv", "w")
dimFile = open("tmp/dimFile.csv", "w")
propFile.write('Source,Target,Target Type,Match Mode,\n')
dimFile.write('Source,Target,Target Type,Match Mode,\n')
for line in file:
    if '<PROP_MAPPING_PROP' in line:
        propFile.write(line.split('PROP_NAME="', 1)[-1].split('"/>')[0].replace('" TARGET_NAME="',',')+',Property,N/A\n')
    elif '<PROP_MAPPING_DIM' in line:
        dimFile.write(line.split('PROP_NAME="', 1)[-1].replace('" TARGET_NAME="',',').replace('"/>',',Dimension,'+line.split('MATCH_MODE="', 1)[-1].split('" ')[0]))
    else:
        pass
dimFile.close()
propFile.close()
file.close()

#Get the dimension groups
file = open(client+".dimension_groups.xml", "r")
dimGroup = open("tmp/dimGroup.csv", "w")
for line in file:
    if "<DIMENSION_GROUP NAME=" in line or "<DIMNAME>" in line or "</DIMENSION_GROUP>" in line:
        dimGroup.write(line.replace('  <DIMENSION_GROUP NAME="','').replace('">','').replace('    <DIMNAME>','').replace('</DIMNAME>','').replace('  </DIMENSION_GROUP>',''))
    else:
        pass
dimGroup.close()
file.close()
	
#Get Filterable Properties
file = open(client+".record_filter.xml", "r")
filters = open("tmp/filters.csv", "w")
filters.write('Properties/Dimensions\n')
for line in file:
    if '<PROPNAME>' in line:
       filters.write(line.replace('  <PROPNAME>','').replace('</PROPNAME>',''))
    else:
        pass
filters.close()
file.close()

#Get the Search Interfaces
file = open(client+".recsearch_config.xml", "r")
searchint = open("tmp/searchint.csv", "w")
searchint.write('Searchable Properties and Dimensions\n')
for line in file:
    if 'NAME=' in line:
        searchint.write('\n'+line.split('NAME="', 1)[-1].replace('">',',[Search Interface]'))
    elif '</MEMBER_NAME>' in line:
        newline = line[line.find('>')+1:line.find('</')]
        searchint.write(newline+'\n')
    else:
        pass
searchint.close()
file.close()

#Get the Relevance Ranking Module
file = open(client+".relrank_strategies.xml", "r")
relrank = open("tmp/relrank.csv", "w")
for line in file:
    if "RELRANK_STRATEGY" in line or "RELRANK_STATIC" in line:
        relrank.write(line.replace('  <RELRANK_STRATEGY NAME="','').replace('">','').replace('    <RELRANK_STATIC NAME="','').replace('" ORDER="',',').replace('"/>','').replace('  </RELRANK_STRATEGY>',''))
    else:
        pass
relrank.close()
file.close()

#Get the Record Adapters
file = open("pipeline.epx", "r")
recordadapter = open('tmp/recordadapter.csv','w')
recordadapter.write('Adapter Name,Type,Class,Class Path/File Name,Pass Throughs\n')
for line in file:
    if 'RECORD_ADAPTER ' in line:
        adapterName = line.split(' NAME="', 1)[-1].split('"')[0]
        className = line.split('JAVA_CLASSNAME="', 1)[-1].split('"')[0]
        classPath = line.split('JAVA_CLASSPATH="', 1)[-1].split('"')[0]
        if 'JAVA_ADAPTER' in line:
            newline = adapterName+','+'Custom'+','+className+','+classPath
        else:
            type = line.split('COL_DELIMITER="', 1)[-1].split('"')[0]
            classPath = line.split('URL="', 1)[-1].split('"')[0]
            recordadapter.write(adapterName+','+type+','+'N/A'+','+classPath+','+'N/A\n')
    elif 'QUERY_NAME' in line:
            passThroughs = line.replace('    <PASS_THROUGH NAME="','').replace('">','=').replace('</PASS_THROUGH>','')
            recordadapter.write(newline+','+passThroughs)
    else:
        pass
recordadapter.close()
file.close()

#Get Data Files
file = open("tmp/recordadapter.csv", "r")
datafiles = open('tmp/datafiles.csv','w')
list = []
list2 = []
for line in file:
    if 'QUERY_NAME' in line:
        views = line.split('QUERY_NAME=', 1)[-1]
        list.append(views)
    elif 'N/A' in line:
        files = line.split('N/A,', 1)[-1].split(',')[0]+'\n'
        list2.append(files)
    else:
        pass
datafiles.write('Views:\n'+''.join(list)+'\nFiles:\n'+''.join(list2))
datafiles.close()
file.close()

#Get the Record Manipulators
file = open("pipeline.epx", "r")
recordmanip = open('tmp/recordmanipTmp.csv','w')
recordmanip.write('Manipulator Name,Record Source,Manipulations\n')
search = '  <RECORD_MANIPULATOR'
search2 = '    <EXPRESSION LABEL'
lines = file.readlines()
final = set()
for i, line in enumerate(lines):
    if line.startswith(search):
        new = line.split('NAME="', 1)[-1].split('"')[0]
        new2 = lines[i + 1].split('>', 1)[-1].split('<')[0]
    elif line.startswith(search2):
        if '      <COMMENT>' in lines[i + 1]:
            if len(lines[i + 1]) > 16:
                new3 = lines[i + 1].split('<COMMENT>', 1)[-1].split('<')[0]
            else:
                new3 = lines[i + 2].replace('   ', '')
        else:
            new3 = 'No Comment Provided - Add Manually'
        recordmanip.write(new+','+new2+','+new3+'\n')
    else:
        pass
recordmanip.close()
file.close()

#Removes Duplicate Manipulators
lines_seen = set()
outfile = open('tmp/recordmanip.csv', "w")
for line in open('tmp/recordmanipTmp.csv', "r"):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
    else:
        pass
os.remove('tmp/recordmanipTmp.csv')
outfile.close()

#Get the Java Manipulators
file = open("pipeline.epx", "r")
javamanip = open('tmp/javamanip.csv','w')
javamanip.write('Manipulator Name,Record Source,Manipulations\n')
search = '  <JAVA_MANIPULATOR'
lines = file.readlines()
for i, line in enumerate(lines):
    if line.startswith(search):
        name =  line.split(' NAME="', 1)[-1].split('"')[0]
        if len(lines[i + 1]) > 24:
            comment = lines[i + 1].split('>', 1)[-1].split('<')[0]
        else:
            comment = 'No Comment Provided - Add Manually'
        recSource = lines[i + 2].split('>', 1)[-1].split('<')[0]
        javamanip.write(name+','+recSource+','+comment+'\n')
    else:
        pass
javamanip.close()		
file.close()

#Get the Records Assemblers
file = open("pipeline.epx", "r")
assembler = open('tmp/assembler.csv','w')
search = '  <RECORD_ASSEMBLER'
lines = file.readlines()
for i, line in enumerate(lines):
    if line.startswith(search):
        name = line.split(' NAME="', 1)[-1].split('"')[0]+',[Assembler Name]\n'
        #assembler.write('\n'+line.split(' NAME="', 1)[-1].split('"')[0]+' [Assembler Name]\n')
        n = 1
        count = lines[i+n]
        while '    <RECORD_SOURCE>' in count:
            assembler.write(count.split('>', 1)[-1].split('<')[0]+',[Sources]\n')
            n = n+1
            count = lines[i+n]
    elif '    <RECORD_JOIN' in line:
        join = line.split('"', 1)[-1].split('"')[0]+',[Join Type]\n'
        #assembler.write(line.split('"', 1)[-1].split('"')[0]+' [Join Type]\n')
        assembler.write(name+join+'\n')
    else:
        pass
assembler.close()		
file.close()

#Get Record Caches
file = open("pipeline.epx", "r")
recordcache = open('tmp/recordcache.csv','w')
recordcache.write('Cache Name,General,Sources,Record Index\n')
search = '  <RECORD_CACHE'
lines = file.readlines()
for i, line in enumerate(lines):
    if line.startswith(search):
        if 'COMBINE_RECORDS="TRUE"' in line:
            combine = '(Combine Recs)'
        else:
            combine = ''
        max =  line.split('MAX_RECORDS="', 1)[-1].split('"')[0]
        name =  line.split('NAME="', 1)[-1].split('"')[0]
        recSource = lines[i + 2].split('>', 1)[-1].split('<')[0]
        key = lines[i + 4].split('ID="', 1)[-1].split('"')[0]
        recordcache.write(name+','+max+combine+','+recSource+','+key+'\n')
    else:
        pass
recordcache.close()		
file.close()
