with open('../input.txt') as file:
	print(max([sum([int(num) for num in elem.split('\n')]) for elem in file.read().split('\n\n')]))