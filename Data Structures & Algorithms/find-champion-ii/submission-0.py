class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams = set([n for n in range(n)])
        
        """
        {0, 1, 2, 3}
        [[2,0],[0,1],[2,3]]

        [2, 0]
        remove 0 from teams
        [0, 1]
        remove 1 from teams
        [2, 3]
        remove 3

        {2}
        """

        for e in edges:
            if e[1] in teams:
                teams.remove(e[1])

        return list(teams)[0] if len(teams) == 1 else -1