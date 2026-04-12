# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS again
    ans = 0
    def recurse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = self.recurse(root.left)
        r = self.recurse(root.right)
        self.ans = max(self.ans, l + r)
        return 1 + max(l, r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recurse(root)
        return self.ans