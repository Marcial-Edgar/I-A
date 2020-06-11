import copy

tablero = [ [ 1, 0, 1], 
			[ 0, 0, 0], 
			[ 2, 0, 2] 
					] 
for i in range(3):
	for j in range (3):
		print(tablero[i][j], end= ' ')
	print()	
print()

x = copy.deepcopy(tablero)

for a in range(4):
		
	if tablero[0][0] != 0:
		x[1][2]=copy.deepcopy(tablero[0][0])
		x[0][0]=copy.deepcopy(tablero[1][2])
		
	if tablero[0][1] != 0:
		x[2][2]=copy.deepcopy(tablero[0][1])
		x[0][1]=copy.deepcopy(tablero[2][2])

	if tablero[0][2] != 0:
		x[2][1]=copy.deepcopy(tablero[0][2])
		x[0][2]=copy.deepcopy(tablero[2][1])
				
	if tablero[1][0] != 0:
		x[0][2]=copy.deepcopy(tablero[1][0])
		x[1][0]=copy.deepcopy(tablero[0][2])
		
	if tablero[1][2] != 0:
		x[2][0]=copy.deepcopy(tablero[1][2])
		x[1][2]=copy.deepcopy(tablero[2][0])

	if tablero[2][0] != 0:
		x[0][1]=copy.deepcopy(tablero[2][0])
		x[2][0]=copy.deepcopy(tablero[1][2])

	if tablero[2][1] != 0:
		x[0][0]=copy.deepcopy(tablero[2][1])
		x[2][1]=copy.deepcopy(tablero[0][0])
								
	if tablero[2][2] != 0:
		x[1][0]=copy.deepcopy(tablero[2][2])
		x[2][2]=copy.deepcopy(tablero[1][0])
		
	tablero = copy.deepcopy(x)
		
	for i in range(3):
		for j in range (3):
			print(x[i][j], end= ' ')
		print()
	print()

