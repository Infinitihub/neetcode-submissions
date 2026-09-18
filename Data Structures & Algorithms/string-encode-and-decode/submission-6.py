class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) +'#'+s
        return encoded
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            count = int(s[i:j])
            res.append(s[j+1:j+count+1])
            i = j+count+1
        return res

