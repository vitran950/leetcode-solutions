class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        ans = float("inf")
        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1

        return ans if ans != float("inf") else 0