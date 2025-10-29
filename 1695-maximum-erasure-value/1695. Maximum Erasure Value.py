from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0 
        curr = 0
        ans = 0
        hash = defaultdict(int)
        for right in range(len(nums)):
            curr += nums[right]
            hash[nums[right]] += 1
            while hash[nums[right]] > 1:
                hash[nums[left]] -= 1
                if hash[nums[left]] == 0:
                    del hash[nums[left]]
                curr -= nums[left]
                left += 1
            ans = max(ans, curr)
        return ans