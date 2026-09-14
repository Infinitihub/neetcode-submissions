class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_dict = defaultdict(int)
        for val in nums:
            map_dict[val] += 1
            if map_dict[val] > 1:
                return True
        return False