# Find the contiguous subarray within an array, A of length N which has the largest sum.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum=A[0]
        max_until=A[0]
        for i in range(1,len(A)):
            max_until=max(max_until+A[i],A[i])
            max_sum=max(max_sum,max_until)
        return max_sum