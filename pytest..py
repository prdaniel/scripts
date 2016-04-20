
string = 'car truck 8 4 bus 6 1'
string_list = string.split()
string_map = []
for char in string_list:
    try:
        if int(char):
            string_map.append('int')
    except:
        string_map.append('str')

sorted_list = sorted(string_list)

     
print string_map
print sorted_list
'''
list_length = len(sorted_list)
list_count = 0
while list_length >= 0:
    try:
        item = int(sorted_list[list_count])
        print item
        map_count = 0
        map_length = len(sorted_list)
        while map_length >= 0:
            if string_map[map_count] == 'int':
                string_map[map_count] = item
                break
            else:
                map_count+=1
                map_length-=1
        list_length-=1
        list_count+=1
    except:
        item = sorted_list[list_count]
        print item
        map_count = 0
        map_length = len(sorted_list)
        while map_length >= 0:
            if string_map[map_count] == 'str':
                
                string_map[map_count] = item
                break
            else:
                map_count+=1
                map_length-=1
        list_length-=1
        list_count+=1
        list_length-=1
        list_count+=1
'''
lst=[]
lst2 = []


def map():
    if j == 'int':
        string_map[count] = i

def t(i,j,count):

    try:
        i = int(i)
        if j == 'int':
            string_map[count] = i
            break
        else:
            count+=1
            t(i,j,count)
    except:
        if j == 'str':
            string_map[count] = i
            break
        else:
            count+=1
            t(i,j,count)            
    

for i in sorted_list:
    count = 0
    for j in string_map:
        t(i,j,count)
        
print lst
print lst2
                
print string_map
                
                
                
        