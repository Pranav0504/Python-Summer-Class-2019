
NUM_GRADES=4
total = 0

for grades in range (NUM_GRADES):
    grade = float(input('Enter in a grade: '))
    total = total + grade
print('Your average grade is' , round(total / NUM_GRADES,2))
