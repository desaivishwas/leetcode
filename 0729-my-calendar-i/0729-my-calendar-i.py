class MyCalendar:

    def __init__(self):
        self.start  = []
        self.end = {}

    def book(self, start: int, end: int) -> bool:
        index = bisect_left(self.start, start)

        if index - 1 >= 0 and self.end[self.start[index-1]] > start:
                return False
        if index < len(self.start) and self.start[index] < end:
                return False

        self.start.insert(index, start)
        self.end[start] = end
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)