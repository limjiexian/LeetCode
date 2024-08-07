from typing import List

class Solution:

    # encode a list of strings INTO a single string
    def encode(self, strs: List[str]) -> str:
        # count the number, then put #
        
        encodedString = ""

        # count the freq, then attach freq & # to the lhs of the string then concatenate with encodedString
        for s in strs:
            size = len(s)
            encodedString = encodedString + str(size) + "#" + s

        print(encodedString)
        return encodedString
        
    # decode that single string back to list of strings
    def decode(self, s: str) -> List[str]:
        # so we will check number, keep move to the right, then once we get #, we will know the number of characters then only extract
        # that amt of characters
        decodedString = []

        count = ""
        i, j = 0, 0
        
        while i < len(s):
            # print("i = ", i)
            # print("s = ", s[i])

            if s[i] != "#":
                count = count + s[i]
                i += 1
            else:
                j = int(count) + i + 1
                sliced = s[i+1:j]
                # print("sliced = ", sliced)
                decodedString.append(sliced)
                i = j
                count = ""

        return decodedString
    
sol = Solution()
Input =  ["neet","code","love","you"]
# Input = [""]

fordecode = sol.encode(Input)
output = sol.decode(fordecode)

print(output)