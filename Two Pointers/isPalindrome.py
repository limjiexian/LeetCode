class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindrome == after remove digits, convert all to lower case, this phrase is the same when u read it forward or backward

        # Attempt thought process
        
        # convert to lowercase
        # remove non-alphanumeric characters
        newS = ""

        if s == "":
            return True

        s = s.lower()

        for char in s:
            # if char.isdigit() or char.isalpha():
            #     newS = newS + char

            # if char.isalnum():
            #     newS = newS + char



        # check if reading forward == reading backward
        # if string = 5
        # 5 // 2 = 2

        size = len(newS)

        for i in range(size // 2):
            j = size - i - 1

            if newS[i] != newS[j]:
                return False

        # alternatively we can also reverse the string
        # but this will use more memory as we are creating a reversed ver of the string
        # e.g. newS == newS[::-1]

        return True


# neetcode solution
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1

#         while l < r:
#             while l < r and not self.alphaNum(s[l]):
#                 l += 1
#             while r > l and not self.alphaNum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l, r = l + 1, r - 1
#         return True
    
#     def alphaNum(self, c):
#         return (ord('A') <= ord(c) <= ord('Z') or 
#                 ord('a') <= ord(c) <= ord('z') or 
#                 ord('0') <= ord(c) <= ord('9'))




sol = Solution()

s = "race a car"

output = sol.isPalindrome(s)

print(output)