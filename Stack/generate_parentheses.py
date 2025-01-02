from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """ DFS """
        # if n == 3
        # means we have 3 opening and 3 closing
        # at any point we must always have more opening than closing
        # e.g. can have 3 opening and 0 closing, but we can never have 3 closing and 0 opening. this wont be valid
        
        res, sol = [], []

        if n == 0:
            return ""

        def dfs(o, c):
            if o == n and c == n:
                joined_string = "".join(sol)
                res.append(joined_string)
                return
            
            if o > n or c > n:
                return

            if c > o:
                return

            # add open
            sol.append("(")
            dfs(o+1, c)
            sol.pop()

            # add close
            if o > c:
                sol.append(")")
                dfs(o, c+1)
                sol.pop()
        
        dfs(0, 0)

        return res
            


        