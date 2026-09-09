class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_let = list(s)
        s_let.sort()
        t_let = list(t)
        t_let.sort()
        if s_let == t_let:
            return True
        return False


        