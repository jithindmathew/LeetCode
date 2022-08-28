class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name) or name[0] != typed[0]:
            return False
        
        curr_name = 0
        curr_typed = 0
        
        while curr_typed < len(typed):
            if curr_name < len(name) and name[curr_name] == typed[curr_typed]:
                curr_name += 1
            elif typed[curr_typed] != typed[curr_typed - 1]:
                return False
            
            curr_typed += 1
        return curr_name == len(name)
        