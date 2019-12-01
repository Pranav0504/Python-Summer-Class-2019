print('1.')
print('KPH\tMPH')
for KPH in range(60,131,10):
    MPH = KPH*0.6214
    print(KPH,'\t',round(MPH,1))

print('''
2.''')
print('''This program displays a list of numbers, their squares and their
reciprocal in steps of 2''')
start = int(input('Enter the starting number: '))
end = int(input('Enter in the finishing number: '))
print('Number\tSquare\tReciprocal')
print('----------------------------')
for number in range(start, end+1,2):
          square = number**2
          reciprocal = round(1/number,3)
          print(number, '\t', square, '\t' ,reciprocal)

print('''
3.''')
tips=0
tip_count=0
paper_total=0
paper_count=0
not_home=0
partial_payment_count=0

for i in range(12):
    amt = float(input('Please enter the amount recieved: '))
    if amt>5.50:
        tips = tips + (amt - 5.50)
        paper_total += 5.50
        tip_count = tip_count + 1
    elif amt == 0:
        not_home = not_home + 1
    elif amt < 5.50:
        partial_payment_count = partial_payment_count + 1
        paper_total = paper_total + amt
    else:
        paper_total = paper_total + amt
print('Paper amount: ${:.2f}'.format(paper_total))
print('Tips amount: ${:.2f}'.format(tips))
print('Tip count: ', tip_count)
print('Not home: ', not_home)
print('Partial payment count: ', partial_payment_count)
        
print('''
4.''')
num = int(input('Enter a number: '))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(num,0,-1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


print('''
5.''')
temp = int(input('What is the temperature outside in Fahrenheit: '))
humidity = int(input('What is the hummidity: '))

if temp >= 100:
    print('cancel school')
elif temp>= 92 and humidity>75:
    print('cancel school')
elif temp>= 85 and humidity>=85:
    print('cancel school')
elif temp>=75 and humidity>=65 and temp<85 and humidity<85:
    print('classes outside')
elif temp<= 25 and temp>=0:
    print("it's cold outside")
elif temp<0:
    print('cancel school')
else:
    print('schools in session')
print('''
6.''')
number=int(input('Please enter in a number: '))
for num in range(2,number):
    if number%num == 0:
        print('Your number is composite')
        break
else:
        print('Your number is prime')
        
