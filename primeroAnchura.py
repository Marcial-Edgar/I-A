import json
with open('base.json','r') as miarchivo:
	JSONDATA = json.load(miarchivo)

ini = input("Que carpeta quiere: ")
fin = input("Cual archivo busca: ")


ruta=[]

fifo=[]
 
def primeroAnchura(Carpeta,Archivo,iteraciones):

	ruta.append(Carpeta)

	if Carpeta == Archivo:
		return (True,iteraciones)
 
	fifoAdd(Carpeta)
 
	if len(fifo) == 0:
		return (False,iteraciones)
 
	return primeroAnchura(fifo.pop(0),Archivo,iteraciones+1)
 
def fifoAdd(Carpeta):

	for k,v in JSONDATA['Base'].items():
		if v == Carpeta:
			fifo.append(k)
 
resultado,iteraciones = primeroAnchura(ini,fin,1)
if resultado:
	print("Archivo encontrado en {} iteraciones".format(iteraciones))
else:
	print("No se ha encontrado nada")
print("La ruta recorrida ha sido: {}".format(ruta))

