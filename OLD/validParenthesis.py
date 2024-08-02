# # First Attempt
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         size = len(s)

#         dict = {"]": "[", ")": "(", "}": "{"}
        
#         # sanity check
#         if s == "":
#             return True
        
#         if size == 1:
#             return False

#         stack.append(s[0])

#         for i in range(1, size):
#             v1 = s[i]

#             if v1 in dict and stack:
#                 v2 = stack.pop()
#                 if v2 == dict[v1]:
#                     continue
#                 else:
#                     return False
#             stack.append(s[i])

#         if not stack:
#             return True
#         else:
#             return False

# 1st Attempt After reading Solution
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         dict = {"]": "[", ")": "(", "}": "{"}

#         if len(s) == 1:
#             return False

#         for char in s:
#             if char in set("({["):
#                 stack.append(char)
#             else:
#                 if stack:
#                     if dict[char] != stack.pop():
#                         return False
#                 else:
#                     return False
#         if stack:
#             return False
#         else: 
#             return True

# 2nd Attempt After reading Solution
class Solution():
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]": "[", ")": "(", "}": "{"}

        # if Left bracket then we append
        # if Right bracket, stack is not empty then we check top item is it the opposite bracket if it i not means false
        # if Right bracket, stack is empty then return false
        
        for char in s:
            if char in set("({["):
                stack.append(char)
            else:
                if not stack or dict[char] != stack[-1]:
                    return False
                else:
                    stack.pop()

        return not stack

sol = Solution()

s = "()"
# s = "()[]{}"
# s = "(]"
# s ="(){}}{"

result = sol.isValid(s)

print(result)

