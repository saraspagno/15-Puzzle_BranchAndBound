from heapq import heappush, heappop


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    # todo: can I do this?
    def empty(self):
        return not self.heap
