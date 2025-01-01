class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """ Brute Force """
        # s1_counter = {}

        # for i in range(len(s1)):
        #     s1_counter[s1[i]] = 1 + s1_counter.get(s1[i], 0)
        
        # print("s1 = ", s1_counter.values())
        

        # for i in range(len(s2)-len(s1)+1):
        #     substring_counter = {}
        #     w2 = s2[i:i+len(s1)]

        #     for char in w2:
        #         substring_counter[char] = 1 + substring_counter.get(char, 0)
            
        #     # print("substring = ", substring_counter.values())
        #     # print(s1_counter == substring_counter)
        #     # print()

        #     if s1_counter == substring_counter:
        #         return True
        
        # return False

        """ Sliding Window """
        # our window size will be the size of s1
        # move the window until we reach the end of s2
        #     - each time we shift to the right
        #         - check if it matches with the substring in s2
        #         - return true if so
        
        # return false at the end

        # s1_counter = {}
        # s2_counter = {}

        # for i in range(len(s1)):
        #     s1_counter[s1[i]] = 1 + s1_counter.get(s1[i], 0)
            
        # print("s1_counter = ", s1_counter.items())
        # print()
        
        # l = 0
        # k = 0
        # for r in range(len(s2)):
        #     s2_counter[s2[r]] = 1 + s2_counter.get(s2[r], 0)
        #     k += 1

        #     if k > len(s1):
        #         s2_counter[s2[l]] -= 1

        #         if s2_counter[s2[l]] == 0:
        #             del s2_counter[s2[l]]

        #         l += 1 
        #         k -= 1
            
        #     print("s2_counter = ", s2_counter.items())
        #     print()

        #     if s1_counter == s2_counter:
        #         return True
            
        # return False

        """ Sliding Window Optimal """

        need_map = {}
        have_map = {}
        have = 0

        for i in range(len(s1)):
            need_map[s1[i]] = 1 + need_map.get(s1[i], 0)
        
        need = len(need_map)
        count = 0
        l = 0

        for r in range(len(s2)):
            have_map[s2[r]] = 1 + have_map.get(s2[r], 0)
            count += 1

            if s2[r] in need_map and need_map[s2[r]] == have_map[s2[r]]:
                have += 1
            
            if count > len(s1):
                if s2[l] in need_map and need_map[s2[l]] == have_map[s2[l]]:
                    have -= 1
                    
                have_map[s2[l]] -= 1
                l += 1

            if need == have:
                return True

        return False
        










        