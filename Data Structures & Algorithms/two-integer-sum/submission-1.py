class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for i, x in enumerate(nums):
            check = target - x
            if check in sum_map:
                return [sum_map[check], i]
            sum_map[x] = i
            
        