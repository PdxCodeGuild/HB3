# Number To Phrase

print('\nWelcome To Number To Phrase Version 2')
print('Lets converts some numbers!!!!!!!\n')

ones_digit = [
    "Zero",
    "One",
    "Two",
    "Three",
    "Four", 
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    ]

tens_digit = [
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
 ]

phrase_prefix = [
    "",
    "",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
] 

while True:
    num_enter = int(input('Please enter a number from(1-999):\n'))

    # checking if the numbers entered by the user  is the list or not
    if num_enter > 999:
        print(f"The number entered {num_enter} can't be convert:")

# checking ones digit numbers
    elif num_enter < 10:
        results = ones_digit[num_enter]

# checking tens digits numbers
    elif num_enter >= 10 and num_enter <= 19:
        results = tens_digit[num_enter%10]

# checking three digits numbers
    else:
        value = [0, 0, 0,]
        num_phrase = 0
        while num_enter > 0:
            value[num_phrase] = num_enter % 10
            num_phrase += 1
            num_enter //= 10

        results = ""
        if value[2]!= 0:
            if value[1]== 0:
                if value[0] ==0:
                    results += ones_digit[value[2]] + " " + "Hundred " 
                elif value[0] != 0:
                    results += ones_digit[value[2]] + " " + "Hundred " + ones_digit[value[0]]


            else:
                results += ones_digit[value[2]] + " Hundred "

        if value[1] !=0:
            if value[1]== 1:
                results += tens_digit[value[0]]

            else:
                if value[0]==0:
                    results += phrase_prefix[value[1]]
                else:
                    results += phrase_prefix[value[1]] + "-" + ones_digit[value[0]]

    print(results)
       
        


# num_phrase = {
#     0:"zero",
#     1:"one",
#     2:"two",
#     3:"three",
#     4:"four",
#     5:"five",
#     6:"six",
#     7:"seven",
#     8:"eight",
#     9:"nine",
#     10:"ten",
#     11:"eleven",
#     12:"twelve",
#     13:"thirteen",
#     14:"fourteen",
#     15:"fifteen",
#     16:"sixteen",
#     17:"seventeen",
#     18:"eighteen",
#     19:"nineteen",
#     20:"twenty",
#     40:"forty",
#     30:"thirty",
#     50:"fifty",
#     60:"sixty",
#     70:"seventy",
#     80:"eighty",
#     90:"ninety",
#     100:"Hundred", 

# }

# while True:
#     num_enter = int(input('Please enter a number from(1-100):\n'))

#     # Trying to address the numbers that in & not in the dictionary
#     if num_enter < 1000:        
#         if num_enter in num_phrase:
#             value = num_phrase.get(num_enter)
#             print(f"Your number {num_enter} and in word is ({value})\n")

#     # To address bigger odd numbers like (35, 45,65,75 etc.)
#         elif num_enter > 20 and num_enter < 100:
#             ones_digit_num = num_enter % 10
#             ones_digit_num = num_phrase.get(ones_digit_num)
#             tens_digit_num = num_enter // 10
#             tens_digit_num *= 10
#             tens_digit_num = num_phrase.get(tens_digit_num)


#             result = tens_digit_num + "-" + ones_digit_num

#             print(f"Your number {num_enter} and in word is ({result})\n")

#         elif num_enter > 120 and num_enter < 1000:
#             ones_digit_num = num_enter % 100
#             ones_digit_num = num_phrase.get(ones_digit_num)

#             tens_digit_num = num_enter // 100
#             tens_digit_num *= 100
#             tens_digit_num = num_phrase.get(tens_digit_num)
#             result = tens_digit_num + "-" + ones_digit_num

#             print(f"Your number {num_enter} and in word is ({result})\n")

#     else:
#         print(f"Your number {num_enter} is invalid number please enter a number from (0-100)\n")
#         break







       