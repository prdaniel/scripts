from __future__ import print_function
import os
import fileinput

#################################################################################################
##############################Create Tables from Generator ##########################################
def pythonDocCreator(inFile,outFile):
    if os.path.getsize(inFile) > 0:
        # Grabs the header row for the table    
        with open(inFile,'r') as myfile:
            head = myfile.readlines()
        head = head[0].split(',')
        # Creates a list of the number of columns
        columns = len(head) - 1
        l = []
        while columns > -1:
            string = str(columns)
            l.append(string)
            columns = columns - 1
        # Sets the number of columns for the table 
        columns = len(head)
        with open(outFile,'a') as file:
            file.write('\ntable = document.add_table(rows=1, cols='+str(columns)+')\nhdr_cells = table.rows[0].cells\n')
        # Reverses the list above
        l = l[::-1]
        # Adds the header to the table
        columns = len(head) - 1
        x = 0
        while columns > -1:
            k = l[x]
            g = head[x]
            with open(outFile,'a') as file:
                file.write('hdr_cells['+str(k)+'].text = "'+g.rstrip()+'"\n')
            x  = x +1
            columns = columns -1
    
        with open(outFile,'a') as file:
            file.write('row_cells = table.add_row().cells\n')
                
        with open(inFile,'r') as myfile:
            entry = myfile.readlines()
            for line in entry[1:]:
                if len(line) > 1:
                    with open(outFile,'a') as file:
                        file.write('row_cells = table.add_row().cells\n')
                        line = line.split(',')
                        columns = len(head) - 1
                        x = 0
                        while columns > -1:
                            k = l[x]
                            g = head[x]
                            with open(outFile,'a') as file:
                                file .write('row_cells['+k+'].text = str("'+line[int(k)].rstrip()+'")\n')
                            x  = x +1
                            columns = columns -1
                else:
                    pass
    else:
        pass
    
#######################################TestCalls##################################################
#createPython("createDoc3rd.py")
#pythonDocCreator("tmp/propertyMapper.txt","createDoc3rd.py")
#addPageBreak("createDoc3rd.py")
#pythonDocCreator("tmp/recordAdapters.txt","createDoc3rd.py")   
#endPython("createDoc3rd.py")

#createPython("createDoc3rd.py")
#for file in os.listdir("C:/Daniel/techSpectoDoc/pipeline/tmp"):
    #pythonDocCreator('C:/Daniel/techSpectoDoc/pipeline/tmp/'+file,"createDoc3rd.py")
    #addPageBreak("createDoc3rd.py")
#endPython("createDoc3rd.py")
#################################################################################################
##############################Create Opening/Closing Lines ##########################################
def createPython(outFile):
    with open(outFile,'w') as file:
        file .write('from docx import Document\nfrom docx.shared import Inches\n\ndocument = Document()\n\n')
def endPython(outFile):                 
    with open(outFile,'a') as file:
        file .write('\n\ndocument.add_page_break()\n\ndocument.save("C:/Daniel/techSpectoDoc/techspecdoc.docx")')
def pageBreak(outFile):                 
    with open(outFile,'a') as file:
        file .write('\ndocument.add_page_break()')
#################################################################################################
#######################################TestCalls##################################################
createPython("techspecdoc.py")
for file in os.listdir("C:/Daniel/techSpectoDoc/pipeline/tmp"):
    pythonDocCreator('C:/Daniel/techSpectoDoc/pipeline/tmp/'+file,"techspecdoc.py")
    pageBreak("techspecdoc.py")
endPython("techspecdoc.py")
#################################################################################################
#####################################Create MS Word Doc##########################################
os.system('techspecdoc.py')
