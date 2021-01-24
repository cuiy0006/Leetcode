# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if left == None and right == None:
                return True
            elif right == None or left == None:
                return False
            
            if left.val != right.val:
                return False
            
            return helper(left.left, right.right) and helper(left.right, right.left)
        
        if root == None:
            return True
        return helper(root.left, root.right)
