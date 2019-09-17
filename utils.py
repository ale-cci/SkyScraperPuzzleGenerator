import random
from subprocess import call

def countTops(line: list, reverse:bool = False):
	if reverse:
		line = list(reversed(line))
	max = -1
	count = 0
	for i in line:
		if i > max:
			max = i
			count += 1
	return count
def bprint(board: list):
	for line in board:
		print(line)
def trasposta(board: list):
	t = [[] for i in range(len(board))]
	for line in board:
		for i, cell in enumerate(line):
			t[i].append(cell)
	return t

def plausible(board:list, line: list):
	for i, item in enumerate(line):
		for tLine in board:
			if tLine[i] == item:
				return False
	return True

def randCells(boardSize: int):
	randx = list(range(1, boardSize-1))
	randy = list(range(1, boardSize-1))
	random.shuffle(randx)
	random.shuffle(randy)
	for x in randx:
		for y in randy:
			yield(x, y)

	# Picking side values that will be removed
	sides = list(range(1, boardSize-1))
	pairs = []
	for i in sides:
		pairs += [(0, i), (boardSize-1, i), (i, 0), (i, boardSize-1)]
	random.shuffle(pairs)
	# pairs = pairs[:len(pairs)//3]
	for pair in pairs:
		yield pair

def nof_solutions(size: int, board: list, pos = (1, 1)):

	nextPos = next_position(pos, size)
	while board[pos[0]][pos[1]] != 0 and nextPos != (size+1, 1):
		pos = nextPos
		nextPos = next_position(pos, size)
	if nextPos == (size+1, 1):
		return 1

	solutions = 0
	possibleVals = possibleValues(size, board, pos) # !!!
	for value in possibleVals:
		board[pos[0]][pos[1]] = value
		if not checkCross(board, pos):
			continue
		solutions += nof_solutions(size, board, nextPos)
		if solutions > 1:
			return solutions
	board[pos[0]][pos[1]] = 0
	return solutions

def possibleValues(size:int, board:list, pos:(int, int)):
	pvals = list(range(1, size+1))
	for i in range(1, size+1):
		f, s = board[i][pos[1]], board[pos[0]][i]
		if f in pvals:
			pvals.remove(f)
		if s in pvals:
			pvals.remove(s)
	return pvals

def next_position(pos, size):
	if pos[1] == size:
		return (pos[0]+1, 1)
	else:
		return (pos[0], pos[1]+1)

def checkCross(board, pos):
	lines = [board[pos[0]], [l[pos[1]] for l in board]]
	for line in lines:
		if 0 in line:
			return True
		if line[0] != 0 and countTops(line[1:-1]) != line[0]:
			return False
		if line[-1] != 0 and countTops(list(reversed(line[1:-1]))) != line[-1]:
			return False
	return True

def saveOnFile(board: list, solution:list, fileName: str):

	with open(fileName, "w") as out:
		out.write(str(len(board)-2)+"\n")
		for line1, line2 in zip(solution, board):
			for cell1, cell2 in zip(line1, line2):
				out.write(str(cell1) + " "+ str(cell2)+ " ")
			out.write("\n")
	print("Successfully saved '{}'".format(fileName))
