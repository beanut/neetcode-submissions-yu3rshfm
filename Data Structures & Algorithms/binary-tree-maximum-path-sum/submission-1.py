# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        curMax = float("-inf")

        def dfs(cur: Optional[TreeNode]) -> int:
            nonlocal curMax
            if not cur:
                return 0

            l = dfs(cur.left)
            r = dfs(cur.right)

            sigma = max(l + cur.val, r + cur.val, cur.val)
            curMax = max(curMax, cur.val + l + r, cur.val + max(l, r), cur.val)
            
            return sigma
        
        dfs(root)
        return curMax

