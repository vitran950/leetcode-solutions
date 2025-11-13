class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        stack = []
        count = 0
        for i in range(len(timeSeries)):
            curr = timeSeries[i]
            if stack and stack[-1] >= curr:
                diff = abs(curr - stack[-1]) + 1 
                count += duration - diff
            else:
                count += duration
            stack.append(curr + duration - 1)
        return count