from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Given:
        - string s

        Task:
        - split s into substrings where every substrings is a palindrome

        Palindrome = read the same from front and from back
        """

        def check_p(word):
            l, r = 0, len(word)-1

            while l < r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            
            return True

        res, sol = [], []

        def dfs(i):
            # base case 
            if i >= len(s):
                res.append(sol[:])
                return
            
            for j in range(i, len(s)):
                word = s[i:j+1]
                # aab
                # a
                if check_p(word):
                    sol.append(word)
                    dfs(j+1)
                    sol.pop()
        
        dfs(0)
        
        return res








