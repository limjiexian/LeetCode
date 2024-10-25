from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Given string digits -> made up of digits from 2 to 9 (inclusive)
        # each digit is mapped to a set of chars
        # Goal:
        # - return all possible combi that digits could represent

        # 3 - DEF
        # 4 - GHI

        if len(digits) == 0:
            return []
        
        res =  []
        part = []

        mapH = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(i):
            # base case
            if i >= len(digits):
                ans = ""
                for c in part:
                    ans += c
                
                res.append(ans)
                return

            digitList = mapH[digits[i]]
            
            for c in digitList:
                part.append(c)
                backtrack(i+1)
                part.pop()
            
        backtrack(0)

        return res

        # Time Complexity:
        # - The number of digits is `n`.
        # - Each digit can map to approximately `m` characters (average case, m = 3 or 4 depending on the digit).
        # - So for each slot, you can choose m character. so since we got n digits
        # - The total number of combinations to explore is `m^n`.
        # - Constructing each combination involves concatenating `n` characters, which takes O(n) time.
        # - Therefore, the total time complexity is: O(m^n * n).

        # Space Complexity:
        # - The result list `res` will hold `m^n` combinations, each of length `n`.
        # - This requires O(m^n * n) space to store all possible combinations.
        # - The recursive call stack has a maximum depth of `n` (the length of the input string).
        # - Therefore, the total space complexity is: O(m^n * n).


