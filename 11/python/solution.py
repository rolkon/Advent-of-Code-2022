from tqdm import tqdm

class Monke:
	def __init__(self, items, operation, test_value, cond_true, cond_false):
		self._items = items
		self._operation = operation
		self._test_value = test_value
		self._cond_true = cond_true
		self._cond_false = cond_false
		self._inspection_counter = 0
		self._modulo_divisor = None #part 2: collect multiplied test values of all monkes
	
	def inspect_item(self):
		item = self._items[0]
		operand = self._operation[0]
		value = self._operation[1]

		if value == 'old':
			value = self._items[0]
		else:
			value = int(value)

		if operand == '+':
			self._items[0] += value
		if operand == '*':
			self._items[0] *= value

		#self._items[0] /= 3 #part 1: relief that item was not damaged

		# method for keeping values from exploding: by modulo-ing the value by
		# the multiple of all divisors of the monkeys, division tests stay the same,
		# but values stay in a manageable range
		self._items[0] %= self._modulo_divisor

		self._inspection_counter += 1

	def test_item(self):
		if self._items[0] % self._test_value == 0:
			return self._cond_true
		else:
			return self._cond_false

	def catch_item(self, item):
		self._items.append(item)

	def throw_item(self):
		#print('throw')
		return self._items.pop(0)

	def has_items(self):
		return len(self._items) > 0

	def get_items(self):
		return self._items

	def get_inspection_count(self):
		return self._inspection_counter

	def set_modulo_divisor(self, modulo_divisor):
		self._modulo_divisor = modulo_divisor

file = open('../input.txt')
monke_schema = file.read().split('\n\n')
file.close()

monkes = []
modulo_divisor = 1

for scheme in monke_schema:
	instr = scheme.split('\n')[1:]

	start_items = instr[0].split(' ')[4:]
	start_items = [int(item.split(',')[0]) for item in start_items]

	operation = instr[1].split(' ')[6:]

	test_value = int(instr[2].split(' ')[-1])
	modulo_divisor *= test_value

	cond_true = int(instr[3].split(' ')[-1])
	cond_false = int(instr[4].split(' ')[-1])

	monkes.append(Monke(start_items, operation, test_value, cond_true, cond_false))

for monke in monkes:
	monke.set_modulo_divisor(modulo_divisor)

for i in tqdm(range(10000)):
	for monke in monkes:
		while monke.has_items():
			monke.inspect_item()
			monke_throw_index = monke.test_item()
			monkes[monke_throw_index].catch_item(monke.throw_item())

monke_inspection_count = [monke.get_inspection_count() for monke in monkes]
monke_business_factor = sorted(monke_inspection_count)[-1] * sorted(monke_inspection_count)[-2]

print(monke_inspection_count)

print("Part 2: ", monke_business_factor)

