class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights)-1
        while left < right:
            l_Value = heights[left]
            r_Value = heights[right]
            area = min(l_Value, r_Value) * (right - left)
            max_area = max(area, max_area)
            if l_Value < r_Value:
                left += 1
                while heights[left] < l_Value:
                    left += 1
            else:
                right -= 1
                while heights[right] < r_Value:
                    right -= 1
        return max_area
