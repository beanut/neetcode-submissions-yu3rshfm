# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root: Optional[TreeNode]) -> Int:
            if not root:
                return 1
            
            l = dfs(root.left)
            if l == -1:
                return -1

            r = dfs(root.right)
            if r == -1:
                return -1

            if abs(l - r) > 1:
                return -1
            
            return max(l, r) + 1
        
        return dfs(root) != -1