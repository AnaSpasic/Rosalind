"""
Rosaling problem: Calculating Expected Offspring
https://rosalind.info/problems/iev/

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond 
to the number of couples in a population possessing each genotype pairing for a given factor. 
In order, the six given integers represent the number of couples having the following genotypes:
AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
under the assumption that every couple has exactly two offspring.
"""

import csv 
import numpy as np 


with open ('IEV_input.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    csv_data = [row for row in reader]

number_of_pairs = [int(element) for element in csv_data[0]]


# every couple has exactly two children
num_children = [2, 2, 2, 2, 2, 2]

# number of children for every genotype pair
total_children = np.array((number_of_pairs)) * np.array((num_children)) 

# probability of offspring with dominant phenotype from parents having the genotype in respective order
# AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa 
dominant_probability = [1, 1, 1, 0.75, 0.5, 0]


expected_num_of_offspring = sum (total_children * np.array((dominant_probability)))


with open('IEV_output.txt','w' ) as file2:
    file2.write(str(expected_num_of_offspring)) 
    