# Imports

# Options
maximum_size = 100

# Functions
def build_sequence(start, length):
	new_sequence = []
	for i in range (length):
		new_sequence.append(start + i)

	return new_sequence

def total_sequence(sequence):
    total = 0
    for element in sequence:
        total += element

    return total

tn = lambda n : int((n*(n+1))/2)
tri_part_sum = lambda start, length: tn(length + start) - tn(start - 1)
        
# Code
list_of_sequences = []
nums = 2

while tri_part_sum(3,nums) <= maximum_size:
    start = 3
    while tri_part_sum(start, nums) <= maximum_size:
        
        list_of_sequences.append(tuple(build_sequence(start, nums), tri_part_sum(start, nums)))