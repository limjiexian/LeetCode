from collections import deque
from typing import List

def max_sum_subarray_at_most_k(nums: List[int], k: int) -> int:
    if not nums:
        return 0

    # Step 1: Compute prefix sum
    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]
    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    # Step 2: Initialize deque and max sum
    q = deque()  # Monotonic deque to store [index, effective_prefix_sum]
    max_sum = float('-inf')

    # Step 3: Iterate through the array
    for i in range(len(nums)):
        # Calculate the effective prefix sum
        effective_prefix = prefix_sum[i] - (prefix_sum[i - k] if i >= k else 0)

        # Remove elements outside the valid window
        if q and q[0][0] < i - k + 1:
            q.popleft()

        # Maintain monotonic deque: Remove smaller effective prefix sums
        while q and effective_prefix > q[-1][1]:
            q.pop()

        # Add the current effective prefix sum with its index to the deque
        q.append((i, effective_prefix))

        # Update the max subarray sum
        max_sum = max(max_sum, q[0][1] if q else 0)

    return max_sum
