from flask import Flask, request, render_template
import string
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        shift_num = request.form['shift_num']
        print(input_text, shift_num)
    return render_template('index.html')

@app.route('/receive_form/', methods=['POST'])
def ROT26(input_text, shift_num):
    a_z = string.ascii_lowercase
    a_z_shifted = a_z[shift_num:] + a_z[:shift_num]
    table = str.maketrans(a_z, a_z_shifted)
    return input_text.translate(table)

app.run(debug=True)