class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        if len(tokens) == 0:
            return 0
        if len(tokens) == 1:
            return 1 if power >= tokens[0] else 0

        tokens.sort()
        i, j = 0, len(tokens)-1
        result = 0
        left_turn = True
        while i <= j:
            if left_turn:
                if power >= tokens[i]:
                    score += 1
                    power -= tokens[i]
                i += 1
                if power < tokens[j] and power < tokens[i]:
                    left_turn = False
                result = max(result, score)
                continue
            else:
                if score > 0:
                    score -= 1
                    power += tokens[j]
                if power >= tokens[i] and power >= tokens[j]:
                    left_turn = True
                j -= 1
                result = max(result, score)
                continue       
        return result
