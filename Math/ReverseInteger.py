# Reverse digits of an integer.

# Example1:

# x = 123,

# return 321
# Example2:

# x = -123,

# return -321

# Return 0 if the result overflows and does not fit in a 32 bit signed integer

import math
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A<0:
            ans='-'+str(A)[:0:-1]
        else:
            ans=str(A)[::-1]
        if int(ans)>math.pow(2,31)-1 or int(ans)<math.pow(-2,31):
            return 0
        else:
            return int(ans)
