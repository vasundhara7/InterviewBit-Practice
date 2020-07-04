# Problem Description

# Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.



# Input Format
# First and only argument is an integer array A.



# Output Format
# Return 1 if any such integer p is found else return -1.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=True)
        visited=set()
        for i in range(len(A)):
            if A[i] in visited:
                continue
            else:
                visited.add(A[i])
                if A[i]==i:
                    return 1
        return -1
