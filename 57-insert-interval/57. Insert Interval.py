class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        left = 0 
        right = len(intervals)-1
        target = newInterval[0]
        while left <= right: 
            mid = (left + right) // 2 # 1
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        intervals.insert(left, newInterval)
        
        result = []
        i = 0
        while i < len(intervals):
            if result and result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
            i += 1

        return result


        