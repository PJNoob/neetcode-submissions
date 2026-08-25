# * Sort the array so that we can use the two-pointer technique effectively.
# * Fix one number using i, and then find two other numbers whose sum is the negative of nums[i].
# * Skip duplicate values of i to avoid generating duplicate triplets.
# * Set left = i + 1 and right = last index to search for the remaining two numbers.
# * Calculate the sum of nums[i] + nums[left] + nums[right].
# * If the sum is 0, we found a valid triplet, so add it to the result.
# * After finding a triplet, skip duplicate values at left and right to avoid duplicate triplets.
# * Move both pointers inward after finding a valid triplet to search for another combination.
# * If the sum is less than 0, increase left because the array is sorted and we need a larger value.
# * If the sum is greater than 0, decrease right because we need a smaller value.
# * Continue until left and right meet, then move i to the next number and repeat.
# * Time complexity is O(n²) because we iterate through each number and perform a linear two-pointer search.
# * Space complexity is O(1) extra space, excluding the space required for the output.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums) - 2):

            if i > 0 and (nums[i] == nums[i - 1]):
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total == 0:
                    res.append([nums[left], nums[right], nums[i]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                
                elif total > 0:
                    right -= 1

                elif total < 0:
                    left += 1

        return res
        