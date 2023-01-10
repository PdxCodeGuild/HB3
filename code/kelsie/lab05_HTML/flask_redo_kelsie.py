from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method=="GET":
        return render_template('index.html')
 


@app.route('/result/', methods=["POST", "GET"])
def result():
    n = 13
    new_text = ""
    if request.method=="POST":
        text = request.form['input_text']
        for i in range(len(text)):
            char = text[i]
            if char==" ":
                new_text += " "
            else:
                new_text += chr((ord(char) + n-97) % 26 + 97)
    return render_template('result.html', new_text=new_text)



if __name__ == "__main__":
    app.run(debug=True)




