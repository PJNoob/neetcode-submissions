class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        l = 0
        r = 0
        length = 0

        while r < len(s):

            dic[s[r]] += 1
            while (dic[s[r]] > 1):
                dic[s[l]] -= 1
                l += 1

            length = max(length, r - l + 1)

            r += 1

        return length