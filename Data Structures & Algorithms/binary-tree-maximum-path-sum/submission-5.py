# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res

            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            curMax = max(l + node.val + r, l + node.val, node.val + r, node.val)
            
            res = max(res, curMax)

            return max(l + node.val, node.val + r, node.val)
        
        _ = dfs(root)

        return res