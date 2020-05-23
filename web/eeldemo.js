eel.expose(run);
async function run() {
  let return_value = await eel.flowfeedback()();
  console.log("Got this from python: " + return_value);
  var Watertype=return_value.split("#")[1];
  var Frr=return_value.split("#")[0];
  var Cscore=return_value.split("#")[2];
  $(".FlowRate").html(Watertype);
  $(".PerformanceIndex").html(Frr);
  $(".CreditScore").html(Cscore+"%");
  return (return_value);
}
run();
//var ct = 0;
/*while (ct !== 1000) {
  current = run();
  ct++;
}*/
