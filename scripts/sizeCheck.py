import os

path = 'C:/Daniel/Scripts/'
log = 'C:/Daniel/Scripts/baseline_update.out'
def sizeCheck(file,size):
    try:
        record = os.path.getsize(path+file)
        print record
        if record >= size:
            checkR = True
        else:
            print "SEVERE small " + file
            checkR = False
            with open(log, 'a') as f:
                f.write('SEVERE '+file+' File was too small. Baseline did not run.\n')
    except WindowsError as Error:
        checkR = False
        print 'SEVERE Missing '+file+' File: Baseline Did Not Run!'
        with open(log, 'a') as f:
            f.write('SEVERE Missing ' +file+' Files!\n')
	
sizeCheck('test.txt',300000)