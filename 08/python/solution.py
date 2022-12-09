import numpy as np

file = open('../input.txt')
tree_map = np.array([list(line) for line in file.read().split('\n')], dtype=int)

file.close()

# part 1
def is_visible(row, col, tree_map):
	if row == 0 or col == 0:
		return True

	if row == tree_map.shape[0]-1 or col == tree_map.shape[0]-1:
		return True

	visible_left = all(trees < tree_map[row, col] for trees in tree_map[row,:col])
	visible_right = all(trees < tree_map[row, col] for trees in tree_map[row,col+1:])
	visible_top = all(trees < tree_map[row, col] for trees in tree_map[:row,col])
	visible_bot = all(trees < tree_map[row, col] for trees in tree_map[row+1:,col])


	return any([visible_left, visible_right, visible_top, visible_bot])

# part 2
def walk_treeline(path, tree_height, curr_distance):
	if len(path) == 0:
		return curr_distance

	if path[0] >= tree_height or len(path) == 1:
		return curr_distance +1
	else:
		return walk_treeline(path[1:], tree_height, curr_distance+1)

def get_scenic_score(row, col, tree_map):
	path_left = np.flip(tree_map[row, :col])
	path_right = tree_map[row, col+1:]
	path_top = np.flip(tree_map[:row, col])
	path_bot = tree_map[row+1:, col]

	paths = [path_left, path_right, path_top, path_bot]

	scenic_score = 1

	for path in paths:
		scenic_score *= walk_treeline(path, tree_map[row, col], 0)

	return scenic_score

total_visible = 0
curr_max_scenic_score = {'row':0, 'col':0, 'score':0}


for row in range(tree_map.shape[0]):
	for col in range(tree_map.shape[0]):
		# part 1
		total_visible += is_visible(row, col, tree_map)
		# part 2
		scenic_score = get_scenic_score(row, col, tree_map)

		if scenic_score > curr_max_scenic_score['score']:
			curr_max_scenic_score['row'] = row
			curr_max_scenic_score['col'] = col
			curr_max_scenic_score['score'] = scenic_score 

print(total_visible)
print(curr_max_scenic_score)