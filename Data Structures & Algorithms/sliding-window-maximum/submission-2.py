class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """

        """
        q = deque() # stores indixes

        res = []

        for i, n in enumerate(nums):
            # shrink window from left
            while q and q[0] <= i - k:
                q.popleft()

            # remove smaller elems
            while q and nums[q[-1]] <= n:
                q.pop()
            
            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res

