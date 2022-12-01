# Number To Romans Number

print('\nWelcome To Number To Romans Numbers Version 3')
print('Lets converts some numbers!!!!!!!\n')

while True:
    num_enter = int(input('Please enter a number (1-1000) or enter 0 to quit:\n'))

    if num_enter == 0:
        print("Goodby and thank you for using this app.!!!!")
        break
    
    def int_romans_n(x):

        nums_digit = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

        romans_figs = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']

        i = 12

        roman_numerals = ''

        while x != 0:
            if nums_digit[i] <= x:
                roman_numerals += romans_figs[i]
                x -= nums_digit[i]

            else:
                i -= 1
        return roman_numerals
    print(int_romans_n(num_enter))



    







