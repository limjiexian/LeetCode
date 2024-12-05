from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """ Sorting -> O(m * nlogn) """
        res = defaultdict(list)

        for s in strs:
            # sorted will return sorted strings in list
            # ['char1', 'char2', 'char3']
            # The join() method takes all items in an iterable and joins them into one string.
            sol = "".join(sorted(s))
            res[sol].append(s)
        
        return res.values()

        """ Hashing -> O(m * n) """
        # res = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26

        #     for char in s:
        #         count[ord("a") - ord(char)] += 1
            
        #     res[tuple(count)].append(s)
        
        # return res.values()