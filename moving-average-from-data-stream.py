# 346

class MovingAverage():
    def __init__(self, size):
        self.size = size
        self.que = []
        
    def next(self, val):
        self.que.append(val)
        print(sum(self.que[-self.size:])/len(self.que[-self.size:]))

m = MovingAverage(4)
m.next(9)
m.next(8)
m.next(2)
m.next(3)
m.next(33)
