import os
import shutil
import datetime

#Change clientDir to current client
clientDir ='C:/Daniel/apps/ColeParmer/'
pipelineDir = clientDir+'pipeline/'
pipelineNewDir = clientDir+'ncname_pipeline/'
ncnamelog = open(clientDir+'logs/ncname.log','w')
fieldnames = open(clientDir+'endecafieldnames.properties','w')

#Temp output Files
allDims = 'allDimensions.txt'
ncnameDims = 'ncnameDimensions.txt'

#Set Date
now = datetime.datetime.now()

#Create List of All the Dimensions
pipeline = open(pipelineDir+'pipeline.epx','r')
pipelineOut = open(allDims,'w')

for line in pipeline:
    if '<PROP_MAPPING_DIM' in line:
	    pipelineOut.write(line.split('TARGET_NAME="',1)[-1].split('"')[0]+'\n')
pipelineOut.close()
pipeline.close()

pipelineOut = open(allDims,'r')
pipelineNew = open(ncnameDims,'w')

list = []
for i in pipelineOut:
    list.append(i)
#Create Valid NCName Dimensions	
chars = [' ','@','$',',','%','&','/','+','\t',';',':','"',"'",')','(','?','#','-']
charlen = len(chars)-1
n = 0
while charlen >= 0:
    newlist = []
    index = chars[n]
    for line in list:
        newlist.append(line.replace(index,'.'))
        list = []
        for j in newlist:
            list.append(j)
    if charlen == 0:
        break
    else:
        newlist = []
    charlen = charlen-1
    n+=1
for k in newlist:
    NCNameValid = k.rstrip().replace('...','..').replace('..','.').rstrip('.')+'\n'
    pipelineNew.write(NCNameValid)	
pipelineNew.close()
pipelineOut.close()
#Replace all pipeline references of the invalid NCName Dimenesions with Valid NCName Dimensions
if not os.path.exists(pipelineNewDir):
    os.makedirs(pipelineNewDir)

def createLists():
    pipelineOut = open(allDims,'r')
    pipelineNew = open(ncnameDims,'r')
    global list
    global list2
    list = []
    list2 = []
    for dim in pipelineOut:
        list.append(dim.rstrip())
    for dim2 in pipelineNew:
        list2.append(dim2.rstrip())

def replaceFiles():
    listlen = len(list) - 1
    index = 0
    infile = open(filePath)    
    outfile = open(filePath2,'w')   
    contents = infile.read()
    while listlen >= 0:
        contents = contents.replace(list[index],list2[index])
        fieldnames.write(list2[index]+'='+list[index]+'\n')
        index+=1
        listlen = listlen-1
    outfile.write(contents)
    outfile.close()
    infile.close()

def createFiles():	
    for files in os.listdir(pipelineDir):
        global filePath
        global filePath2
        filePath = pipelineDir+files
        filePath2 = pipelineNewDir+files
        replaceFiles() 

def checkFiles():
    listFiles = []
    listFiles2 = [] 
    for files in os.listdir(pipelineNewDir):
         listFiles.append(files)
    for files2 in os.listdir(pipelineDir):
        listFiles2.append(files2)
    listFileslen = len(listFiles) - 1
    index = 0
    ncnamelog.write(now.strftime("%Y-%m-%d %H:%M:%S")+'\n')
    while listFileslen >= 0:
        if os.stat(pipelineNewDir+listFiles[index]).st_size == 0:
            ncnamelog.write('SEVERE: '+pipelineNewDir+listFiles[index]+' is empty!\n')
        else:
            if max(enumerate(open(pipelineNewDir+listFiles[index])))[0] != max(enumerate(open(pipelineDir+listFiles2[index])))[0]:
                ncnamelog.write('SEVERE: '+pipelineNewDir+listFiles[index]+': '+str(max(enumerate(open(pipelineNewDir+listFiles[index])))[0])+' != '+str(max(enumerate(open(pipelineDir+listFiles2[index])))[0])+'\n')
            else:
               if not os.path.exists(clientDir+'pipeline_'+now.strftime("%Y-%m-%d")+'/'):
                   shutil.copytree(pipelineDir,clientDir+'pipeline_'+now.strftime("%Y-%m-%d")+'/')
               ncnamelog.write('Copying '+listFiles[index]+' to pipeline directory\n')
               shutil.copy2(pipelineNewDir+listFiles[index], pipelineDir)
        index+=1
        listFileslen = listFileslen-1

createLists()
createFiles()		
checkFiles()





	

