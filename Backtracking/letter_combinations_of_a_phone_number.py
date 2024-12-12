from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given:
        - string digits -> ranges from 2 ~ 9
        - each digit -> mapped to a set of char
            - a digit can represent any one of the char it maps to

        Task:
        - return all possible letter combinations that can be formed by the digits
        
        3 def
        4 ghi

        dg, dh, di

        eg, eh, ei 

        sol will be = ["d","g"]
        """

        map_digits = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        sol, res = [], []

        if digits == "":
            return []

        def dfs(i):
            if i >= len(digits):
                s = "".join(sol)
                res.append(s)
                return

            num = digits[i]

            for char in map_digits[num]:
                sol.append(char)
                dfs(i+1)
                sol.pop()

            return

        dfs(0)

        return res


            





