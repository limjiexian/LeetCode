class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # two integer arrays nums1, and nums2
        # size m and n respectively
        # sorted in ascending order
        # return median value among all the elements of the two arrays

        # array is sorted and that we need find an element -> this tells us that we need use binary search
        # solution is log(m+n) means we need perform binary search on each array individually

        # idea 
        # say we got len = 12
        # means we merged array will have 6
        # but we cant merge them together as that will take us O(n+m) time to go through the merging
        # so what we will do instead is, we will just obtain the first half of the "merged" array

        # we will perform binary search only on the smaller array
        # obtain our 3 elements and then go to the bigger array and get our other 3 elements


        # We assign nums1 and nums2 to A and B respectively for simplicity.
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)  # Total number of elements in both arrays.
        half = total // 2  # Halfway point of the combined array length.

        # Ensure A is the smaller array; if B is smaller, swap A and B.
        # This ensures we do binary search on the smaller array for efficiency.
        if len(B) < len(A):
            A, B = B, A

        # Initialize binary search boundaries for the smaller array A.
        l, r = 0, len(A) - 1
        
        # Start binary search to find the correct partition between A and B.
        while True:
            # i is the partition index for A, mid-point in binary search.
            i = (l + r) // 2
            # j is the partition index for B, calculated to ensure left and right sides of both arrays combine to half.
            j = half - i - 2  # Offset by 2 because indices start from 0.

            # Determine the elements just before and after the partition in A.
            # Aleft is the element just before the partition in A; if i is out of bounds (negative), we assign -infinity.
            Aleft = A[i] if i >= 0 else float("-infinity")
            # Aright is the element just after the partition in A; if i+1 exceeds the length of A, we assign infinity.
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            # Similarly, determine the elements just before and after the partition in B.
            # Bleft is the element just before the partition in B; if j is out of bounds (negative), we assign -infinity.
            Bleft = B[j] if j >= 0 else float("-infinity")
            # Bright is the element just after the partition in B; if j+1 exceeds the length of B, we assign infinity.
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Now, check if we have a valid partition.
            # A valid partition means all elements on the left of both partitions are less than or equal to all elements on the right.
            if Aleft <= Bright and Bleft <= Aright:
                # If the total number of elements is odd, the median is the middle element.
                # This will be the smaller of the two values on the right side (Aright and Bright).
                if total % 2:
                    return min(Aright, Bright)
                # If the total number of elements is even, the median is the average of the largest left-side element
                # and the smallest right-side element.
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # If the partition is not valid, adjust the search range.
            # If Aleft is greater than Bright, it means we need to move the partition in A to the left, 
            # because too many large elements are on the left side of A.
            elif Aleft > Bright:
                r = i - 1  # Move the search range left by adjusting the right boundary.

            # If Bleft is greater than Aright, it means we need to move the partition in A to the right, 
            # because too many small elements are on the left side of B.
            else:
                l = i + 1  # Move the search range right by adjusting the left boundary.
