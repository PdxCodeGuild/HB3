def scavenge():

    scavenge_level = input("How thoroughly would you like to search? (1- low; 2- medium; 3- high) ")
    while int(scavenge_level) not in range(1, 4):
        print("Invalid input, please try again")
        scavenge_level = input("How thoroughly would you like to search? (1- low; 2- medium; 3- high) ")
    return(scavenge_level)

def travel():

    destination = input("Enter grid coordinate of desired location (ex: A1, B4, etc")
    while destination not in locations:
        print("Please enter valid destination ")
    return destination