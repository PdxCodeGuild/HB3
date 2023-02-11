'''
    *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
         Project: Lab 5 - Intro to Flask
         Author: Scott Lefgren
         Email: scojlefg@gmail.com
         Date: January 9, 2023
   ___________________          _-_
   \==============_=_/ ____.---'---`---.____
               \_ \    \----._________.----/
                 \ \   /  /    `-_-'
             __,--`.`-'..'-_
            /____          ||
                 `--.____,-'
   
    *'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*'|<>|'*
   ''' 

from flask import Flask, request, render_template

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

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    
        text_string = request.form['input_text']
        cipher_string = ""
        for j in text_string:
            cipher_string += cipher_dict[j]
        # end for
    
        print(cipher_string + " is the cipher" )
    return render_template('lab05.html')

app.run(debug=True)