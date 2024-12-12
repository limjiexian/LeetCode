class Solution:
    def numDecodings(self, s: str) -> int:
        """ Brute Force """
        # def dfs(i):
        #     # base case
        #     if i >= len(s):
        #         return 1
            
        #     # cannot select digit if that digit is == 0
        #     if s[i] == "0":
        #         return 0

        #     # select 1 digit
        #     count = dfs(i+1)

        #     # select 2 digit
        #     # cannot select 2 if it is > 26
        #     if i+1 < len(s) and int(s[i:i+2]) <= 26:
        #         count += dfs(i+2)   

        #     return count
        
        # return dfs(0)
        
        """ With Cache """
        # memo = {}
        
        # def dfs(i):
        #     if i >= len(s):
        #         return 1

        #     if i in memo:
        #         return memo[i]
            
        #     if s[i] == "0":
        #         return 0

        #     memo[i] = dfs(i+1)

        #     if i+1 < len(s) and int(s[i:i+2]) <= 26:
        #         memo[i] += dfs(i+2)
            
        #     return memo[i]

        # dfs(0)

        # return 0 if 0 not in memo else memo[0]

        """ Iterative Bottom up """
        # dp = {len(s) : 1}

        # for i in range(len(s)-1, -1, -1):
        #     if s[i] == "0":
        #         dp[i] = 0
        #         continue
        #     else:
        #         dp[i] = dp[i+1]
            
        #     if i+1 < len(s) and int(s[i:i+2]) <= 26:
        #         dp[i] += dp[i+2]

        # return dp[0]

        """ Two Pointer """
        
        # 226 1 0
        #   c f b

        front, back = 1, 0


        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                current = 0
            else:
                current = front

            if i+1 < len(s) and s[i] != "0" and int(s[i:i+2]) <= 26:
                current += back
            
            current, front, back = 0, current, front
        
        return front
            





