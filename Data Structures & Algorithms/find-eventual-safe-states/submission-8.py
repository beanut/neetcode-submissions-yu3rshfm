class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        sys.setrecursionlimit(15000)
        """
        0 = unvisited
        1 = in DFS path
        2 = fully visited/explored
        """
        state = [0] * len(graph)

        def dfs(node) -> bool:
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True

            state[node] = 1

            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            
            state[node] = 2
            return True
        
        return [n for n in range(len(graph)) if dfs(n)]
