###Imports###
import os
###End Imports###

###Package Directory###
path = os.path.dirname(os.path.realpath(__file__))
###End Package Directory###

####Worddat Eneperf Parse####
class worddat():
    
    ###Create Directory###
    def createDir(self):
        global worddir
        worddir = path+'/worddat/'
        if not os.path.exists(worddir):
            os.mkdir(worddir)
    ###End Create Directory###
    
    ###Remove Duplicates###
    def remDups(self):
        file2 = 'sportsmansguide.worddat'
        nodups = worddir+'sportsmansguideND.worddat'
        with open(file2) as result:
            unique = set(result.readlines())
            with open(nodups, 'w') as rmdump:
                rmdump.writelines(set(unique))
        rmdump.close()
    ###End Remove Duplicates###
     
    ###Create Worddat Ouput Files###        
    def createWorddat(self):
        worddat.createDir(self)
        worddat.remDups(self)
        file3 = open(worddir+'sportsmansguideND.worddat','r'); ofile = open(worddir+'eneperfQueries.out','w'); ofile2 = open(worddir+'sitemapBlock.out','w')
        for line in file3:
            ofile.write('/search?terms='+line.rstrip()+'&opts=mode+matchall&rank=0&offset=0&compound=1&irversion=640\n')
            ofile2.write('  <URL><PARAM NAME="Ntt">'+line.rstrip()+'</PARAM></URL>\n') # For SiteMap Generator
        ofile.close(); ofile2.close(); file3.close()
        os.remove(worddir+'sportsmansguideND.worddat')
    ###End Create Worddat Ouput Files###        
        
####End Worddat Eneperf Parse####

