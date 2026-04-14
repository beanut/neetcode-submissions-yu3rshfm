# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(cur: Optional[TreeNode], lower: int, upper: int) -> bool:
            if not cur:
                return True
            if not lower < cur.val < upper:
                return False
            
            return dfs(cur.left, lower, cur.val) and dfs(cur.right, cur.val, upper)

        return dfs(root, float("-inf"), float("inf"))