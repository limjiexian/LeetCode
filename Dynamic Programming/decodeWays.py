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

        dp = dp2 = 0
        dp1 = 1

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1
            
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp += dp2
            
            dp, dp1, dp2 = 0, dp, dp1
        
        return dp1
            