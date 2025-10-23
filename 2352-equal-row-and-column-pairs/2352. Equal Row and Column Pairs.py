from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hash1 = defaultdict(int)
        for row in grid:
            hash1[tuple(row)] += 1
        
        hash2 = defaultdict(int)
        for col in zip(*grid):
            hash2[tuple(col)] += 1

        ans = 0
        for key in hash1.keys():
            if key in hash2:
                ans += hash1[key] * hash2[key]        

        return ans