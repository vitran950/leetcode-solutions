from heapq import *
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for key, val in counts.items():
            heappush(heap, (val, key))
            while len(heap) > k:
                heappop(heap)
        ans = [b for a,b in heap]
        return ans