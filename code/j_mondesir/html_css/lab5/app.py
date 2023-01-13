from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/num/", methods=["POST"])
def generator():
    if request.method == 'POST':
        num = int(request.form['num'])
        letters = string.ascii_letters
        digit = string.digits
        punctuation = string.punctuation
        number = letters + digit + punctuation
        password = []
        while len(password) != num:
            password.append(random.choice(number))
            final = ''.join(password)
        return render_template('index.html', answer=final)


if __name__ == "__main__":

    app.run()
