<!DOCTYPE html>
<html>
<head>
	<title>Currency Converter</title>
</head>
<body>
	<div id="json_resp"></div>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script>
	var html_resp,custom_resp,from_curr='{{f}}',to_curr='{{t}}';
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange=function(){
	if(xhttp.readyState==4 && xhttp.status==200){
		html_resp =  $(xhttp.responseText).find('#currency_converter_result')["0"].innerText.split(' '); 
		console.log(html_resp[0]+"="+html_resp[3]);
		custom_resp='{"data":[{"from":["'+from_curr+'","'+html_resp[0]+'"]},{"to":["'+to_curr+'","'+html_resp[3]+'"]}]}';
		document.getElementById("json_resp").innerHTML=custom_resp;
		}
	};
	xhttp.open("GET","https://www.google.com/finance/converter?a={{a}}&from={{f}}&to={{t}}",true);
	xhttp..setRequestHeader( 'Access-Control-Allow-Origin', '*');
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send();
	</script>
</body>
</html>