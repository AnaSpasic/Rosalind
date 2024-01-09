"""
Rosaling problem: Matching Random Motifs
https://rosalind.info/problems/rstr/

Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x
(see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random 
string to be created more than once.

"""

import csv

with open ('RSTR_input.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    csv_data = [row for row in reader]

N_strings = int (csv_data[0][0])
GC = float (csv_data[0][1])
motif = csv_data[1][0] # motif as string type


# probability of a single nucleotide
P = {'G':GC/2, 'C':GC/2, 'A':(1-GC)/2, 'T':(1-GC)/2}


# a = probability that a string is the same as motif 
a = 1

for nt in motif:
    a *= P[nt] 

# b = probability that a string is not the same as the motif
b = 1 - a

# c = probability that none of the N strings are the same as the motif
c = b ** N_strings

# d = probability that at least one string is the same as the motif
d = 1 - c


with open('RSTR_output.txt','w' ) as file2:
    file2.write(str(round(d,3)))