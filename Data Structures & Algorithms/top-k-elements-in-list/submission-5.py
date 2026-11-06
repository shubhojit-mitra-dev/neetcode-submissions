class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: Counter[int] = Counter(nums)
        min_heap: List[tuple[int, int]] = []

        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for _, num in min_heap]