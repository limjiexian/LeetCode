from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given:
            - nums
            - k
        
        Return:
            - the k most frequent elements within the array
                - we will always have unique ans

        """
        """ Sorting """
        # hash_map = {}

        # # count the freq of each num and store them into hash map
        # for num in nums:
        #     hash_map[num] = 1 + hash_map.get(num, 0)

        # arr = []

        # for num, freq in hash_map.items():
        #     arr.append([freq, num])
        
        # arr.sort()
        
        # res = []
        # for i in range(k):
        #     top_num = arr.pop(-1)
        #     res.append(top_num[1])
        
        # return res

        """ Heap """
        # hash_map = {}

        # # count the freq of each num and store them into hash map
        # for num in nums:
        #     hash_map[num] = 1 + hash_map.get(num, 0)

        # heap = []

        # for num, freq in hash_map.items():
        #     heapq.heappush(heap, [freq, num])

        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # res = []

        # while heap:
        #     res.append(heapq.heappop(heap)[1])
        
        # return res

        """ Bucket Sort """
        freq_table = [[] for i in range(len(nums)+1)]

        hash_map = {}

        # count the freq of each num and store them into hash map
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)

        for num, freq in hash_map.items():
            freq_table[freq].append(num)
        
        res = []

        for i in range(len(freq_table)-1, -1, -1):
            for num in freq_table[i]:
                res.append(num)
                k -= 1

                if k == 0:
                    return res

        return res

        # [represent the freq count]
        # [the element that has that amount of freq ]
