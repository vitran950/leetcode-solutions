import heapq
from collections import defaultdict

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        hash = defaultdict(list)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fraction = arr[i] / arr[j]
                # Use negative fraction because heapq is a min heap
                heapq.heappush(heap, -fraction)
                hash[-fraction] = [arr[i], arr[j]]
                if len(heap) > k:
                    heapq.heappop(heap)
        return hash[heapq.heappop(heap)]
