for i in range(1,9):
    for dashes in range(i*-1+8):
        dashes = '-'
        print(dashes,end='')
    for zeroes in range(i*2-1):
        zeroes = '0'
        print(zeroes,end='')
    for dashes in range(i*-1+8):
        dashes = '-'
        print(dashes,end='')
    print()
