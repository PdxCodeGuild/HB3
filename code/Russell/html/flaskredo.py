from flask import Flask, render_template, request
app = Flask(__name__)

# def index():
#     return render_template('test.html')


@app.route('/', methods=['GET', 'POST'])
def unit_conversion():
    if request.method == 'POST':
        distance = request.form['distance']
        c_from = request.form['c_from']
        c_to = request.form['c_to']

        conversion_dict = {
            'ft': 0.3048,
            'mi': 1609.34,
            'm': 1,
            'km': 1000,
            'yd': 0.9144,
            'in': 0.0254
        }

        distance_in = distance
        unit_in = c_from
        unit_out = c_to

        in_meters = int(distance_in) * conversion_dict[unit_in]
        distance_out = round(in_meters / conversion_dict[unit_out], 2)

        conversion = (f"{distance_in}{unit_in} is {distance_out}{unit_out} ")
        print(conversion)
        # return conversion

        return render_template('test.html', conversion=conversion)

    else:
        return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
