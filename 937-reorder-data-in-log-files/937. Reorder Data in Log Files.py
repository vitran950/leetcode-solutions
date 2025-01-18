import heapq
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        heap = []
        arr2 = []
        
        for log in logs:
            if log[-1].isdigit():
                arr2.append(log)
            else:
                split_word = log.split()
                id = split_word[0]
                rest = " ".join(split_word[1:])
                heapq.heappush(heap, (rest, id))
        
        arr1 = []
        while len(heap) > 0:
            word = heapq.heappop(heap)
            arr1.append(word[1] + " " + word[0])

        return arr1 + arr2