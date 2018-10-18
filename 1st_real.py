known_users = ["Alice", "Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi! My Name is travis")
    
    Name = input("what is your name?: ").strip().capitalize()
    
    if Name in known_users:
        print ("Hello {}!".format(Name))
        remove = input("Would you like to be removed? (y/n)").strip().lower()
        
        if remove == "y":
            known_users.remove(Name)
        elif remove == "n":
            print("ok")
        
    else:
        print("hmmm i don't think i have met you yet {}".format(Name))
        add = input("Would you like to be add to the list? (y/n)").strip().lower()
        
        if add == "y":
            known_users.append(Name)
            
        elif add == "n":
            print("ok, goodbye")
        

    





