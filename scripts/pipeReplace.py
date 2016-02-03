import os
import shutil
import datetime

#Set Date
now = datetime.datetime.now()

pipelineDir = 'C:/Daniel/apps/ColeParmer/pipeline/'
pipelineNewDir = 'C:/Daniel/apps/ColeParmer/new/'
clientDir ='C:/Daniel/apps/ColeParmer/'

if not os.path.exists(pipelineNewDir):
    os.makedirs(pipelineNewDir)

def createLists():
    pipelineOut = open('pipelineOut.txt','r')
    pipelineNew = open('pipelineNew.txt','r')
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
    while listFileslen >= 0:
        if os.stat(pipelineNewDir+listFiles[index]).st_size == 0:
            print 'SEVERE: '+pipelineNewDir+listFiles[index]+' is empty!'
        else:
            if max(enumerate(open(pipelineNewDir+listFiles[index])))[0] != max(enumerate(open(pipelineDir+listFiles2[index])))[0]:
                print 'SEVERE: '+pipelineNewDir+listFiles[index]+': '+str(max(enumerate(open(pipelineNewDir+listFiles[index])))[0])+' != '+str(max(enumerate(open(pipelineDir+listFiles2[index])))[0])
            else:
               if not os.path.exists(clientDir+'pipeline_'+now.strftime("%Y-%m-%d")+'/'):
                   shutil.copytree(pipelineDir,clientDir+'pipeline_'+now.strftime("%Y-%m-%d")+'/')
               print 'Copying '+listFiles[index]+' to pipeline directory'
               shutil.copy2(pipelineNewDir+listFiles[index], 'C:/Daniel/apps/ColeParmer/newFinal')
        index+=1
        listFileslen = listFileslen-1
		
createLists()
createFiles()		
checkFiles()



	

		


	
