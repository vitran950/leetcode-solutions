class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        hash = set(nums1)
        result = float("inf")
        for num in nums2:
            if num in hash and num < result:
                result = num
        return result if result != float("inf") else -1