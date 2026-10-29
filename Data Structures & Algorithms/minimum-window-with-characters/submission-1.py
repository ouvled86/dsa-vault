class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_table = defaultdict(int)

        for ch in t:
            t_table[ch] += 1

        need = len(t_table)
        have = 0

        s_table = defaultdict(int)
        ret = None
        i, j = 0, 0
        while i < len(s):
            while i < len(s) and s[i] not in t_table:
                i += 1
            if i >= len(s):
                break
            
            j = max(i, j)
            while j < len(s) and have < need:
                ch = s[j]
                s_table[ch] += 1
                if ch in t_table and s_table[ch] == t_table[ch]:
                    have += 1
                j += 1

            if have == need:
                subs = s[i:j]
                if ret:
                    if len(subs) < len(ret):
                        ret = subs
                else:
                    ret = subs

            leaving_ch = s[i]
            if leaving_ch in t_table and s_table[leaving_ch] == t_table[leaving_ch]:
                have -= 1
                
            s_table[leaving_ch] -= 1
            i += 1

        return ret if ret else ""



