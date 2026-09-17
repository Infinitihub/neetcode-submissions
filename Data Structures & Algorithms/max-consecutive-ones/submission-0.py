class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        max_count = 0
        for x in nums:
            if x == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                max_count = max(max_count, count)
                count = 0
        return max_count