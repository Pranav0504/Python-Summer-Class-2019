import random
print('''1.
''')
month = int(input('Please enter a number to represent a month :'))
day = int(input('Please enter a number to represent a day :'))
if day > 31 or month > 12:
    print('That is not a valid number for the day or month.')
else:
    if month == 1 and day <= 31:
        print('It is January ', day,'and it is winter.')
    elif month == 2 and day <= 30:
        print('It is February ', day,'and it is winter.')
    elif month == 3 and day < 20:
        print('It is March ',day,'and it is winter.')
    elif month == 3 and day >= 20 and day<=31:
        print('It is March ',day,'and it is spring.')
    elif month == 4 and day <= 30:
        print('It is April ',day,'and it is spring.')
    elif month == 5 and day<=31:
        print('It is May ',day,'and it is spring.')
    elif month == 6 and day < 21 :
        print('It is June ',day,'and it is spring.')
    elif month == 6 and day>= 21 and day<= 30:
        print('It is June ',day,'and it is summer.')
    elif month == 7 and day <= 31:
        print('It is July ',day,'and it is summer.')
    elif month == 8 and day <= 31 :
        print('It is August ',day,'and it is summer.')
    elif month == 9 and day < 23:
        print('It is September ',day,'and it is summer.')
    elif month == 9 and day >= 23 and day <= 30:
        print('It is September ',day,'and it is autumn.')
    elif month == 10 and day <= 31:
        print('It is October ',day,'and it is autumn.')
    elif month == 11 and day <= 30:
        print('It is November ',day,'and it is autumn.')
    elif month == 12 and day < 21:
        print('It is December ',day,'and it is autumn.')
    elif month == 12 and day >= 21 and day <= 31:
        print('It is December ',day,'and it is winter.')
    else:
        print('The day that was entered was wrong for the specific month.')

print('''
2.
''')
rank = input('Enter a card rank :')
suit = input('Enter a card suit :')

if rank == '2':
    rank = 'Two'
elif rank == '3':
    rank = 'Three'
elif rank == '4':
    rank = 'Four'
elif rank == '5':
    rank = 'Five'
elif rank == '6':
    rank = 'Six'
elif rank == '7':
    rank = 'Seven'
elif rank == '8':
    rank = 'Eight'
elif rank == '9':
    rank = 'Nine'
elif rank == '10':
    rank = 'Ten'
elif rank.upper() == 'J':
    rank = 'Jack'
elif rank.upper() == 'Q':
    rank = 'Queen'
elif rank.upper() == 'K':
    rank = 'King'
elif rank.upper() == 'A':
    rank = 'Ace'

if suit.upper() == 'C':
    suit = 'Clubs'
elif suit.upper() == 'D':
    suit = 'Diamonds'
elif suit.upper() == 'H':
    suit = 'Hearts'
elif suit.upper() == 'S':
    suit = 'Spades'

print(rank,'of',suit)

print('''
3.
''')

phrase = input('Enter a phrase :')
extra = phrase.replace(" ", "")


if not(extra.isalpha()):
    print('Your phrase is invalid, try again.')
    phrase = input('Enter a phrase :')

phrase = phrase.upper()
for i in range(-1,-1*(len(phrase)+1),-1):
    print(phrase[i],end='')
    
    
    


