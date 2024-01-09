"""
Rosaling problem: Consensus and Profile
https://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus 
strings exist, then you may return any one of them.)
"""


import numpy as np
from Bio import SeqIO


fasta_file_path = 'CONS_input.txt'
sequences = SeqIO.parse(fasta_file_path, "fasta")

DNA_strings = []

for seq_record in sequences:
        DNA_strings.append(list(seq_record.seq)) # get every sequnce as array of characters


N = len(DNA_strings[0]) # all given strings have the same size

DNA_strings = np.array(DNA_strings) 


profile = np.zeros ((4, N), dtype = int) 
# profile matrix of dimensions 4xN filled with number of nucletides in each column of DNA_strings matrix
for i in range(N):
    profile[0, i] = sum(DNA_strings[:, i] == 'A')
    profile[1, i] = sum(DNA_strings[:, i] == 'C')
    profile[2, i] = sum(DNA_strings[:, i] == 'G')
    profile[3, i] = sum(DNA_strings[:, i] == 'T')



consensus_ind = np.zeros (N)
# consensus_ind is filled with indices of characters that have the highest occurance in a given profile column
for i in range(N):
    consensus_ind [i] = np.argmax (profile [:, i])


consensus = np.zeros (N, dtype = str)

# dictionary in which every index (key) has a nucletide assigned (value)  
nucleotids = {0:'A', 1:'C', 2:'G', 3:'T'}

# consensus array in which indices from consensus_ind array are exchanged for corresponding nucleotides -> making consensus sequence
for i in range(N):  
    consensus [i] = nucleotids [consensus_ind[i]] 
    
    
    
# for the purpose of the required output format:   
profile = profile.astype(str)
consensus_l = consensus.tolist()
consensus_s = ''.join(consensus_l)

    
with open('CONS_output.txt','w' ) as file2:
    file2.write(f"{consensus_s} \nA: {' '.join(profile[0])} \nC: {' '.join(profile[1])} \nG: {' '.join(profile[2])} \nT: {' '.join(profile[3])}") 

