class Solution:
    def trap(self, height: List[int]) -> int:

        """ Brute Force """
        # n = len(height)

        # total_area = 0
        # for i in range(n):
        #     print()

        #     # global max left
        #     max_left = 0
        #     for j in range(0, i):
        #         max_left = max(max_left, height[j])
            
        #     max_right = 0
        #     for j in range(i+1, n):
        #         max_right = max(max_right, height[j])

        #     # print("max_left = ", max_left)
        #     # print("max_right = ", max_right)

        #     area = min(max_left, max_right) - height[i]

        #     if area > 0:
        #         total_area += area
        
        # return total_area
        
        """ Similar to Brute Force but O(n) instead """

        # n = len(height)

        # # starting both is 0
        # l_wall, r_wall = 0, 0

        # max_left = [0] * n
        # max_right = [0] * n

        # for i in range(n):
        #     j = n-1-i

        #     max_left[i] = l_wall
        #     max_right[j] = r_wall

        #     l_wall = max(l_wall, height[i])
        #     r_wall = max(r_wall, height[j])
        
        # total_area = 0

        # for i in range(n):
        #     potential_area = min(max_left[i], max_right[i])

        #     area = potential_area - height[i]

        #     total_area += max(0, area)
        
        # return total_area

        """ Two Pointer """

        n = len(height)
        l, r = 0, n-1
        max_left, max_right = height[l], height[r]

        total_area = 0
        i = 0 

        while l < r:
            if max_left < max_right:
                # we shift l pointer first, cos max_left is the wall that is left side of l
                l += 1

                area = max_left - height[l]
                total_area += max(0, area)
            
                # update new max_left
                max_left = max(max_left, height[l])
            else:
                r -= 1

                area = max_right - height[r]
                total_area += max(0, area)

                max_right = max(max_right, height[r])
        
        return total_area




