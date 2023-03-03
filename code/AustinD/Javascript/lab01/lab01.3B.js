<!DOCTYPE html>
<html>
<body>

<form>
  <label for="distance">Distance:</label>
  <input type="text" id="distance" name="distance">
  <br>
  <label for="start_unit">Unit being converted:</label>
  <input type="text" id="start_unit" name="start_unit">
  <br>
  <label for="end_unit">Unit being converted to:</label>
  <input type="text" id="end_unit" name="end_unit">
  <br>
  <br>
  <input type="button" value="Submit" onclick="convert()">
</form>

<div id="alert"></div>

<script>
const conversion = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yards' : 0.9144,
    'inches' : 0.0254
}

function convert() {
    let dist = parseFloat(document.getElementById("distance").value);
    let start_unit = document.getElementById("start_unit").value.toLowerCase();
    let end_unit = document.getElementById("end_unit").value.toLowerCase();
    let acceptable = Object.keys(conversion).join(', ');
    if (!conversion.hasOwnProperty(start_unit)) {
        document.getElementById("alert").innerHTML = `Not an accepted value, please select ${acceptable}`;
    }
    if (!conversion.hasOwnProperty(end_unit)) {
        document.getElementById("alert").innerHTML = `Not an accepted value, please select ${acceptable}`;
    } else {
        let measurement = conversion[start_unit];
        let target = conversion[end_unit];
        let converted = dist * measurement/target;
        document.getElementById("alert").innerHTML = `${dist} ${start_unit} is ${converted} ${end_unit}`;
    }
}

</script>
</body>
</html>
