# Problem Description

# Given two Binary Trees A and B, you need to merge them in a single binary tree.

# The merge rule is that if two nodes overlap, then sum of node values is the new value of the merged node.

# Otherwise, the non-null node will be used as the node of new tree.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return the root node in the tree
    def solve(self, A, B):
        if not A:
            return B
        if not B:
            return A
        A.val+=B.val
        A.left=self.solve(A.left,B.left)
        A.right=self.solve(A.right,B.right)
        return A
