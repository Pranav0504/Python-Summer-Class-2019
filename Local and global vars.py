def add_up(sum_list):
    total = 0
    for i in range(0,len(sum_list)):
        total += sum_list[i]
    print(total)
    
def multiply(mult_list):
    total = 1
    for j in range(0,len(mult_list)):
        total *= mult_list[j]
    print(total)
    
def cases(case_list):
    total_u = 0
    total_l = 0
    for k in case_list:
        if k.isupper():
            total_u += 1
        elif k.islower():
            total_l += 1
    print('There are',total_u,'upper case letters')
    print('There are',total_l,'lower case letters')

print('''
1.
''')
add_up([1,2,3,4,5,6,7,8])

print('''
2.
''')
multiply([1,2,3,4,5])

print('''
3.
''')
cases('HelLo anD How aRe You DoIng')

    
