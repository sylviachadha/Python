films = {
    "movie1":[3,2],   # age, num of seats
    "movie2":[18,2],
    "movie3":[15,2],
    "movie4":[10,2]
    }

while True:
    choice = input("What film u want to watch?: ").strip()
    if choice in films:
        # cast to integer cz input function returns string
        age = int(input("How old are you: ? ").strip())

        # check user age
        if age > films[choice][0]:
            
            # check enough seats

            num_seats = films[choice][1] 
            if num_seats> 0:
                print("Enjoy the film! ")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out! ")
        else:
            print("You r too young to watch the film")
        
    else:
        print("We don't have that film....")
        
        
    
