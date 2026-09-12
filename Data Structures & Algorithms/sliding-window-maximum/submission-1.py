class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # store indexes
        l, r = 0, 0
        # You want to store values in decreasing order. Store by index to make it easier
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: #Don't need the smaller values if the later index is greater
                q.pop()
            q.append(r)

            if l > q[0]: # Checks if max is in bounds of window
                q.popleft()
            
            if (r+1) >= k: # Makes sure that only appends the max after window is fully created
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

        