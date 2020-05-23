const url='http://127.0.0.1:5000/get_chain';
$('.btn').click(function(){
  $.getJSON(url,function(result){
    var lengthofchain=result.length;
    var chainVariables=result.chain;
    //console.log(chainVariables[1].message);
    //console.log(chainVariables[1].message.split("#"));
    for(var i=lengthofchain-3;i<lengthofchain;i++)
    {
      for(var j=1;j<=4;j++)
      { var inc=lengthofchain-i;
        switch (j) {
            case 1:
            $(".R"+inc+"C1").html(chainVariables[i].message.split("#")[1]);
            break;
            case 2:
            $(".R"+inc+"C2").html(chainVariables[i].message.split("#")[2]);
            break;
            case 3:
            $(".R"+inc+"C3").html(chainVariables[i].message.split("#")[3]);
            break;
            case 4:
            $(".R"+inc+"C4").html(chainVariables[i].timestamp);
            break;
          default:
          alert("Something is fishy! Check console or retry to setup");

        }
        //$(".R"+i+"C"+j).html("Text");
      }
    }
    //console.log(result.chain[0].message)
  });
})
