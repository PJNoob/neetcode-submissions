class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        map1 = [0]*26
        map2 = [0]*26

        for c in s1:
            map1[ord(c) - ord('a')] += 1

        for c in s2[:len(s1)]:
            map2[ord(c) - ord('a')] += 1

        if map1 == map2:
            return True

        for right in range(len(s1), len(s2)):

            left = right - len(s1)

            map2[ord(s2[right]) - ord('a')] += 1
            map2[ord(s2[left]) - ord('a')] -= 1

            if map1 == map2:
                return True

        return False

