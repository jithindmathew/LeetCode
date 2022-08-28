# 359

class Logger:
    def __init__(self):
        self.logs = dict()
        
    def shouldPrintMessage(self, time: int, message: str) -> bool:
        
        if message not in self.logs or (message in self.logs and self.logs[message] + 10 <= time):
            self.logs[message] = time
            
            return True
        
        return False
    
log = Logger()
print(log.shouldPrintMessage(8, "hbh"))
print(log.shouldPrintMessage(17, "hbh"))
