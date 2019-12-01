print('''This program will display your login information.
''')

f_name = input('Please enter your first name :')
l_name = input('Please enter your last name :')
ID = input('Please enter your student id number :')

if len(f_name)>=3:
    f_name = f_name.upper()
    f_name = f_name[:3]
else:
    f_name = f_name.upper()

if len(l_name)>=3:
    l_name = l_name.lower()
    l_name = l_name[0:3]
else:
    l_name = l_name.lower()
    
while not(ID.isnumeric()):
    print('That student ID is invalid, try again.')
    ID = input('Please enter your student id number :')

if len(ID)>=3:
    ID = ID[-3:]

print('Your login name is :',f_name+l_name+ID)
