"""
Rosaling problem: Finding a Shared Motif
https://rosalind.info/problems/lcsm/

Given: A collection of k(k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""


from Bio import SeqIO



fasta_file_path = 'LCSM_input.txt'
sequences = SeqIO.parse(fasta_file_path, "fasta")
lista =[]

for seq_record in sequences:
        lista.append(str(seq_record.seq))


s1 = lista[0]
n = len(s1)
subs = []

# subs is a list of all possible substrings of the first sequence
for i in range(1, n+1):
    for j in range(0, n-i+1):
        substring = s1[j:j+i]
        subs.append(substring)
            

lista_subs = []
# lista_subs is a list of all substrings that are present in every sequence from fasta file        
for substring in subs:

   a = []
   for s in lista:
      a.append(substring in s) 
    
   if all(a):
        lista_subs.append(substring)
       
# find the longest common substring
longest_string = [max(lista_subs, key=len)]    

# if there is no common substring, empy string will be given as output
if lista_subs:
    longest_string_1 = longest_string[0]
    
else:
    longest_string_1 = ''
    

with open('LCSM_output.txt','w' ) as file2:
    file2.write(longest_string_1)
  










