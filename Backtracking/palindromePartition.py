from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Given a string s
        # Goal: 
        # - split s into substrings whereby every substring is a palindrome
        # - return all possible palindrome

        # palindrome == word that read the same backwards or forwards

        res = []
        part = []

        def backtrack(i):
            # base case
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return res
    
    def isPalin(self, s, i, j):
        l, r = i, j

        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1

        return True

# time complexity:
# at each char, we got two option, start new parition or extend the partition
# e.g. abc, we can either start new partition "a" or extend it to be "ab"
# say then next iteration, if previously we start new partition "a" means we can choose to start another new partition
# "b" or extend "bc"

# therefore we can say it will take 2^n time as we have 2^n choices
# since each choice we will run isPalin which take n time
# total time complexity = O(2^n * n)

# space complexity:
# recursion will take O(depth of the decision tree)
# worst case depth will be if we start new partition for each char, aka you partition the string into individual characters.
# so depth = len(word)

# res will have 2^n possible partitions, and for each parition their size will be worst case = n

# total space complexity = O(2^n * n)
