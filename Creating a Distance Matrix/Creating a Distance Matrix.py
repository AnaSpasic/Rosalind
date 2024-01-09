"""
Rosaling problem: Creating a Distance Matrix
https://rosalind.info/problems/pdst/

Given: A collection of n(n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is 
allowed an absolute error of 0.001.
"""

from Bio import SeqIO
import numpy as np


# function to calculate the p-distance between two DNA sequences
def p_distance (seq1, seq2):
    
    H = 0
    for nt in range (len(seq1)): 
        if seq1 [nt] != seq2 [nt]:
            H += 1 
    return round(H/len(seq1), 4)


lista_dna = []
fasta_file_path = 'PTST_input.txt'
sequences = SeqIO.parse(fasta_file_path, "fasta")

for seq_record in sequences:
        lista_dna.append(seq_record.seq)
            
# number of sequences        
N = len(lista_dna)
            
# distance matrix
D = np.zeros ((N,N)) 

# calculate the p-distance for all pairs of sequences and fill the distance matrix
for i in range(N):
    for j in range (i, N):
        if i == j:
            D[i,j] = 0
        else:
            D[i,j] = p_distance (lista_dna[i], lista_dna[j])
            D[j,i] = D [i,j] 


# export Sample Output
with open('PTST_output.txt','w' ) as file2:
    file2.write(str(D))