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
            if char.isalnum():
                newS = newS + char

        # check if reading forward == reading backward
        # if string = 5
        # 5 // 2 = 2

        size = len(newS)

        for i in range(size // 2):
            j = size - i - 1

            if newS[i] != newS[j]:
                return False

        return True





sol = Solution()

s = "race a car"

output = sol.isPalindrome(s)

print(output)