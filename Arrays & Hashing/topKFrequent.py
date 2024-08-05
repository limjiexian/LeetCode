from typing import List

class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = int array
        # given k, return k most frequent elements
        # so like e.g. return k=3 aka top 3 most frequent elements

        # # SOL 1 nlogn time
        # # use hashmap then u can get all the frequency of the number
        # hashmap = {}
        # for num in nums:
        #     hashmap[num] = 1 + hashmap.get(num, 0)
        
        # # iterate through the hashmap and store the freq into heap data structure
        # heap = [(-freq, num) for num, freq in hashmap.items()]
        
        # heapq.heapify(heap)

        # topK = []
        # for i in range(k):
        #     # each pop will take log n
        #     # so we will have k log n time
        #     freq, num = heapq.heappop(heap)
        #     topK.append(num)
        
        # return topK

        # Sol 2 n time
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        # say total num of element is = 5
        # if we do len(freq) we will get = 5
        # and then the list will become 0,1,2,3,4
        # so need do len(nums) + 1 to make it become 0,1,2,3,4,5
        freq = [[] for i in range(len(nums)+1)]

        for num, c in hashmap.items():
            freq[c].append(num)

        output = []
        
        # since when we initialize the freq array, we set size = len(freq) + 1 which is = 6
        # but max count can only be 5 cos max # of element is 5
        # so must len(freq)-1 
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                output.append(n)
            if k == len(output):
                return output