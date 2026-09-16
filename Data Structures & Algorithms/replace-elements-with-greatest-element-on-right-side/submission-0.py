class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = float("-inf")
        res = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr) -1:
                res[i] = -1
                max_val = arr[i]
            else:
                res[i] = max_val
                max_val = max(max_val, arr[i])
        return res
            
            