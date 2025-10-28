from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        hash = Counter(s)
        sorted_freq = sorted(hash.items(), key=lambda x: (-x[1], x[0]))

        ans = []
        for character in sorted_freq:
            letter = character[0]
            freq = character[1]
            for _ in range(freq):
                ans.append(letter)

        return "".join(ans)
            


