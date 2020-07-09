# Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

# Given an array A of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array. Return the answer modulo 1000000007.



# Problem Constraints
# 1 <= |A| <= 200000

# 1 <= A[i] <= 109

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def calculate(self,x1,x2):
        x=x1^x2
        dist=0
        while x>0:
            dist+=x&1
            x=x>>1
        return dist
    
    def hammingDistance(self, A):
        ans=0
        for i in range(0,32):
            count=0
            for j in range(0,len(A)):
                if A[j]&(1<<i):
                    count+=1
            ans+=count*(len(A)-count)*2
        return ans%1000000007
