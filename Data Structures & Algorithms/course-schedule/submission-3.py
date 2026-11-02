class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i : [] for i in range(numCourses)} # map course to prereqs
        for c, pre in prerequisites:
            adj[c].append(pre)

        state = [0] * numCourses

        """
        0 = unvisited
        1 = being visited
        2 = finished visiting
        """

        def dfs(node):
            if state[node] == 1:
                return False # cycle detected
            if not adj[node]:
                # no more prereqs --> course can be completed
                return True

            state[node] = 1
            for pre in adj[node]:
                if not dfs(pre):
                    return False
            state[node] = 2
            adj[node].clear()
            return True
        
        for c in range(numCourses):
            if state[c] != 2:
                if not dfs(c):
                    return False
        
        return True
