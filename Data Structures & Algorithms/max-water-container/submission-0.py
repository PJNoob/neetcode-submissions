class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        finalArea = 0

        while left < right:
            area = abs(min(heights[left], heights[right]) * (right - left))
            finalArea = max(finalArea, area)

            if (heights[left] < heights[right]):
                left += 1

            else:
                right -= 1

        return finalArea