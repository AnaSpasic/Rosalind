"""
Rosaling problem: Independent Alleles
https://rosalind.info/problems/lia/

Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 
0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two 
children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's
family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
"""


import csv


with open ('LIA_input.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    csv_data = [row for row in reader]
   

k = int (csv_data[0][0])
N = int (csv_data[0][1])


# each pair has two children; generation_size is number of members in geeration
generation_size = 2**k  

# organism with any genotype that mates with an organism having genotype Aa Bb will have offspring 1/4 AaBb (Aa 1/2 * Bb 1/2)
inheritance = {'AaBb':0.25, 'other':0.75}

# probability that none of the genration memebers has AaBb genotype
none = (inheritance['other'])**generation_size 

# probability that at least one member has AaBb genotype in k-th generation
P = 1 - none

# probability that at least N memebrs has AaBb genotype in k-th generation
for i in range (1,N):
    Pt = generation_size * inheritance['AaBb']**i * inheritance['ostalo']**(generation_size - i) 
    P -= Pt
 
# for the purpose of the output
P = round(P, 3)


with open('LIA_output.txt','w' ) as file2:
    file2.write(str(P))