class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = float(-inf)
        curr, ans = 0, 0
        for i in range(len(nums)):
            if prev >= nums[i]:
                curr = 0
            curr += nums[i]
            ans = max(ans, curr)
            prev = nums[i]
        return ans