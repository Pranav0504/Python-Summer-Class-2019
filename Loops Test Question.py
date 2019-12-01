import random
more = 'y'

print('This program will simulate the game of Rock, Paper, Scissors')
print('''Winning rules of Rock Paper Scissors is as follows:
Rock beats scissors
Paper beats rock
Scissors beats paper
When both selections are the same, it is a tie.''')

while more == 'y' or more == 'Y' or more == 'yes' or more == 'Yes':
    cpu = random.randint(1,3)
    u_num = int(input('Please select your number. 1 for rock, 2 for paper and 3 for scissors :'))
    if u_num == cpu:
        print("It's a tie!")
        more = input('Would you like to play again?(y for yes) :')
    else:
        if cpu == 1 and u_num == 2:
            print('Paper beats rock so ')
            print('Player wins!')
            more = input('Would you like to play again?(y for yes) :')
        elif cpu == 1 and u_num == 3:
            print('Rock beats scissors so ')
            print('Computer wins!')
            more = input('Would you like to play again?(y for yes) :')
        elif cpu == 2 and u_num == 1:
            print('Paper beats rock so ')
            print('Computer wins!')
            more = input('Would you like to play again?(y for yes) :')
        elif cpu == 2 and u_num == 3:
            print('Scissors beats paper so ')
            print('Player wins!')
            more = input('Would you like to play again?(y for yes) :')
        elif cpu == 3 and u_num == 1:
            print('Rock beats scissors so ')
            print('Player wins!')
            more = input('Would you like to play again?(y for yes) :')
        elif cpu == 3 and u_num == 2:
            print('Scissors beats paper so ')
            print('Computer wins!')
            more = input('Would you like to play again?(y for yes) :')
        
        



