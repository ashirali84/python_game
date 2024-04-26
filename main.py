import random
user1 = ['s','w','g']

def game(computer, user):

    if user in user1:
        pass
    else:
        exit("inviled options")
        
    if (computer == user):

        return None
    
    elif computer == 's':
        if user == 'w':
            return False
        elif user == 'g':
            return True
    elif computer == 'w':
        if user == 's':
            return True
        elif user == 'g':
            return False 
    elif computer == 'g':
        if user == 's':
            return False
        elif user == 'w':
            return True                  
print("computer tern: 1.Snake(s) 2.Water(w) or 3.Gun(g)?\n")
comTern = random.randint(1, 3)
if comTern == 1:
    computer = 's'
elif comTern == 2:
    computer = 'w'    
elif comTern == 3:
    computer = 'g'    

usr = input("user term: Snake(s) Water(w) or Gun(g)? ")
user =usr.lower()
a = game(computer, user)
if a == None:
    print("Both are seledting same things:")
elif a == True:
    print("you win")    
elif a == False:
    print("you loss") 
print("\t Computer selecting" , comTern)       



