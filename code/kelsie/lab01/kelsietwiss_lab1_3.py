
units_of_measurement = { # create a dictionary containing the unit conversions
"feet" : 0.3048 ,
"miles" : 1609.34 ,
"meters" : 1 ,
"kilometers" : 1000 ,
"yards" : 0.9144 ,
"inches" : 0.0254
}

distance = input("What is the distance? ") # get input of distance
convert = (float(distance)) # convert input to float

unit = input("What is the unit of measurement? ") # get input of unit of measurement

meters = (units_of_measurement[unit]) # access the appropriate key value pair

answer = convert * meters # find the answer by multiplying the converted distance with the meter conversion

print(f"{distance} in {unit} is equal to {answer} meters.") # print the answer message