class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for src,target,time in times:
            edges[src].append((target,time))
        
        minHeap = [(0,k)]
        t = 0
        visited = set()

        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            t = max(w1,t)
            visited.add(n1)
            for target, time in edges[n1]:
                if target not in visited:
                    heapq.heappush(minHeap,(time + w1,target))
        
        return t if len(visited) == n else -1