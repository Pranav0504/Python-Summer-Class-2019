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
c1 = float(input('Please enter in the first payment:'))
c2=float(input('Please enter in the second payment:'))
c3=float(input('Please enter in the third payment:'))
c4=float(input('Please enter in the fourth payment:'))
c5=float(input('Please enter in the fifth payment:'))
c6=float(input('Please enter in the sixth payment:'))
c7=float(input('Please enter in the seventh payment:'))
c8=float(input('Please enter in the eigth payment:'))
c9=float(input('Please enter in the ninth payment:'))
c10=float(input('Please enter in the tenth payment:'))
c11=float(input('Please enter in the eleventh payment:'))
c12=float(input('Please enter in the twelfth payment:'))
total=0
print('The total was : $', c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
if c1>5.50:
    c1-5.50 = t1
    total+=1
elif c2>5.50:
    c2-5.50 = t2
    total+=1
elif c3>5.50:
    c3-5.50 = t3
    total+=1
elif c4>5.50:
    c4-5.50 = t4
    total+=1
elif c5>5.50:
    c5-5.50 = t5
    total+=1
elif c6>5.50:
    c6-5.50 = t6
    total+=1
elif c7>5.50:
    c7-5.50 = t7
    total+=1
elif c8>5.50:
    c8-5.50 = t8
    total+=1
elif c9>5.50:
    c9-5.50 = t9
    total+=1
elif c10>5.50:
    c10-5.50 = t10
    total+=1
elif c11>5.50:
    c11-5.50 = t11
    total+=1
elif c12>5.50:
    c12-5.50 = t12
    total+=1
    
print('The total amount of tips was :$',t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11+t12)

print('The total number of tips was :',total)
total_not_home=0
if c1 == 0:
    total_not_home+=1
elif c2 == 0:
    total_not_home+=1
elif c3 == 0:
    total_not_home+=1
elif c4 == 0:
    total_not_home+=1
elif c5 == 0:
    total_not_home+=1
elif c6 == 0:
    total_not_home+=1
elif c7 == 0:
    total_not_home+=1
elif c8 == 0:
    total_not_home+=1
elif c9 == 0:
    total_not_home+=1
elif c10 == 0:
    total_not_home+=1
elif c11 == 0:
    total_not_home+=1
elif c12 == 0:
    total_not_home+=1

print('The number of people not home was :',total_not_home)
partial_payment=0
if c1>0 and c1<5.50:
    partial_payment+=1
elif c2>0 and c2<5.50:
    partial_payment+=1
elif c3>0 and c3<5.50:
    partial_payment+=1
elif c4>0 and c4<5.50:
    partial_payment+=1
elif c5>0 and c5<5.50:
    partial_payment+=1
elif c6>0 and c6<5.50:
    partial_payment+=1
elif c7>0 and c7<5.50:
    partial_payment+=1
elif c8>0 and c8<5.50:
    partial_payment+=1
elif c9>0 and c9<5.50:
    partial_payment+=1
elif c10>0 and c10<5.50:
    partial_payment+=1
elif c11>0 and c11<5.50:
    partial_payment+=1
elif c12>0 and c12<5.50:
    partial_payment+=1

print('The number of partial payments was :',partial_payment)

    

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
        
