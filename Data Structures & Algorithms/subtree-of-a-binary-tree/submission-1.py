# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isEqual(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        return p.val == q.val and self.isEqual(p.left, q.left) and self.isEqual(p.right, q.right)

    def findRootAndCheck(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val and self.isEqual(root, subRoot):
            return True
        return self.findRootAndCheck(root.left, subRoot) or self.findRootAndCheck(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        return self.findRootAndCheck(root, subRoot)