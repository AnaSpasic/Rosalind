"""
Rosaling problem: Mendel's First Law
https://rosalind.info/problems/iprb/

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing 
a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

"""

import numpy as np
import csv

with open ('IPRB_input.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    csv_data = [row for row in reader]

k = int (csv_data[0][0])
m = int (csv_data[0][1]) 
n = int (csv_data[0][2])    

# total population at the beggining
pop0 = k+m+n

# probabilities of the first branching event
branching_1 = np.array ([k/pop0, m/pop0, n/pop0])

# population after the first event
pop1 = pop0-1

# probabilities of the second branching event
branching_2 = np.array ([(k-1)/pop1, m/pop1, n/pop1,
                            k/pop1, (m-1)/pop1, n/pop1,
                            k/pop1, m/pop1, (n-1)/pop1])
                            
# probabilities of the first branching event to be the same size as branching_2 (for the purpose of multiplication)                        
branching_1_3 = np.repeat (branching_1, 3, axis=0) 

# probability of the final outcome (given mating pair) 
mating_probabilities = branching_1_3 * branching_2
# kk,km,kn,
# mk,mm,mn,
# nk,nm,nn

# probabilities that the dominant allele is inherited for each pair
A = np.array ([1, 1, 1, 1, 3/4, 1/2, 1, 1/2, 0])

# probabilities that the dominant allele is inherited for each pair taking into accout the probability of each mating pair occuring
prob_A = mating_probabilities * A 

# probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
probability_A = sum(prob_A)

# for the purpose of the output
probability_A = round(probability_A, 5)


with open('IPRB_output.txt','w' ) as file2:
    file2.write(str(probability_A))
