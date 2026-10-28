class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Tree => No loops, connected

        """
        
        adj = defaultdict(list)

        for c in connections:
            adj[c[0]].append((c[1], 1))
            adj[c[1]].append((c[0], 0))
        
        q = deque([0])
        visited = {0}
        reversals = 0

        while q:
            cur = q.popleft()

            for neigh, shouldReverse in adj[cur]:
                if neigh not in visited:
                    reversals += 1 if shouldReverse else 0
                    q.append(neigh)
                    visited.add(neigh)
        
        return reversals

            
