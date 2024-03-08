from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        largest = 0
        for num in nums:
            hash[num] += 1
            largest = max(largest, hash[num])
        count = 0
        for key, value in hash.items():
            if value == largest:
                count += value
        return count 