#rot13 converter by Dan Kennedy
print "Welcome to Dan Kennedy's python ROT13 Encoder & Decoder!\n\n"

alpha = "abcdefghijklmnopqrstuvwxyz "
#string = "Fraq hf gur pbqr lbh hfrq gb qrpbqr guvf zrffntr"

#create dictionary of letters and corresponding integers
dic = {}
count = 1
for i in alpha:
    dic[i] = count
    count+=1

#Decodes rot13 message
def rot13decoder():
    string = raw_input('Please enter the rot13 message for decoding: \n')
    message = ""
    for i in string:
        if i.lower() in dic:
            rot = int(dic[i.lower()]) - 13
            if rot == 14:
                message+=' '
            elif rot < 1:
                base = 26
                newrot = base + rot
                message+=dic.keys()[dic.values().index(newrot)]
            else:
                message+=dic.keys()[dic.values().index(rot)]
                
    print '\nMessage decoded to: \n'+message+'\n\nHope You Enjoyed!!'

#Encodes message to rot13    
def rot13encoder():
    string = raw_input('Please enter message for rot13 encoding: \n')    
    message = ""
    for i in string:
        if i.lower() in dic:
            rot = int(dic[i.lower()]) + 13
            if rot == 40:
                message+=' '
            elif rot > 26:
                rot = rot - 26
                base = 0
                newrot = base + rot
                message+=dic.keys()[dic.values().index(newrot)]
            else:
                message+=dic.keys()[dic.values().index(rot)]
                
    print '\nMessage encoded to: \n'+message+'\n\nHope You Enjoyed!!'

#runs the encoder/decoder based on user input
endecode = raw_input('1) Enter 1 to Encode a message\n2) Enter 2 to Decode a message\n')
while endecode != '1' or endecode != '2':
    if endecode == '1':
        rot13encoder()
        break
    elif endecode == '2':
        rot13decoder()
        break
    else:
        endecode = raw_input('1) Enter 1 to Encode a message\n2) Enter 2 to Decode a message\n')

