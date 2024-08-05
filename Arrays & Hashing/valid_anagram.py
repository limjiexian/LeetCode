from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if t is an anagram of s then -> return True, else False
        # anagram == basically same word just that the letters are rearranged
        
        counterS, counterT = {}, {}

        if len(s) != len(t):
            return False

        for char in s:
            counterS[char] = 1 + counterS.get(char, 0)
        
        for char in t:
            counterT[char] = 1 + counterT.get(char, 0)

        if counterS == counterT:
            return True
        else:
            return False
        