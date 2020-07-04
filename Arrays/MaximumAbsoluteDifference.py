# You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

# For example,

# A=[1, 3, -1]

# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

# So, we return 5.

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        plus=0
        max_plus=-10000000000
        min_plus=100000000000
        minus=0
        max_minus=-10000000000
        min_minus=100000000000
        for i in range(len(A)):
            plus=A[i]+(i+1)
            minus=A[i]-(i+1)
            max_plus=max(max_plus,plus)
            min_plus=min(min_plus,plus)
            max_minus=max(max_minus,minus)
            min_minus=min(min_minus,minus)
        return max((max_plus-min_plus),(max_minus-min_minus))