from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        """ Brute Force """
        # n
        # ne
        # nee
        # neet
        #     c
        #     co
        #     cod
        #     code
        #         x 

        # slowly increase the length of the word we are dealing with
        #   - each increment, we check if this word we have so far isit in wordDict
        #   - if it is, we will then call dfs to explore the remaining length of the full word

        # def dfs(i):
        #     if i >= len(s):
        #         return True

        #     for j in range(i, len(s)):
        #         word = s[i:j+1]

        #         if word in wordDict:
        #             if dfs(j+1):
        #                 return True

        #     return False

        # return dfs(0)

        """ Cache """

        # memo = {}

        # def dfs(i):
        #     if i >= len(s):
        #         return True

        #     if i in memo:
        #         return memo[i]

        #     for j in range(i, len(s)):
        #         word = s[i:j+1]

        #         if word in wordDict:
        #             if dfs(j+1):
        #                 memo[i] = True
        #                 return memo[i]

        #     memo[i] = False
        #     return memo[i]

        # dfs(0)

        # return memo[0]


        """ Iterative Bottom Up start from 0 """
        # n = len(s) + 1
        # dp = [False] * (n) # + 1 cos we need include "" empty string case
        # dp[0] = True # cos dp[0] is a makeable as we dont need any word in wordDict to make it cos it is a empty string -> thats why True

        # for i in range(n):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in wordDict:
        #             dp[i] = True
        #             break # if we already found dp[i] is solvable then we dont need to continue loop our j so we break

        # return dp[-1]


        """ Iterative Bottom Up start from n"""
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # Base case: an empty string is always "segmentable"

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                word = s[i:j+1]
                
                if word in wordDict and dp[j+1]:
                    dp[i] = True
                
        return dp[0]

















