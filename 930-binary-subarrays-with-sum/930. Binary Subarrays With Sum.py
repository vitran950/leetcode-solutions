from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        hash = defaultdict(int)
        count = 0
        hash[0] = 1
        for i in range(len(prefix)):
            if prefix[i] - goal in hash:
                count += hash[prefix[i] - goal]
            hash[prefix[i]] += 1

        return count