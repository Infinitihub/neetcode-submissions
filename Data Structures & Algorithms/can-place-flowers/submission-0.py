class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_bed = [0] + flowerbed + [0]

        l = 0
        r = 2
        count = 0
        for i in range(1, len(flowerbed)+1):
            if new_bed[l] == 0 and new_bed[r] == 0 and new_bed[i] == 0 and count != n:
                new_bed[i] = 1
                count += 1
            l += 1
            r += 1
        return count == n