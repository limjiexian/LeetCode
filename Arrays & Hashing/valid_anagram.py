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
        
        """ hash map time: O(n + m), space: O(1) """
        # hash_map = {}
        
        # if len(s) != len(t):
        #     return False

        # for i in range(len(s)):
        #     s_char = s[i]
        #     t_char = t[i]

        #     hash_map[s_char] = 1 + hash_map.get(s_char, 0)
        #     hash_map[t_char] = hash_map.get(t_char, 0) - 1
        
        # for value in hash_map.values():
        #     if value > 0:
        #         return False

        # return True

        """ sorting: time -> O(nlogn + mlogm) space -> O(1)/O(n) depending on the sorting algo """
        # new_s = sorted(s)
        # new_t = sorted(t)

        # if new_s == new_t:
        #     return True
        # else:
        #     return False