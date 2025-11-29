class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                old_temp, spot = stack.pop()
                ans[spot] = i - spot
            stack.append((temperature, i))
        return ans