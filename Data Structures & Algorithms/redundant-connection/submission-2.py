class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # 1-indexed
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(u) -> int:
            res = u

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            
            return res

        def union(u, v):
            p1 = find(u)
            p2 = find(v)

            if p1 == p2:
                return True # u and v are connected
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            return False
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
        
                
            