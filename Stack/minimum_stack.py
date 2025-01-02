""" Two Stack """
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_stack = []
        
#     def push(self, val: int) -> None:
#         stack = self.stack
#         min_stack = self.min_stack

#         stack.append(val)
        
#         if min_stack:
#             min_val = min(min_stack[-1], val)
#             min_stack.append(min_val)
#         else:
#             min_stack.append(val)
        
#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]

""" One Stack """
class MinStack:

    def __init__(self):
        self.stack = []    # [val, min_val so far]

    def push(self, val: int) -> None:
        stack = self.stack
        
        if stack:
            min_val = min(stack[-1][1], val)
            stack.append([val, min_val])
        else:
            stack.append([val, val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
