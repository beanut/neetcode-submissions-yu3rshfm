# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        store = []

        def inorder(cur: Optional[TreeNode]):
            if not cur:
                return
            if cur.left:
                inorder(cur.left)
            store.append(cur.val)
            inorder(cur.right)
        
        inorder(root)
        return store[k - 1]


        
        