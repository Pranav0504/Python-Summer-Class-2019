print('1.')
num = int(input('How many grades do you want to average?'))
count=1
grade_total = 0
while count <= num:
    grade_total += float(input('Please enter a grade'))
    count += 1
print('Your average is ', round(grade_total/num, 2))

print('''
2.''')

grade_total = 0
more = 'Y'
count = 0

while more == 'Y':
    grade_total += float(input('Please enter a grade'))
    count += 1
    ans = input('Do your want to enter in another grade?(Y for yes)')
    if ans != 'Y' and ans != 'y' and ans != 'Yes' and ans != 'yes':
        more = 'N'
print('Your average is ', round(grade_total/count, 2))

print('''
3.''')


    
