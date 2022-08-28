# 604

from typing import List

class StringIterator:
    
    def __init__(self, compressedString: str):
        
        self.string = ""
        self.pointer = 0
        
        for i in range(0, len(compressedString), 2):
            self.string += compressedString[i]*int(compressedString[i + 1])
            
    def next(self):
        self.pointer += 1
        
        if self.pointer <= len(self.string):
            return self.string[self.pointer - 1]
        else:
            return ' '
        
    def hasNext(self):
        if self.pointer == len(self.string):
            return False
        else:
            return True
        
iterator = StringIterator("L1e2t1C1o1d1e1")

print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
