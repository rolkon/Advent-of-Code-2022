file = open('../input.txt')
cpu_instr = file.read().split('\n')
file.close()

x_reg = 1
program_ptr = 0
clk_cntr = 0
total_signal_strength = 0
crt_pos = 0

def compute_step(clk_cntr, x_reg, crt_pos):

	if crt_pos in [x_reg-1, x_reg, x_reg+1]:
		crt_draw = '#'
	else:
		crt_draw = '.'

	clk_cntr += 1
	signal_strength = 0
	crt_pos += 1
	crt_pos %= 40

	newline = False

	if clk_cntr % 40 == 0:
		newline = True

	if (clk_cntr - 20) % 40 == 0:
		signal_strength = clk_cntr * x_reg

	return clk_cntr, signal_strength, crt_pos, crt_draw, newline

def draw_step(clk_cntr, x_reg, crt_pos, total_signal_strength):
	clk_cntr, signal_strength, crt_pos, crt_draw, newline = compute_step(clk_cntr, x_reg, crt_pos)

	total_signal_strength += signal_strength

	print(crt_draw, end='')
	if newline:
		print()

	return clk_cntr, total_signal_strength, crt_pos

print('Part 2 answer:')
while True:
	if program_ptr == len(cpu_instr):
		break

	instr = cpu_instr[program_ptr].split(' ')

	if instr[0] == 'noop':
		clk_cntr, total_signal_strength, crt_pos = draw_step(clk_cntr, x_reg, crt_pos, total_signal_strength)

	else:
		clk_cntr, total_signal_strength, crt_pos = draw_step(clk_cntr, x_reg, crt_pos, total_signal_strength)
		clk_cntr, total_signal_strength, crt_pos = draw_step(clk_cntr, x_reg, crt_pos, total_signal_strength)

		x_reg += int(instr[1])

	program_ptr += 1

print()
print('Part 1 answer:', total_signal_strength)