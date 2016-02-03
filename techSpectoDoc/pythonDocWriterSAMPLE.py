
#############################Create Python Script to Create Word Doc ##################################
with open("createDoc3rd.py",'w') as file:
    file .write('from docx import Document\nfrom docx.shared import Inches\n\ndocument = Document()\n\n')
#################################################################################################

##############################Create Header Row for Table ###########################################
with open("tmp/propertyMapper.txt",'r') as myfile:
    head = myfile.readlines()
head = head[0].split(',')

columns = len(head) - 1
l = []
while columns > -1:
    string = str(columns)
    l.append(string)
    columns = columns - 1
  
columns = len(head)
with open("createDoc3rd.py",'a') as file:
    file.write('table = document.add_table(rows=1, cols='+str(columns)+')\nhdr_cells = table.rows[0].cells\n')

l = l[::-1]
columns = len(head) - 1

x = 0
while columns > -1:
    k = l[x]
    g = head[x]
    with open("createDoc3rd.py",'a') as file:
        file.write('hdr_cells['+str(k)+'].text = "'+g.rstrip()+'"\n')
    x  = x +1
    columns = columns -1
#################################################################################################

##################################Create Table Entries ##############################################
with open("tmp/propertyMapper.txt",'r') as myfile:
    with open("createDoc3rd.py",'a') as file:
        entry = myfile.readlines()
        for line in entry[1:]:
            file.write('row_cells = table.add_row().cells\n')
            line = line.split(',')
            file .write('row_cells[0].text = str("'+line[0].rstrip()+'")\n')
            file .write('row_cells[1].text = str("'+line[1].rstrip()+'")\n')
            file .write('row_cells[2].text = str("'+line[2].rstrip()+'")\n')
            file .write('row_cells[3].text = str("'+line[3].rstrip()+'")\n')
#################################################################################################

########################Closes Python script and Creates the name of Word Doc ##########################
with open("createDoc3rd.py",'a') as file:
    file .write('\n\ndocument.add_page_break()\n\ndocument.save("C:/Daniel/techSpectoDoc/DKTEST.docx")')
#################################################################################################
    
    
