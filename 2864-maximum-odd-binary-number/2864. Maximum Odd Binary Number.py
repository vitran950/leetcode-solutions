class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        numbers_as_integers = [int(num) for num in s]
        numbers_as_integers.sort(reverse=True)
        result = ""
        for i in range(1, len(numbers_as_integers)):
            result += str(numbers_as_integers[i])
        return result + "1"
