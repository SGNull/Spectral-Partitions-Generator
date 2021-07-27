# Imports
import csv

# Options
DEPTH = 120   # Total numerical increments
WIDTH = 60   # Maximum amount of numbers in the sequences
OUTPUT_NAME = "output_test"

# Code
def build_sequence_list(start, length):
	new_sequence = []
	for i in range (length):
		new_sequence.append(start + i)

	return new_sequence

tn = lambda n : int((n*(n+1))/2)
tri_part_sum = lambda start, length: tn(length + start - 1) - tn(start - 1)

def build_original_list(maximum_size):
    list_of_sequences = []   # Example structure of this list after the code is ran: [([1,2,3], 6), ([2,3,4], 9), ([3,4,5], 12), ...]

    nums = 2
    start = 3
    total = tri_part_sum(start, nums)

    # with the following code simplified, it does look rather strange. These are seperate while loops, because each one modifies the total in a different way.
    while total <= maximum_size:
        while total <= maximum_size:
            list_of_sequences.append((build_sequence_list(start, nums), total))
            start += 1
            total += nums

        nums += 1
        start = 3
        total = tri_part_sum(start, nums)
    
    return list_of_sequences
        
def build_matrix_list(max_increments, max_length):
    list_of_lists_of_sequences = [] # Example structure: [[[1,2,3], 6, [1,2,3,4], 10, [1,2,3,4,5], 15, ...], [[2,3,4], 9, [2,3,4,5], 14, [2,3,4,5,6], 20], ...]

    for inc in range(max_increments):
        new_row = []
        for length in range(max_length):
            sequence = map(str, build_sequence_list(3 + inc, length + 2))
            new_row.append(', '.join(sequence))

            total = tri_part_sum(3 + inc, length + 2)
            new_row.append(str(total))

        list_of_lists_of_sequences.append(new_row)
    
    return list_of_lists_of_sequences

def matrix_output_csv(big_ol_matrix):
    with open(OUTPUT_NAME + ".csv", "w", newline='') as output_file:
        output = csv.writer(output_file, )
        output.writerows(big_ol_matrix)

output_matrix = build_matrix_list(DEPTH, WIDTH)

matrix_output_csv(output_matrix)