class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]
            if start > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1] = [ans[-1][0], max(end, ans[-1][1])]
        return ans