class DetectSquares:

    def __init__(self):
        self.mapp = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.mapp[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0

        x, y = point

        points = list(self.mapp.keys())

        print(points)

        for xx, yy in points:
            if (abs(yy - y) != abs(xx - x)) or x == xx or y == yy:
                continue

            ans += self.mapp[(x, yy)] * self.mapp[(xx, y)] * \
                self.mapp[(xx, yy)]

        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
