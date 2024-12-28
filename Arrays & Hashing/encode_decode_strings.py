from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            size = len(s)
            res += str(size) + "#" + s
        
            print(res)
        return res

    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1  # move i to be infront of #
            j = i + length # infront of # + length of word 
            word = s[i:j]
            res.append(word)
            i = j

        return res
