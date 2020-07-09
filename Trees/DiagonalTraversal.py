# Consider lines of slope -1 passing between nodes.

# Given a Binary Tree A containing N nodes, return all diagonal elements in a binary tree belonging to same line.

# NOTE:

# See Sample Explanation for better understanding.
# Order does matter in the output.
# To get the same order as in the output traverse the tree same as we do in pre-order traversal.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if not A:
            return []
        d=dict()
        self.util(A,0,d)
        ans=[]
        for i in d:
            for j in d[i]:
                ans.append(j)
        return ans
    def util(self,root,dist,d):
        if root is None:
            return 
        if dist in d:
            d[dist].append(root.val)
        else:
            d[dist]=[root.val]
        self.util(root.left,dist+1,d)
        self.util(root.right,dist,d)
