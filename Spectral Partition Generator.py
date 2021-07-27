# Imports

# Options
maximum_size = 200

# Functions
def build_sequence(start, length):
	new_sequence = []
	for i in range (length):
		new_sequence.append(start + i)

	return new_sequence

tn = lambda n : int((n*(n+1))/2)
tri_part_sum = lambda start, length: tn(length + start - 1) - tn(start - 1)
        
# Code
list_of_sequences = []   # Example structure of this list after the code is ran: [([1,2,3], 6), ([2,3,4], 9), ([3,4,5], 12), ...]

nums = 2
start = 3
total = tri_part_sum(start, nums)

# with the following code simplified, it does look rather strange. These are seperate while loops, because each one modifies the total in a different way.
while total <= maximum_size:
    while total <= maximum_size:
        list_of_sequences.append((build_sequence(start, nums), total))
        start += 1
        total += nums

    nums += 1
    start = 3
    total = tri_part_sum(start, nums)

print(list_of_sequences)