"""
Rosaling problem: Majority Element
https://rosalind.info/problems/maj/

An array A[1..n] is said to have a majority element if more than half of its entries are the same.

Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing positive 
integers not exceeding 105.

Return: For each array, output an element of this array occurring strictly more than n/2 times if 
such element exists, and "-1" otherwise.
"""


import csv
import numpy as np


with open ('MAJ_input.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    csv_data = [row for row in reader]
     
# extract values for k, n, and array A
k = int (csv_data[0][0])
n = int (csv_data[0][1]) 
A = np.array(csv_data[1:], dtype='int')


# function to find majority elements in each sequence
def majority_element (k,n,A):
    count = np.ones(k)
    num = np.zeros(k)
    
    for i in range(k): # 0-3
        A[i,:].sort()

        for j in range(n-1): # 0-6

            if A[i,j] == A[i,j+1]:
                count[i] += 1
                if count[i] > n/2:
                    break
        
        if count[i] > n/2:
            num[i] = (A[i,j])
        else:
            num[i]= -1
        
        
        num = list(num)
        num = [round(float(number)) for number in num]
            
    return num


o = majority_element(k, n, A)


# for the purpose of the output
o_string = ', '.join(map(str, o))

with open('MAJ_output.txt','w' ) as file2:
    file2.write(o_string)