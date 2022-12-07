#make list
card_num = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5]

# slice_card = (card_num[0:15])    #step 2: slicing
card_num.pop(-1)
# slice_card.reverse()             #step 3: reverse
card_num.reverse() 
new_card = card_num

# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.


# if x moduls 2 = 0 return list by index of x multiply by 2

# for x in range(len(new_card)):
#     if x % 2 == 0:
#         new_card[x] = new_card[x]*2
# print(x)


# Subtract
# def num(x):
#     if x in (10, 18, 16, 14,):
#         return x - 9
#     else:
#         return x

total = sum(new_card.pop[0])












# new_card = []
# for num in new_card:
#     new_card.append(slice_card)
    

# multiply = [1 * num for num in card_num]  #step 4: multiply each item in the list by 2

# subtraction = [n - 9 for n in multiply if multiply <= 9]


        
# print(new_card)
# subtraction = [n - 9 for n in card_num if card_num <= 9]
# print(subtraction)


