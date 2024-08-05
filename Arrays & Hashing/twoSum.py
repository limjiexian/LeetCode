class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = array of integers
        # target = the number we want to see if nums contain 2 numbers that total up to this target number
        # store nums in hash, as we store, we also check if the complement can be found in our hashmap if so means we already found the index for the two sums

        numsHash = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in numsHash:
                return [numsHash[complement], index]
   
            numsHash[num] = index


