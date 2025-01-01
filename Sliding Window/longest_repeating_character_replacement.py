class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """ Sliding Window  O(n * 26)"""

        # l, r = 0, 0
        # max_length = 0
        # count = 0

        # freq_table = [0] * 26
        # while r < len(s):

        #     freq_table[ord(s[r]) - ord("A")] += 1

        #     while (r-l+1) - max(freq_table) > k:
        #         freq_table[ord(s[l]) - ord("A")] -= 1
        #         l += 1

        #     max_length = max(max_length, (r-l+1))

        #     r += 1
    
        # return max_length

        """ Sliding Window Optimal """

        # everytime we check max(freq_table) -> O(26)
        # technically we dont need to do this, by keeping track of the char with the max freq
        
        # max_length will only be maximised after we find a char with freq higher than our max freq seen so far
        # because our condition is length - max_freq <= k
        #     - essentially we want to maximise length right?
        #     - aka we want maximise max_freq also
        #     - cos max length will basically be max_freq + k

        l, r = 0, 0
        max_length = 0
        freq_counter = {}
        max_freq = 0

        for r in range(len(s)):
            freq_counter[s[r]] = 1 + freq_counter.get(s[r], 0)
            max_freq = max(max_freq, freq_counter[s[r]]) # O(1)

            if (r-l+1) - max_freq > k:
                freq_counter[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, (r-l+1))
            
        return max_length

