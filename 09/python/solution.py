import numpy as np

ul = [-1, -1]
up = [-1,  0]
ur = [-1,  1]
ri = [ 0,  1]
dr = [ 1,  1]
do = [ 1,  0]
dl = [ 1, -1]
le = [ 0, -1]
no = [ 0,  0]

step_matrix = np.array([
	[ul, ul, up, ur, ur],
	[ul, no, no, no, ur],
	[le, no, no, no, ri],
	[dl, no, no, no, dr],
	[dl, dl, do, dr, dr]])


def move_head(rope, direction):

	if direction == 'U':
		rope[0,0] -= 1
	if direction == 'D':
		rope[0,0] += 1
	if direction == 'L':
		rope[0,1] -= 1
	if direction == 'R':
		rope[0,1] += 1

	return rope

def move_tail(rope):
	pos_h = rope[0]
	pos_t = rope[1]

	rel_pos = rope[0] - rope[1]
	step_matrix_pos = rel_pos + [2, 2] #add offset

	rope[1] += step_matrix[step_matrix_pos[0], step_matrix_pos[1]]

	return rope

def move_chain(rope_chain, direction):
	for i in range(len(rope_chain)):
		if i == 0:
			rope_chain[i] = move_head(rope_chain[i], direction)
			rope_chain[i] = move_tail(rope_chain[i])

		else:
			rope_chain[i, 0] = rope_chain[i-1,1]
			rope_chain[i] = move_tail(rope_chain[i])

	return rope_chain

file = open('../input.txt')
rope_steps = file.read().split('\n')
file.close()

pos_h = np.array([0, 0])
pos_t = np.array([0, 0])

rope_chain = np.array([[pos_h.copy(), pos_t.copy()]] * 9)

new_positions_1 = set()
new_positions_2 = set()

for rope_step in rope_steps:
	direction, nr_steps = rope_step.split(' ')
	nr_steps = int(nr_steps)

	for step in range(nr_steps):
		rope_chain = move_chain(rope_chain, direction)

		new_positions_1.add(tuple(rope_chain[0,1]))
		new_positions_2.add(tuple(rope_chain[8,1]))

print('Part 1 Answer: ', len(new_positions_1))
print('Part 2 Answer: ', len(new_positions_2))