class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            comp_area = min(heights[l], heights[r]) * (r-l)
            if comp_area > area:
                area = comp_area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return area
        