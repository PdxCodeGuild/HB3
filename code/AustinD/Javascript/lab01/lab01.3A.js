<!DOCTYPE html>
<html>
<body>
<script>

const conversion = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yards' : 0.9144,
    'inches' : 0.0254
}

while (true) {
    let dist = parseFloat(prompt('what is the distance? '));
    let start_unit = prompt('What is the unit being converted? ').toLowerCase();
    let end_unit = prompt('What is the unit being converted to? ').toLowerCase();
    let acceptable = Object.keys(conversion).join(', ');
    if (!conversion.hasOwnProperty(start_unit)) {
        alert(`Not an accepted value, please select ${acceptable}`);
    }
    if (!conversion.hasOwnProperty(end_unit)) {
        alert(`Not an accepted value, please select ${acceptable}`);
    } else {
        let measurement = conversion[start_unit];
        let target = conversion[end_unit];
        let converted = dist * measurement/target;
        alert(`${dist} ${start_unit} is ${converted} ${end_unit}`);
        break;
    }
}


</script>
</body>
</html>