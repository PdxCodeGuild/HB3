from flask import Flask, render_template, request
import string
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method=="GET":
        return render_template('indexv2.html')
 


letters = {
1 :'a',
2 :'b', 
3 :'c',
4 :'d', 
5 :'e', 
6 :'f', 
7 :'g', 
8 :'h', 
9 :'i', 
10 :'j', 
11 :'k', 
12 :'l', 
13 :'m', 
14 :'n', 
15 :'o', 
16 :'p', 
17 :'q', 
18 :'r', 
19 :'s', 
20 :'t', 
21 :'u', 
22 :'v',
23 :'w', 
24 :'x', 
25 :'y', 
26 :'z',
}

numbers = {
0 :'0',
1 :'1',
2 :'2', 
3 :'3',
4 :'4', 
5 :'5', 
6 :'6', 
7 :'7', 
8 :'8', 
9 :'9', 
}

punctuation = {
0 : '*',
1 :'.',
2 :'?', 
3 :'!',
4 :',', 
5 :';', 
6 :':', 
7 :'-', 
8 :'\'', 
9 :'"', 
}


@app.route('/result/', methods=["POST", "GET"])
def result():
    ans = []
    if request.method=="POST":
        text = request.form['input_text']
        rotation = request.form['rotation']
        num = int(rotation)
        for char in text:
            if char.isupper():
                char = char.lower()
            if char == " ":
                ans.append(" ")
            for key, value in punctuation.items():
                if char == value:
                    if key <= (10-num):
                        ans.append(punctuation[key + num])
                    else:
                        ans.append(punctuation[key + (num - 10)])
            for key, value in numbers.items():
                if char == value:
                    if key <= (10-num):
                        ans.append(numbers[key + num])
                    else:
                        ans.append(numbers[key + (num - 10)])
            for key, value in letters.items():
                if char == value:
                    if key <=(26-num):
                        ans.append(letters[key + num])
                    else:
                        ans.append(letters[key - num])
          
            
    new_text = ''.join(ans)
    return render_template('result.html', new_text=new_text)



if __name__ == "__main__":
    app.run(debug=True)