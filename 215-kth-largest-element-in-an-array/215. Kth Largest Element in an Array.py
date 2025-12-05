from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        flip = [-element for element in nums]
        heapify(flip)
        for _ in range(k-1):
            heappop(flip)
        return -flip[0]