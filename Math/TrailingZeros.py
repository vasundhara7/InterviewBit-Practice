# Given an integer A, return the number of trailing zeroes in A!.

# Note: Your solution should be in logarithmic time complexity.

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        n=5
        s=0
        while n<=A:
            s+=A//n
            n=n*5
        return s
