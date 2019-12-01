ans='0'
user = input("Please enter a temperature. Celsius or Fahrenheit doesn't matter. :")
if ans.lower() == 'c' or user[-1] == 'c' :
    print('This will convert that temperature to Fahrenheit.')
    f = (float(user[:-1]) * 9/5) + 32
elif ans.lower() == 'f' or user[-1] == 'c':
    print('This will convert that temperature to Celsius.')
    c = (float(user) - 32) * 5/9
    print(user,'degrees fahrenheit is {0:.1f} degrees celsius'.format(c))
while ans.lower() != 'c' and ans.lower() != 'f':
    print('Your input is invalid. Please type the correct letters.')
    ans = input('What were the degrees in? (c for celsius and f for fahrenheit) :')
if ans.lower() == 'c' or user[-1] == 'c' :
    print('This will convert that temperature to Fahrenheit.')
    f = (float(user) * 9/5) + 32
    print(user,'degrees celsius is {0:.1f} degrees fahrenheit.'.format(f))
elif ans.lower() == 'f' or user[-1] == 'c':
    print('This will convert that temperature to Celsius.')
    c = (float(user) - 32) * 5/9
    print(user,'degrees fahrenheit is {0:.1f} degrees celsius'.format(c))
