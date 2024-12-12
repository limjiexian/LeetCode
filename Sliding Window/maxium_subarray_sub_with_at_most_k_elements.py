    

    prefix_sum = [0] * len(nums)

    i = 0
    total = 0
    for num in nums:
        total += num
        prefix_sum[i] = total
        i += 1

    q = deque()

    max_subarray = float("-inf")

    for i in range(len(nums)):
        # remove indices that are out of bound
        if q and q[0] < i - k + 1:
            q.popleft()

        # maintain monotonic deque
        # check if this new element is larget than the elements inside the queue
        #   - if so, we pop all these right element out
        while q and prefix_sum[i] > prefix_sum[q[-1]]:
            q.pop()

        q.append(i)

        # we check the max subarray value for [i-k+1, i] range
        # but we only do this after we have at least processed k size subarray
        # e.g. if k = 3, i needs to be at least 2, then we can process 0, 1, 2
        if i >= k - 1 and q:
            max_subarray = max(max_subarray,  prefix_sum[q[0]] - prefix_sum[i-k])

    return max_subarray