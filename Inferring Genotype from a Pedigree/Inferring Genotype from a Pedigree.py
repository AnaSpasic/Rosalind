"""
Rosaling problem: Inferring Genotype from a Pedigree
https://rosalind.info/problems/mend/

Given: A rooted binary tree T in Newick format encoding an individual's pedigree for a Mendelian factor 
whose alleles are A (dominant) and a (recessive).

Return: Three numbers between 0 and 1, corresponding to the respective probabilities that the individual 
at the root of T will exhibit the "AA", "Aa" and "aa" genotypes.
 
"""

from Bio import Phylo
from io import StringIO
import csv


with open ('MEND_input.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    treedata = '\n'.join(','.join(row) for row in reader) # read csv file as string

# function to calculate genotype probabilities based on Mendelian inheritance
def inheritance_tree(root):
    if root.clades == []: 
        d = {'AA':0, 'Aa':0, 'aa':0}
        if root.name == 'AA':
            d['AA'] = 1
        elif root.name == 'Aa':
            d['Aa'] = 1
        else:
            d['aa'] = 1
            
        return d
        
    else:
        d = inheritance(inheritance_tree(root.clades[0]), inheritance_tree(root.clades[1]))
        return d
    
    
# genotype of two parents (leaves) determines genotype of a child (root)

# function to calculate genotype probabilities for a child based on parental genotypes
def inheritance(d1, d2):

    d3 = {'AA':0, 'Aa':0, 'aa':0}
    
    # all possible allele combinations and probabilities of a certain genotype
    d3 ['AA'] = d1['AA']*d2['AA']*1 + d1['AA']*d2['Aa']*0.5 + d1['Aa']*d2['AA']*0.5 + d1['Aa']*d2['Aa']*0.25
        
    d3 ['Aa'] = d1['AA']*d2['Aa']*0.5 + d1['AA']*d2['aa']*1 + d1['Aa']*d2['AA']*0.5 + d1['Aa']*d2['Aa']*0.5 + d1['Aa']*d2['aa']*0.5 + d1['aa']*d2['AA']*1+ d1['aa']*d2['Aa']*0.5
        
    d3 ['aa'] = d1['Aa']*d2['Aa']*0.25 + d1['Aa']*d2['aa']*0.5 + d1['aa']*d2['Aa']*0.5 + d1['aa']*d2['aa']*1

    return d3




handle = StringIO(treedata)
tree = Phylo.read(handle, "newick")
Phylo.draw(tree) 
tree = tree.clade


# for the purpose of the output
AA = round(inheritance_tree(tree) ["AA"], 3)
Aa = round(inheritance_tree(tree) ["Aa"], 3)
aa = round(inheritance_tree(tree) ["aa"], 3)

with open('MEND_output.txt','w' ) as file2:
    file2.write (f'{str(AA)} {str(Aa)} {str(aa)}')
   