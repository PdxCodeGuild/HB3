feet_to_meters_dict = { '1 foot' : .3048  }

distance = input("What is the distance in feet? ") # ask for user input to determine distance
distance = int(distance) # convert the input to an integer

meters = (feet_to_meters_dict["1 foot"]) # call on the value for the key " 1 foot"

answer = (distance * meters) # multiply the distance by the key that was called on

print(f"{distance} feet is {answer} meters") # print the result
