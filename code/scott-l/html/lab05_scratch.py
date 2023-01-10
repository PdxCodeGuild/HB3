'''
    *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
         Project: Lab 5 - Rot Cipher Scratch File
         Author: Scott Lefgren
         Email: scojlefg@gmail.com
         Date: January 5, 2023
   ___________________          _-_
   \==============_=_/ ____.---'---`---.____
               \_ \    \----._________.----/
                 \ \   /  /    `-_-'
             __,--`.`-'..'-_
            /____          ||
                 `--.____,-'
   
    *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
   ''' 

'''
   Write a program that prompts the user for a string, 
   and encodes it with ROT13. For each character, find 
   the corresponding character, add it to an output string. 
   Notice that there are 26 letters in the English language, 
   so encryption is the same as decryption.

'''

cipher_dict = {
    'a':'n', 'b':'o', 'c':'p','d':'q','e':'r', 
    'f':'s','g':'t','h':'u','i':'v', 'j':'w', 
    'k':'x', 'l':'y','m':'z','n':'a','o':'b',
    'p':'c','q':'d','r':'e','s':'f','t':'g',
    'u':'h','v':'h','w':'j','x':'k','y':'l','z':'m',' ':' ',
    'A':'N', 'B':'O', 'C':'P','D':'Q','E':'R', 
    'F':'S','G':'T','H':'U','I':'V', 'J':'W', 
    'K':'X', 'L':'Y','M':'Z','N':'A','O':'B',
    'P':'C','Q':'D','R':'E','S':'F','T':'G',
    'U':'H','V':'H','W':'J','X':'K','Y':'L','Z':'M'
}

text_string = input("Enter some words: ")

print(f' The length of the string is {len(text_string)} characters')

print(type(text_string))
print(text_string)

temp_ascii = list(text_string)

holder =[]
holder1  =[]
str1 = ""
for j in text_string:
    holder.append(ord(j))
    holder1.append(cipher_dict[j])
    str1 += cipher_dict[j]




print(holder)


print(temp_ascii)

print(holder1)
print(str1)



