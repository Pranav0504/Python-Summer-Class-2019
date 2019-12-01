for i in range(1,6):
    print('|',end='')
    for dashes in range(i*-1+5):
        dashes = '-'
        print(dashes,end='')
    print('/',end='')
    for num in range(2*i-2,0,-1):
        print(num,end='')
    print('\\',end='')
    for dashes in range(i*-1+5):
        dashes = '-'
        print(dashes,end='')
    print('|',end='')
    print()
    
