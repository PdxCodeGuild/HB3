let distance = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'm': 1,
    'yrd': 0.9144,
    'in': 0.0254
}

let btn = document.getElementById('btn');

btn.addEventListener('click', function () {
    let input = parseInt(document.getElementById('userInput').value);
    let from = document.getElementById('from_length')
    let from_input = from.options[from.selectedIndex].value;
    let to = document.getElementById('to_length')
    let to_input = to.options[to.selectedIndex].value;
    let result = document.getElementById('result');
    let value = input * distance[from_input] / distance[to_input];
    result.innerText = value;

})