import os

#Prompts the user to input the client name for the pipeline files. Typing tmi20130815 would result to tmi20130815.thesaurus.xml
client = raw_input('(Ex. Type tmi20110908 for tmi20110908.record_filter.xml)\nInput Client Name for Pipeline Files: ')

#Make tmp directory
if not os.path.exists('tmp'):
    os.makedirs('tmp')

#Get Properties	to be created
file = open(client+".prop_refs.xml", "r")
properties = open("tmp/properties.txt", "w")
properties.write('Name,Type\n')
for line in file:
    if '<PROP_REF ' in line:
        properties.write(line.replace('  <PROP_REF NAME="', '').replace('" TYPE="', ',').replace('DOUBLE', 'FLOATING POINT').replace('"/>',''))
    else:
        pass
properties.close()
file.close()

#Get Dimensions	to be created
file = open("dimensions.xml", "r")
file2 = open("externaldimensions.xml", "r")
dimensions = open("tmp/dimensions.txt", "w")
dimensions.write('Name,External Type\n')
for line in file:
    if 'DIMENSION NAME' in line:
        dimensions.write(line.replace('  <DIMENSION NAME="', '').replace('" SRC_TYPE="', ',').replace('INTERNAL','NORMAL').replace('">',''))
    else:
        pass
for line2 in file2:
    if 'DIMENSION NAME' in line2:
        dimensions.write(line2.replace('  <DIMENSION NAME="', '').replace('" SRC_TYPE="', ',').replace('">',''))
    else:
        pass
dimensions.close()
file2.close()
file.close()
	
#Get properties and dimensions from the pipeline.epx
file = open("pipeline.epx", "r")
propertyMapper = open("tmp/propertyMapper.txt", "w")
propertyMapper.write('Source,Target,Target Type,Match Mode\n')
for line in file:
    if '<PROP_MAPPING_PROP' in line:
        propertyMapper.write(line.split('PROP_NAME="', 1)[-1].split('"/>')[0].replace('" TARGET_NAME="',',')+',Property,N/A\n')
    elif '<PROP_MAPPING_DIM' in line:
        propertyMapper.write(line.split('PROP_NAME="', 1)[-1].replace('" TARGET_NAME="',',').replace('"/>',',Dimension,'+line.split('MATCH_MODE="', 1)[-1].split('" ')[0]))
    else:
        pass
propertyMapper.close()
file.close()

#Get the dimension groups
file = open(client+".dimension_groups.xml", "r")
dimensionGroups = open("tmp/dimensionGroups.txt", "w")
dimensionGroups.write('Group,Dimensions')
search = '  <DIMENSION_GROUP'
lines = file.readlines()
for i, line in enumerate(lines):
    if line.startswith(search):
        dimensionGroups.write('\n'+line.split(' NAME="', 1)[-1].split('"')[0]+',')
        n = 1
        count = lines[i+n]
        while '<DIMNAME>' in count:
            dimensionGroups.write(count.split('>', 1)[-1].split('<')[0]+';')
            n = n+1
            count = lines[i+n]
    else:
        pass
dimensionGroups.close()
file.close()
	
#Get Filterable Properties
file = open(client+".record_filter.xml", "r")
recordFilter = open("tmp/recordFilter.txt", "w")
recordFilter.write('Properties/Dimensions\n')
for line in file:
    if '<PROPNAME>' in line:
       recordFilter.write(line.replace('  <PROPNAME>','').replace('</PROPNAME>',''))
    else:
        pass
recordFilter.close()
file.close()

#Get the Search Interfaces
file = open(client+".recsearch_config.xml", "r")
searchInterfaces = open("tmp/searchInterfaces.txt", "w")
searchInterfaces.write('Searchable Properties and Dimensions\n')
for line in file:
    if 'NAME=' in line:
        searchInterfaces.write('\n'+line.split('NAME="', 1)[-1].replace('">',',[Search Interface]'))
    elif '</MEMBER_NAME>' in line:
        newline = line[line.find('>')+1:line.find('</')]
        searchInterfaces.write(newline+'\n')
    else:
        pass
searchInterfaces.close()
file.close()

#Get the Relevance Ranking Module
file = open(client+".relrank_strategies.xml", "r")
relevanceRanking = open("tmp/relevanceRanking.txt", "w")
for line in file:
    if "RELRANK_STRATEGY" in line or "RELRANK_STATIC" in line:
        relevanceRanking.write(line.replace('  <RELRANK_STRATEGY NAME="','').replace('">','').replace('    <RELRANK_STATIC NAME="','').replace('" ORDER="',',').replace('"/>','').replace('  </RELRANK_STRATEGY>',''))
    else:
        pass
relevanceRanking.close()
file.close()

#Get the Record Adapters
file = open("pipeline.epx", "r")
recordAdapters = open('tmp/recordAdapters.txt','w')
recordAdapters.write('Adapter Name,Type,Class,Class Path/File Name,Pass Throughs\n')
for line in file:
    if 'RECORD_ADAPTER ' in line:
        adapterName = line.split(' NAME="', 1)[-1].split('"')[0]
        className = line.split('JAVA_CLASSNAME="', 1)[-1].split('"')[0]
        if 'JAVA_CLASSPATH="' in line:
            classPath = line.split('JAVA_CLASSPATH="', 1)[-1].split('"')[0]
        else:
            classPath = 'N/A'
        if 'JAVA_ADAPTER' in line:
            newline = adapterName+','+'Custom'+','+className+','+classPath
        else:
            type = line.split('COL_DELIMITER="', 1)[-1].split('"')[0]
            classPath = line.split('URL="', 1)[-1].split('"')[0]
            recordAdapters.write(adapterName+',Delimited('+type+'),'+'N/A'+','+classPath+','+'N/A\n')
    elif 'QUERY_NAME' in line or 'ADAPTER_BEAN' in line:
            passThroughs = line.replace('    <PASS_THROUGH NAME="','').replace('">','=').replace('</PASS_THROUGH>','')
            recordAdapters.write(newline+','+passThroughs)
    else:
        pass
recordAdapters.close()
file.close()

#Get Data Files
file = open("tmp/recordAdapters.txt", "r")
dataFilesViews = open('tmp/dataFilesViews.txt','w')
list = []
list2 = []
for line in file:
    if 'QUERY_NAME' in line:
        views = line.split('QUERY_NAME=', 1)[-1]
        list.append(views)
    elif 'ADAPTER_BEAN' in line:
        views = line.split('ADAPTER_BEAN=', 1)[-1]
        list.append(views)
    elif 'N/A' in line:
        files = line.split('N/A,', 1)[-1].split(',')[0]+'\n'
        list2.append(files)
    else:
        pass
dataFilesViews.write('Views:\n'+''.join(list)+'\nFiles:\n'+''.join(list2))
dataFilesViews.close()
file.close()

#Get the Record Manipulators
file = open("pipeline.epx", "r")
recordManipulators = open('tmp/recordManipulatorsTmp.txt','w')
recordManipulators.write('Manipulator Name,Record Source,Manipulations\n')
search = '  <RECORD_MANIPULATOR'
search2 = '    <EXPRESSION LABEL'
lines = file.readlines()
final = set()
for i, line in enumerate(lines):
    if line.startswith(search):
        new = line.split('NAME="', 1)[-1].split('"')[0]
        if '<RECORD_SOURCE>' in lines[i + 1]:
            new2 = lines[i + 1].split('>', 1)[-1].split('<')[0]
        elif '<RECORD_SOURCE>' in lines[i + 2]:
            new2 = lines[i + 2].split('>', 1)[-1].split('<')[0]
        else:
            new2 = 'Find the <RECORD_SOURCE> in pipeline.epx'
    elif line.startswith(search2):
        if '      <COMMENT>' in lines[i + 1]:
            if len(lines[i + 1]) > 16:
                new3 = lines[i + 1].split('<COMMENT>', 1)[-1].split('<')[0]
            else:
                new3 = lines[i + 2].replace('   ', '')
        else:
            new3 = 'No Comment Provided - Add Manually'
        recordManipulators.write(new+','+new2+','+new3+'\n')
    else:
        pass
recordManipulators.close()
file.close()

#Removes Duplicate Manipulators
lines_seen = set()
outfile = open('tmp/recordManipulators.txt', "w")
for line in open('tmp/recordManipulatorsTmp.txt', "r"):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
    else:
        pass
os.remove('tmp/recordManipulatorsTmp.txt')
outfile.close()

#Get the Java Manipulators
file = open("pipeline.epx", "r")
javaManipulators = open('tmp/javaManipulators.txt','w')
javaManipulators.write('Manipulator Name,Record Source,Manipulations\n')
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
        javaManipulators.write(name+','+recSource+','+comment+'\n')
    else:
        pass
javaManipulators.close()		
file.close()

#Get the Records recordAssemblers
file = open("pipeline.epx", "r")
recordAssembler = open('tmp/recordAssembler.txt','w')
search = '  <RECORD_ASSEMBLER'
lines = file.readlines()
for i, line in enumerate(lines):
    if line.startswith(search):
        name = line.split(' NAME="', 1)[-1].split('"')[0]+',[Assembler Name]\n'
        n = 1
        count = lines[i+n]
        while '    <RECORD_SOURCE>' in count:
            recordAssembler.write(count.split('>', 1)[-1].split('<')[0]+',[Sources]\n')
            n = n+1
            count = lines[i+n]
    elif '    <RECORD_JOIN' in line:
        join = line.split('"', 1)[-1].split('"')[0]+',[Join Type]\n'
        recordAssembler.write(name+join+'\n')
    else:
        pass
recordAssembler.close()		
file.close()

#Get Record Caches
file = open("pipeline.epx", "r")
recordCache = open('tmp/recordCache.txt','w')
recordCache.write('Cache Name,General,Sources,Record Index\n')
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
        recordCache.write(name+','+max+combine+','+recSource+','+key+'\n')
    else:
        pass
recordCache.close()		
file.close()

#Get Wildcard Fields
file = open(client+".recsearch_indexes.xml", "r")
wildcarding = open('tmp/wildcarding.txt','w')
search = '  <RECSEARCH_INDEX'
lines = file.readlines()
for i, line in enumerate(lines):
    if line.startswith(search):
        if  '<WILDCARD_INDEX/>' in lines[i + 2]:
            wildcarding.write(line.split('NAME="', 1)[-1].split('"')[0]+'\n')
        else:
            pass
    else:
        pass
wildcarding.close()		
file.close()

#Get Rollup Properties
file = open(client+".rollups.xml", "r")
rollups = open('tmp/rollups.txt','w')
for line in file:
    if '<ROLLUP NAME="' in line:
        rollups.write(line.split('"', 1)[-1].split('"')[0]+'\n')	
rollups.close()		
file.close()

#Get Sort Fields
file = open(client+".record_sort_config.xml", "r")
sorting = open('tmp/sorting.txt','w')
for line in file:
    if '<RECORD_SORT NAME="' in line:
        sorting.write(line.split('"', 1)[-1].split('"')[0]+'\n')	
sorting.close()		
file.close()

#Get Stop Words
file = open(client+".stop_words.xml", "r")
stopWords = open('tmp/stopWords.txt','w')
for line in file:
    if '<STOP_WORD>' in line:
        stopWords.write(line.split('>', 1)[-1].split('<')[0]+',')	
stopWords.close()		
file.close()
