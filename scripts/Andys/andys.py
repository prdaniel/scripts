import os
import sys

file=open("mmid_attributes.txt", "r")
copy=open("newFile.txt", "w")
for line in file:
    if "~~" in line:
        copy.write(line)		
file.close()
copy.close()

file=open("mmid_attributes.txt", "r")
subFile=open("subFile.txt", "w")
for line in file:
    subFile.write(line.split("~~")[0].strip()+"\n")
subFile.close()
file.close()
    
copy=open("newFile.txt", "r")
mmfit=open("mmfit.txt", "w")

for line in copy:
    if "|Mmid|" in line:
        mmfit.write(line.replace("Mmid","Mmid_fit", 1)) 
mmfit.close()
copy.close()

copy=open("newFile.txt", "r")
mmfit=open("mmfit.txt", "a")

for line in copy:
    if "|Universal|" in line:
        mmfit.write(line.replace("Universal","Universal_fit", 1)) 
mmfit.close()
copy.close()


final=open("subFile.txt", "a")
mmfit=open("mmfit.txt", "r")
for line in mmfit:
    final.write(line)
mmfit.close()
final.close()

num_lines = sum(1 for line in open('mmid_attributes.txt'))
num_lines2 = sum(1 for line in open('subFile.txt'))
if num_lines2 >= num_lines:
    print "Good Files"
else:
    print "Error in Process"
