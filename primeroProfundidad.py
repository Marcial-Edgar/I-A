"""
Cada funcion recibe la Carteta donde
empezara a buscar y el archivo a buscar

La funcion retorna True si encuentra 
el archivo, e imprime la ruta

en caso contrario retorna falso

def primeroProfundidad(Carpeta,Archivo):
	pass
def primeroAnchura(Carpeta,Archivo):
	pass
"""
import json
with open('base.json','r') as miarchivo:
	JSONDATA = json.load(miarchivo)

ini = input("Que carpeta quiere: ")
fin = input("Cual archivo busca: ")

ruta=[]
 
def buscar(Carpeta,Archivo):

	ruta.append(Carpeta)
 
	if Carpeta == Archivo:
		return Archivo
 
	for k,v in JSONDATA['Base'].items():
 
		if v == Carpeta:
 
			resultado = buscar(k,Archivo)
 
			if resultado:
				return resultado
 
	ruta.pop()

	return 0
 
result = buscar(ini,fin)

if result:
	print(ruta)
else:
	print("Ruta NO encontrada")
