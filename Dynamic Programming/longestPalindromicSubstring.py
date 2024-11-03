# How it works
# - start from center, if satisfy palindrome, then we expand left & right both by 1
# - once done, we check if this new set is it longer than what we found so far? if so then update accordingly
# - basically for the above 2 step right, we simply just repeat it at different index.
# - so like, we start from l=r=i=0
# - so for every position in the string, we try to apply the expand from center
# - edge case will be, we need consider odd length palindrome and even length palindrome
# - for odd we do l, r = i, i cos [a b a]
# - for even we do l, r = i, i+1 cos [a b b a]

# Time complexity O(n^2) cos for each char we do while loop to check if we can expand 
# For each character, we expand outward to check if we can form a palindrome.
# In the worst case, this expansion could cover the entire string if the character is part of a long palindrome, 
# which would take up to O(n) per center.

# Space complexity O(1)
# since we never use any data struct to store, is just resL and resLength

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Palindrome = string that reads the same forward and backward
        # Goal
        # - return longest substring of s

        resL = 0
        resLength = 0

        for i in range(len(s)):
            # odd length
            # aba

            l, r = i, i

            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if resLength < (r - l + 1):
                    resL = l
                    resLength = r - l + 1

                l -= 1
                r += 1

            # even length
            l, r = i, i + 1

            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if resLength < (r - l + 1):
                    resL = l
                    resLength = r - l + 1

                l -= 1
                r += 1
            
        print(resL)
        print(resLength)
        return s[resL: resL + resLength]
    


