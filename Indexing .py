print('1.')

s1 = 'I Love Python'
for i in s1:
    print(i)


print('''
2.''')


preamble = '''We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.'''
total = 0

for i in preamble:
    if i == ' ':
        total += 1
print(total,'spaces.')
