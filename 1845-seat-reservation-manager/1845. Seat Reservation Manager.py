from heapq import *
class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.reserved = set()
        for i in range(1, n + 2):
            heappush(self.heap, i)

    def reserve(self) -> int:
        num = heappop(self.heap)
        self.reserved.add(num)
        return num

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber in self.reserved:
            self.reserved.remove(seatNumber)
            heappush(self.heap, seatNumber)            


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)