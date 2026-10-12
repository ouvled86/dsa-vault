class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        pq = [(0, k)]
        ret = 0
        visits = set()

        while pq:
            curr_w, curr_u = heapq.heappop(pq)
            if curr_u in visits: continue
            visits.add(curr_u)
            ret = curr_w
    
            for new_u, new_w in edges[curr_u]:
                if new_u not in visits:
                    heapq.heappush(pq, (new_w + curr_w, new_u))
        
        return ret if len(visits) == n else -1