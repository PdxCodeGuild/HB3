let userOne = prompt('What is the distance: ')
let userTwo = prompt('What is the unit: ')

let distance = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'm': 1,
    'yrd': 0.9144,
    'in': 0.0254
}

console.log(userOne, userTwo, "is", distance[userTwo] * userOne, 'm')








