# You are given a read only array of n integers from 1 to n.

# Each integer appears exactly once except A which appears twice and B which is missing.

# Return A and B.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Note that in your output A should precede B.
from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        d=Counter(A)
        for i in range(len(A)):
            if i+1 not in d:
                a=i+1
                continue
            if d[i+1]>1:
                b=i+1
                continue
        return [b,a]
            

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        x = sum(A) - sum(set(A))
        k = sum(A) - int(n*(n+1)/2)
    
        return [x,x-k]
