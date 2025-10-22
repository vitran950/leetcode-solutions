from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(num%2 + prefix_sum[-1])
        
        counts = defaultdict(int)
        ans = 0
        for element in prefix_sum:
            if element - k in counts:
                ans += counts[element - k]
            counts[element] += 1
        return ans