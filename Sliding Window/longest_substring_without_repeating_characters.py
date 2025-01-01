class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """ Brute Force """
        # max_count = 0
        # for i in range(len(s)):
        #     hash_set = set()
        #     count = 0 
        #     for j in range(i, len(s)):
        #         if s[j] in hash_set:
        #             break

        #         hash_set.add(s[j])
        #         count += 1
        #         max_count = max(max_count, count)

        # return max_count

        """ Sliding Window """
        l, r = 0, 0
        hash_set = set()
        count = 0
        max_count = 0
        
        while r < len(s):
            # if found duplicate
            # keep deleting l elements until we no longer have duplicate
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
                count -= 1

            hash_set.add(s[r])
            r += 1
            count += 1
            max_count = max(max_count, count)

        return max_count

