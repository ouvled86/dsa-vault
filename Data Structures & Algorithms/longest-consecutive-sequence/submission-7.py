class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        lookup = set()

        for n in nums:
            lookup.add(n)
        
        res = 0
        for n in nums:
            if n - 1 in lookup:
                continue
            s = 1
            num = n + 1
            lookup.discard(n)
            while num in lookup:
                s += 1
                num += 1
                lookup.discard(num - 1)
            res = max(res, s)
       
        return res