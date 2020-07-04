# Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

# Example:

		
# Input: 	

# 1 2 3
# 4 5 6
# 7 8 9

# Return the following :

# [ 
#   [1],
#   [2, 4],
#   [3, 5, 7],
#   [6, 8],
#   [9]
# ]

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n=len(A)
        ans=[]
        
        for col in range(n):
            start_col=col
            start_row=0
            li=[]
            while start_col>=0 and start_row<n:
                li.append(A[start_row][start_col])
                start_col-=1
                start_row+=1
            ans.append(li)
        
        for row in range(1,n):
            start_row=row
            start_col=n-1
            li=[]
            while start_col>=0 and start_row<n:
                li.append(A[start_row][start_col])
                start_col-=1
                start_row+=1
            ans.append(li)
        return ans
