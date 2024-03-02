rollnumber = []
ten = [''] * 1000000
english = [0]*1000000
math = [0]*1000000
physics = [0]*1000000
chemistry = [0]*1000000
cs = [0]*1000000

def menu():
    print('MAIN MENU')
    print('1. REPORT')
    print('2. ADMIN')
    print('3. EXIT')

def prof(value): 
    print('\nPUPIL DETAIL..')
    print('Roll number:', value)
    print('Name:', ten[value])
    print('English:',english[value])
    print('Math:', math[value])
    print('Physics:', physics[value])
    print('Chemistry:', chemistry[value])
    print('CS:', cs[value])

def create():
    print('\n\nCreate a profile')
    
    roll_number = int(input('Roll number: '))
    rollnumber.append(roll_number)
    
    name = str(input('Name: '))
    ten[roll_number] = name
    
    english_score = float(input('English: '))
    english[roll_number] = english_score
    
    maths = float(input('Maths: '))
    math[roll_number] = maths
           
    physics_score = float(input('Physics: '))
    physics[roll_number] = physics_score  
    
    chemistry_score = float(input('Chemistry: '))
    chemistry[roll_number] = chemistry_score
    
    cs_score = float(input('CS: '))
    cs[roll_number] = cs_score
    
    more = input('\nWants to enter more record (y/n)?:')

    if more == 'y':
        create()
    else:
        return

def display():
    if len(rollnumber) > 0:
        print('\nPUPIL DETAIL..')
        for number in rollnumber:
            print('\nRoll number:', number)
            print('Name:', ten[number])
            print('English:',english[number])
            print('Math:', math[number])
            print('Physics:', physics[number])
            print('Chemistry:', chemistry[number])
            print('CS:', cs[number])
    elif len(rollnumber) == 0:
        print('\nNO RECORD FOUND!')
        
def search():
    find_num = int(input('Enter the rollno you want to search: '))
    if find_num in rollnumber:
        prof(find_num)
    elif find_num not in rollnumber:
        print('\nRECORD NOT FOUND!')
    
def modify():
    print('\nMODIFY RECORD')
    find_modi = int(input('Enter roll number: '))
    if find_modi in rollnumber:
        print('Name: ', ten[find_modi])
        mod_yn = input('Wants to edit(y/n)?: ')
        if mod_yn == 'y':
            ten[find_modi] = input('Enter the name: ')
        
        print('English marks: ', english[find_modi])
        mod_yn = input('Wants to edit(y/n)?: ')
        if mod_yn == 'y':
            endlish[find_modi] = float(input('Enter english score: '))
    
        print('Maths marks: ', math[find_modi])
        mod_yn = input('Wants to edit(y/n)?: ')
        if mod_yn == 'y':
            math[find_modi] = float(input('Enter maths score: '))
    
        print('Physics marks: ', physics[find_modi])
        mod_yn = input('Wants to edit(y/n)?: ')
        if mod_yn == 'y':
            physics[find_modi] = float(input('Enter physics score: '))
    
        print('Chemistry marks: ', chemistry[find_modi])
        mod_yn = input('Wants to edit(y/n)?: ')
        if mod_yn == 'y':
            chemistry[find_modi] = float(input('Enter chemistry score: '))
    
        print('CS marks: ', cs[find_modi])
        mod_yn = input('Wants to edit(y/n)?: ')
        if mod_yn == 'y':
            cs[find_modi] = float(input('Enter CS score: '))
    
        prof(find_modi)
    
    elif find_modi not in rollnumber:
        print('\nRECORD NOT FOUND!')

def delete():
    print('\nDELETE RECORD:')
    find_del = int(input('Enter roll number: '))
    print()
    if find_del in rollnumber:
        prof(find_del)
        rollnumber.remove(find_del)
        print('record found and deleted')
    elif find_del not in rollnumber:
        print('\nRECORD NOT FOUND!')
    

def admin():
    print('ADMIN MENU')
    print('1. CREATE PUPIL RECORD')
    print('2. DISPLAY ALL PUPILS RECORDS')
    print('3. SEARCH PUPIL RECORD')
    print('4. MODIFY PUPIL RECORD')
    print('5. DELETE PUPIL RECORD')
    print('6. BACK TO MAIN MENU')
    
    choice_in_admin = int(input('Enter choice(1-6): '))
    return choice_in_admin

def report():
    print('REPORT MENU')
    print('1. CLASS RESULT')
    print('2. PUPIL RESULT')
    print('3. BACK TO MAIN MENU')
    choice_in_report = int(input('Enter choice(1-3): '))
    return choice_in_report

def class_report():
    if len(rollnumber) > 0:
        print('Rollno', ' ', ' ', 'Name', ' ', ' ', ' ', ' ', ' ', ' ', 'English', ' ', ' ', 'Maths', ' ', ' ', 'Physics', ' ', ' ', 'Chemistry', ' ', ' ', 'CS', ' ')
        for rollnum in rollnumber:
            print(rollnum, ' ', ' ', ' ', ' ', '', ten[rollnum], ' ', ' ',english[rollnum], ' ', ' ', ' ', ' ', '',math[rollnum], ' ', ' ', ' ', ' ', '', physics[rollnum], ' ', ' ', ' ', ' ', '', chemistry[rollnum], ' ', ' ', ' ', ' ', '', cs[rollnum], ' ', ' ', '\n')
    elif len(rollnumber) == 0:
        print('\nNO RECORD FOUND!')
  

menu()
option = str(input('Enter option: '))
while True:
    if option == '2':
        print('\nENTERING ADMIN...')
        print()
        choice_out_admin = admin()
        if choice_out_admin == 6:
            menu()
            option = str(input('Enter option: '))
                
        if choice_out_admin == 1:
            create()
            
        if choice_out_admin == 2:
            display()
        
        if choice_out_admin == 3:
            search()
        
        if choice_out_admin == 4:
            modify()
        
        if choice_out_admin == 5:
            delete()
            
    if option == '1':
        print('\nENTERING REPORT...')
        print()
        choice_out_report = report()
        if choice_out_report == 3:
            menu()
            option = str(input('Enter option: '))
        if choice_out_report == 2:
            search()
        if choice_out_report == 1:
            class_report()
    
    elif option == '3':
        break