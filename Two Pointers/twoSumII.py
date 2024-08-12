class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array of integers sorted in non-decreasing order (aka same or ascending)
        # return indexes of two numbers that add up to target number
        # the two number cannot be the same value
        
        size = len(numbers)
        left, right = 0, (size - 1)
        
        while left < right:
            total = numbers[left] + numbers[right]
            
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                # 1-indexed means array indexes start from 1 instead of 0. so we need +1
                return [left+1, right+1]  

        



