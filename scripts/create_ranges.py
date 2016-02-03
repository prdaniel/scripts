def createRange():
    global list
    list = []
    global dimid
    dimid = 1000800
    iterate = 0
    while iterate < 6:
        count = 0
        while count<33:
            list.append(dimid)
            count+=1
            dimid+=1
        iterate+=1
        
def writeOG():
    infile = open('price_range.xml','r')
    outfile = open('price_range_out.xml','w')
    for line in infile:
        if 'NAME' in line:
            outfile.write('  <DIMENSION NAME="Price_Range_US" SRC_TYPE="INTERNAL">\n')
        elif 'Price_Range</SYN>' in line:
            outfile.write('        <SYN CLASSIFY="FALSE" DISPLAY="TRUE" SEARCH="FALSE">Price_Range_US</SYN>\n')
        else:
            outfile.write(line)
    outfile.close()
    infile.close()
    
def writeLine():
    sites = ['Price_Range_CA','Price_Range_UK','Price_Range_IN','Price_Range_DAVIS','Price_Range_MFLX']
    index = 0
    iterate = 0
    id = 12
    while iterate < 5:
        infile = open('price_range.xml','r')
        outfile = open('price_range_out.xml','a')
        count = 0
        for line in infile:
            if 'NAME' in line:
                outfile.write('  <DIMENSION NAME="'+sites[index]+'" SRC_TYPE="INTERNAL">\n')
            elif 'Price_Range</SYN>' in line:
                outfile.write('        <SYN CLASSIFY="FALSE" DISPLAY="TRUE" SEARCH="FALSE">'+sites[index]+'</SYN>\n')
            elif 'DIMENSION_ID' in line:
                outfile.write('    <DIMENSION_ID ID="'+str(id)+'"/>\n')
            elif 'DVAL_ID' in line:
                outfile.write('          <DVAL_ID ID="'+str(dimid)+'"/>\n')
            else:
                outfile.write(line)
        outfile.close()
        infile.close()
        index+=1
        id+=1
        iterate+=1
        
def createFinal():
    ifile = open('price_range_out.xml','r')
    ofile = open('price_range_final.xml','w')
    lindex = 0
    for i in ifile:
        if '          <DVAL_ID ID="1000998"/>' in i:
            ofile.write('          <DVAL_ID ID="'+str(list[lindex])+'"/>\n')
            lindex+=1
        else:
            ofile.write(i)
            
createRange()
writeOG()		
writeLine()
createFinal()
    
