class Directory:
	root = None
	def __init__(self, parent, name):
		self.name = name
		self.subdirs = {} # recursive directory with link to parent
		self.parent = parent
		self.files = {} # dict of files with filesize as value
		self.total_size = 0

	def parse_input(self, instructions):
		'''
		Recursive function to parse the input
		'''
		if len(instructions) == 0:
			return

		instruction = instructions[0]

		cmd = instruction[0].split(' ')
		if cmd[0] == 'cd':
			if cmd[1] == '/':
				root.parse_input(instructions[1:])

			elif cmd[1] == '..':
				self.parent.parse_input(instructions[1:])

			else:
				self.subdirs[cmd[1]].parse_input(instructions[1:])


		elif cmd[0] == 'ls':
			for param in instruction[1:]:
				file = param.split(' ')

				if file[0] == 'dir' and file[1] not in self.subdirs:
					self.subdirs[file[1]] = Directory(self, file[1])

				elif file[1] not in self.files:
					self.files[file[1]] = int(file[0])

			self.parse_input(instructions[1:])

	def print_tree(self, level):
		print(' |'*level, self.name, self.total_size, self.files)
		for key in self.subdirs.keys():
			self.subdirs[key].print_tree(level+1)

	def calculate_sizes(self):
		total_size = 0
		for key in self.subdirs.keys():
			total_size += self.subdirs[key].calculate_sizes()

		for key in self.files.keys():
			total_size += self.files[key]

		#print(total_size)
		self.total_size = total_size
		return total_size

	def get_size(self):
		return self.total_size

	def get_list_of_sizes(self, size_list):
		for key in self.subdirs.keys():
			self.subdirs[key].get_list_of_sizes(size_list)

		size_list.append(self.total_size)

		return size_list

# define constants
total_system_space = 70000000
total_required_space = 30000000


file = open('../input.txt')
shell_instructions = file.read()
file.close()

instruction_blocks = shell_instructions.split('$')
if '' in instruction_blocks:
	instruction_blocks.remove('')

instructions = [block.strip().split('\n') for block in instruction_blocks]

root = Directory(None, '/')
Directory.root = root

for instruction in instructions:
	if '' in instruction:
		instruction.remove('')

root.parse_input(instructions)
root.calculate_sizes()

size_list = root.get_list_of_sizes([])

sizes_under_threshold = [size for size in size_list if size <= 100000]

print('Part 1 answer: ', sum(sizes_under_threshold))

current_space_left = (total_system_space - root.get_size())
space_to_be_freed = total_required_space - current_space_left

sizes_over_threshold = [size for size in size_list if size >= space_to_be_freed]

print('Part 2 anser: ', sorted(sizes_over_threshold)[0])
