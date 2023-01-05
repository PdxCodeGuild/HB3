from flask import Flask, request, render_template
import string
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        shift_num = request.form['shift_num']
        print(f'The input text is: {input_text}; The shift is: {shift_num}')
        a_z = string.ascii_lowercase
        a_z_shifted = a_z[int(shift_num):] + a_z[:int(shift_num)]
        table = str.maketrans(a_z, a_z_shifted)
        print(f'The shifted string is: {input_text.translate(table)}')
    return render_template('index.html')

app.run(debug=True)