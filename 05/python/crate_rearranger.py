file = open('../input.txt')
crate_operations = file.read()
file.close()

crate_arrangement = crate_operations.split('\n\n')[0]
crate_movements = crate_operations.split('\n\n')[1]

# remove crate staple index and rearrange bottom to top to fill stacks
crate_arrangement = crate_arrangement.split('\n')[:-1][::-1]

# each row has nr_stacks * 3 + (nr_stacks-1) * 1 characters
# 3 for the crate, 1 in the middle for the placeholder.
number_crate_stacks = (len(crate_arrangement[0])+1)//4

crate_stack_9000 = []
crate_stack_9001 = []
for i in range(number_crate_stacks):
	crate_stack_9000.append([])
	crate_stack_9001.append([])

for row in crate_arrangement:
	for i in range(number_crate_stacks):
		crate_name = row[i*4+1]
		if crate_name != ' ':
			crate_stack_9000[i].append(row[i*4+1])
			crate_stack_9001[i].append(row[i*4+1])

for movement in crate_movements.split('\n'):
	instructions = movement.split(' ')
	nr_crates = int(instructions[1])
	from_stack = int(instructions[3])
	to_stack = int(instructions[5])

	# part 1
	for i in range(nr_crates):
		crate_stack_9000[to_stack-1].append(crate_stack_9000[from_stack-1].pop())

	crate_stack_9001[to_stack-1].extend(crate_stack_9001[from_stack-1][-nr_crates:])
	crate_stack_9001[from_stack-1] = crate_stack_9001[from_stack-1][:-nr_crates]

print('Solution part 1: ', end='')
for stack in crate_stack_9000:
	print(stack[-1], end='')
print()

print('Solution part 2: ', end='')
for stack in crate_stack_9001:
	print(stack[-1], end='')
print()