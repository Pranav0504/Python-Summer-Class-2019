age=14
guess=0
count = 1
print('This program will give you three times to guess my age.')

while count <= 3:
    guess=int(input('What is your guess?:'))
    if guess==age:
        print('Congratulations')
        print('You got it!')
        break
    elif guess<age:
        print('Sorry, too low.')
    else:
        print('Sorry, too high')
    count += 1
    
    

