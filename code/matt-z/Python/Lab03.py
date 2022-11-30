def validate(num):
    cc_nums = [int(i) for i in num]
    return cc_nums

cc = input("What's the credit card number? ")

cc_num = validate(cc)

#print(cc_num)

check_digit = cc_num.pop()
cc_num.reverse()

#print(cc_num)

def double(lst):
    result = list(lst)
    for i in range(len(result)):
        if i % 2 == 0:
            result[i] = result[i]*2
    return result

new_list = double(cc_num)

subtract_9 = [i-9 if i > 9 else i for i in new_list]

#print(subtract_9)
 
credit_sum = sum(subtract_9)

#print(credit_sum)

calc_check_digit = str(credit_sum)[1]

if check_digit == int(calc_check_digit):
    print('Valid!')