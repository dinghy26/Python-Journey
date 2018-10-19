film = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
}

while True:
    choice = input("Hello what movie you like to watch? ").strip().title()

    if choice in film:
        age = int(input("How older are you? ").strip())

        #Check user age
        
        if age >= film[choice][0]:
            # check count of tickets

            if film[choice][1]>0:
                print("enjoy the movie")
                film[choice][1] = film[choice][1]-1

            else:
                print("sorry no more tikets")


        else:
            print("you are to young to see that film")   



    else:
        print("We dont have that film...")


