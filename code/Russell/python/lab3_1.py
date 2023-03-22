def cc_checker(card_number):

    #card_number = '4556737586899855'
    #card_number.split()
    # print(card_number)

    number_as_int = [int(x) for x in card_number]
    print((number_as_int))

    check_digit = number_as_int.pop(15)
    # print(check_digit)
    print(number_as_int)

    number_as_int.reverse()
    print(number_as_int)

    for index in range(len(number_as_int)):
        if index % 2 == 0:
            number_as_int[index] = number_as_int[index] * 2
        
    print(number_as_int)

    new_list = []

    for i in number_as_int:
        if i > 9:
            i = i - 9
            new_list.append(i)
        else:
            new_list.append(i)
        
    print(new_list)

    new_list = sum(new_list)

    print(new_list)

    if new_list % 10 == check_digit:
        return True
    
print(cc_checker('4556737586899855'))