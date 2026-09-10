class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 # Two windows, left index and right index
        while numbers[l] + numbers[r] != target:
            #If greater than target, right index value is too big so decrease right pointer to decrease
            #Only works since sorted
            if numbers[l] + numbers[r] > target:
                r -= 1
            #If less than target, increase left pointer to increase
            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                l += 1
                r += 1
                return [l,r]
        l += 1
        r += 1
        return [l,r]