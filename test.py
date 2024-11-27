class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Given
        - string s

        Task
        - return longest substring of s that is a palindrome
        
        """

        res, sol = [], []

        def checkP(k):
            l, r = 0, len(k)-1

            while l < r:
                if k[l] == k[r]:
                    l += 1
                    r -= 1
                else:
                    return False
                
            return True

        # brute force
        def dfs(i):
            if i >= len(s):
                if checkP(sol[:]):
                    res.append("".join(sol[:]))
                return
            
            # include
            sol.append(s[i])
            dfs(i+1)
            sol.pop()

            # exclude
            dfs(i+1)
        
        dfs(0)

        return res[0]


s = Solution()
s.longestPalindrome(s="abbc")

            