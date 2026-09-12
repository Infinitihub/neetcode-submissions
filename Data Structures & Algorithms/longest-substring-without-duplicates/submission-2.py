class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0
        # l, r = 0,1
        # let_set = set(s[l])
        # max_length = 1
        # while r < len(s):
        #     if s[r] not in let_set:
        #         let_set.add(s[r])
        #         length = r - l + 1
        #         max_length = max(max_length, length)
        #         r+=1
        #     elif s[r] in let_set:
        #         let_set.remove(s[l])
        #         l += 1

        #         let_set.add(s[r])
        #         r += 1
        # return max_length

        let_set = set()
        l = 0
        length = 0

        for r in range(len(s)):
            while s[r] in let_set:
                let_set.remove(s[l])
                l +=1
            let_set.add(s[r])
            length = max(length, r-l+1)
        return length


        