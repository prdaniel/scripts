###Imports###
import os
from Tkinter import *
import tkMessageBox
from eneperf import *
###End Imports###

###Set Classes###
worddat = worddat()
###End Set Classes###

###Test Functions###
def dgraph():
    print 'DGRAPH'
    
def assembler():
    print 'ASSEMBLER'
###End Test Functions###
    
###Package Directory###
path = os.path.dirname(os.path.realpath(__file__))
###End Package Directory###

###Gets Info for Checkbox app###
infoList = []
fileList = []

for j in os.listdir(path+'/info/'):
    if 'info' in j:
        infoList.append(j.split('.')[0].rstrip())
        with open(path+'/info/'+j) as infile:
            line = infile.read()
            fileList.append(line)
###End Gets Info for Checkbox app###

###Checkbox###
##Generates the GUI window##
master = Tk()
Label(master, text="What would you like to generate?").grid(row=0, sticky=W)

##Creates Function Dictionary##
funDic = {}

##Creates Variables List for IntVar()##
variables = []
for var in range(0,len(infoList)):
    variables.append(IntVar())

##Sets the variables for the while loop below##
length = len(infoList) - 1    
varbs = 0    
rows = 1

##Creates the Checkboxes and Info buttons##
while length >= 0 :
    #Info Buttons#
    if length == 2:
        def infoMessage():
            tkMessageBox.showinfo(infoList[length].replace('_',' ').upper(),fileList[length])
    elif length == 1:
        def infoMessage():
            tkMessageBox.showinfo(infoList[length-1].replace('_',' ').upper(),fileList[length-1])
    elif length == 0:
        def infoMessage():
             tkMessageBox.showinfo(infoList[length-2].replace('_',' ').upper(),fileList[length-2])
    #Adds functions to the funDic dictionary#        
    funDic[infoList[length]] = infoMessage
    #Creates the checkboxes#
    Checkbutton(master, text=infoList[length].replace('_',' ').upper(), variable=variables[varbs]).grid(row=rows, sticky=W)
    #Creates the Info Button#
    Button(master, text = "Info", command = funDic[infoList[length]]).grid(row=rows, column=1, sticky=W)
    #While Loop Counters#
    length = length - 1
    rows+=1
    varbs+=1
#Creates the submit button#
Button(master, text='Submit', command=master.quit).grid(row=10, sticky=W, pady=4)
mainloop()
###End Checkbox###

###Dictionary###
worddatlog = {'variable': variables[0].get(), 'function': worddat.createWorddat}
dgraphlog = {'variable': variables[1].get(), 'function': dgraph}
assemblerlog = {'variable': variables[2].get(), 'function': assembler}
###End Dictionary###

###List of Dictionary###
list = [worddatlog, dgraphlog, assemblerlog]
###End List of Dictionary###

###Run Checked Functions###
for i in list:
    if i['variable'] == 1:
        i['function']()
###End Run Checked Functions###
