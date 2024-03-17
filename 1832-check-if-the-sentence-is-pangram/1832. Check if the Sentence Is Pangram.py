class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hash = set(sentence)
        return True if len(hash) == 26 else False