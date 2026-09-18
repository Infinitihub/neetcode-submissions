class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum():
                string += char.lower()

        l, r = 0, len(string) -1
        while l <= r:
            if string[l] != string[r]:
                return False
            else:
                l +=1
                r -=1
        return True

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         string = ""
#         for char in s:
#             if char.isalnum():
#                 string += char.lower()
#         if string == string[::-1]:
#             return True
#         return False
        