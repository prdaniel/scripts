def createSingleLine():    
    infile = open('dimensions.txt','r')
    outfile = open('dimlist.txt','w')

    for line in infile:
        length = len(line)
        if length < 2:
            outfile.write(line)
        else:
            outfile.write(line.rstrip())
    outfile.close()
    infile.close()
    
def parseLines():
    infile = open('dimlist.txt','r')
    outfile = open('range_list.txt','w')
    for line in infile:
        if '<DVAL TYPE="RANGE">' in line:
            outfile.write(line.split('"', -1)[1].split('"')[0]+'\n')
        elif '<DVAL TYPE="SIFT">' in line:
            outfile.write(line.split('"', -1)[1].split('"')[0]+'\n')
        
def flatten():
    infile = open('content.txt','r')
    outfile = open('flatcontent.txt','w')
    for line in infile:
        if '</ContentItem>' in line:
            outfile.write(line)
        else:
            outfile.write(line.replace('\n','~'))
 
def replace():
    infile = open('flatcontent.txt','r')
    rangefile = open('range_list.txt','r')
    outfile = open('finalcontent.txt','w')
    list = []
    for i in rangefile:
        list.append(i.rstrip())
    length = len(list)
    n = 0
    for line in infile:
        if list[n] in line or 'Length (in.)' in line or 'Width (in.)' in line or 'Depth (in.)' in line or 'Height raised (in.)' in line or 'Normality' in line:
            outfile.write(line.replace('<String>dynRank</String>','<String>static</String>').replace('~','\n'))
            n += 1
        else:
            outfile.write(line.replace('~','\n'))
flatten()                
replace()
            
        
    
