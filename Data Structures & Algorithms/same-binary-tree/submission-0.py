# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def rec(root_p, root_q):
            if not root_p and not root_q:
                return True
            if not root_p or not root_q:
                return False
            
            left = rec(root_p.left, root_q.left)
            right = rec(root_p.right, root_q.right)

            equivalent = root_p.val == root_q.val 
            return equivalent and left and right

        return rec(p, q)