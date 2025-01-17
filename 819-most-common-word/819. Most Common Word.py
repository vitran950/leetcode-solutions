from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set()
        for word in banned:
            banned_words.add(word.lower())
        
        clean_paragraph = paragraph.replace(",", " ").replace("!", " ").replace("?", " ").replace("'", " ").replace(".", " ").replace(";", " ")
        cleaner_paragraph = clean_paragraph.split()

        result = defaultdict(int)
        for word in cleaner_paragraph:
            if word.lower() not in banned_words:
                result[word.lower()] += 1
            
        ans = max(result, key=result.get)
        return ans