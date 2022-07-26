""" Computes GC content for seqences from a source in FASTA format;
	compares GC content and returns the sequence with the highest. """

f = open('rosalind_gc.txt', 'r')

sequence_dict = {}
for line in f:
	if line.startswith('>'):
		code = line[:9:-1].split()[0]
		sequence_dict[code] = ''
	else:
		sequence_dict[code] += line.split()[0]

def count_gc(sequence):
	return sequence.upper().count('G') + sequence.upper().count('C')

gc_dict = {}
for key, value in sequence_dict.items():
	gc_dict[key] = count_gc(value)

gc_percentage_dict = {}
for key, value in gc_dict.items():
	gc_percentage_dict[key] = (value / len(sequence_dict[key])) * 100

print(gc_percentage_dict)
max_percentage_key = max(gc_percentage_dict, key=gc_percentage_dict.get)
print(f'Rosalind_{max_percentage_key}\n{gc_percentage_dict[max_percentage_key]}')