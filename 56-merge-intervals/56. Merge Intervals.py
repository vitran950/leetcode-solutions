class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        hash = {}
        prev = [0, 0] 
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if prev[1] >= start:
                temp_large = max(end, prev[1])
                prev_key = prev[0]
                hash[prev_key] = temp_large
                prev = [prev_key, temp_large]
            else:
                hash[start] = end
                prev = interval
        return [[k, v] for k, v in hash.items()]