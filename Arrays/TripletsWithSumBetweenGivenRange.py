# Given an array of real numbers greater than zero in form of strings.
# Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .
# Return 1 for true or 0 for false.

# Example:

# Given [0.6, 0.7, 0.8, 1.2, 0.4] ,

# You should return 1

# as

# 0.6+0.7+0.4=1.7

# 1<1.7<2

# Hence, the output is 1.

class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        if len(A)<3:
            return 0
        A=[float(x) for x in A]
        a=A[0]
        b=A[1]
        c=A[2]
        for i in range(3,len(A)):
            if (a+b+c)>1 and (a+b+c)<2:
                return 1
            elif (a+b+c)>2:
                if (a>b and a>c):
                    a=A[i]
                elif(b>a and b>c):
                    b=A[i]
                else:
                    c=A[i]
            else:
                if (a<b and a<c):
                    a=A[i]
                elif(b<a and b<c):
                    b=A[i]
                else:
                    c=A[i]
                
        if (a+b+c)>1 and (a+b+c)<2:
            return 1 
        else:
            return 0