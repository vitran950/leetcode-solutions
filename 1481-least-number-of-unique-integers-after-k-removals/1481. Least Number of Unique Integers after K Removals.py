from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        sorted_count = sorted(count.values(), reverse=True)
        i = 0

        while i < k:
            sorted_count[-1] -= 1
            if sorted_count[-1] == 0:
                sorted_count.pop()
            i += 1

        return len(sorted_count)