from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form['input_text']
        rotate = int(request.form['rotate'])
        encoded = ''
        abcs = 'abcdefghijklmnopqrstuvwxyz'
        for char in word:
            if char.isalpha():
                encoded += abcs[(abcs.index(char) + rotate) % 26]
            else:
                encoded += char
        print(encoded)
        context = {'encoded': encoded}
        return render_template('index.html', **context)
    else:
        return render_template('index.html')

app.run(debug=True)