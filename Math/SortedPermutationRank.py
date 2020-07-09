# Given a string, find the rank of the string amongst its permutations sorted lexicographically.
# Assume that no characters are repeated.

# Example :

# Input : 'acb'
# Output : 2

# The order permutations with letters 'a', 'c', and 'b' : 
# abc
# acb
# bac
# bca
# cab
# cba
# The answer might not fit in an integer, so return your answer % 1000003

class Solution:
    # @param A : string
    # @return an integer
    def fact(self,n) : 
        f = 1
        while n >= 1 : 
            f = f * n 
            n = n - 1
        return f 
    def findRank(self, A):
        a=sorted(A)
        count=0
        for i in range(len(A)):
            x=a.index(A[i])
            count+=x*self.fact(len(A)-i-1)
            a.pop(x)
        return (count+1)% 1000003
