class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # SCAN edges one by one
        adjList = [[] for _ in range(n + 1)] # 1-indexed

        # BFS connectedness helper
        def bfs(u, v):
            q = deque([u])
            visited = {u}

            while q:
                cur = q.popleft()

                for neigh in adjList[cur]:
                    if neigh == v:
                        return True
                    if neigh not in visited:
                        q.append(neigh)
                        visited.add(neigh)
                    
            return False

        for u, v in edges:
            if bfs(u, v):
                return [u, v]
            else:
                adjList[u].append(v)
                adjList[v].append(u)