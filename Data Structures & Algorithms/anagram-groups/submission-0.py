class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            alpha_table = [0] * 26
            for c in s:
                alpha_table[ord(c) - ord('a')] += 1
            res[tuple(alpha_table)].append(s)
        
        return list(res.values())