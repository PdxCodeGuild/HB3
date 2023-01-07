from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)



letters =['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_text = []

@app.route('/result/', methods=['GET' , 'POST'])
def encrypt():
    text = request.args.get('input_text')
    for index in range(len(letters)):
        char = letters[index]
        if char in list(text):
            if index < 13:
                char = letters[index + 13]
                new_text.append(char)
            elif index >12 :
                char = letters[index-13]
                new_text.append(char)
    return render_template('result.html')
