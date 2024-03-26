class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        
        seen = set(nums)
        for i in range(1, max(nums) + 2):
            if i not in seen:
                return i
        
        return 1 
