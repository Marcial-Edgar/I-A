
import queue

escenario =[["#","#","#","O","#","#","#","#"],
			["#"," "," "," "," "," "," ","#"],
			["#"," ","#"," ","#","#"," ","#"],
			["#","B","#"," "," "," "," ","#"],
			["#"," ","#"," ","#","#"," ","#"],
			["#"," ","#","#","#","#"," ","#"],
			["#"," "," "," "," "," "," ","#"],
			["#","#","#","#","#","#","#","#"]]


def camino(escenario, path=""):
	for x, pos in enumerate(escenario[0]):
		if pos == "O":
			inicio = x
	x = inicio
	y = 0
	pos = set()
	for mov in path:
		if mov == "L":
			x -= 1
		elif mov == "R":
			x += 1
		elif mov == "U":
			y += 1
		elif mov == "D":
			y -= 1
		pos.add((y, x))

	for y, fila in enumerate(escenario):
		for x, col in enumerate(fila):
			if (y, x) in pos:
				print("+ ", end="")
			else:
				print(col + " ", end="")
		print()
def validar(escenario, movimientos):
	for x, pos in enumerate(escenario[0]):
		if pos == "O":
			inicio = x
	x = inicio
	y = 0
	for mov in movimientos:
		if mov == "L":
			x -= 1
		elif mov == "R":
			x += 1
		elif mov == "U":
			y += 1
		elif mov == "D":
			y -= 1
		if not(0 <= x < len(escenario[0]) and 0 <= y < len(escenario)):
			return False
		elif (escenario[y][x] == "#"):
			return False
	return True
def fin(escenario, movimientos):
	for x, pos in enumerate(escenario[0]):
		if pos == "O":
			start = x
	x = start
	y = 0
	for mov in movimientos:
		if mov == "L":
			x -= 1
		elif mov == "R":
			x += 1
		elif mov == "U":
			y += 1
		elif mov == "D":
			y -= 1
	if escenario[y][x] == "B":
		print("Camino a seguir " + movimientos)
		camino(escenario, movimientos)
		return True
	return False

x = queue.Queue()
x.put("")
add = ""

while not fin(escenario, add): 
	add = x.get()
	for j in ["L ", "R ", "U ", "D "]:
		put = add + j
		if validar(escenario, put):
			x.put(put)
