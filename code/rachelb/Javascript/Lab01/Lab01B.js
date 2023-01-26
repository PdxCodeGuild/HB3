let validation = document.querySelector('#validate');
let run_cc = document.querySelector('#run_cc');
let output_cc = document.querySelector('#output_cc');
run_bt.onclick = function() {
  let name = name_input.value;
  cardvalidation;
  output_div.innerText = 'Heres ' + name + '!';
  
}




let converter = document.querySelector('#converter');
let run_bt = document.querySelector('#run_convert');
let output_div = document.querySelector('#output_convert');
run_bt.onclick = function() {
  let name = converter.value;
  alert(name);
  output_div.innerText = 'You converted' + name + '!';
}
