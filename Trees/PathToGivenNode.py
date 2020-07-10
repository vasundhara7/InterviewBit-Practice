# Given a Binary Tree A containing N nodes.

# You need to find the path from Root to a given node B.

# NOTE:

# No two nodes in the tree have same data values.
# You can assume that B is present in the tree A and a path always exists.

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
        path=[]
        self.getpath(A,B,[],path)
        return path[0]
    
    def getpath(self,root,key,r,path):
        if not root:
            return
        if root:
            r.append(root.val)
            if root.val==key:
                path.append(r[:])
                return path
            else:
                self.getpath(root.left,key,r[:],path)
                self.getpath(root.right,key,r[:],path)

            
        
