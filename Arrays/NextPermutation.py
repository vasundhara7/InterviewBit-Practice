# Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

# If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        pos=-1
        
        n=len(A)
        for i in range(n-2,-1,-1):
            if A[i]<A[i+1]:
                pos=i
                break
        if pos==-1:
            return sorted(A)
        
        i=pos+1
        next_min=i
        mini=A[i]
        while i<n:
            if A[i]>A[pos] and A[i]<mini:
                mini=A[i]
                next_min=i
            i+=1
            
        A[pos],A[next_min]=A[next_min],A[pos]
        # li=sorted(A[pos+1:])
        return A[:pos+1]+A[n-1:pos:-1]
            
