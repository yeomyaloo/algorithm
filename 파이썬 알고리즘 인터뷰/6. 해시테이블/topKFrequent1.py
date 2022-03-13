import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        heap = []
        for i in freqs:
            heapq.heappush(heap, (-freqs[i],i))
        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(heap)[1])
        return topk