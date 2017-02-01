window.onload=GetResp();
	function GetResp(){
		var html_resp;
		var xhttp = new XMLHttpRequest();
		xhttp.onreadystatechange=function(){
			console.log(xhttp.responseText);
		};
		xhttp.open("GET","https://www.google.com/finance/converter?a=300&from=INR&to=AED",true);
		xhttp.send();
	}