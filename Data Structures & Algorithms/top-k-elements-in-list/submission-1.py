class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        abc = defaultdict(int)
        # abc = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            # abc[num] = 1 + abc.get(num, 0)
            abc[num] += 1
        
        for n, v in abc.items():
            freq[v].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if k == len(res):
                    return res

