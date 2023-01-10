from flask import Flask, render_template, redirect, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/next', methods=['GET', 'POST'])
def next():
    amount = int(request.form['amount'])
    user_input = request.form['units_in']
    end_units = request.form['units_out']
    
    units_in = {
    "feet": .3048,
    "miles": 1609.34,
    "meters": 1,
    "kilometers": 1000,
    "yards": 0.9144,
    "inches": 0.0254
    }
    
    units_out = {
    "feet": 1/.3048,
    "miles": 1/1609.34,
    "meters": 1,
    "kilometers": 1/1000,
    "yards": 1/.9144,
    "inches": 1/.0254
    }
    
    input_switch = units_in[user_input]

    output_switch = units_out[end_units]

    input_conversion = amount * input_switch

    final_switch = input_conversion * output_switch
    
    
    context = {
        "num_1": amount,
        "units_in": user_input,
        "end_units": end_units,
        "num_2": final_switch
    }
    return render_template("other.html", **context)


app.run(debug=True)

if __name__ == '__main__':
    app.run()
