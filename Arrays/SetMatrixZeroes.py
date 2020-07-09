# Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.

# Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.



# Input Format:

# The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.
# Output Format:

# Return a 2-d matrix that satisfies the given conditions.
# Constraints:

# 1 <= N, M <= 1000
# 0 <= A[i][j] <= 1
# Examples:

# Input 1:
#     [   [1, 0, 1],
#         [1, 1, 1], 
#         [1, 1, 1]   ]

# Output 1:
#     [   [0, 0, 0],
#         [1, 0, 1],
#         [1, 0, 1]   ]

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m=len(A)
        n=len(A[0])
        row=col=False
        
        for i in range(m):
            
            for j in range(n):
                
                if i==0 and A[i][j]==0:
                    
                    row=True
                
                
                if j==0 and A[i][j]==0:
                    
                    col=True
               
                if A[i][j]==0:
                    A[i][0]=0
                    A[0][j]=0
        
        for i in range(1,m):
            for j in range(1,n):
                if A[0][j]==0 or A[i][0]==0:
                    A[i][j]=0
        if row:
            for i in range(m):
            
                A[0][i]=0
        if col:
            for j in range(n):
            
                A[j][0]=0
        
        return A
                        
