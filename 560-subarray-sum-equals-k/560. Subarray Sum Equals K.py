from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        count = 0
        hash = defaultdict(int)
        hash[0] = 1
        for i in range(len(prefix)):
            if prefix[i] - k in hash:
                count += hash[prefix[i] - k]
            hash[prefix[i]] += 1
        return count