class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ Brute Force """
        # new_str = ""
        # for char in s:
        #     if char.isalnum():
        #         new_str += char.lower()
        
        # print("new_str = ", new_str)
        
        # if new_str == new_str[::-1]:
        #     return True
        # else:
        #     return False

        """ Two Pointer O(n) and O(1) space """
        
        l, r = 0, len(s)-1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() == s[r].lower():
                l += 1 
                r -= 1
            else:
                return False
    
        return True

