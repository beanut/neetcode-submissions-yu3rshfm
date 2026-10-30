class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.par = [i for i in range(n)]

    def find(self, u):
        # while vertex is not its own representative
        while u != self.par[u]:
            self.par[u] = self.par[self.par[u]]
            u = self.par[u]
        return u

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 == p2:
            return False # u and v are already connected
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        
        return True # u and v are united

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)

        emailToAccount = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAccount:
                    # if we reach here it means account a not only belongs to account a at index i, but it also belongs to account at index emailToAccount[a]
                    # this means we can perform a merge on these two indices
                    uf.union(i, emailToAccount[e])
                else:
                    emailToAccount[e] = i            
        
        emailGroup = defaultdict(set) # index of account -> [emails]

        for i, a in enumerate(accounts):
            par = uf.find(i)
            emailGroup[par].update(accounts[i][1:])
        
        res = []
        for (i, accs) in emailGroup.items():
            res.append([accounts[i][0]] + list(accs))

        return res