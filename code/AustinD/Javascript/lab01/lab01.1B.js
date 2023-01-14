<!DOCTYPE html>
<html>
<body>

<input type="text" id="cc-num">
<button onclick="creditcard()">Validate</button>
<div id="output_div"></div>

<script>
const double = x => x*2;
const subtract_9_if_over_9 = x => x > 9 ? x - 9 : x;
const creditcard = () => {
  let entry = document.getElementById("cc-num").value;
  const cc = entry.split("").map(Number);
  const check_digit = cc[cc.length - 1];
  let validation_digits = cc.slice().reverse();
  validation_digits.forEach((val, index) => {
    if (index % 2 === 0) validation_digits[index] = double(val);
  });
  validation_digits = validation_digits.map(subtract_9_if_over_9);
  validation_digits = validation_digits.reduce((a,b) => a + b);
  if (check_digit !== (validation_digits % 10)) {
    document.getElementById("output_div").innerHTML = "Invalid Credit Card";
  } else {
    document.getElementById("output_div").innerHTML = "Valid Credit Card";
  }
}
</script>

</body>
</html>
