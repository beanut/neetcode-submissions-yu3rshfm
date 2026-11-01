# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, pathMax):
            nonlocal res
            if not node:
                return
            if pathMax <= node.val:
                res += 1
            nextMax = max(pathMax, node.val)
            if node.left:
                dfs(node.left, nextMax)
            if node.right:
                dfs(node.right, nextMax)

        dfs(root, root.val)

        return res