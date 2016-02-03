def countnums(array):
    guess = raw_input('Pick a number:\n'+str(array)+'\n')
    left = 0
    right = 0
    status = True
    if int(guess) not in array:
        print 'Number is not in array!\nTry again: '
        countnums(array)
    for i in array:
        if status:
            if i != int(guess):
                left = left + i
            if i == int(guess):
                status = False
                pass
        else:
            right = right + i
            
    if left == int(guess) and right == int(guess):
        print '\nSUCCESS: Wow!! Both the left side and right side add up to '+guess+'!\n\nLets try and find another number!'
        countnums(array) 
    elif left == int(guess):
        print '\nSUCCESS: The sum of the numbers to the left of '+guess+' add up to '+guess+'!\n\nTry to find another number!'
        countnums(array) 
    elif right == int(guess):
        print '\nSUCCESS: The sum of the numbers to the right of '+guess+' add up to '+guess+'!\n\nTry to find another number!'
        countnums(array) 
    else:
        print '\nFAIL: The sum of the numbers to the left and to the right do not add up to '+guess+'!\n\nTry Another Number'
        countnums(array)      
        
    
    
array = [1,2,3,1,2,9,11,5,4,2]            
countnums(array)      