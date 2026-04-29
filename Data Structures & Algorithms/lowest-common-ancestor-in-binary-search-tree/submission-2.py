# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Three cases:
    # p <= cur <= q --> LCA == cur
    # p & q < cur --> lowestCommonAncestor(cur.left, p, q)
    # cur < p & q --> lowestCommonAncestor(cur.right, p, q)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        elif max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
