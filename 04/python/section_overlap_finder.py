file = open('../input.txt')
section_list = file.read().split('\n')
file.close()

fully_contained_counter = 0
overlap_counter = 0

for i, section in enumerate(section_list):
	ranges = section.split(',')
	ranges = [[int(s) for s in r.split('-')] for r in ranges]

	lowerb = ranges[0][0] - ranges[1][0]
	upperb = ranges[0][1] - ranges[1][1]

	# part1
	if lowerb * upperb <= 0:
		fully_contained_counter += 1

	# part2
	elif lowerb <= 0:
		if (ranges[0][1] - ranges[1][0]) * lowerb <= 0:
			overlap_counter += 1
	elif lowerb >0:
		if (ranges[0][0] - ranges[1][1]) * lowerb <= 0:
			overlap_counter += 1

print('Part 1 result: ', fully_contained_counter)
print('Part 2 result: ', fully_contained_counter + overlap_counter)