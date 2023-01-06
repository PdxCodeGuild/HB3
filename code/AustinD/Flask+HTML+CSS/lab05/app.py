from flask import Flask, request

app = Flask(__name__)

conversion = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

def convert_units(dist, start_unit):
    if start_unit not in conversion:
        return f'Not an accepted value, please select {acceptable}'
    else:
        measurement = (conversion[start_unit])
        converted = dist * measurement/(conversion['m'])
        return f'{dist} {start_unit} is {converted} meters.'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dist = int(request.form['dist'])
        start_unit = request.form['start_unit']
        result = convert_units(dist, start_unit)
        return result
    return '''
    <html>
    <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss/dist/tailwind.min.css">
    </head>
    <body class="bg-gray-100 h-screen flex items-center justify-center">
        <form method="POST" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
            <div class="mb-4">
                <label class="block text-blue-700 text-sm font-bold mb-2" for="dist">
                    Enter distance:
                </label>
                <input class="shadow appearance-none border rounded w-full py-2 px-3 text-green-700 leading-tight focus:outline-none focus:shadow-outline" id="dist" type="text" name="dist">
            </div>
            <div class="mb-6">
                <label class="block text-blue-700 text-sm font-bold mb-2" for="start_unit">
                    Enter unit:
                </label>
                <input class="shadow appearance-none border rounded w-full py-2 px-3 text-green-700 leading-tight focus:outline-none focus:shadow-outline" id="start_unit" type="text" name="start_unit" placeholder="ft, mi, m, km, yd, in">
            </div>
            <div class="flex items-center justify-between">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                    Convert
                </button>
            </div>
        </form>
    </body>
    </html>
'''

if __name__ == '__main__':
    app.run()
