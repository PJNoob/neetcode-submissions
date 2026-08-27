# Intuition

# Place two pointers at the two ends of the array, with left at the beginning and right at the last index.
# Treat the two pointers as the walls of a container, where the width is the distance between them.
# Calculate the area using the shorter of the two heights multiplied by the width (right - left).
# Keep track of the maximum area found so far in finalArea.
# If the left height is smaller than the right height, move the left pointer one step to the right because only a taller left wall can potentially increase the area.
# Otherwise, move the right pointer one step to the left because the right wall is the limiting height.
# Never move the taller wall first, because the shorter wall determines the current container's height, and reducing the width while keeping the shorter wall cannot produce a larger area.
# Repeat the process until the two pointers meet, checking every potentially better container.
# Return the maximum area stored in finalArea.

# Why this works

# The width decreases every time a pointer moves.
# To compensate for the smaller width, we try to find a taller shorter wall by moving the pointer pointing to the shorter height.
# This guarantees an O(n) solution instead of checking all pairs.

# Complexity

# Time Complexity: O(n) because each pointer moves at most n times.
# Space Complexity: O(1) because only a few variables are used.

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