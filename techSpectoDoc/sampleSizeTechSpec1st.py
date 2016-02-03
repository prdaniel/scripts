import os

#Make tmp directory
if not os.path.exists('tmp'):
    os.makedirs('tmp')


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
