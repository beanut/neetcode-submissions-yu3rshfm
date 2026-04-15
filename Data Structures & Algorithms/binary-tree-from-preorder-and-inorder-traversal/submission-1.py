# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: 
            return None
        idx = {v:i for i,v in enumerate(inorder)}
        preIdx = 0

        def helper(l: int, r: int) -> Optional[TreeNode]: # [l, r] functions as an inclusive range
            nonlocal preIdx
            if l > r: 
                return None
            newNode = TreeNode(preorder[preIdx])
            mid = idx[preorder[preIdx]]
            preIdx += 1
            newNode.left = helper(l, mid - 1)
            newNode.right = helper(mid + 1, r)
            return newNode
        
        return helper(0, len(inorder) - 1)
