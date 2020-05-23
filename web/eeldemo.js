eel.expose(run);

function my_javascript_function(a, b) {
  console.log(a + b);
}

async function run() {
  let return_value = await eel.flowfeedback()();
  console.log("Got2 this from python: " + return_value);
  $(".FlowRate").html(return_value);
  return (return_value);
}
var ct = 0;
while (ct !== 1000) {
  current = run();
  ct++;
}
