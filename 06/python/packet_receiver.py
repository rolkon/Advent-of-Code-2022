from collections import Counter

def detect_marker(signal_src, nr_distinct):
	for i in range(nr_distinct, len(signal_src)+1):
		substr = signal_src[i-nr_distinct:i]

		if max(Counter(substr).values()) == 1:
			return i

file = open('../input.txt')
signal_src = file.read()
file.close()

#part 1:
print("Result part 1: ", detect_marker(signal_src, 4))

#part 2:
print("Result part 1: ", detect_marker(signal_src, 14))