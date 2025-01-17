import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            distance = math.sqrt(points[i][0]**2 + points[i][1]**2)
            heappush(heap, (-distance, i))
            if len(heap) > k:
                heappop(heap)
        
        result = []
        for dist in heap:
            element = dist[1]
            result.append(points[element])
        
        return result