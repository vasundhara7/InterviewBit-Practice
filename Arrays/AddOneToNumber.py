# Given a non-negative number represented as an array of digits,

# add 1 to the number ( increment the number represented by the digits ).

# The digits are stored such that the most significant digit is at the head of the list.

# Example:

# If the vector has [1, 2, 3]

# the returned vector should be [1, 2, 4]

# as 123 + 1 = 124.

from collections import deque
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        q=deque()
        carry=0
        while len(A)>1 and A[0]==0:
            A.pop(0)
        for i in range(len(A)-1,-1,-1):
            if i==len(A)-1:
                s=A[i]+1
            else:
                s=carry+A[i]
            
            if s>9:
                carry=1
                s=s%10
            else:
                carry=0
            q.appendleft(s)
        if carry==1:
            q.appendleft(carry)
        return q
