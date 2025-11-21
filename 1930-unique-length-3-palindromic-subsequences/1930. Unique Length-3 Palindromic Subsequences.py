from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hash = defaultdict(list)
        for i, c in enumerate(s):
            hash[c].append(i)

        result = set()
        for k, v in hash.items():
            if len(v) < 2: 
                continue
            
            lowest = min(v)
            highest = max(v)

            for k in range(lowest + 1, highest):
                word = s[lowest] + s[k] + s[highest]
                result.add(word)

            # pairs = []
            # sorted_v = sorted(v)
            # for i in range(len(sorted_v) - 1):
            #     curr = sorted_v[i]
            #     for j in range(i + 1, len(sorted_v)):
            #         new = sorted_v[j]
            #         if new - curr >= 2:
            #             pairs.append([curr, new])
            
            # for pair in pairs:
            #     first_element = pair[0]
            #     last_element = pair[1]
            #     for k in range(first_element + 1, last_element):
            #         word = s[first_element] + s[k] + s[last_element]
            #         result.add(word)           

        return len(result)