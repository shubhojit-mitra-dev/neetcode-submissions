class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: Dict[int] = Counter(nums) # {1: 3, 2: 2, 3: 1}
        freq: List[List[int]] = [[] for i in range(len(nums) + 1)]
        
        # [[], [3], [2], [1], [], [], []]
        for num, cnt in count.items():
            freq[cnt].append(num)

        res: List[int] = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
