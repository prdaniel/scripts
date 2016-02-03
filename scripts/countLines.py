import os

#Change the baseline variable to the directory of the client 
baseline = 'C:/Daniel/apps/ColeParmer/test_data/'

outfile  = baseline+'datasizes.out'

def getDataFiles(baseline):
    #Creates output file
    ofile = open(outfile,'w')
    ofile.write('This script will output the line count of each data file at a 75% threshold for the data size check.\n\n')
    ofile.close()
    #Iterates through the ../test_data/baseline directory to grab all the data files
    for j in os.listdir(baseline):
        if '.py' not in j and '.zip' not in j:
            getLineCount(j);

def getLineCount(infile):
    file = open(infile, 'r')
    ofile = open(outfile,'a')
    #Counts the lines in each file and multiplies by .75 and writes the result to the output file.
    count = 0
    for line in file:
        count+=1
    count = count*.75
    ofile.write('('+str(count).split('.')[0]+",'"+infile+"')\n")

getDataFiles(baseline)