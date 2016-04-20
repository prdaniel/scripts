ls2 = ['c','d','x']
lst = ['a','b','c']
same = []

a = list(set(lst).intersection(set(ls2)))

'''
[same.append(x) for x in lst for y in ls2 if x==y]
print same
'''
