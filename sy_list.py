known_users = ["Alice", "Bob", "Claire", "Dan","Emma","Fred","Georgie","Harry"]

print(len(known_users))

while True:
    print("Hi, My name is Travis")
    name = input("What is your name?: ").strip().capitalize() # user prompt
    if name in known_users:
        print("Hello {} " .format(name))  # string concatenation
        user_ans = input("Would u like to be removed from system (y/n): ?").strip().lower()
        if  user_ans == 'y':
            print("Before", known_users)
            known_users.remove(name)   # remove method of list - removes 1st occurence only
            print("After", known_users)
        elif user_ans == 'n':
            print("No problem, I don't want you to leave anyway!")

        
    else:
        print("I don't think i have met you yet {} ".format(name))
        add_me = input("Would you like to be added to the system (y/n): ?").strip().lower()
        if add_me == "y":
            print("Before", known_users)
            known_users.append(name)   # append method of list 
            print("After", known_users)
        elif add_me == "n":
            print("No worries, see you around! ")

            
        
        
        
        
    
