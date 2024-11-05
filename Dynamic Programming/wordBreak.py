from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Given:
        - string s
        - dict of strings wordDict, consist of unique words
        
        Goal:
        - return true if s can be segmented into a space-separated sequence of dictionary words
        
        we can reuse the words in the dictionary
        """
        ### Backtracking without Cache
        # def backtrack(i):
        #     # base case
        #     if i >= len(s):
        #         return True
            
        #     for word in wordDict:
        #         if (i + len(word)) <= len(s) and s[i:i+len(word)] == word:
        #             if backtrack(i+len(word)):
        #                 return True

        #     return False

        # return backtrack(0)

        ### Backtracking with Cache
        # dp = {i: -1 for i in range(len(s)+1)}
        # dp[len(s)] = True

        # def backtrack(i):
        #     # base case
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     for w in wordDict:
        #         if ((i + len(w)) <= len(s)) and (s[i:i+len(w)] == w):
        #             if backtrack(i+len(w)):
        #                 dp[i] = True
        #                 return True

        #     dp[i] = False
        #     return False

        # return backtrack(0)     


        ### Backtracking bottom up approach                
        dp = {i: False for i in range(len(s)+1)}
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w) <= len(s)) and (s[i:i+len(w)] == w):
                    dp[i] = dp[i+len(w)]

                # idk why if remove this break, it will break the code as well LOL maybe ask YX if got chance
                if dp[i]:
                    break
        
        return dp[0]


        """
        d[9] = True
        d[8] =


        d[0] = d[4]
        
        """






















