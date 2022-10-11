class MyCalendar:

    def __init__(self):
        self.cal = [(0, 0), (10 ** 9 + 1, 10 ** 9 + 1)]

    def book(self, start: int, end: int) -> bool:
        # binary search
        l = 0
        r = len(self.cal) - 1

        while l < r:
            mid = (l + r) // 2

            if end == self.cal[mid][0]:
                l = mid
                break
            elif end > self.cal[mid][0]:
                l = mid + 1
            else:
                r = mid

        if start < self.cal[l - 1][1]:
            return False

        self.cal.insert(l, (start, end))

        return True

