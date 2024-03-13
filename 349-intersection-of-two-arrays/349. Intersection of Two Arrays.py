class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = set(nums1)
        result = set()
        for num in nums2:
            if num in hash:
                result.add(num)
        return list(result)