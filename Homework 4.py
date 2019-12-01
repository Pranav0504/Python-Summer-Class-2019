FirstName=Pranav
LastName=Patil
print('FirstName'+' '+'LastName')

FName=input('First name:')
LName=input('Last name:')
print('Hello',+'FName',+'LName')

Width=input('What is the width of the room:')
Length=input('What is the length of the room:')
print('The amount of carpet in square feet is',Width*Length)
Area=Width*Length

CostOfCarpet=input('What is the cost per square yard of carpet:')
print('Amount of carpet in square feet:',Area)
print('Amount of carpet in square yards:',Area/9)
print('Cost of carpet would be:', (Area/9)*CostOfCarpet)


Quarters=input('How many quarters:')
Dimes=input('How many dimes:')
Nickels=input('How many nickels:')
Pennies=input('How many pennies:')
VQuarters=Quarters*25
VDimes=Dimes*10
VNickels=Nickels*5
print('The total amount of change is:', VQuarters+VDimes+VNickels+Pennies)
