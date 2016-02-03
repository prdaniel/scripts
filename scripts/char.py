import fileinput
for line in fileinput.FileInput("C:\Daniel\Scripts\charTest.txt",inplace=1):
    line = line.replace("","")
    print line,
	