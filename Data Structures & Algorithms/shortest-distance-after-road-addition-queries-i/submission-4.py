class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        queries always go from smaller to larger number
        bfs approach
        """
        connections = defaultdict(list)
        res = []

        def bfs():
            q = deque([0])
            level = 0
            visited = {0}

            while q:
                level_size = len(q)

                for _ in range(level_size):
                    node = q.popleft()
                    if node == n - 1:
                        res.append(level)
                        return
                    
                    neighs = [node + 1] + connections[node]
                    for neigh in neighs:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
                
                level += 1
        
        for query in queries:
            connections[query[0]].append(query[1])
            bfs()
        
        return res
                
                

