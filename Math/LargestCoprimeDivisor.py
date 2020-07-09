# You are given two positive numbers A and B. You need to find the maximum valued integer X such that:

# X divides A i.e. A % X = 0
# X and B are co-prime i.e. gcd(X, B) = 1
# For example,

# A = 30
# B = 12
# We return
# X = 5

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    def gcd(self,x,y):
        if x==y:
            return x
        big=max(x,y)
        small=min(x,y)
        while True:
            rem=big%small
            if rem!=0:
                big=small
                small=rem
            else:
                return small
    
    def cpFact(self, A, B):
        while self.gcd(A,B)!=1:
            A=A/self.gcd(A,B)
        return int(A)
