class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = float('inf')
        nums.sort()
        
        for i in range(len(nums) - 2):
            left = i + 1 
            right = len(nums) - 1
            while left < right: 
                check = nums[i] + nums[left] + nums[right]
                if abs(check - target) <= abs(result - target):
                    result = check

                if check < target:
                    left += 1
                elif check > target:
                    right -= 1
                else:
                    return check
        
        return result