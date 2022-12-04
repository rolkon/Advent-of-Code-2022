import numpy as np

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priorities = {}

for i, letter in enumerate(alphabet):
	priorities[letter] = i+1

def get_common_priority(string_list):

	priority_lists = [[priorities[letter] for letter in string] for string in string_list]
	sorted_priority_sets = [sorted(set(priority_list)) for priority_list in priority_lists]

	# 53 elements because priorities start at 1
	occurence_map = np.zeros([len(string_list), 53], dtype=bool)

	for i in range(len(sorted_priority_sets)):
		occurence_map[i, sorted_priority_sets[i]] = True

	occurence_map = np.logical_and.reduce(occurence_map, axis=0)

	return occurence_map.nonzero()[0][0]


file = open('../input.txt')
rucksacks = file.read().split('\n')
file.close()

# part 1
sum_priorities = 0

for rucksack in rucksacks:
	left_side = rucksack[:len(rucksack)//2]
	right_side = rucksack[len(rucksack)//2:]

	sum_priorities += get_common_priority([left_side, right_side])

print("Part 1 result: ", sum_priorities)

# part 2
sum_priorities = 0

for i in range(0, len(rucksacks), 3):
	sum_priorities += get_common_priority(rucksacks[i:i+3])

print("Part 2 result: ", sum_priorities)