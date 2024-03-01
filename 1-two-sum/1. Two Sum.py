from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = defaultdict()

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash:
                return [hash[difference], i]
            hash[nums[i]] = i
            