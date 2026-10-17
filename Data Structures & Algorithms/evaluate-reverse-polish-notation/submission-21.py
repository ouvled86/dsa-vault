class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evaluator = []

        for s in tokens:
            if len(s) > 1 or s.isdigit():
                evaluator.append(int(s))
            else:
                roperand = evaluator.pop()
                loperand = evaluator.pop()
                # operation = str(loperand) + s + str(roperand)
                res = 0
                if s == '+':
                    res = loperand + roperand
                elif s == '-':
                    res = loperand - roperand
                elif s == '*':
                    res = loperand * roperand
                else:
                    res = loperand / roperand
                evaluator.append(int(res))
      
        return evaluator.pop()
        