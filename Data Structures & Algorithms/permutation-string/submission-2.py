class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):   return False

        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)

        matches = 0
        for i in range(26):
            if s1_count.get(chr(ord('a') + i)) == s2_count.get(chr(ord('a') + i)):
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)
            if s1_count.get(s2[r], 0) == s2_count.get(s2[r], 0):
                matches += 1
            elif s1_count.get(s2[r], 0) == s2_count.get(s2[r], 0) - 1:
                matches -= 1
            
            s2_count[s2[l]] = s2_count.get(s2[l], 0) - 1
            if s1_count.get(s2[l], 0) == s2_count.get(s2[l], 0):
                matches += 1
            elif s1_count.get(s2[l], 0) == s2_count.get(s2[l], 0) + 1:
                matches -= 1
            l += 1

        return matches == 26

