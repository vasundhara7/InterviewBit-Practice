# Given a Binary Tree A consisting of N nodes.

# You need to find all the cousins of node B.

# NOTE:

# Siblings should not be considered as cousins.
# Try to do it in single traversal.
# You can assume that Node B is there in the tree A.
# Order doesn't matter in the output.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        if not A:
            return []
        if not A.left and not A.right:
            return []
        q=[]
        q.append(A)
        q.append(None)
        found=False
        while q and not found:
            while q[0] is not None:
                x=q.pop(0)
                if (x.left and x.left.val==B) or(x.right and x.right.val==B):
                    found=True
                else:
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
            q.pop(0)
            if len(q):
                q.append(None)
        
        ans=[]
        for i in q:
            if i is not None:
                ans.append(i.val)
        return ans
        
        
        
        