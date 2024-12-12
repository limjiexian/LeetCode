class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Given:
        - s

        Task:
        - return number of substrings within s that are palindromes

        """

        """ Brute Force O(n^3)"""

        # def check_palindrome(s1):
        #     l, r = 0, len(s1)-1

        #     while l < r:
        #         if s1[l] != s1[r]:
        #             return False

        #         l += 1
        #         r -= 1
            
        #     return True
        
        # count = 0 

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         word = s[i:j+1]
        #         if check_palindrome(word):
        #             count += 1
                
        # return count

        """ Two pointer """
        even_count = 0
        odd_count = 0
        for i in range(len(s)):
            # odd
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                even_count += 1
            
            # even
            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                l -= 1
                r += 1
                odd_count += 1

        
        total = even_count + odd_count 

        return total


