lista = [
	["A","B",1], ["B","A",1], ["A","Z",2], ["Z","A",2], ["Z","X",2],
	["X","Z",2], ["X","Y",2], ["Y","X",2], ["Y","W",1], ["W","Y",1],
	["W","R",1], ["R","W",1], ["R","T",2], ["T","R",2], ["T","Z",3],
	["Z","T",3], ["W","U",2], ["U","W",2], ["U","V",3], ["V","U",3],
	["V","H",3], ["H","V",3], ["H","I",1], ["I","H",1], ["G","H",2],
	["H","G",2], ["S","G",3], ["G","S",3], ["S","V",2], ["V","S",2],
	["R","S",1], ["S","R",1], ["S","E",4], ["E","S",4], ["F","E",2],
	["E","F",2], ["G","F",3], ["F","G",3], ["E","D",1], ["D","E",1],
	["C","D",2], ["D","C",2], ["C","B",1], ["B","C",1], ["D","B",2],
	["B","D",2]
]

from operator import itemgetter
import random

ruta = []
nodos = []
caminosPosibles = []
def buscar(inicio, fin):
		llegamos = 0
		anterior = ""
		iteracion = 1
		while (llegamos == 0):
				#for n in lista:
					#if n[0] == inicio and n[1] != anterior:
							#nodos.append(n)
				nodos = [n for n in lista if (n[0] == inicio and n[1] != anterior)]
				valorMenor = (min(nodos, key=itemgetter(2))[2])
				#for item in nodos:
					#if item[2] == valorMenor and item[1] != anterior:
							#caminosPosibles.append(item)
				caminosPosibles = [cp for cp in nodos if (cp[2] == valorMenor and cp[1] != anterior) ]
							#print(caminosPosibles)

				if (len(caminosPosibles) > 1):
						seguir = 0
						indice = random.randint(0, len(caminosPosibles) - 1 )
						cuentaPasos = 1
						while(seguir == 0):
								menor = caminosPosibles[indice]
								#evitar que el nodo siguiente haya pasado en la ruta, tanto como inicio, como termino
								if (len([item for item in ruta if item[1] == menor[1]]) == 0 and len([item for item in ruta if item[0] == menor[1]]) == 0 ):
										seguir = 1
								cuentaPasos += 1
								if (cuentaPasos > len(caminosPosibles)):
										seguir = 1
										llegamos = 1
										print ('*** No se ha podido llegar al objetivo, se entró un ciclo en la ruta ***')
				else:
						menor = caminosPosibles[0]
				ruta.append(menor)
				siguiente = menor[1]
				anterior = inicio
				
				if (siguiente == fin):
						llegamos = 1
				else:
						inicio = siguiente
				iteracion += 1
buscar("Z","I")
print ('llegamos en ', len(ruta), ' iteraciones ')
print ('usando la siguiente ruta ')
print (ruta)
