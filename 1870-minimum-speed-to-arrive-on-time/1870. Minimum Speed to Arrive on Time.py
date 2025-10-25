class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 > hour:
            return -1
        
        left = 1
        right = 10**7

        while left <= right:
            mid = (left + right) // 2
            temp = 0
            for i in range(len(dist) - 1):
                temp += ceil(dist[i] / mid)
            temp += dist[-1] / mid
            
            if temp <= hour:
                right = mid - 1
            else:
                left = mid + 1

        return left if left != 10**7 + 1 else -1