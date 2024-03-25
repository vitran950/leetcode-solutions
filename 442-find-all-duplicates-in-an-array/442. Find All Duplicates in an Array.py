from collections import defaultdict
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash = defaultdict(int)
        for num in nums:
            hash[num] += 1
        
        result = []
        for key, value in hash.items():
            if value == 2:
                result.append(key)
        
        return result
