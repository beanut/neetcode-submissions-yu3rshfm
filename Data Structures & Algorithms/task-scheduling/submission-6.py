class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        # max-heap of frequencies
        maxHeap = [c for c in cnt.values()]
        heapq.heapify_max(maxHeap)

        # priority queue of tasks under cooldown
        cooldown = deque()

        time = 0

        while maxHeap or cooldown:
            
            if not maxHeap:
                # this is where I fumbled
                # need to -1 cuz +1 later
                time = cooldown[0][1] - 1 # oldest element in the deque (smallest time)
            else:
                cur = heapq.heappop_max(maxHeap) - 1
                if cur:
                    cooldown.append((cur, time + n + 1))

            time += 1
            
            if cooldown and cooldown[0][1] == time:
                rem, ready = cooldown.popleft()
                heapq.heappush_max(maxHeap, rem)
        
        return time

