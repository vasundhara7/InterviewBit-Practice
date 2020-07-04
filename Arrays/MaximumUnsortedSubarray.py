# You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
# Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
# If A is already sorted, output -1.

# Example :

# Input 1:

# A = [1, 3, 2, 4, 5]

# Return: [1, 2]

# Input 2:

# A = [1, 2, 3, 4, 5]

# Return: [-1]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        s=-1
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                s=i
                break
        if s==-1:
            return [-1]
        e=-1
        for i in range(len(A)-1,0,-1):
            if A[i]<A[i-1]:
                e=i
                break
        min_val=min(A[s:e+1])
        max_val=max(A[s:e+1])
        for i in range(s):
            if A[i]>min_val:
                s=i
                break
        for i in range(len(A)-1,e,-1):
            if A[i]<max_val :
                e=i
                break
        
        return [s,e]
        
            
            
        
