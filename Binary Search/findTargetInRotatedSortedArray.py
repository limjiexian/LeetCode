class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[r]:    # mid belongs to right portion
                # case 1
                # target smaller than nums[mid]
                # this means target wont be in right array as, nums[mid] is the smallest element in right array liao
                # therefore we will eliminate right array if this is true

                # case 2
                # target > nums[r]
                # nums[r] is the largest element in right array 
                # therefore, we will also eliminate right and go left if this is true

                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: 
                    l = mid + 1

                # nums = [5,6,0,1,2,3]
                # target = 0
                # mid = 1

            else:   # mid belongs to left portion

                # nums = [3,4,5,6,0,1,2]
                # target = 6
                # mid = 5
                
                # case 1 check if target < nums[l]
                # case 2 check if target > nums[mid]
                # if true we eliminate left and go right
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

