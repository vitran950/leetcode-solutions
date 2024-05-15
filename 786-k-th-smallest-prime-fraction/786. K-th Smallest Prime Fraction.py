import heapq
from collections import defaultdict

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        dictionary = defaultdict(list)
        heap = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fraction = arr[i] / arr[j]
                heap.append(fraction)
                dictionary[fraction] = [arr[i], arr[j]]
        heapify(heap)
        i = 0
        while i < k - 1:
            heapq.heappop(heap)
            i += 1
        return dictionary[heapq.heappop(heap)]
