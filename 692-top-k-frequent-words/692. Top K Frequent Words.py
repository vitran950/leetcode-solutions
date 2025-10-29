from collections import Counter
from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = []
        for key, val in counts.items():
            heappush(heap, (-val, key))
        
        ans = []
        for _ in range(k):
            word = heappop(heap)[1]
            ans.append(word)

        return ans