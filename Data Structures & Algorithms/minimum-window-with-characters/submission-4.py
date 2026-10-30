class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_table = defaultdict(int)

        for ch in t:
            t_table[ch] += 1

        need = len(t_table)
        have = 0

        s_table = defaultdict(int)
        i, j = 0, 0
        ret_len = math.inf
        ret_i, ret_j, = -1, -1

        while i < len(s):
            s_table[s[i]] += 1
            if s[i] in t_table and s_table[s[i]] == t_table[s[i]]:
                have += 1

            while have == need:
                if i - j + 1 < ret_len:
                    ret_len = i - j + 1
                    ret_i = i
                    ret_j = j
                s_table[s[j]] -= 1
                if s[j] in t_table and s_table[s[j]] < t_table[s[j]]:
                    have -= 1
                j += 1
            
            i += 1
                

        return s[ret_j:ret_i + 1] if ret_j >= 0 and ret_i >= 0 else ""



