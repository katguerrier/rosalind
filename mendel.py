def calc_prob_dominance(k,m,n):
	''' Calculates the probability that any individual offspring will express a dominant trait (per simple Mendelian inheritance patterns) given 
	the makeup of a population k, m, n, where k is the number of individuals in the population who are homozygous dominant for the trait, m heterozygous, and
	n homozygous recessive. '''

	pop_size = k + m + n


	prob_a_hetdom = k / pop_size
	prob_a_homo = m / pop_size
	prob_a_hetrec = n / pop_size


	given_homo_prob_hetdom = (k / (pop_size - 1))
	given_homo_prob_homo = ((m - 1) / (pop_size - 1))
	given_homo_prob_hetrec = (n / (pop_size - 1))

	given_rec_prob_hetdom = k / (pop_size - 1)
	given_rec_prob_homo = (m / (pop_size - 1))
	given_rec_prob_rec = ((n - 1) / (pop_size - 1))


	prob_dominance = ((prob_a_hetdom) + 
					 (prob_a_homo * 
					 	( given_homo_prob_hetdom + 
					 	  (given_homo_prob_homo * 0.75) + 
					 	  (given_homo_prob_hetrec * 0.5)
					 )) + 
					 (prob_a_hetrec * 
					 	( given_rec_prob_hetdom + 
					 		given_rec_prob_homo * 0.5)
					 ))

	return prob_dominance

def calc_dom_offspring(a, b, c, d, e, f,):
	''' Calculates the expected value of offspring who will express a dominant trait in the next generation, given information about the parent population. 
	The six values passed to this function shall be the number of parents of specific genotypes. Let the dominant trait be represented by D, recessive by d.
	Then:
		A = DD x DD			B = DD x Dd			C = DD x dd			D = Dd x Dd			E = Dd x dd			F = dd x dd									
	The assumption is made that all couples produce exactly 2 offspring.																				'''

	return ( (2 * (a + b + c)) + (1.5 * d) + e)