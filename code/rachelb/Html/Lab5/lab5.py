from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def Converter():
    if request.method == 'POST':
        user_distance = request.form['distance']
        user_input = request.form['input']
        user_output = request.form['output']
        # print(user_distance + " " + user_input)
        # print(user_output)
    

        unit = {'feet':0.3048,
        'mile':1609.34, 
        'meter':1,
        'kilometer':1000}
        
        convert_to = int(user_distance) * unit[user_input]
        unit_convert = convert_to / unit[user_output]
        total = round(unit_convert,2)
        print(f"{user_distance} {user_input} is {total} {user_output}")
    return render_template('index.html')
    # return render_template

#----How to get input from html into the flask-----
    
app.run(debug=True)

