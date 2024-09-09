from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Input: tokens = ["1","2","+","3","*","4","-"]

        # Output: 5

        # Explanation: ((1 + 2) * 3) - 4 = 5

        operations = {"+": lambda x, y: x + y,
                      "-": lambda x, y: x - y, 
                      "*": lambda x, y: x * y, 
                      "/": lambda x, y: int(x / y)} # to round to 0 when doing divison, instead of like e.g -1.5 round down to -2, we want round down to 0. thats when we use int(x/y)

        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
            # Why Subtraction Needs b - a
            # In the expression b - a for subtraction in RPN, here's the step-by-step reasoning:

            # Order of Operations:

            # In RPN, when an operator like - is encountered, it operates on the two most recent numbers from the stack.
            # For b - a, a is the number popped last and thus represents the second operand (right side of the operator). b is the number popped before a and represents the first operand (left side of the operator).
                y = int(stack.pop()) # 1
                x = int(stack.pop()) # 2    
                op = token # +
                val = operations[op](x,y)
                stack.append(val)
        

        return stack.pop()
            
sol = Solution()
# tokens=["2","1","+","3","*"]
tokens=["1","2","+","3","*","4","-"]

output = sol.evalRPN(tokens)
print(output)