class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        hash = set()
        while i < len(nums):
            if nums[i] in hash:
                nums.remove(nums[i])
            else:
                hash.add(nums[i])
                i += 1
        return len(nums)