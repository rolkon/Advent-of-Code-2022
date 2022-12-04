# Part 1:
# A, X: Rock
# B, Y: Paper
# C, Z: Scissors

# Part 2:
# A: Rock
# B: Paper
# C: Scissors

# X for losing
# Y for draw
# Z for winning

# Rock: 	1 point
# Paper:	2 points
# Scissors:	3 points
# Losing:	0 points
# Draw:		3 points
# Winning:	6 points

import numpy as np

part1_matrix = np.array([
	[4, 8, 3],
	[1, 5, 9],
	[7, 2, 6]])

part2_matrix = np.array([
	[3, 4, 8],
	[1, 5, 9],
	[2, 6, 7]])

lookup = {'A':0, 'X':0, 'B':1, 'Y':1, 'C':2, 'Z':2}

total_points_part1 = 0
total_points_part2 = 0

with open('../input.txt') as file:
	strategy_list = file.read().split('\n')

	for strategy in strategy_list:
		hands = strategy.split(' ')
		total_points_part1 += part1_matrix[lookup[hands[0]], lookup[hands[1]]]
		total_points_part2 += part2_matrix[lookup[hands[0]], lookup[hands[1]]]

	print("Part 1 result: ", total_points_part1)
	print("Part 2 result: ", total_points_part2)