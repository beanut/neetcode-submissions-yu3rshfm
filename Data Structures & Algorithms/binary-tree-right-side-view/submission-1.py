# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        store = []

        def dfs(cur: Optional[TreeNode], level: int):
            if not cur:
                return 
            
            if level == len(store):
                store.append(0)
            
            store[level] = cur.val

            dfs(cur.left, level + 1)
            dfs(cur.right, level + 1)
        
        dfs(root, 0)

        return store