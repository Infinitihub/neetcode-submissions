class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Basically make check if number is start of sequence
        #Start is defined if n -1 is not in the array
        #If it is, then count how long it is
        num_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in num_set:
                length = 0
                while (num+length) in num_set:
                    length +=1
                longest = max(length, longest)
        return longest
        