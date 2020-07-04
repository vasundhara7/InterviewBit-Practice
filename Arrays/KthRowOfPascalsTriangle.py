# Given an index k, return the kth row of the Pascal’s triangle.

# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

# Example:

# Input : k = 3

# Return : [1,3,3,1]
#  NOTE : k is 0 based. k = 0, corresponds to the row [1]. 
# Note:Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A==0:
            return [1]
        dp=[0]*(A+1)
        dp[0]=1
        li=dp[:]
        for i in range(1,A+1):
            dp=li[:]
            li=[0]*(A+1)
            for j in range(0,i+1):
                if j==0:
                    li[j]=1
                else:
                    li[j]=dp[j]+dp[j-1]
        return li
