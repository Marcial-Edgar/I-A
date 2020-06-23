from bottle import route, run, template, request, response
from pyswip import Prolog

# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors
		
@route('/resultados', method='POST')
@enable_cors
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

