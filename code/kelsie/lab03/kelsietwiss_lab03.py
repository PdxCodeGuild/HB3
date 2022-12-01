def verify(number) :

    int_list = [int(x) for x in str(number)]    # convert the input number into a list of integers
    short_list = int_list[:15:]            # slice off the last digit
    short_list.reverse()                         # reverse the list
    half_list = short_list[::2]               # seperate every other digit
    doubled_list = [2 * x for x in half_list]   # double the seperated digits
    

    small_list = []
    big_list = []
    
    # for each digit in the doubled_list that is larger than 9, subtract 9 from it and add the resulting digit to big_list
    # for each digit that is smaller then 9, add it to the small_list
    for x in doubled_list:                  
           if x > 9 :
            big_list.append(x-9)
    else :
         small_list.append(x)


    total = sum(small_list + big_list + (short_list[1::2])) # add small_list and big_list to the integers left from the speration of the half_list
    
    total_list = [int(x) for x in str(total)] # turn the individual digits of the total into a list of integers
  
    
    if int_list.pop(15) == total_list[1] :   # comparing the last digit of the total_list to the last digit of the entered credit card number
        print(True)
    else :
        print(False)                           # return boolean

verify(4556837586799855)