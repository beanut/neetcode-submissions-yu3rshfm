# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(cur: TreeNode, curMax: int):
            nonlocal count
            if not cur:
                return
            
            if cur.val >= curMax:
                count += 1
            
            nextMax = max(cur.val, curMax)
            dfs(cur.left, nextMax)
            dfs(cur.right, nextMax)

        dfs(root, root.val)
        return count
