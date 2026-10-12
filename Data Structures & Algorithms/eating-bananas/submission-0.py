class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        rate = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            time_taken = 0
            for p in piles:
                time_taken += math.ceil(p / mid)
            if time_taken <= h:
                rate = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return rate




