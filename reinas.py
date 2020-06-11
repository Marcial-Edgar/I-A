global N 
N = 4 ## N es igual a 4 reinas

##imprimir el talero de la matriz con la solucion
def imprimeSolucion(Tablero): 
	for i in range(N): 
		for j in range(N): 
			print (Tablero[i][j], end = ' ') 
		print()

##Funcion de utilidad para verificar si una reina se puede colocar
def seguridad(Tablero, fila, columna): 

	for i in range(columna): 
		if Tablero[fila][i] == 1: 
			return False
	for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)): 
		if Tablero[i][j] == 1: 
			return False
	for i, j in zip(range(fila, N, 1), range(columna, -1, -1)): 
		if Tablero[i][j] == 1: 
			return False
	return True


def resolverNreinas(Tablero, columna): 
	if columna >= N: 
		return True
	for i in range(N): 
		if seguridad(Tablero, i, columna): 
			Tablero[i][columna] = 1
			if resolverNreinas(Tablero, columna + 1) == True: 
				return True
			Tablero[i][columna] = 0
	return False

def resuelveNQ(): 
	Tablero = [ [0, 0, 0, 0], 
				[0, 0, 0, 0], 
				[0, 0, 0, 0], 
				[0, 0, 0, 0] 
			] 

	if resolverNreinas(Tablero, 0) == False: 
		print ("La solucion no existe")
		return False

	imprimeSolucion(Tablero) 
	return True

resuelveNQ() 
