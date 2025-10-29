from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occurrence = set(count.values())
        return len(occurrence) == len(count)