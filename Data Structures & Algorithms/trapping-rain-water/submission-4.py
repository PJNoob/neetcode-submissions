# Intuition

# Place two pointers at both ends of the array, with left at the beginning and right at the end.
# Maintain leftMax and rightMax to keep track of the highest wall encountered so far from the left and right sides.
# Compare height[left] and height[right] to decide which side can safely calculate trapped water.
# If height[left] <= height[right], process the left side because the right side currently has a wall at least as tall as the left wall.
# Update leftMax with the maximum height seen from the left so far.
# Calculate trapped water at the left position as leftMax - height[left]; if the current height is the tallest so far, this naturally gives 0.
# Move left one position to the right and continue processing.
# If height[left] > height[right], process the right side because the left side currently has a wall taller than the right wall.
# Update rightMax with the maximum height seen from the right so far.
# Calculate trapped water at the right position as rightMax - height[right].
# Move right one position to the left and continue processing.
# Add the trapped water at each position to res, which represents the total amount of water collected.
# Continue until left and right meet, meaning every relevant position has been processed.
# Return res, which is the total trapped water.


# The key intuition

# Water at a position depends on the shorter of the tallest walls on its left and right.
# Instead of calculating the left and right maximum for every position separately, we maintain leftMax and rightMax while moving inward.
# We process the side with the smaller current boundary, because that side determines the maximum water that can be trapped there.

# Complexity

# Time Complexity: O(n) — each pointer moves across the array at most once.
# Space Complexity: O(1) — only left, right, leftMax, rightMax, and res are used.

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0

        res = 0

        while left < right:
            if height[left] <= height[right]:
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
                left += 1

            else:
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
                right -= 1

        return res