import os

def paramPipeline(infile,newLine,identifier):

    infile = 'E:/Endeca/Apps/Gamestop/config/pipeline/'+infile
    tmp = infile+'.tmp'
    bak = infile+'.bak'
    fail = infile+'.FAIL'
	
    if os.path.isfile(bak):
        os.remove(bak)
	    
    with open(infile, 'r') as espFile:
        with open (tmp, 'w') as espFileTmp:
            for line in espFile:
                espFileTmp.write(newLine+'\n' if identifier in line else line)
    infilenum = sum(1 for line in open(infile))
    tmpnum = sum(1 for line in open(tmp))
    if tmpnum == infilenum:
        os.rename(infile, bak)
        os.rename(tmp, infile)
        if os.path.isfile(fail):
            os.remove(fail)
        return True
    else:
        os.rename(tmp, fail)
        with open('E:/Endeca/Apps/Gamestop/logs/baseline_update.out', 'a') as f:
            f.write('SEVERE paramPipeline script in test.py Failed\nTroubleshoot:\n1. Check the '+infile+' and '+fail+' files for issues\n2. Check test.py for issues\n3. Re-run the paramPipeline script')
            return False
with open('E:/Endeca/Apps/GameStop/config/script/'+os.environ["ENDECA_ENV"]+'environment.properties', 'r') as env:
    for line in env:
        if 'dgraph.auth.host' in line:
            recordstore = line.split('= ', 1)[-1].rstrip()
        elif 'eac.host' in line:
            eac = line.split('= ', 1)[-1].rstrip()

valid5 = paramPipeline('GameStopTEST.esp','  <PROJECT_MANAGER_CONFIG APPLICATION="GameStop" PORT="8006" URL="'+eac+'"/>','PORT')
valid6 = paramPipeline('pipelineTEST.epx','    <PASS_THROUGH NAME="HOST">'+recordstore+'</PASS_THROUGH>','HOST')
valid7 = paramPipeline('pipelineTEST.epx','    <PASS_THROUGH NAME="PORT">8500</PASS_THROUGH>','PORT')
