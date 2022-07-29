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