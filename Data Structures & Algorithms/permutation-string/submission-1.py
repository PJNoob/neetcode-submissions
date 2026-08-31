class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for c in s1:
            map1[c] += 1

        for c in s2[:len(s1)]:
            map2[c] += 1

        if map1 == map2:
            return True

        for right in range(len(s1), len(s2)):
            map2[s2[right]] += 1

            left = right - len(s1)

            map2[s2[left]] -= 1

            if map2[s2[left]] == 0:
                del map2[s2[left]]

            if map1 == map2:
                return True

        return False