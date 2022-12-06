Credit_Card_Number = input() #Lines 1 - 2 will recieve user input and insert them under a list assigned to Credit Card Variable
Credit_Card = [int(x) for x in Credit_Card_Number]
print(Credit_Card) 
Check_Digit = Credit_Card.pop()
print(Credit_Card[: 15 : ]) 
Credit_Card.reverse()
print(Credit_Card) #This will print the digits in reverse order 
Card_Numbers_Doubled = Credit_Card #I have copied my list into a new variable
Card_Numbers_Doubled[: : 2] = [int(x *2) for x in Credit_Card[ : :2]] #This doubles every other element within the new list and only applies to every other number 
print(Card_Numbers_Doubled)
Card_Numbers_With_Subtraction=[] #Similar to line 7, I will assign the revised list to a new varaible
for x in Card_Numbers_Doubled:
    if int(x) > 9:
        Card_Numbers_With_Subtraction.append(x-9)
    else: #lines 12 - 13 will subtract any digit over 9 as lines 14 - 15 will simply append to the new list if digit is less than 9
        Card_Numbers_With_Subtraction.append(x)
print(Card_Numbers_With_Subtraction) #This will print the new list
Sum_Of_Numbers = sum(Card_Numbers_With_Subtraction)
print(Sum_Of_Numbers) #this will print the sum of numbers in the list
Match_Digit = Sum_Of_Numbers % 10 #This modulus 10 will isolate the last digit
print(Match_Digit) #This will print the digit that is to match with the check digit
if Match_Digit == Check_Digit: #This line will compare to match digit and check digit
    print("Valid!")
else:
    print("Not Valid")