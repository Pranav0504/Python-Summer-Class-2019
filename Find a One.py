import random
grid = []
temporary = []
total = 0
win = False
for j in range(0,10):
     temporary.append(0)
     grid.append(temporary)


for k in range(0,10):
     r = random.randint(0,9)
     c = random.randint(0,9)
     grid[r][c] = 1

while win == False and total < 10:
    user_r = int(input('''
What row would you like to guess :'''))
    user_c = int(input('''
What column would you like to guess :'''))
    if grid[user_r][user_c] == 1:
         print('You got it!')
         total = 10
         win = True
    else:
          print('Try again')
    total += 1


         
         
    
