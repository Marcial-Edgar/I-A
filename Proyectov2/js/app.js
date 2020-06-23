function runAjaxSend()
{
	console.log( "llamando a runAjaxSend " );
	
	var formData = { 
		"r1": $("#r1").val(), 
		"r2": $("#r2").val(), 
		"r3": $("#r3").val(), 
		"r4": $("#r4").val() };
		
	
	console.log( formData );
	
	$.ajax({		
		type: "POST",
		url: "http://localhost:8080/resultados",
		data: formData
	}).done(function (result) {
		console.log(result);
		
		var resultado = 
		'<table class="table table-condensed table-hover table-bordered">' +
		'<thead><tr><th>Usted puede postular a los cargos siguientes</th></tr></thead>' + 
		'<tbody>';
		
		
		if (result.R.length === 0) {
			resultado += '<tr><td>Sin resultados por ahora. Intente más adelante</td></tr>';
		}
		
		result.R.map(function(item){
			resultado += '<tr><td>'+item.G+'</td></tr>';
			});
		
		resultado += '<tbody>';
		resultado += '</table>';
		
		
		$( "#respuesta" ).slideDown("slow");
		$( "#result" ).html(resultado);
		$( "#result" ).slideDown("slow");
	}).fail (function (xhr) {
		console.log( "fail" , xhr);
	}).always (function (xhr) {
		console.log( "always" , xhr);
	});

}


$(document).ready(function(){
	
	$("#send").click(function(evt){
		evt.preventDefault();
		$( "#respuesta" ).hide();
		$( "#result" ).hide();
		
		$( "#enviando" ).slideDown( "slow" , function() {
			setTimeout(function(){
				$( "#enviando" ).slideUp( "slow", function(){
					runAjaxSend();
					} );
				}, 2000);
		  });				
		});	
	});
