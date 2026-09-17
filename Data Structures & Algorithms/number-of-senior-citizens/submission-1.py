class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for string in details:
            age = int(string[11] + string[12])
            if age > 60:
                count += 1
        return count