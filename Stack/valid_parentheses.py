class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_mapper = {
            "{" : "}",
            "(" : ")",
            "[" : "]",
            "{" : "}",
        }

        for char in s:
            if char in bracket_mapper:
                stack.append(char)
            else:
                if not stack:
                    return False

                item = stack.pop()

                if char != bracket_mapper[item]:
                    return False
        
        return True if not stack else False


