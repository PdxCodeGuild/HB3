

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        contact_name = request.form['input_text']
    
        print(contact_name + " say's hello world" )
    return render_template('lab05.html')

app.run(debug=True)