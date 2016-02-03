
num = int(input('How many employees will you be entering into the system today? '))
employees = []
while num > 0:
   employees.append([raw_input('What is the employees name? '),raw_input('What is the employees age? ')])
   num = num - 1

   
names = []  
for i in employees:
    names.append(i[0])
print names

age = []  
for j in employees:
    age.append(j[1])
print age
