with open('../01_input.txt') as file:
	print(sum(sorted([sum([int(num) for num in elem.split('\n')]) for elem in file.read().split('\n\n')], reverse=True)[:3]))