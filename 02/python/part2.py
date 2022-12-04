# A: Rock
# B: Paper
# C: Scissors

# X for losing
# Y for draw
# Z for winning

import numpy as np

game_matrix = np.array([
	[3, 4, 8],
	[1, 5, 9],
	[2, 6, 7]])

lookup = {'A':0, 'X':0, 'B':1, 'Y':1, 'C':2, 'Z':2}

total_points = 0

with open('input.txt') as file:
	for line in file.readlines():
		hands = line.split('\n')[0].split(' ')
		result = game_matrix[lookup[hands[0]], lookup[hands[1]]]
		total_points += result

		print(hands[0], hands[1], result, total_points)
