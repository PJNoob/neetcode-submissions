# stiver video

# Start with two pointers, left at the beginning and right at the end of the array.
# Keep a res variable to store the smallest value found so far.
# Calculate mid to divide the current search space into two halves.
# Check whether the left half is sorted by comparing nums[left] with nums[mid].
# If nums[left] <= nums[mid], the left half is sorted, so nums[left] is the smallest element in that half.
# Update res with nums[left] because it could be the minimum.
# Move left to mid + 1 because if the array is rotated, the minimum could be in the other half.
# Otherwise, the left half is not sorted, which means the rotation point and therefore the minimum lies somewhere between left and mid.
# Update res with nums[mid] because nums[mid] could be the minimum.
# Move right to mid - 1 to continue searching the portion containing the minimum.
# Continue until left > right, meaning the search space has been completely processed.
# Return res, which contains the minimum value.

# Time Complexity: O(log n) because binary search cuts the search space roughly in half every iteration.
# Space Complexity: O(1) because you only use a few variables.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        res = float("infinity")

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid]:
                res = min(res, nums[left])
                left = mid + 1

            else:
                res = min(res, nums[mid])
                right = mid - 1

        return res