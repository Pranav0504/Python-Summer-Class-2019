print("1.")
print('6*(1-2)')
print(-6)

print('''
2a.''')
Radius=float(input('Please type a radius of a circle:'))
print('The area of the circle is',3.14*(Radius**2))

print('''
2b.''')
Width=float(input('Please enter the width of a rectangle:'))
Length=float(input('Please enter the lenght of a rectangle:'))
print('The area of this rectangle is',Width*Length)

print('''
3.''')
Celsius=float(input('What is the temperature in Celsius right now:'))
print('The temperature in Fahrenheit right now is',Celsius*1.8+32)

print('''
Bonus''')
Principal=10000
Times_Per_Year=12
Interest_Rate=0.08
Time=float(input('''You are compounding 10000 dollars monthly at an interest rate of 8 percent.
How long in years would you like to compound this amount:'''))
Amount=Principal*((1+Interest_Rate/Times_Per_Year)**(Times_Per_Year*Time))
print('After',Time,'years of compounding, you would have',Amount,'dollars')
