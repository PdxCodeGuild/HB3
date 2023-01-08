from flask import Flask, render_template, request
app = Flask(__name__)



letters =['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method=="GET":
        return render_template('index.html')




@app.route('/result/', methods=["POST", "GET"])
def result():
    new_text = []
    if request.method=="POST":
        text = request.form['input_text']
        for index, char in enumerate(letters):
            if char in list(text):
                print(index, char)
                if index < 13:
                    new_char = letters[index + 13]
                    new_text.append(new_char)
                elif index >12 :
                    new_char = letters[index-13]
                    new_text.append(new_char)
    return render_template('result.html', new_text=new_text)



if __name__ == "__main__":
    app.run(debug=True)








