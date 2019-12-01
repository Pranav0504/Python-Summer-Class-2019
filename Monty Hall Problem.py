import random
play_again = 'Y'
while play_again == 'Y' or play_again == 'y':
    
    winner=random.randint(1,3)
    print('''Hello and welcome to a famous gameshow and problem called the Monty
    Hall Problem.''')
    print('''In front of you, you have 3 doors. Behind 2 of them are a goat and
    behind the other door is your dream car.''')
    
    player_choice=int(input('Please select the number of a door (enter 1,2, or 3):'))
    open_door = 0 # records the number of the door will be opened
    switch_door = 0 # the number of the door if the player choose to switch
 
    ## OPEN A DOOR WITH A GOAT
 
    ## if the player chose a door with a goat,
    ## open the other door with the goat
    ## but first, set the possible switch door to winner
    ## since we will choose the other door to open
    if player_choice != winner:
        switch_door = winner
        #write the if statements to open the other door
        if player_choice == 1:
            if winner == 3:
                open_door = 2
        if player_choice == 1:
            if winner == 2:
                open_door = 3
        if player_choice == 2:
            if winner == 1:
                open_door = 3
        if player_choice == 2:
            if winner == 3:
                open_door = 1
        if player_choice == 3:
            if winner == 1:
                open_door=2
        if player_choice == 3:
            if winner == 2:
                open_door=1
     

   
 
    ## if the player chose the door with the car,
    ## open one of the other two doors, each having a goat
    ## choose a random one (each with probability ½)
    ## use random.randrange(1,4,2) to get either door 1 or 3
    ## use random.randint(1,2) to select either door 1 or 2
    ## use random.randint(2,3) to select either door 2 or 3
    else:
        if player_choice == 1:
            open_door = 3
            switch_door= 3
        if player_choice == 2:
            open_door = 1
            switch_door=3
        if player_choice == 3:
            open_door = 2
            switch_door=1
    
    
 
    print('Door', open_door, 'is opened and there is a goat behind it.')
    print('Do you want to switch?')
    print('Y for Yes, I want to switch')
    print('N for No, I don’t want to switch')
    want_switch = input()
    if want_switch == 'Y':
        player_choice = switch_door         #switch to the other door
 
    if player_choice == winner:
        print('Congratulations! You win the car!')
        play_again = input('Would you like to play again?(Y for yes)')
    else:
        print('You win a goat!')
        play_again = input('Would you like to play again?(Y for yes)')

print('Thanks for playing!')
        
        
        
    
