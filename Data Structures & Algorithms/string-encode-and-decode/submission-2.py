class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}-{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        print(s.find('-'))
        while s:
            dash_index = s.find('-')
            s_size = int(s[0:dash_index]) + dash_index + 1
            res.append(s[dash_index + 1 : s_size])
            s = s[s_size:]


        return res

