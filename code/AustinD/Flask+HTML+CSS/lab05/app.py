from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)

conversion = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_unit = request.form['from']
    to_unit = request.form['to']
    value = int(request.form['value'])
    if from_unit == to_unit:
        return "Check your from & to values."
    if from_unit in conversion and to_unit in conversion:
        output = value * (conversion[from_unit] / conversion[to_unit])
        result = f'{value}{from_unit} is {output}{to_unit}.'
    else:
        return "Invalid unit(s) selected."
    
    return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run()