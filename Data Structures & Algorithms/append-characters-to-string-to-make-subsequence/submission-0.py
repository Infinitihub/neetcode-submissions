class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0

        n = len(s)
        m = len(t)

        while i < n and j < m:
            if s[i] == t[j]:
                j += 1
            i += 1
        return len(t[j:m])