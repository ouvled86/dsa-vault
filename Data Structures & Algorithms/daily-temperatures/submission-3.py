class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        res = [0] * l
        warmer = []
        
        for i in range(0, l):
            if not warmer:
                warmer.append((temperatures[i], i))
            else:
                while warmer and warmer[-1][0] < temperatures[i]:
                    curr = warmer.pop()
                    res[curr[1]] = i - curr[1]
                warmer.append((temperatures[i], i))

        return res

