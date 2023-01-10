from flask import Flask, render_template, request
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

@app.route('/result/', methods=["POST", "GET"])
def result():
    ans = []
    if request.method=="POST":
        text = request.form['input_text']
        for char in text:
            if char == " ":
                ans.append(" ")
            for key, value in letters.items():
                if char == value:
                    if key <=13:
                        ans.append(letters[key + 13])
                    else:
                        ans.append(letters[key - 13])
    new_text = ''.join(ans)
    return render_template('result.html', new_text=new_text)



if __name__ == "__main__":
    app.run(debug=True)
