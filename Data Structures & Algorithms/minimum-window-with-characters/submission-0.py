class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        tmap = Counter(t)
        smap = {}

        have = 0
        need = len(tmap)
        res = ""
        min_len = float("inf")

        l = 0
        for r in range(len(s)):
            char = s[r]
            smap[char] = 1 + smap.get(char, 0)

            if char in tmap and smap[char] == tmap[char]:
                have += 1

            # Contract from the left once all conditions are satisfied
            while have == need:
                window_len = r - l + 1
                if window_len < min_len:
                    min_len = window_len
                    res = s[l : r + 1]

                # Remove the left character
                left_char = s[l]
                smap[left_char] -= 1
                if left_char in tmap and smap[left_char] < tmap[left_char]:
                    have -= 1
                l += 1

        return res