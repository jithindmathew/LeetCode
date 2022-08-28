# 170

class Twosum():
    
    def __init__(self):
        self.data = dict()
        self.data[0] = 3
        
    def add(self, number):
        if number not in self.data:
            self.data[number] = 1
        else:
            self.data[number] += 1
    
    def find(self, value):
        for i in self.data.keys():
            target = value - i
            
            if target == i:
                return self.data[i] >= 2
            else:
                return target in self.data

two = Twosum()

two.add(8)
two.add(8)
two.add(7)
print(two.find(2))
            
