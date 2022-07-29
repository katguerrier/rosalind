def count_bases(sequence):
	""" Given a DNA sequence, returns the number of times each nucleotide appears in it."""

	sequence = sequence.upper()
	return f"{sequence.count('A')} {sequence.count('C')} {sequence.count('G')} {sequence.count('T')}"
	
def transcribe(sequence):
	""" Given a DNA sequence, transcribe it into RNA. """

	sequence = sequence.upper()
	return sequence.replace('T', 'U')

def comp_strand(sequence):
	""" Given a DNA sequence, returns its complementary strand. """

	nuc_comps = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

	output = ''
	for c in sequence.upper():
		output += nuc_comps[c]
	return output

def rev_comp(sequence):
	""" Returns the reverse complement strand for a sequence of DNA."""
	return comp_strand(sequence[::-1])

def calc_point_mutations(seq1, seq2):
	""" Returns the number of corresponding nucleotides that differ between two sequences. """
	seq1 = seq1.upper().strip()
	seq2 = seq2.upper().strip()

	i = 0
	mutations = 0
	while i < len(seq1):
		if seq1[i] != seq2[i]:
			mutations += 1
		i+=1
	return mutations

def compute_mrna(protein):
	''' Computes the total number of possible mRNA sequences from which a given protein string could be translated, modulo 1,000,000. '''

	# The number of codons corresponding to each amino acid:
	a_dict = {'F': 2, 'L': 6, 'S': 6, 'Stop': 3, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4}
	
	prod = 3 # 3 'STOP' sequences.
	for a in protein:
		prod = (prod * a_dict) % 1000000

	return prod