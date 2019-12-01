s = ''
n1 = int(input('Please enter the starting number :'))
n2 = int(input('Please enter the finishing number :'))
for num in range(n1,n2+1):
    if num % 7 ==0 and num%5==0:
        print(num,end = ', ')
