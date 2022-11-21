# Number To Phrase

print('\nWelcome To Number To Phrase Version 2')
print('Lets converts some numbers!!!!!!!\n')

ones_digit = [
    "",
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


num_enter = int(input('Please enter a number from(1-999):\n'))

# checking if the numbers entered by the user  is the list or not
if num_enter > 999:
    print(f"The number entered {num_enter} can't be convert please enter a number from (1- 999):")

else:
    value = [0, 0, 0,]
    num_phrase = 0
    while num_enter > 0:
        value[num_phrase] = num_enter % 10
        num_phrase += 1
        num_enter //= 10

    results = ""
    if value[2]!= 0:
        results += ones_digit[value[2]] + " Hundred "

    if value[1] !=0:
        if value[1]== 1:
            results += tens_digit[value[0]]

        else:
            results += phrase_prefix[value[1]] + " " +ones_digit[value[0]]

    

    print(results)





       