from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # two operands, then if got operator, pop these 2 operands
        stack = []
        operator = "+-*/"
        res = 0

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token in operator:
                b = int(stack.pop())
                a = int(stack.pop())

                if token == "+":
                    total = a + b
                elif token == "-":
                    total = a - b
                elif token == "*":
                    total = a * b
                else:
                    # longer method
                    # if (a/b) < 0:
                    #     total = math.ceil(a/b)
                    # else:
                    #     total = a // b

                    # Behavior of int()
                    # Truncates fractional parts (does not round):
                    # For positive numbers, it behaves like math.floor().
                    # For negative numbers, it behaves like math.ceil().

                    total = int(a/b)

                stack.append(total)
            else:
                stack.append(token)
        
        return stack[-1]
            