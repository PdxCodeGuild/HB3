from flask import Flask, render_template, request
from string import  ascii_letters as ABCs 


app = Flask(__name__)

@app.route('/')
def index():


    return render_template('index.html')


@app.route('/rotC', methods=["POST"])
def rot_cipher():

   user_input = request.form.get('user-input')
   shift_number = request.form.get('rotation')

#    converting string to an integer
   new_shift_num = int(shift_number)

   
   cipher_text =""
   for char in user_input:
      if char.isalpha():
        position = ABCs.index(char)
        new_position = (position + new_shift_num) % 26

        cipher_text += ABCs[new_position]
    

      else:
          cipher_text += char

     

      context = {

        'cipher_text': cipher_text
        
        }


   return render_template('rotC.html', context=context)