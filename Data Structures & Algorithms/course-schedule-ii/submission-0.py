class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i : [] for i in range(numCourses)}
        for c, pre in prerequisites:
            adj[c].append(pre)

        state = [0] * numCourses
        """
        0 = unvisited
        1 = in DFS path
        2 = already visited
        """

        def dfs(node):
            if state[node] == 1:
                return []
            
            state[node] = 1
            path = []
            print(adj[node])
            for pre in adj[node]:
                # print(pre)
                if state[pre] != 2:
                    re = dfs(pre)
                    if not re:
                        return []
                    path.extend(re)
            state[node] = 2
            adj[node].clear()
            return path + [node]

        res = []
        for c in range(numCourses):
            if state[c] == 0:
                re = dfs(c)
                # print(re)
                if not re:
                    return []
                res.extend(re)
        return res
