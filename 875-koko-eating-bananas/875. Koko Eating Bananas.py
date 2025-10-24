class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]

        while left <= right:
            mid = (left + right) // 2
            temp = 0
            for pile in piles:
                temp += ceil(pile / mid)
            if temp <= h:
                right = mid - 1
            else:
                left = mid + 1
                
        return left
