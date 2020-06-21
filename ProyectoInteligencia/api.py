from bottle import route, run, template, request
from pyswip import Prolog

@route('/ingreso')
def ingreso():
	return '''
		<h1>Postulaciones</h1>
		<hr>
		<form action="/resultados" method="post">
			<p>
            Indique su nivel de inglés:<br> 
				<select name="r1"> 
					<option value="">Seleccione</option>
					<option value="bajo">Bajo</option>
					<option value="medio">Medio</option>
					<option value="alto">Alto</option>
				</select>
            </p>
            <p>
            Indique su nivel de programación:<br> 
				<select name="r2">
					<option value="">Seleccione</option>
					<option value="bajo">Bajo</option>
					<option value="medio">Medio</option>
					<option value="alto">Alto</option>
				</select>
            </p>
            <p>
            Indique su preferencia de lenguaje de programación:<br> 
				<select name="r3">
					<option value="">Seleccione</option>
					<option value="java">Java</option>
					<option value="csharp">C# .NET</option>
					<option value="php">PHP</option>
					<option value="python">Python</option>
					<option value="javascript">Javascript</option>
					<option value="sql">SQL</option>
					<option value="shell">Shell</option>
				</select>
			</p>
			<p>
            Tiene disponibilidad para trabajar en turnos día/noche: <br>
				<select name="r4">
					<option value="">Seleccione</option>
					<option value="si">Sí</option>
					<option value="no">No</option>
				</select>
            </p>
            <input value="Ver resultados" type="submit" />
        </form>
	''' 

@route('/resultados', method='POST')
def do_resultados():
	r1 = request.forms.get('r1')
	r2 = request.forms.get('r2')
	r3 = request.forms.get('r3')
	r4 = request.forms.get('r4')
	#aplicar verificacion de contenido, y en caso que no venga un dato
	#incluir el comodin de prolog _
	if not r1:
		r1 = "_"
	if not r2:
		r2 = "_"
	if not r3:
		r3 = "_"
	if not r4:
		r4 = "_"
	
	prolog = Prolog()
	prolog.consult("reglas.pl")	
	g = prolog.query("reglas("+r1+","+r2+","+r3+","+r4+",G)")
	L = list(g)
	return {"R": L}    
	
run(host='localhost', port=8080)

