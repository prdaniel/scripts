#nums = ['0','1','2','3','4','5','6','7','8','9']
#lets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#cnum = 0
#clets = 0

#numslen = len(nums)-1
#letslen = len(lets)-1

def alpha():
    lets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    clets = 0
    letslen = len(lets)-1
    while letslen >= 0:
        lcheck = check+' '+str(lets[clets]).upper()
        print lcheck
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
    
nums()
