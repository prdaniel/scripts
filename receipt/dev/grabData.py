import time
now = time.strftime("%x")

def getInfo():
    if1 = open('C:/Daniel/dev/receipt/dev/document.xml','r')
    of1 = open('C:/Daniel/dev/receipt/dev/document_tmp1.csv','a')
    for i in if1:
        if 'preserve' in i:
            if '$' in i:
                price = i.split('>',1)[-1].split('<')[0]+'\n'
                if len(price) < 15:
                    pass
                else:
                    if checkTab in price:
                        tab = price.split(checkTab1,1)[-1].replace('\t$',',$').replace(' $',',$')
                        if '$' in tab:
                            of1.write(tab.rstrip()+','+now+'\n')
                    elif checkTabUp in price:
                        tab1 = price.split(checkTabUp1,1)[-1].replace('\t$',',$').replace(' $',',$')
                        if '$' in tab1:
                            of1.write(tab1.rstrip()+','+now+'\n')
                    elif checkSpace in price:
                        space = price.split(checkSpace1,1)[-1].replace(' $',',$').replace('\t$',',$')
                        if '$' in space:
                            of1.write(space.rstrip()+','+now+'\n')
                    elif checkSpaceUp in price:
                        space1 = price.split(checkSpaceUp1,1)[-1].replace(' $',',$').replace('\t$',',$')
                        if '$' in space1:
                           of1.write(space1.rstrip()+','+now+'\n')

def alpha():
    lets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    clets = 0
    letslen = len(lets)-1
    while letslen >= 0:
        global checkSpace
        global checkTab
        global checkSpaceUp
        global checkTabUp
        global checkSpace1
        global checkTab1
        global checkSpaceUp1
        global checkTabUp1
        checkSpace = check+' '+str(lets[clets])
        checkSpaceUp = check+' '+str(lets[clets]).upper()
        checkTab = check+'\t'+str(lets[clets])
        checkTabUp = check+'\t'+str(lets[clets]).upper()
        checkSpace1 = check+' '
        checkSpaceUp1 = check+' '
        checkTab1 = check+'\t'
        checkTabUp1 = check+'\t'
        getInfo()
        clets+=1
        letslen = letslen-1

def nums():
    nums = ['0','1','2','3','4','5','6','7','8','9']
    cnum = 0
    numslen = len(nums)-1
    while numslen >= 0:
        global check
        check = str(nums[cnum])
        alpha()
        cnum+=1
        numslen = numslen-1

def createDoc():
    infile=open('C:/Daniel/dev/receipt/dev/document_tmp1.csv','w')
    infile.write('Product,Price,Date\n')
    infile.close()
    nums()

createDoc()


    
