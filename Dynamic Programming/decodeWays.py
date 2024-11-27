# 440pm Start
# 510pm Stop attempt
# 540pm Finish youtube sol

# idea
# In bottom-up, we check this condition to decide whether:
# dp[i] should include dp[i + 2] (for a two-character decoding).
# Or just dp[i + 1] (for a single-character decoding).

class Solution:
    def numDecodings(self, s: str) -> int:
        # Decode Requirement
        # - group digits
        # - mapped them back to letters
        # 01 cannot be mapped into a letter because it contains a leading zero

        # Goal
        # - return the number of ways to decode a string s

        """ DFS brute force """
        # def dfs(i):
        #     # base case 
        #     if i == len(s):
        #         return 1

        #     if s[i] == "0":
        #         return 0

        #     count = dfs(i+1)

        #     if i+1 < len(s) and int(s[i:i+2]) <= 26:
        #         count += dfs(i+2)

        #     return count

        # return dfs(0)

        
        """ DFS cache """
        # memo = {i: -1 for i in range(len(s))}

        # def dfs(i):
        #     if i == len(s):
        #         return 1

        #     if memo[i] != -1:
        #         return memo[i]
            
        #     if s[i] == "0":
        #         return 0

        #     memo[i] = dfs(i+1)  
            
        #     if i+1 < len(s) and int(s[i:i+2]) <= 26:
        #         memo[i] += dfs(i+2)
            
        #     return memo[i] 

        # dfs(0)

        # return memo[0] if memo[0] != -1 else 0

        """ Iterative Bottom up """

        # memo = [0] * (len(s) + 1)
        # memo[len(s)] = 1  # Base case: one way to decode an empty string

        # for i in range(len(s)-1, -1, -1):
        #     if s[i] == "0":
        #         memo[i] = 0
        #     else:
        #         memo[i] = memo[i+1]

        #         if i+1 < len(s) and int(s[i:i+2]) <= 26:
        #             memo[i] += memo[i+2]

        # return memo[0]

        """ Two Pointer """
        front, back = 1, 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                current = 0
            else:
                current = front

                if i+1 < len(s) and int(s[i:i+2]) <= 26:
                    current += back
                
            temp = front
            front = current
            back = temp
        
        return front
            