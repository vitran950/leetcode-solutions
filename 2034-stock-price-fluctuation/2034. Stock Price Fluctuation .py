from collections import defaultdict
from heapq import *

class StockPrice:

    def __init__(self):
        self.records = defaultdict(int)
        self.latest = 0
        self.largest = []
        self.smallest = []

    def update(self, timestamp: int, price: int) -> None:
        self.records[timestamp] = price
        self.latest = max(timestamp, self.latest)
        heappush(self.largest, (-price, timestamp))
        heappush(self.smallest, (price, timestamp))

    def current(self) -> int:
        return self.records[self.latest]

    def maximum(self) -> int:
        curr = self.largest[0]
        while curr and self.records[curr[1]] != -curr[0]:
            heappop(self.largest)
            curr = self.largest[0]
        return -curr[0]

    def minimum(self) -> int:
        curr = self.smallest[0]
        while curr and self.records[curr[1]] != curr[0]:
            heappop(self.smallest)
            curr = self.smallest[0]
        return curr[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()