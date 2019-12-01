play = 'y'
num = 0
while play == 'y':
    num += int(input('Enter the number of grams of sugar for an item: '))
    play = input('Would you like to add another item (y for yes) :')
print('You ate ', num, 'grams of sugar.')
if num >= 20 and num <= 32:
    print('Good job, you are leading a healthy lifestyle.')
elif num < 20:
    print('Try to eat a little bit more sugar.')
else:
    print('Try to eat less sugar.')
