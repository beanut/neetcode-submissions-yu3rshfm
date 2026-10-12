from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([amount])
        distance = {amount : 0} # amount left : number of coins needed

        while q:
            cur = q.popleft()

            if cur == 0:
                return distance[0]
            
            for c in coins:
                rem = cur - c

                if rem >= 0 and rem not in distance:
                    distance[rem] = 1 + distance[cur]
                    q.append(rem)
        
        return -1
                