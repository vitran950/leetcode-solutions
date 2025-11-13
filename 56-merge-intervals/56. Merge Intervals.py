class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if stack[-1][1] >= curr[0]:
                prev = stack.pop()
                stack.append([prev[0], max(curr[1], prev[1])])
            else:
                stack.append(curr)

        return stack    