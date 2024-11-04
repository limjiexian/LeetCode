
# Idea
# expand from center, slowly check the if valid palindrome as we expand
# each time we expand, it also means we found a new substring of palindrome, so count += 1
# do for even length and odd length palindrome

# Time complexity:
# O(n^2) * 2 ~= O(n^2)

# Space
# O(1) as we only use l, r, count

class Solution:
    def countSubstrings(self, s: str) -> int:
        # return number of substrings that are palindromes

        count = 0 

        for i in range(len(s)):
            # odd length palindrome
            l, r = i, i 

            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1

            l, r = i, i+1

            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1

        return count

            
