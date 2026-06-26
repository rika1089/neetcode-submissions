from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque()   # will store indices of useful elements
        ans = []

        for i in range(n):
            # Remove indices that are out of the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Append the maximum once the first window is formed
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans