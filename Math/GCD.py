# Given 2 non negative integers m and n, find gcd(m, n)

# GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
# Both m and n fit in a 32 bit signed integer.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        big=max(A,B)
        small=min(A,B)
        if small==0:
            return big
        while True:
            rem=big%small
            if rem==0:
                return small
            big=small
            small=rem
