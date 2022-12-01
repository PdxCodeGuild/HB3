
units_of_measurement = { # create a dictionary containing the unit conversions
"feet" : 0.3048 ,
"miles" : 1609.34 ,
"meters" : 1 ,
"kilometers" : 1000 ,
"yards" : 0.9144 ,
"inches" : 0.0254
}

distance = input("What is the distance? ") # get input of distance
convert_distance = (float(distance)) # convert input to float

input_unit = input("What is the input unit of measurement? ") # get input of unit of measurement

output_unit = input("What is the output unit of measurement? ") # get output unit of measurement

meters = (units_of_measurement[input_unit]) # access appropriate key value pair


meters_distance = meters * convert_distance # convert the input distance to meters


output = (units_of_measurement[output_unit]) # access key value pair for output units

answer = meters_distance / output # divide the meters_distance by the output unit

print(f"{distance} {input_unit} is equal to {answer} {output_unit}.") # print answer message

 