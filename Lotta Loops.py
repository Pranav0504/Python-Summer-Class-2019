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

