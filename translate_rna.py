""" Translates a sequence of RNA into an amino acid sequence """

def translate(rna):
	codon_table = {
		"UUU": 'F', "CUU": 'L', "AUU": 'I', "GUU": 'V',
		"UUC": 'F', "CUC": 'L', "AUC": 'I', "GUC": 'V',
		"UUA": 'L', "CUA": 'L', "AUA": 'I', "GUA": 'V',
		"UUG": 'L', "CUG": 'L', "AUG": 'M', "GUG": 'V',
		"UCU": 'S', "CCU": 'P', "ACU": 'T', "GCU": 'A',
		"UCC": 'S', "CCC": 'P', "ACC": 'T', "GCC": 'A',
		"UCA": 'S', "CCA": 'P', "ACA": 'T', "GCA": 'A',
		"UCG": 'S', "CCG": 'P', "ACG": 'T', "GCG": 'A',
		"UAU": 'Y', "CAU": 'H', "AAU": 'N', "GAU": 'D',
		"UAC": 'Y', "CAC": 'H', "AAC": 'N', "GAC": 'D',
		"UAA": 'Stop', "CAA": 'Q', "AAA": 'K', "GAA": 'E',
		"UAG": 'Stop', "CAG": 'Q', "AAG": 'K', "GAG": 'E',
		"UGU": 'C', "CGU": 'R', "AGU": 'S', "GGU": 'G',
		"UGC": 'C', "CGC": 'R', "AGC": 'S', "GGC": 'G',
		"UGA": 'Stop', "CGA": 'R', "AGA": 'R', "GGA": 'G',
		"UGG": 'W', "CGG": 'R', "AGG": 'R', "GGG": 'G'
	}

	i = 0
	amino = ''
	while i < len(rna):
		codon = rna[i] + rna[i+1] + rna[i+2]
		if codon_table[codon] == 'Stop': break
		else: 
			amino += codon_table[codon]
			i+=3

	return amino