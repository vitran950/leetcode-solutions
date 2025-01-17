from collections import deque

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def corr_mid(mid, diff): 
            corr_pos = mid + diff
            if corr_pos < len(nums):
                return corr_pos
            elif corr_pos == len(nums):
                return 0 
            else:
                return corr_pos - len(nums)

        diff = nums.index(min(nums))
        original_nums = deque(nums)
        original_nums.rotate(-diff)

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 
            if original_nums[mid] == target:
                return corr_mid(mid, diff)
            if original_nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
            