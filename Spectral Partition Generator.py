# Imports
from csv import writer

# Functions
tn = lambda n : int((n*(n+1))/2)
tri_part_sum = lambda start, length: tn(length + start - 1) - tn(start - 1)

def build_sequence_list(start, length):
	new_sequence = []
	for i in range (length):
		new_sequence.append(start + i)

	return new_sequence
        
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

def matrix_output_csv(big_ol_matrix, output_name):
    with open(output_name + ".csv", "w", newline='') as output_file:
        output = writer(output_file, )
        output.writerows(big_ol_matrix)

# Code
depth = int(input("Enter the number of times sequences will be incremented: "))
width = int(input("Enter the maximum length of the sequences: "))
output_name = input("Enter the name of the output: ")

print("Generating data...")
output_matrix = build_matrix_list(depth, width)

print("Writing data to " + output_name + ".csv...")
matrix_output_csv(output_matrix, output_name)