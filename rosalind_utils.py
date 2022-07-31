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
	"""Computes the total number of possible mRNA sequences from which a given protein string could be translated, modulo 1,000,000. """

	# The number of codons corresponding to each amino acid:
	a_dict = {'F': 2, 'L': 6, 'S': 6, 'Stop': 3, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4}
	
	prod = 3 # 3 'STOP' sequences.
	for a in protein:
		prod = (prod * a_dict) % 1000000

	return prod

def compute_mass(protein):
	""" Computes the mass of a protein, given a protein string (chain of amino acids). """

	mass_table = {
		'A': 71.03711,
		'C': 103.00919,
		'D': 115.02694,
		'E': 129.04259,
		'F': 147.06841,
		'G': 57.02146,
		'H': 137.05891,
		'I': 113.08406,
		'K': 128.09496,
		'L': 113.08406,
		'M': 131.04049,
		'N': 114.04293,
		'P': 97.05276,
		'Q': 128.05858,
		'R': 156.10111,
		'S': 87.03203,
		'T': 101.04768,
		'V': 99.06841,
		'W': 186.07931,
		'Y': 163.06333,
		'water': 18.01056
	}

	sum = 0

	for c in protein:
		sum += mass_table[c]

	return sum