class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, result = [nums[0]], [nums[-1]], []
        
        for i in range(1, len(nums)):
            pre.append(nums[i]*pre[i-1])
            post.append(nums[len(nums)-1-i]*post[i-1])

        for i in range(len(nums)):
            left = pre[i-1] if (i-1) >= 0 else 1
            right = post[len(nums)-2-i] if (len(nums)-2-i) >= 0 else 1
            result.append(left*right)
        
        return result
        
        
