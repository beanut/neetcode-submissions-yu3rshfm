class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]

        for source, target, time in times:
            adj[source].append((target, time))
        
        heap = [(0, k)]
        visited = set()
        t = 0
        while heap:
            edge, vertex = heapq.heappop(heap)
            if vertex in visited:
                continue
            visited.add(vertex)
            t = edge
            for next_vertex, next_time in adj[vertex]:
                if next_vertex not in visited:
                    heapq.heappush(heap, (next_time + edge, next_vertex))
        
        return t if len(visited) == n else -1

