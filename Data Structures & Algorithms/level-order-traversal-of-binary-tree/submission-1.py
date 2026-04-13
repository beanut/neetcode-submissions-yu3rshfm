# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = [] # List[List[int]]

        def dfs(cur: Optional[TreeNode], level: int):
            if not cur:
                return
            
            if len(store) == level:
                store.append([])
            
            store[level].append(cur.val)

            dfs(cur.left, level + 1)
            dfs(cur.right, level + 1)
        
        dfs(root, 0)

        return store

