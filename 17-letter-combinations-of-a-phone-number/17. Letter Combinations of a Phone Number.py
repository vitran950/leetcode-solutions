class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append(curr[:])
                return
            nums = hash[int(digits[i])]
            for num in nums:
                curr.append(num)
                backtrack(curr, i+1)
                curr.pop()                

        ans = []
        backtrack([], 0)
        return ["".join(x) for x in ans]