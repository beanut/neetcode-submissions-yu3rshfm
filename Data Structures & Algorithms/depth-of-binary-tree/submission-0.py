# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # do a DFS 
    def recurse(self, root: Optional[TreeNode], cur: int) -> int:
        if not root:
            return cur
        
        return max(self.recurse(root.left, cur + 1), self.recurse(root.right, cur + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, 0)