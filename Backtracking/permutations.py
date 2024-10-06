class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Given an array nums of unique integers
        # Goal: return all possible permutations.
        n = len(nums)
        
        res, sol = [], []

        def backtrack():

            # base case 
            if n == len(sol):
                res.append(sol[:])
                return
            

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()

                    sol.pop()
        backtrack()

        return res

        # time complexity:
        # O(n!)
        """
        Because we are generating all possible permutations of n distinct elements and there are n! ways to arrange them.
        At each level of recursion, we have fewer choices (first n, then n-1, and so on), leading to n! permutations. Backtracking avoids reusing elements, ensuring each permutation is generated exactly once. 
        Therefore, the total time complexity is O(n!)

        TLDR:
        backtracking avoids invalid paths, and since there are only n! valid paths (the permutations), time complexity will be O(n!)
        """

        # space complexity:
        # res storage is n! * n, n! possible sol, for each solution is a list with size n, therefore O(n! *n)
        # recursion stack is = depth of tree = n = O(n)
        # total = O(n! *n + n) = O(n! * n)
