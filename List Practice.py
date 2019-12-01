m_list = ['Batman', 'Avengers', 'Alladin', 'Frozen', 'Toy Story']
print(m_list)
print('Option 1 : Reset List')
print('Option 2 : View List')
print('Option 3 : View One Item')
print('Option 4 : Edit List')
print('Option 5 : Add to List')
print('Option 6 : Quit')
user = 0
while user != 6:
    user = int(input('What would you like to do?(enter in the number of the option) :'))
    if user is not(range(1,7)):
        print('Your number is invalid, try again')
    elif user ==1:
        m_list = []
    elif user==2:
        print(m_list)
    elif user==3:
        s_num = int(input('What movie number would you like to view :'))
        print(m_list[s_num])
    elif user == 4:
        edit = int(input('What movie would you like to replace?(enter the number) :'))
        m_list[edit] = input('What movie do you want to replace it with? :')
    elif user == 5:
        add = input('What movie would you like to add :')
        m_list.append(add)
print('Done')



        
        
        
        
        
