print('1.')
price=float(input('Enter in the cost of anything random:'))
if price <= 10:
    print(0.9*price)
else:
    print(0.8*price)

print('2.')

age = int(input('Please enter in your age:'))
gender = input('Please enter in your gender (m or f):')

if age <= 12 and age >= 10 and gender == f:
    print('You are eligible for the soccer team.')
else:
    print('You are not eligible for the soccer team.')
    
