"""
Rosaling problem: Finding a Spliced Motif
https://rosalind.info/problems/sseq/

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. 
If multiple solutions exist, you may return any one.

"""

from Bio import SeqIO

# function to find the indices of a spliced motif (substring) in a sequence
def find_spliced_motif (string, substring):

    ind = -1
    location = []
    
    for i in range (len(substring)):
        for j in range(ind+1, len(string)):
            if substring[i] == string[j]:
                ind = j
                location.append(ind+1)
                break
        
    if len(location) != len(substring):
        location = -1
        
    return location



fasta_file_path = 'SSEQ_input.txt'
sequences = SeqIO.parse(fasta_file_path, "fasta")

for index, seq_record in enumerate(sequences):
    # Access sequence ID and sequence data
    if index == 0:
        string = seq_record.seq
    elif index == 1:
        substring = seq_record.seq


           
a = find_spliced_motif(string, substring)
 
with open('SSEQ_output.txt','w' ) as file2:
    file2.write(str(a))
  