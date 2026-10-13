class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        nums_by_freq = defaultdict(list)

        for n in nums:
            freq_table[n] = 1 + freq_table.get(n, 0)
        for n, c in freq_table.items():
            nums_by_freq[c].append(n)

        end = len(nums)
        res = []
        while len(res) < k:
            for i in nums_by_freq[end]:
                res.append(i)
            end -= 1

        return res