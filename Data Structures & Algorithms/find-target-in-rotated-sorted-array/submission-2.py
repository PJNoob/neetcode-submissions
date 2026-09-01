# Start with two pointers, left at the beginning and right at the end of the array.
# Calculate mid to divide the current search space into two halves.
# First check if nums[mid] is the target. If it is, immediately return mid.
# Determine which half is sorted by comparing nums[left] with nums[mid].
# If nums[left] <= nums[mid], the left half is sorted.
# Check whether the target lies inside this sorted left half by checking nums[left] <= target <= nums[mid].
# If the target is inside the left half, move right to mid - 1 because we only need to search that half.
# If the target isn't inside the left half, move left to mid + 1 because the target must be in the other half.
# Otherwise, the right half is sorted because the left half contains the rotation point.
# Check whether the target lies inside the sorted right half using nums[mid] <= target <= nums[right].
# If the target is inside the right half, move left to mid + 1.
# Otherwise, move right to mid - 1 because the target must be in the other half.
# Continue until left > right. If the loop finishes without finding the target, return -1.

# Time Complexity: O(log n) because we eliminate roughly half of the search space at every iteration.
# Space Complexity: O(1) because we only use left, right, and mid.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
        