from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def get_choices(gene): 
            ans = []
            for i in range(8):
                curr = gene[i]
                for letter in letters:
                    if letter == curr:
                        continue
                    word = gene[:i] + letter + gene[i+1:]
                    if word in valid:
                        ans.append(word)
            return ans
                        
        queue = deque([(startGene, 0)])
        valid = set(bank)
        letters = ['A', 'C', 'G', 'T']

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            directions = get_choices(gene)
            for direction in directions:
                valid.remove(direction)
                queue.append((direction, steps + 1))
        
        return -1