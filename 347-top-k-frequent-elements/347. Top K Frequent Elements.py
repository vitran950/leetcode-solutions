from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)

        for num in nums:
            hash[num] += 1

        # hash = {num: nums.count(num) for num in nums}

        sorted_hash = sorted(hash.items(), key=lambda x:x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_hash[i][0])

        return result