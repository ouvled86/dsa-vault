class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        unique_chars = set()
        i, j = 0, 1
        max_len = 1
        unique_chars.add(s[0])
        while j < len(s):
            curr_len = j - i + 1
            if s[j] not in unique_chars:
                max_len = max(max_len, curr_len)
                unique_chars.add(s[j])
            else:
                while s[i] != s[j]:
                    unique_chars.remove(s[i])
                    i += 1
                i += 1
                # if s[i] == s[j]:
                #     i += 1
                # else:
                #     i = j
                #     unique_chars.clear()
                #     unique_chars.add(s[i])
            j += 1
        return max_len