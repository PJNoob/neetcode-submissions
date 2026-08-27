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
                # print(f"left height: {height[left]}\nleftMax height: {height[leftMax]}\n left res: {res}")
                left += 1

            else:
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
                # print(f"right height: {height[right]}\nrightMax height: {height[rightMax]}\n right res: {res}")
                right -= 1

        return res