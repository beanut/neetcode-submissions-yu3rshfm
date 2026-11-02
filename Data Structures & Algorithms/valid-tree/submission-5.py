class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        comps = n
        par = [i for i in range(n)]
        rank = [1] * n

        def find(u):
            res = u
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(u, v):
            nonlocal comps
            pu, pv = find(u), find(v)
            if pu == pv:
                # u and v already connected
                return False
            
            if rank[pv] > rank[pu]:
                par[pu] = pv
                rank[pv] += rank[pu]
            else:
                par[pv] = pu
                rank[pu] += rank[pv]
            
            comps -= 1
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False # cycle detected
        
        return comps == 1
            
        
        
