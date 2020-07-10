# Problem Description

# Given a binary tree A with N nodes.

# You have to remove all the half nodes and return the final binary tree.

# NOTE:

# Half nodes are nodes which have only one child.
# Leaves should not be touched as they have both children as NULL.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, root):
        if root is None:
            return None
        root.left=self.solve(root.left)
        root.right=self.solve(root.right)
        if not root.left and not root.right:
            return root
        if not root.left:
            new_root=root.right
            temp=root
            root=None
            del(temp)
            return new_root
        if not root.right:
            new_root=root.left
            temp=root
            root=None
            del(temp)
            return new_root
        return root