from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"]) # '/' flask import, all of these flask class may be considered as an object.. i think
def hello_world():
#these notes are for my own to use as a study guide in the future
    if request.method == "POST": #this is basically saying if our request.method.. flask exclusive method is a post which is my response, always a post response
        # print("HELLOOOOOOOOO", type(request)) #this is how I will get info on my proxy THIS is the post message
        user_input = request.form["input_text"] #request.form another flask excluseive.. means what it sounds
        # print(user_input)
        context = { #this is a very important specifc flask dictionary
            "user_input": user_input
        }
        print("done")
        return render_template("lab5.html", **context) #that template folder is extremely important to remeber to have, it a flask exclusive.. this is where your html/css templates go
    else:
        return render_template("lab5.html") #these returns are what you will see in the bash terminal or python which ever you use

@app.route('/goodbye', methods=["GET", "POST"]) #new route named.. make sure to place / BEFORE this is all required stuff refer back to docs
def goodbye_world():
    if request.method == "POST": 
        dictionary_2 = {'ft':0.3048 , 'mi':1609.34 , 'km':1000, 'm': 1} #I have created a dictionary with the conversions 
        distance = request.form["distance"]
        units = request.form["units"]
        ounits = request.form["ounits"]
        converts = (float(distance) * float(dictionary_2[units])) #this should convert the units to meters and then convert the appropraite output
        if ounits == 'ft':
            answer = converts * 1/.3048
        elif ounits == 'mi':
            answer = converts * 1/1609.34 #information that will convert
        elif ounits == 'km':
            answer = converts * 1/1000
        elif units == 'km' and ounits == 'm':
            answer = converts
        else:
            answer = distance
        print(f" {distance} {units} is {answer} {ounits}") #this print statment will show the results
        answer = f" {distance} {units} is {answer} {ounits}"
        
        context = {
            "answer": answer
        }
        return render_template("metric.html" , **context) 
    else:
        return render_template("metric.html")

app.run(debug=True)













#  I have created a list with 1 as the key and value 0.3058 as this is what we multiply
# user = input('What is the distance in feet: ') #input statment for user in feet
# base = dictionary['meters'] #I have created a variable with the key from my dictionary
# print(f'{user} ft is {int(user) * round(base, 4)} m') 

# dictionary_2 = {'ft':0.3048 , 'mi':1609.34 , 'km':1000, 'm': 1 } #I have created a dictionary with the conversions 
# distance = input('What is the distance?: ') # I have made a variable for user input for distance
# units = input('What are the units?: ') #I have made a variable for user input for units
# answer = dictionary_2.get(units, ) #This .GET method will check for keys and output the value
# print(f"{distance} {units} is {int(distance) * int(answer)} {units}")

# dictionary_2['yard'] = 0.9144 #This will add a value and key to my list
# dictionary_2['inch'] = 0.0254 
# print(dictionary_2)
