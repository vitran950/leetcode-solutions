from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                hash[product] += 1

        count = 0
        for val in hash.values():
            if val > 1: 
                perm = (val * (val - 1) // 2) * 8  
                count += perm
        return count