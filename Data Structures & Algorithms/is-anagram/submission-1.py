class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_total = 0
        t_total = 0

        for i in range(len(s)):
            s_total += ord(s[i]) * ord(s[i])
            t_total += ord(t[i]) * ord(t[i])

        return s_total == t_total