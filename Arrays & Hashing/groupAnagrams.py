from typing import List
from collections import defaultdict

""" class Solution:

    # why this initial method is bad
    # Mutability and Hashmap as Key:

    # Mutability: A key for a dictionary or a set must be immutable. Dictionaries (hashmaps) are mutable, meaning their contents can change (you can add, remove, or update key-value pairs). If you used a mutable object like a dictionary as a key, its hash value would change if its contents were modified. This would break the integrity of the dictionary’s internal structure because the key's hash value is used for lookups.
    # Hashability:

    # Hashability: To be used as a key in a dictionary or an element in a set, an object must be hashable. An object is hashable if it has a constant hash value throughout its lifetime, which allows it to be used in hash-based collections like dictionaries and sets.
    # Hashmaps (Dictionaries) and Hashability: In Python, dictionaries themselves are not hashable. This is because dictionaries are mutable. The hash value of a mutable object like a dictionary can change if its contents change, which makes it unsuitable for use as a key.
    # Why Hashmaps (Dictionaries) Are Not Hashable
    # Hash Function: Hashable objects need a consistent hash value, which is used by hash-based data structures for quick lookups.

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given array of strings -> strs
        # group anagrams into list of list 
        # anagrams = two set of words that are the same, is jsut that the letters are rearranged


        # lets try to identity anagrams first
        # if two words are anagrams, means their hash map will be the same
        # so we will first store all the strings into their respective hash map
        
        hashmaps = []
        for i in range(len(strs)):
            hashmap = {}
            
            for char in strs[i]:
                hashmap[char] = 1 + hashmap.get(char, 0)
            
            hashmaps.append(hashmap)

        returnList = []
        # group hashmap that are same
        for i in range(len(hashmaps)):
            list1 = []
            list1.append(strs[i])
            for j in range(i+1, len(hashmaps)):
                if hashmaps[i] == hashmaps[j]:
                    list1.append(strs[j])

            returnList.append(list1)
        
        return returnList """


class Solution:
    def groupAnagrams(self, strs: List[str] ) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # total we have 26 letters

            # a = 80
            # b = 81
            # ord is to get the asci character
            for char in s:
                count[ord(char) - ord("a")] += 1
            
            # need tuple the list, because list is mutable hence cant be used as a key in dict
            res[tuple(count)].append(s)
        return res.values()
                
sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]

output = sol.groupAnagrams(strs)

print(output)