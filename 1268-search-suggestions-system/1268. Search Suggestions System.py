import heapq

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        current = ""
        result = []
        for c in searchWord:
            heap = []
            current += c
            for product in products:
                if product.startswith(current):
                    heapq.heappush(heap, product)
            words = []
            i = 0
            while len(heap) > 0 and i < 3:
                words.append(heapq.heappop(heap))
                i += 1
            result.append(words)
        return result