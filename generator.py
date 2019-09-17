#!/usr/bin/env python3
import random
from utils import *
from subprocess import call


levels = str(input("Insert the number of levels for each puzzle: ")).split(" ")

for dim, nof_puzzle in enumerate(levels):
	nof_puzzle = int(nof_puzzle)
	size = dim + 3
	boardCells = size + 2

	for id in range(nof_puzzle):
		# Random Generating a new Board
		board = []
		for i in range(size):
			currentLine = list(range(1, size+1))
			random.shuffle(currentLine)
			while not plausible(board, currentLine):
				random.shuffle(currentLine)
			board.append(currentLine)
		tboard = trasposta(board)
		new_board = [[0] + [countTops(line) for line in tboard] + [0]]
		for line in board:
			new_board += [[countTops(line)] + line + [countTops(line, True)]]
		new_board += [[0] + [countTops(line, True) for line in tboard] + [0]]

		# Removing Values from the board
		solution = [l[:] for l in new_board]
		for x, y in randCells(boardCells):
			tmp = new_board[y][x]
			new_board[y][x] = 0
			if nof_solutions(size, [l[:] for l in new_board]) != 1:
				new_board[y][x] = tmp

		# Wrinting data on file
		fname = "p%d%03d" % (size-3, id)

		# bprint(solution)
		bprint(new_board)

		saveOnFile(new_board, solution, "PUZZLE/%s.puzzle" % fname)

		# compressing file in .pzl
		call("./compress PUZZLE/{0}.puzzle PZL/{0}.pzl".format(fname), shell=True)
