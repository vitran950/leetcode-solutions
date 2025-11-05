class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in hash:
                temp = num
                curr = 0
                while temp in hash: 
                    curr += 1
                    temp += 1
                longest = max(curr, longest)
        return longest