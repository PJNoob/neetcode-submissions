class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arrS = set(nums)
        res = 0

        for num in arrS:
            if (num - 1) in arrS:
                continue
            count = 0
            while num in arrS:
                count += 1
                num += 1
            res = max(res, count)

        return res