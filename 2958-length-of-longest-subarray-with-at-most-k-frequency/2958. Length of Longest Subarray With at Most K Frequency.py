from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        temp = defaultdict(int)
        result = 0

        for right in range(len(nums)):
            temp[nums[right]] += 1
            while temp[nums[right]] > k:
                temp[nums[left]] -= 1
                if temp[nums[left]] == 0:
                    del temp[nums[left]]
                left += 1
            result = max(result, right-left+1)

        return result