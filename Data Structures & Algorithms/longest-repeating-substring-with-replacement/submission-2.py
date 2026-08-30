class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(int)
        left = 0
        right = 0
        maxLength = 0

        while right < len(s):
            freqMap[s[right]] += 1
            if (right - left + 1) - max(freqMap.values()) > k:
                freqMap[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
            right += 1

        return maxLength