from collections import defaultdict, deque
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left = 0
        sub = deque([])
        occur = defaultdict(int)
        result = defaultdict(int)
        n = len(s)
        for right in range(n):
            sub.append(s[right])
            occur[s[right]] += 1

            while len(occur) > maxLetters or right - left + 1 > maxSize:
                sub.popleft()
                occur[s[left]] -= 1
                if occur[s[left]] == 0:
                    del occur[s[left]]
                left += 1

            window_size = right - left + 1
            for size in range(minSize, min(window_size, maxSize) + 1):
                if size > window_size:
                    break
                sub_str = ''.join(list(sub)[-size:])
                if len(set(sub_str)) <= maxLetters:
                    result[sub_str] += 1

        ans = 0
        for v in result.values():
            ans = max(ans, v)
        return ans