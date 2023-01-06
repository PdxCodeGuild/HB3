from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/result/', methods=['GET' , 'POST'])
def encrypt():
    if request.method =='POST':
        text = request.form['input_text']
        text = list(text)
        for char, x in enumerate(text):
            if char[x] <12:
                new_text.append(letters[x + 13])
            elif char[x] >=12:
                new_text.append(letters[x - 13])
            return new_text
            

if __name__ == "__main__":
    app.run(debug=True)



letters =['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

new_text = []



