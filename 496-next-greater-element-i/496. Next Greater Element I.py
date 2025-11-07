class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            j = 0
            while j < len(nums2) and nums2[j] != num:
                j += 1
            curr = -1
            while j < len(nums2):
                if nums2[j] > num:
                    curr = nums2[j]
                    break
                j += 1
            ans.append(curr)
        return ans