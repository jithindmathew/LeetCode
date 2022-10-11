import random


class RandomizedSet:

    def __init__(self):
        self.mapp = dict()
        self.listt = []

    def insert(self, val: int) -> bool:
        if val in self.mapp:
            return False

        self.mapp[val] = len(self.listt)
        self.listt.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.mapp:
            return False

        idx = self.mapp[val]
        temp = self.listt[-1]

        self.listt[idx] = temp
        self.listt.pop()

        self.mapp[temp] = idx
        self.mapp.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.listt)




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
