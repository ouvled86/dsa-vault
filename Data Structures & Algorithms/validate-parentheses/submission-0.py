class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = deque()

        for p in s:
            if parentheses:
                if ((parentheses[-1] == '[' and p == ']')
                    or (parentheses[-1] == '(' and p == ')')
                    or (parentheses[-1] == '{' and p == '}')):
                    parentheses.pop()
                    continue
            parentheses.append(p)
        
        return len(parentheses) == 0