let conversion_dict = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

let distance_in = prompt("Enter distance ")
let unit_in = prompt("Enter unit to convert from (ft, mi, m, km, yd, in) ")
let unit_out = prompt("Enter unit to convert to (ft, mi, m, km, yd, in) ")

let in_meters = parseInt(distance_in) * conversion_dict[unit_in]
let distance_out = in_meters / conversion_dict[unit_out]
let rounded = distance_out.toFixed(2)

alert(distance_in + unit_in + " is " + rounded + unit_out)