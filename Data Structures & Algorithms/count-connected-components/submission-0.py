class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = [[] for _ in range(n)]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()
        count = 0
        
        def bfs(node):
            visited.add(node)
            q = deque([node])

            while q:
                cur = q.popleft()

                for v in adjList[cur]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)

        for vt in range(n):
            if vt not in visited:
                bfs(vt)
                count += 1

        return count
