from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        6:05
        tree = connected and no loops
        """

        adjList = [[] for _ in range(n)]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = {0}
        q = deque([(0, -1)])

        def bfs() -> bool:
            while q:
                cur, parent = q.popleft()

                for v in adjList[cur]:
                    if v != parent:
                        if v in visited:
                            return False
                        q.append((v, cur))
                        visited.add(v)
            
            return True

        return bfs() and len(visited) == n

            
            
